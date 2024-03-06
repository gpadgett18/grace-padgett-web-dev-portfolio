# Grace Padgett
# Python
# Capstone project: backend of a messaging app

import psycopg2 # connect to postgres database

from flask import Flask, jsonify
from flask_cors import CORS # permissions

from flask_mail import Mail, Message # for confirmation email

import hashlib # For generating tokens
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


def startdb(): # function to start database connection and create cursor
    
    global conn, cur
    try: 
        conn = psycopg2.connect(host="dpg-cirfrcp8g3n42okl5gj0-a.oregon-postgres.render.com", 
                    port="5432", 
                    user="inew2374250fall23_user", 
                    password="VeqKMiDIcOWKEAT3SmjF8ZJM5UemCw8O", 
                    database="inew2374250fall23", 
                    options="-c search_path=msg_app")
    except: # print error if can't connect
        print("Error: Could not connect to the database.") 

    cur = conn.cursor() # create a cursor to run queries in database


def closedb(): # function to commit changes and close cursor and connection
    
    conn.commit() # commit changes
    cur.close() # close cursor
    conn.close() # close connection


# check if password meets requirements
@app.route('/validate/<password>', methods=['GET']) #password as route parameter
def validatePassword(password):
    
    x = password # clean up code

    # set flags to 0
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

    # true if passes validation, false if flags
    if flagTotal > 0:
        response = False
    else:
        response = True

    return jsonify(response)


# create new user
@app.route('/user/<name>/<email>/<password>', methods=['GET', 'POST'])
def user(name, email, password):

    # queries used in function
    EXISTING_USER = ( # check if user already exists
        'SELECT * FROM msg_app.user WHERE email LIKE (%s)'
    )
    NEW_USER = ( # create new user
        'INSERT INTO msg_app.user (name, email, password, is_confirmed, token) VALUES (%s, %s, %s, FALSE, %s)'
    )
    startdb() # start up database and create a cursor

    confirmation_link = 'https://t2me-backend.onrender.com/confirm/' # set up link for confirmation

    hash_obj.update(email.encode('utf-8')) # Hashes the user's email to use as a token
    token  = hash_obj.hexdigest()
   
    cur.execute(EXISTING_USER, (email,)) # check if user exists
    user_exists = cur.fetchall()

    if user_exists: # if user exists, display error and return false
        print("ERROR: User already exists.")
        response = False
    else:
        try: # create a new user
            cur.execute(NEW_USER, (name, email, password, token))
            newUser = True
        except: # return false if user can't be added
            print("ERROR: User could not be added to the database.")
            newUser = False
        
        if newUser == True: # send email using link and token if new user created successfully
            try: 
                msg = Message('T2me | Confirm your email', sender = MAIL_SENDER, recipients = [email]) # email subject
                msg.body = ("Confirm your email address here: " + confirmation_link + token) # mail message body
                print("Email created successfully!")
                mail.send(msg) # Sends the email using the gmail account specified in MAIL_SENDER
                response = True # true if email was sent
            except: 
                print("ERROR: Email did not send.")
                response = False # returns false if email can't send
        else:
            response = False # false if new user not added to db

    closedb() # commit changes and close cursor and database connection 

    return jsonify(response) # returns true if new user created and email sent, false if not


# update database when confirmation link is accessed
@app.route('/confirm/<token>') 
def confirm_email(token):
    
    # queries used in function
    EMAIL_CONFIRMATION = ( # update is_confirmed to True for the user
        'UPDATE msg_app.user SET is_confirmed = TRUE WHERE token = %s', (token, )
    )

    startdb() # start up database connection and cursor

    try: 
        cur.execute(EMAIL_CONFIRMATION, (token, )) # run query update database 
        response = True # true if successful
    except:
        print("ERROR: User could not be validated.") 
        response = False # returns false if could not update

    closedb() # commit changes and close cursor and database connection 

    return jsonify(response) # returns true if successfully confirmed, false if not


# view all users (dev route)
@app.route('/allusers', methods=['GET'])
def allusers():

    # queries used in function
    ALL_USERS = ( # get info for all users
        'SELECT * FROM msg_app.user'
    )

    startdb() # start up database and create a cursor
    
    cur.execute(ALL_USERS) # run query get all users
    data = cur.fetchall()
    
    closedb() # commit changes and close cursor and database connection 
   
    return jsonify(data) # return data for all users


# login w email and password
@app.route('/login/<email>/<password>', methods=['GET'])
def login(email, password): # define login function with arguments

    x = email # easier to read
    y = password
    
    # queries used in function
    LOGIN_CREDENTIALS = ( # check if email and password are correct
        "SELECT email, password FROM msg_app.user \
        WHERE email LIKE (%s) AND password LIKE (%s)"
    )
    
    startdb() # start up database and create a cursor
    
    cur.execute(LOGIN_CREDENTIALS, (x, y)) # run query to see if user with matching email and pass exist
    loggedIn = cur.fetchall()
    
    if loggedIn: # return true if credentials are correct
        response = True
    else: # false if matches no users
        response = False
    
    closedb() # commit changes and close cursor and database connection 
    
    return jsonify(response) # return true if credentials are correct, false if not


