#This is a very basic hello World file for flask which when ran gives you a hellow world messgae

from flask import Flask
app = Flask(__name__)

@app.route("/")

def hello():
    return "Hello World, This is my first Flask App!"
    

## Usage instructions
# After you ahve created a file like this with your <Prefered_name.py>
#From command line do teh following
# set FLASK_APP = Prefered_name.py # Make sure that you have th corect path added

# flask run # Run this command to execute the flask hello world app

# You should be able to see it running  at your localhost, http://127.0.0.1:5000/

