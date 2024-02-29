# Grace Padgett
# T2me backend

# connect to postgres database
import psycopg2

from flask import Flask, jsonify
from flask_cors import CORS # permissions

from flask_mail import Mail, Message # for confirmation email

# For generating tokens
import hashlib 
hash_obj = hashlib.sha256()

app = Flask(__name__)
CORS(app) # permissions

# configuration of mail
app.config['MAIL_SERVER']   = 'mail.smtp2go.com'
app.config['MAIL_PORT']     = '2525'
app.config['MAIL_USERNAME'] = 't2me.signup'
app.config['MAIL_PASSWORD'] = 'yF7uyAQ3d75l2qJV'
app.config['MAIL_USE_TLS']  = True
mail = Mail(app)

MAIL_SENDER = 'junkmanager78@gmail.com'

# Database connection and create cursor
def startdb():
    global conn, cur # can be accessed by all functions
    try: 
        conn = psycopg2.connect(host="dpg-cirfrcp8g3n42okl5gj0-a.oregon-postgres.render.com", 
                    port="5432", 
                    user="inew2374250fall23_user", 
                    password="VeqKMiDIcOWKEAT3SmjF8ZJM5UemCw8O", 
                    database="inew2374250fall23", 
                    options="-c search_path=msg_app")
        cur = conn.cursor()
    except Exception as e:
        print("Error: Confirmation Email could not be sent.")
        print(str(e))
    # create a cursor to run queries in database

# Commit changes and close cursor and connection
def closedb():
    # commit changes
    conn.commit()
    # close cursor
    cur.close()
    # close connection
    conn.close()


# check if password meets requirements
@app.route('/validate/<password>', methods=['GET']) #password as route parameter
def validatePassword(password): #define function to validate password requirements
    
    # variable into x (easier to read)
    x = password

    # set flags to false
    flag_len = 0
    flag_alpha = 0
    flag_num = 0
    flag_upper = 0
    flag_lower = 0
    
    # flag if too long/short
    if len(x) < 8 or len(x) > 20: 
        flag_len = 1 

    # using any() to check for any occurrence of a number
    num = any(chr.isdigit() for chr in x) 
    if num != True: # flag if no numbers
        flag_num = 1

    # using any() to check for any occurrence of a letter
    alpha = any(chr.isalpha() for chr in x) 
    if alpha != True: # flag if no letters
        flag_alpha = 1
    
    # flag if only uppercase
    if x.isupper(): 
        flag_upper = 1
    
    # flag if only lowercase
    if x.islower(): 
        flag_lower = 1

    # check for any flags 
    flagTotal = flag_len + flag_alpha + flag_num + flag_upper + flag_lower

    # true if passes validation, flase if flags
    if flagTotal > 0:
        response = False
    else:
        response = True

    # return true/false
    return jsonify(response)

# create new user
@app.route('/user/<name>/<email>/<password>', methods=['GET', 'POST'])
def user(name, email, password):

    # store queries up here to clean up code
    EXISTING_USER = (
        'SELECT * FROM msg_app.user WHERE email LIKE (%s)'
    )
    NEW_USER = (
        'INSERT INTO msg_app.user (name, email, password, is_confirmed, token) VALUES (%s, %s, %s, FALSE, %s)'
    )

    # start up database and create a cursor
    startdb()

    # # link for confirmation
    confirmation_link = 'https://t2me-backend.onrender.com/confirm/'

    # # Hashes the user's email to use as a token
    hash_obj.update(email.encode('utf-8'))
    token  = hash_obj.hexdigest()

    # check if user exists
    cur.execute(EXISTING_USER, (email,))
    user_exists = cur.fetchall()

    if user_exists: # if user exists, return false
        response = False
    else:
        try: # create a new user
            cur.execute(NEW_USER, (name, email, password, token))
            response1 = True
        except: # return false if user can't be added
            response1 = False
            print("User could not be added to the database.")

        try: # send email w confirmation link using token
            msg = Message('T2me | Confirm your email', sender = MAIL_SENDER, recipients = [email]) # Email subject
            msg.body = ("Confirm your email address here: " + confirmation_link + token) # Email message body
            print("Email created successfully!")
            mail.send(msg) # Sends the email using the gmail account specified in MAIL_SENDER
            response2 = True # Confirms that the email was sent
        except: # return false if email can't send
            print("Email could not be sent.")
            response2 = False

        if response1 == True and response2 == True:
            response = True
        else:
            response = False

    # commit changes and close cursor and database connection 
    closedb()

    return jsonify(response)

