#!/usr/biin/python3

""" Simple Flask server with multiple endpoints and user verification """

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

data = [{
    "favorite game": "hockey",
    "favorite meals": [
        "brisket",
        "steak",
        "breakfast tacos"
        ],
    "hometown": "Austin",
    "music": "oldies"
    }]


@app.route("/success/<name>")
def success(name):
    print(f"Welcome {name}\n")
    return redirect(url_for("index"))

# if the user is "admin" then they can access the json data
@app.route("/index")
def index():
    return jsonify(data)

# if the user is not admin, then they do not have access to the json data
@app.route("/failure")
def failure():
    return "You are not an admin and cannot access my secret data"
    

@app.route("/") 

@app.route("/start")
def start():
    return render_template("verifyname.html")

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
    if user == "admin":
        return redirect(url_for("success", name = user)) # pass back to /success with val for name
    else:
        return redirect(url_for("failure"))
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
