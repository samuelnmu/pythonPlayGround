from flask import Flask, render_template,request,session
from flask_session import session

#initialize the flask app
app = Flask(__name__)

#cconfigure session 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
session(app)

#route