# Handle the confirmation token
@app.route('/confirm/<token>')
def confirm_email(token):
    
    # start up database connection and cursor
    startdb()

    # Select the record in the database that has the token and update is_confirmed
    try:
        cur.execute(
            'UPDATE msg_app.user SET is_confirmed = TRUE WHERE token = %s', (token, )
        )
        response = True
    except:
        print("Error: User could not be validated.")
        response = False

    # commit changes and close cursor and database connection 
    closedb()

    return jsonify(response)

# view all users
@app.route('/allusers', methods=['GET'])
def allusers():

    # start up database and create a cursor
    startdb()

    # get all users 
    cur.execute(
        'SELECT * FROM msg_app.user'
    )
    data = cur.fetchall()

    # commit changes and close cursor and database connection 
    closedb()

    # return all users
    return jsonify(data)

# login w username and password
@app.route('/login/<email>/<password>', methods=['GET']) # username and password as params
def login(email, password): # define login function with login arguments

    # variables into x and y (easier to read)
    x = email
    y = password
    
    # query stored in a variable to clean up code and make easy changes
    LOGIN_CREDENTIALS = (
        "SELECT email, password FROM msg_app.user \
        WHERE email LIKE (%s) AND password LIKE (%s)"
    )

    # start up database and create a cursor
    startdb()
    
    # get login info from users table
    cur.execute(LOGIN_CREDENTIALS, (x, y))
    loggedIn = cur.fetchall()

    # commit changes and close cursor and database connection 
    closedb()
    
    # return true if login correct
    if loggedIn:
        response = True
    else: # false if matches no users
        response = False
    
    return jsonify(response)


# some queries stored here because they're used in multiple routes
GROUP_MESSAGES = ( # all messages in a group in chronological order
    'SELECT u.email, message, date_time FROM msg_app.message m \
    JOIN msg_app.user u ON m.sender_id = u.user_id \
    WHERE group_id = %s ORDER BY date_time'
)
FIND_GROUP_ID = ( # get group id using group members (2 members only)
    'SELECT t1.group_id FROM msg_app.group_user_x t1 \
    WHERE user_id = %s \
    AND EXISTS (SELECT * FROM msg_app.group_user_x t2 \
          WHERE t1.group_id = t2.group_id \
		  AND user_id = %s)'
)
NEW_MESSAGE = ( # insert new message into message table
    'INSERT INTO msg_app.message (sender_id, message, date_time, group_id) VALUES (%s, %s, %s, %s)'
)
GET_USER_ID = (
        "SELECT user_id FROM msg_app.user WHERE email LIKE %s"
)

