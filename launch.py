from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import time
import os
app = Flask(__name__)

@app.route('/carpool/')
def goHome():
	print "Home"
	return render_template("carpool/home.html")
@app.route('/carpool/search/')
def getSearch():
	print "Search"
	return render_template("carpool/list.html")

@app.route("/carpool/add/")
def addTrip():
	return render_template("carpool/add.html")
@app.route("/carpool/detail/")
def detailForTrip():
	return render_template("carpool/detail.html")
@app.route("/carpool/tripLogin/")
def loginToTrip():
	return render_template("carpool/login.html")
@app.route('/carpool/applicants/')
def applicants():
	return render_template("carpool/passengers.html")
if __name__ == '__main__':
    app.run()