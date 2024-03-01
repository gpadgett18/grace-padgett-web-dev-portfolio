//express, multer, path, ejs
//setup reqs
const express = require('express');
const multer = require('multer');
const path = require('path');
const ejs = require('ejs');

const app = express();

//multer storage and upload here
const storage = multer.diskStorage({
    destination : './public/uploads',
    filename : function(req, file, cb){
        cb(null, Date.now() + '-' + file.originalname);
    }
})

const upload = multer({
    storage : storage,
    limits: {
        fileSize: 10000000
    },
    fileFilter: function(req, file, cb){
        checkFile(file, cb);
    }
}).single('files')

//set view engine
app.set('view engine', 'ejs');
//set static
app.use(express.static(path.join(__dirname, 'public')));

// Set 'views' directory for any views 
app.set('views', path.join(__dirname, 'views'));

//route to index
app.get('/', (req, res)=>{
    res.render('index');
})

//code for form post goes here
app.post('/upload', (req, res) =>{
    upload(req, res, (err) =>{
    
    if(err){
        res.render('index', {msg: err})
    }else{
        if(req.file == undefined){
            res.render('index', {msg: "No file selected"})
        }else{
            res.render('index', {
                msg: "File Uploaded",
                file: `uploads/${req.file.filename}`
            })
        }
    }
})
})

//function to check for file type
function checkFile(file, cb){
    let fileEx = ['png', 'jpg', 'jpeg', 'gif']
    let isImageExGood = fileEx.includes(file.originalname.split('.')[1]
    .toLowerCase());
    let isMimeGood = file.mimetype.startsWith("image/");
    if (isImageExGood && isMimeGood){
        return cb(null, true)
    }else{
        cb("Error, not an image file")
    }
}

//start server
app.listen(3000, ()=> {
    console.log('server is working');
})