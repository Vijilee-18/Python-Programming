'''
Session is used to remeber a user between requests. 
'''

from flask import Flask , render_template, request, session
import secrets 
app=Flask(__name__)
app.secret_key=secrets.token_hex(16)
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if username=="admin" and password=="1234":
            session["user"]=username
            return render_template("base.html")
if __name__=="__main__":
    app.run(debug=True)