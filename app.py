from flask import Flask, render_template, session, request, redirect, url_for
import csv
from operator import itemgetter

	
app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/home",methods=["GET","POST"])
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=8000)