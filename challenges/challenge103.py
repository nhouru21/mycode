#!/usr/bin/python3
""" Flask quiz game """

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

answers = ["a"]

app = Flask(__name__)
## This is where we want to redirect users to
@app.route("/correct/<name>")
def success(name):
    return f"You are right, {name} was the correct answer\n"
# This is a landing point for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("qmaker.html") # look for templates/postmaker.html
# This is where postmaker.html POSTs data to
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST", "GET"])
def login():
    # POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            user = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            user = "defaultuser"
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            user = "defaultuser" # ...then user is just defaultuser
    if user == answers[0]: 
        return redirect(url_for("success", name = user)) # pass back to /success with val for name
    else:
        return redirect(url_for("start"))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