# ----- some queries stored here because they're used in multiple routes -----
GROUP_MESSAGES = ( # get all messages in a group in chronological order
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
GET_USER_ID = ( # get user ID using email
        "SELECT user_id FROM msg_app.user WHERE email LIKE %s"
)


# create new group (two members only) and add message to database using route parameters 
@app.route('/create/<sender>/<message>/<date_time>/<recipient>', methods=['GET', 'POST']) 
def create(sender=None, message=None, date_time=None, recipient=None): 

    # queries used in function
    NEW_GROUP = ( # create new group with new id
        "INSERT INTO msg_app.group (group_id) VALUES (%s)"
    )
    NEW_GROUP_USERS = ( # add users in group to group_user_x table
        "INSERT INTO msg_app.group_user_x VALUES (%s, %s), (%s, %s)"
    )

    startdb() # start up database and create a cursor

    # get user IDs
    cur.execute(GET_USER_ID, (sender, ))
    user1 = cur.fetchone()
    cur.execute(GET_USER_ID, (recipient, ))
    user2 = cur.fetchone()

    
    if not user1 or not user2: # error statement for incorrect email(s)
        print("ERROR: One or both emails not found.")
        response = False # return false if emails not found
    else:
        cur.execute(FIND_GROUP_ID, (user1, user2)) # check if group already exists
        group_exists = cur.fetchall()
        
        if group_exists:
            print("ERROR: Group already exists.")
            response = False # return False if group already exists
        else:
            cur.execute( # list all group id's and get data
                "SELECT group_id FROM msg_app.group"
            )
            data = cur.fetchall()
            
            i = 1    
            for row in data: # find the next available group id number
                if row[0] == i:
                    i += 1
                else:
                    break
            group_id = i
            
            cur.execute(NEW_GROUP, (group_id, )) # create group
            
            cur.execute(NEW_GROUP_USERS, (group_id, user1, group_id, user2)) # create group users
            
            cur.execute(NEW_MESSAGE, (user1, message, date_time, group_id)) # Insert new message into message table
            
            cur.execute(GROUP_MESSAGES, (group_id, )) # get all messages from group

            message_exists = cur.fetchall() # store new message in variable
            
            if message_exists: # returns true if message successfully added, false if not
                response = True
            else:
                response = False

        closedb() # commit changes and close cursor and database connection 
        
        return jsonify(response) # return true if message successfully added


# reply to a message
@app.route('/reply/<sender>/<message>/<date_time>/<groupID>', methods=['GET', 'POST'])
def reply(sender=None, message=None, date_time=None, groupID=None): 

    # queries used in function
    USER_IN_GROUP = ( # confirm that the user is part of the group
        'SELECT * FROM msg_app.group_user_x WHERE user_id = %s AND group_id = %s'
    )
    
    startdb() # start up database and create a cursor
    
    cur.execute(GET_USER_ID, (sender, )) # get user ID
    user1 = cur.fetchone()
    
    cur.execute(USER_IN_GROUP, (user1, groupID)) # confirm that user is in said group
    group_user_exists = cur.fetchall()
    
    if group_user_exists:
        try:
            cur.execute(NEW_MESSAGE, (user1, message, date_time, groupID)) # Insert new message into message table
            response = True
        except: 
            print("ERROR: Message could not be added to database.")
            response = False # false if message not added to database
    else:
        print("ERROR: User is not in the group.")
        response = False # false if user is not in the group

    closedb() # commit changes and close cursor and database connection 

    return jsonify(response) # return all messages for that group


# display most recent message from each group that the user is a part of
@app.route('/chats/<email>', methods=['GET'])
def chats(email):
    
    startdb() # start up database and create a cursor
    
    cur.execute(GET_USER_ID, (email, )) # get user ID using email
    user1 = cur.fetchone()
    
    cur.execute( # get most recent chat from each group the user is in
        'SELECT DISTINCT on (group_id) u.email, message, date_time, group_id \
        FROM msg_app.message m JOIN msg_app.user u ON m.sender_id = u.user_id \
        WHERE group_id IN \
	        (SELECT group_id FROM msg_app.group_user_x \
	        WHERE user_id = %s) \
        ORDER BY group_id, date_time DESC', (user1, )
    )
    data = cur.fetchall()
    
    closedb() # commit changes and close cursor and database connection 

    response = jsonify(data) # make chats json data
    
    return response # returns each group the user is in and most recent chat from each group


# display all messages in a group
@app.route('/messages/<groupID>', methods=['GET']) 
def messages(groupID): 
    
    startdb() # start up database and create a cursor
    
    cur.execute(GROUP_MESSAGES, (groupID)) # retrieve messages from correct group to be displayed
    messages = cur.fetchall()
    
    closedb() # commit changes and close cursor and database connection 
    
    response = jsonify(messages) # make messages json data
    
    return response # return all messages for the group


# change status of a user to available, busy, or away
@app.route('/status/<email>/<status>', methods=['GET', 'POST'])
def set_status(email, status):
    
    status_options = ['available', 'busy', 'away'] # array of status options
    
    # querie(s) used in function
    CHANGE_STATUS = (
        'UPDATE msg_app.user SET status = %s WHERE email LIKE %s'
    )
    
    startdb() # start up database and create a cursor
    
    if status not in status_options: # check if status provided is valid
        print("ERROR: Status not valid.")
        response = False
    else: # if valid, change status in database
        cur.execute(CHANGE_STATUS, (status, email))
        response = True
    
    closedb() # commit changes and close cursor and database connection 

    return jsonify(response) # returns true if successfully changed, false if not