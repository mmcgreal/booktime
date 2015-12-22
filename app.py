from flask import Flask, render_template, session, request, redirect, url_for
import csv
from operator import itemgetter

	
app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
    return render_template("home.html")


@app.route("/signup",methods=["GET","POST"])
def signup():
    return render_template("signup.html")

@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)