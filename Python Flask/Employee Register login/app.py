from flask import Flask , redirect , url_for , request , render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///employee.db"
db=SQLAlchemy(app)
class Employee(db.Model):
    empName=db.Column("Employee Name" , db.String(50) , nullable=False)
    empMail=db.Column("Employee Mail Id", db.String(50) ,nullable=False)
    empPassword=db.Column("Employee Password" , db.String(20) , primary_key=True)

with app.app_context():
    db.create_all()

@app.route("/")
@app.route("/home")
def home():
    return redirect(url_for("login"))

@app.route("/register" ,methods=["GET",'POST'])
def register():
    if request.method=="POST":
        employeeName=request.form.get("employeeName")
        employeeMail=request.form.get("employeeMail")
        employeePassword=request.form.get("empPassword")
        employeeConfirmPassword=request.form.get("confirmPassword")

        if employeePassword ==employeeConfirmPassword:
            new_user=Employee(
                empName=employeeName,
                empMail=employeeMail,
                empPassword=employeeConfirmPassword
            )
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))
        else:
            return "password doen't match"
    return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        employeeName=request.form.get("employeeName")
        employeePassword=request.form.get("empPassword")
        emp=Employee.query.filter_by(
            empPassword=employeePassword
        ).first()
        if emp:
            return render_template('dashboard.html',empName=employeeName)
        else:
            return "invalid credentials"
    return render_template("login.html")


if __name__=="__main__":

    app.run(debug=True)