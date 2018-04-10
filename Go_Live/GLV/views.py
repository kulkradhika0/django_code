# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
import simplejson as json
from django.views.decorators.csrf import csrf_exempt
import Go_Live.settings
#import requests
import urllib
from GLV.models import *

####################################################

##### Set Passcode in file

####################################################

@csrf_exempt
def setPasscode(request):

	if request.method == 'POST':
		json_data = json.loads(request.body)
		print(json_data)

	else:
		json_data = {'passcode':'3456'}
		print(json_data)

	writeCode = open(Go_Live.settings.PASSCODE,'w')

	ip = writeCode.write(str(json_data['passcode']))
	return JsonResponse({"STATUS":"Success"}, safe=False)

####################################################

##### Read Passcode from file

####################################################

@csrf_exempt
def getPasscode(request):
	passCode = open(Go_Live.settings.PASSCODE,'r')

	op = passCode.read()
	print(op)
	print(type(op))
	return JsonResponse({"passcode":int(op)}, safe=False)

####################################################

##### TEST MODEL ACCESS

####################################################

@csrf_exempt
def testModel(request):
	passCode = open(Go_Live.settings.PASSCODE,'r')

	op = passCode.read()
	print(op)
	print(type(op))
	return JsonResponse({"passcode":int(op)}, safe=False)

####################################################

##### Set Passcode in model

####################################################

@csrf_exempt
def addPasscode(request):

	if request.method == 'POST':
		json_data = json.loads(request.body)
		print(json_data)

	else:
		json_data = {'username':'radhika.kulkarni@vodafone.com','passcode':'1992','order_id':'4'}
		print(json_data)

		user = USER_MASTER(USERNAME=json_data['username'], PASSCODE=int(json_data['passcode']),ORDER_ID=int(json_data['order_id']))
		user.save()

	return JsonResponse({"STATUS":"Success"}, safe=False)

####################################################

##### List Users in model

####################################################

@csrf_exempt
def listUsers(request):

	user_list = USER_MASTER.objects.order_by('ORDER_ID')

	uData = []

	for usr in user_list:
		#user1 = USER_MASTER.objects.get(USER_ID=usr.USER_ID)

		print(usr.USERNAME)

		uRec = {'user_id':str(usr.USER_ID),'username':usr.USERNAME,'passcode':str(usr.PASSCODE),'order_id':str(usr.ORDER_ID)}

		uData.append(uRec)

	return JsonResponse(uData, safe=False)