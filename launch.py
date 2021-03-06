from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
import time
import os
import car
app = Flask(__name__)

@app.route('/carpool/')
def goCarHome():
	print "Home"
	return render_template("carpool/home.html")
@app.route('/carpool/search/',methods=['POST'])
def getCarSearch(name = None, arr = None, dep = None, trips = None):
	name = request.form["name"].lower()
	arr = request.form["arr"].lower()
	dep = request.form["dep"].lower()
	print "Name: "+name
	print "Arr: "+arr
	print "Dep: "+dep
	print "Search"
	trips = []
	trips = car.search(name,arr,dep)
	return render_template("carpool/list.html",trips = trips)

@app.route("/carpool/add/")
def addCarTrip():
	return render_template("carpool/add.html")

@app.route("/carpool/<name>/")
def detailCarForUserTrip(name,departure=None,arrival=None,price=None,numSeats=None,bags=None,summ=None,youInfo=None,departDate = None,googleA = None, googleD = None):
	print "Some"
	price,departure,arrival,numSeats,bags,departDate,summ,youInfo = car.getTripInfo(name)
	googleD = departure.replace(" ","+")
	googleA = arrival.replace(" ","+")
	print "2"
	return render_template("carpool/detail.html",name=name,price = price,departure=departure,arrival=arrival,numSeats=numSeats,departDate=departDate,bags=bags,summ=summ,youInfo=youInfo,googleA=googleA,googleD = googleD)
@app.route("/carpool/tripLogin/")
def loginCarToTrip():
	return render_template("carpool/login.html")
@app.route('/carpool/loginTrip/',methods=['POST'])	
def tripCarLoginAccount(name = None,passw = None,applicants = None):
	name = str(request.form["name"])
	passw = str(request.form["passw"])
	print name,passw
	print "Okar"
	if car.tripLoginCheck(name,passw):
		print "4th"
		applicants = []
		print "third"
		applicants = car.getApplicants(name)
		print "Second to last"
		return render_template("carpool/passengers.html",applicants = applicants,name=name)
	else:
		
		return render_template("carpool/login.html",mess="Invalid Credentials")
@app.route('/carpool/deleteApp/',methods=['POST'])
def deleteCarApplicants(tripName = None, name = None,applicants = None):
	name = str(request.form["name"])
	tripName = str(request.form["tripName"])
	car.deleteApplicant(tripName,name)
	name = tripName
	applicants = []
	print "third"
	applicants = car.getApplicants(name)
	print "Second to last"
	return render_template("carpool/passengers.html",applicants = applicants,name=name)


@app.route('/carpool/addTrip/',methods=['POST'])
def addTheTripCar(name = None,departure=None,arrival=None,price=None,numSeats=None,tripPass=None,bags=None,summ=None,youInfo=None,departDate = None,closeDate = None):
	name = request.form['name']
	departure = request.form['departure']
	arrival = request.form['arrival']
	price = request.form['price']
	numSeats = request.form['numSeats']
	tripPass = request.form['tripPass']
	bags = request.form['bags']
	summ = request.form['summ']
	youInfo = request.form['youInfo']
	departDate = request.form['departDate']
	closeDate = request.form['AppDead']
	print "Name: "+str(name)
	print "Departure: "+str(departure)
	print "Arrival: "+str(arrival)
	print "Price: "+str(price)
	print "numSeats: "+str(numSeats)
	print "tripPass: "+str(tripPass)
	print "bags: "+str(bags)
	print "Departure Date: "+str(departDate)
	print "App Close Date: "+str(closeDate)
	print "summ: "+str(summ)
	print "youInfo: "+str(youInfo)
	print "DONE --------------------------------------"
	if car.addTrip(name,departure,arrival,price,numSeats,tripPass,bags,summ,youInfo,departDate,closeDate) == "Error":
		return render_template("carpool/add.html",mess="Trip Name already in system")
	return render_template("carpool/succ.html",tripPass=tripPass,name=name)

@app.route('/carpool/applyForTrip/',methods=['POST'])
def applyforthetripCar(name = None, email= None, phone = None,tripName = None,mess = None):
	name = request.form["name"]
	email = request.form["email"]
	phone = request.form["phone"]
	tripName = request.form["tripName"]
	mess = request.form["mess"]
	print "Name: "+name
	print "Email: "+email
	print "Phone: "+phone
	print "Trip Name: "+tripName
	print "Message: "+mess
	try:
		car.addApplicant(tripName,name,phone,email,mess)
		return render_template("carpool/seccApply.html",tripName=tripName)
	except:
		return render_template("carpool/error.html")

if __name__ == '__main__':
    app.run()









