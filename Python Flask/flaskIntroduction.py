
'''
Flask is a lightweight Python web framework used to build:
- websites
- APIs
- backend systems
- web applications

Flask helps developers create web servers using Python.
'''

from flask import Flask   # Imports the Flask class from the flask module

firstApp = Flask(__name__)

'''
firstApp is an object (instance) of the Flask class.

Everything in Flask connects through this object.

Flask uses this object to:
- manage routes
- handle requests
- send responses
- configure the application

__name__:
A special built-in Python variable.

It stores the name of the current module.

If this file is run directly:
__name__ becomes "__main__"

Flask uses __name__ to determine:
- application root directory
- template folder location
- static folder location
'''

@firstApp.route("/")
# Defines the route.
# Whenever the user visits "/", Flask executes home() function.

def home():
    return "Flask Learning Begins"

if __name__ == "__main__":
    # Starts Flask development server

    firstApp.run(debug=True)

