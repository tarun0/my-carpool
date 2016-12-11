from firebase import firebase
import random
import os
import time
import sys
import urllib2
import re
import nltk
import time
import requests
import string
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import webbrowser
import datetime
import car
firebase = firebase.FirebaseApplication('https://playgroundabir.firebaseio.com/', None)
#Deletes trips based on applcation close
#My pythonanywhere website runs this method once a day to get the repition
def deleteTrips():
	trips = eval(car.getResp("trips"))
	for i in trips:
		date = eval(str(car.getResp(i+"Info")))[5]
		date = date.replace("/","-")
		if date == str(datetime.date.today()):
			firebase.delete(i+"Info",None)
			firebase.delete(i+"Glance",None)
			firebase.delete(i+"applicants",None)
			trips.remove(i)
	firebase.delete("trips",None)
	firebase.post("trips",str(trips))

deleteTrips()








