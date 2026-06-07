'''
Template are used to  bring the html files .
render_template() is the function used where file name is given as the parameter.
'''

from flask import Flask , render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html") 
if __name__=="__main__":
    app.run(debug=True)
