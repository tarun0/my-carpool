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
def getMyResp(p):
	keys  = eval(getResp("Keys"))
	for item in keys:
		if item in p:
			arrR = eval(getResp(item))
			resP = arrR[random.randint(0, len(arrR)-1)]
			b = resP[1:]
			return b
	return ""
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
	phrase = phrase.lower()
	phrase = phrase.strip()
	if getResp(phrase) == None:
		response = "['"+response+"']"
		firebase.post(phrase,response)
		keys = eval(getResp("Keys"))
		keys.append(phrase)
		firebase.delete("Keys",None)
		firebase.post("Keys",str(keys))
		
		return 1
	else:
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

