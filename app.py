# import Flask
from flask import Flask

# Create an app, being sire to pass __name__
app = Flask(__name__)

# Define what to do when a user hits the index route
@app.route("/")
def hello_world():
    return "Hello World!"