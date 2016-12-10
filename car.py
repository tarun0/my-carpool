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
firebase = firebase.FirebaseApplication('https://playgroundabir.firebaseio.com/', None)

def getResp(phrase):
	a = firebase.get(phrase,None)
	if a == None:
		return None
	keys = []
	for key in a:
		"""
		print "key: %s , value: %s" % (key, a[key])
		"""
		keys.append(key)
	return a[keys[0]]
def putInFirebase(phrase,response):
	phrase = phrase.strip()
	if getResp(phrase) == None:
		a = eval(getResp("trips"))
		if response in a and phrase == "trips":
			return 0
		if len(response) > 1:
			if response[0] == "'":
				response =  "["+response+"]"
			else:
				response = "['"+response+"']"
		else:
			response = "[]"
		firebase.post(phrase,response)
		
		
		return 1
	else:
		a = eval(getResp("trips"))
		if response in a and phrase == "trips":
			return 0
		print "1"
		a = eval(getResp(phrase))
		r = eval(getResp(phrase))
		for item in r:
			print "Item: "+item + "Res: "+response
			if item == response:
				return len(a)
		print "2"
		a.append(response)
		print "3"
		firebase.delete(phrase,None)
		print "4"
		firebase.post(phrase,str(a))
		print "5"
		return len(a)


def addTrip(name,departure,arrival,price,numSeats,tripPass,bags,summ,youInfo,departDate,closeDate):
	if putInFirebase("trips",str(name)) == 0:
		return "Error"
	a = "'"+price+"','"+departure+"','"+arrival+"','"+numSeats+"'"
	b = "'"+bags+"','"+departDate+"','"+summ+"','"+youInfo+"','"+tripPass+"','"+closeDate+"'"
	putInFirebase(name+"Glance",a)
	putInFirebase(name+"Info",b)
	putInFirebase(name+"applicants","")
	return "Succ"
def tripLoginCheck(name,passw):
	a = eval(str(getResp(name+"Info")))
	if a == None:
		return False

	return passw == a[4] 

def getTripInfo(name):

	glace = eval(str(getResp(name+"Glance")))

	info = eval(str(getResp(name+"Info")))
	price = glace[0]
	departure = glace[1]
	arrival = glace[2]
	numSeats = glace[3]
	bags = info[0]
	departDate = info[1]
	summ = info[2]
	youInfo = info[3]
	return price,departure,arrival,numSeats,bags,departDate,summ,youInfo
def addApplicant(tripName,name,phone,email,mess):
	a = [name,phone,email,mess]
	putInFirebase(tripName+"applicants",str(a))
def getApplicants(tripName):
	a = eval(getResp(tripName+"applicants"))
	for i in range(len(a)):
		a[i] = eval(str(a[i]))
	return a

def deleteApplicant(tripName,name):
	a = eval(getResp(tripName+"applicants"))
	for i in range(len(a)):
		a[i] = eval(str(a[i]))
	for i in range(len(a)):
		if a[i][0] == name:
			a.pop(i)
			firebase.delete(tripName+"applicants",None)
			print "4"
			firebase.post(tripName+"applicants",str(a))
			return
def search(name,dep,arr):
	res = []
	trips = eval(getResp("trips"))
	tripslower = eval(getResp("trips").lower())
	if len(name) > 0:
		for i in trips:
			#print eval(str(getResp(i+"Glance")).lower())
			g = eval(str(getResp(i+"Glance")).lower())
			if name in tripslower[trips.index(i)]:
				res.append([i]+g)
			else:
				if (dep in g[1] or g[1].lower() in dep) and len(dep) > 0:
					res.append([i]+g)
				elif (arr in g[2] or g[2].lower()  in arr) > 0:
					res.append([i]+g)
		print res
		return res
	else:
		for i in trips:
			g = eval(str(getResp(i+"Glance")).lower())
			if (dep in g[1] or g[1].lower() in dep) and len(dep) > 0:
				res.append([i]+g)
			elif (arr in g[2] or g[2].lower()  in arr) and len(arr) > 0:
				res.append([i]+g)
		print res
		return res
#print search("","new mexico","purdue")
#print getApplicants("Abirs Trip")
#addApplicant("Abirs Trip","Abir","713-231-7925","shukla14@purdue.edu","I would love to be a part of this")

#addApplicant("Abirs Trip","Chini","71323112","chini@gmail.com","This is dope")
"""a = eval(getResp("Abirs Tripapplicants"))
for i in range(len(a)):
	a[i] = eval(a[i])
print a[1][2]
"""
#print getTripInfo("Abirs Trip")

#addTrip("Abirs Trip","Houston","Purdue","10","2","abiraadi","2","This is a Summary","This is me","2016/07/04","2016/06/04")

#print str(getResp("Abirs TripGlance"))





