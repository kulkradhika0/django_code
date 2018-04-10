# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
import simplejson as json
from django.views.decorators.csrf import csrf_exempt
import Go_Live.settings
#import requests
import urllib

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
		#json_data = json.loads(request.body)
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
