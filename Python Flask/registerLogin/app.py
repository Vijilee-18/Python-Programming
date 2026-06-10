from flask import Flask , render_template,request
app=Flask(__name__)
registerList=[]
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/reg" ,methods=["GET","POST"])
def register():
    if request.method=="POST":
        passWord=request.form.get("password").lower()
        confirmPassword=request.form.get("confirmPassword").lower()
        if passWord==confirmPassword:
            userName=request.form.get("userName")
            mailId=request.form.get("userMail")
            user={
                "name":userName,
                "mail":mailId,
                "password":confirmPassword
            }
            registerList.append(user)
            return "Registration Completed"
        else:
            return "Password and confirm password should be equal"
    return render_template("register.html")
@app.route("/login",methods=["GET","POST"])

def login():

    if request.method=="POST":

        mail=request.form.get("userMail")
        password=request.form.get("password").lower()

        for user in registerList:

            if user["mail"] == mail and user["password"] == password:

                return f"Welcome {user['name']}"

        return "Invalid Mail or Password"

    return render_template("login.html")
if __name__=="__main__":
    app.run(debug=True)

