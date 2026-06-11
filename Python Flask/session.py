'''
Session is used to remeber a user between requests. 
'''

from flask import Flask , render_template, request, session , redirect , url_for
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
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        username=session["user"]
        return render_template("dashboard.html",user=username)
    return redirect(url_for("login"))
if __name__=="__main__":
    app.run(debug=True)
