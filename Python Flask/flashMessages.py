from flask import Flask , flash , render_template , session
app=Flask(__name__)
app.secret_key="Hello"
@app.route("/")
@app.route("/home")
def home():
    flash("Please Login")
    flash("Suiii")
    return render_template("login.html")
if __name__=="__main__":
    app.run(debug=True)