# create new group (two members only) and add message to database using route parameters 
@app.route('/create/<sender>/<message>/<date_time>/<recipient>', methods=['GET', 'POST']) 
def create(sender=None, message=None, date_time=None, recipient=None): 

    # some queries stored here to clean up code
    # create new group with new id
    NEW_GROUP = (
        "INSERT INTO msg_app.group (group_id) VALUES (%s)"
    )
    # add users in group to group_user_x table
    NEW_GROUP_USERS = (
        "INSERT INTO msg_app.group_user_x VALUES (%s, %s), (%s, %s)"
    )

    # start up database and create a cursor
    startdb()

    # get user IDs
    cur.execute(GET_USER_ID, (sender, ))
    user1 = cur.fetchone()
    cur.execute(GET_USER_ID, (recipient, ))
    user2 = cur.fetchone()

    # error statement for incorrect email(s)
    if not user1 or not user2:
        return jsonify("ERROR: One or both emails are incorrect.")
    else:
        # check if group exists
        cur.execute(FIND_GROUP_ID, (user1, user2))
        group_exists = cur.fetchall()

        # error statement if group already exists
        if group_exists:
            response = False
        else:
            # list all group id's and get data
            cur.execute(
                "SELECT group_id FROM msg_app.group"
            )
            data = cur.fetchall()

            # find the next available group id number
            i = 1    
            for row in data:
                if row[0] == i:
                    i += 1
                else:
                    break
            group_id = i

            
            # create group
            cur.execute(NEW_GROUP, (group_id, ))

            # create group users
            cur.execute(NEW_GROUP_USERS, (group_id, user1, group_id, user2))

            # Insert new message into message table
            cur.execute(NEW_MESSAGE, (user1, message, date_time, group_id))
            
            # get all messages from group
            cur.execute(GROUP_MESSAGES, (group_id, ))

            # store cursor data in variable
            message_exists = cur.fetchall() 

            # true if message successfully added, false if not
            if message_exists:
                response = True
            else:
                response = False

        # commit changes and close cursor and database connection 
        closedb()

        # return true if message successfully added
        return jsonify(response)


# reply to a message
@app.route('/reply/<sender>/<message>/<date_time>/<groupID>', methods=['GET', 'POST'])
def reply(sender=None, message=None, date_time=None, groupID=None): 

    # start up database and create a cursor
    startdb()

    # get user ID
    cur.execute(GET_USER_ID, (sender, ))
    user1 = cur.fetchone()

    # make sure user is in said group
    cur.execute(
        'SELECT * FROM msg_app.group_user_x WHERE user_id = %s AND group_id = %s', (user1, groupID)
    )
    group_user_exists = cur.fetchall()
    
    if group_user_exists:
        try:
            # Insert new message into message table
            cur.execute(NEW_MESSAGE, (user1, message, date_time, groupID))
            response = True
        except: # false if message not added to database
            response = False
    else:
        response = False

    # commit changes and close cursor and database connection 
    closedb()

    # return all messages for that group
    return jsonify(response)


# display most recent message from each group that contains the user
@app.route('/chats/<email>', methods=['GET'])
def chats(email):
    
    # start up database and create a cursor
    startdb()
    
    # get user ID from email
    cur.execute(GET_USER_ID, (email, ))
    user1 = cur.fetchone()

    cur.execute(
        'SELECT DISTINCT on (group_id) u.email, message, date_time, group_id \
        FROM msg_app.message m JOIN msg_app.user u ON m.sender_id = u.user_id \
        WHERE group_id IN \
	        (SELECT group_id FROM msg_app.group_user_x \
	        WHERE user_id = %s) \
        ORDER BY group_id, date_time DESC', (user1, )
    )
    data = cur.fetchall()

    # commit changes and close cursor and database connection 
    closedb()

    response = jsonify(data)
    
    # return each group and most recent chat for the user
    return response
    # returns [[sender_id, message, date_time, group_id],...]


# display messages w route parameters of group ID
@app.route('/messages/<groupID>', methods=['GET']) 
def messages(groupID): 
    
    # start up database and create a cursor
    startdb()

    # retrieve messages from correct group to be displayed
    cur.execute(GROUP_MESSAGES, (groupID))
    messages = cur.fetchall()

    # commit changes and close cursor and database connection 
    closedb()

    # make messages json data
    response = jsonify(messages)
    
    # return all messages for the group
    return response
    # returns [[sender email, message, date_time],...]


# list of status options to choose from
status_options = ['available', 'busy', 'away']

# change status of a user to available, busy, or away
@app.route('/status/<email>/<status>', methods=['GET', 'POST'])
def set_status(email, status):
    
    CHANGE_STATUS = (
        'UPDATE msg_app.user SET status = %s WHERE email LIKE %s'
    )

    # start up database and create a cursor
    startdb()

    # check if status provided is valid
    if status not in status_options:
        response = False
    else: # if valid, change status in database
        cur.execute(CHANGE_STATUS, (status, email))
        response = True
    
    # commit changes and close cursor and database connection 
    closedb()

    return jsonify(response)
