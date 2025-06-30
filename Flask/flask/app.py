from flask import Flask

'''Create instance of the Flask class which is our WSGI (web server gateway interface) application'''
# WSGI Application
app=Flask(__name__)


# Creating basic root api
@app.route('/')
def welcome():
    return "Welcome to the Flask API.THis is new file.Learning currently Flask"


@app.route('/index')
def index():
    return "Welcome to the index page.THis is new file.Learning currently Flask"
    
# This is the entry point of our application in which file this condition is return it will be entry point
if __name__=='__main__':
    app.run(debug=True)
    #Debug = true automatically detect changes and update it on localhost