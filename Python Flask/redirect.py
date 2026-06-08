'''
redirect() is used to send the user to another route or page.
url_for() used to generate URLs Dynamically Using the Fuction Name.
'''

from flask import Flask , redirect,url_for
classInstance=Flask(__name__)
@classInstance.route("/")
def home():
    return redirect(url_for("login"))
@classInstance.route("/login")
def login():
    return "This is the Login Page"
if __name__=="__main__":
    classInstance.run()