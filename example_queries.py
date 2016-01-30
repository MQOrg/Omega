import os.path, sys
import json
import urllib2

try:
    import apiai
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import apiai

import time

CLIENT_ACCESS_TOKEN = 'KEY_HERE'
SUBSCRIPTION_KEY = 'KEY_HERE'

keepGoing = True

onOff = True

def onOrOff(onOff,  request):
    if request == "online":
        onOff = True
    else:
        onOff = False
    return onOff

while keepGoing:
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN, SUBSCRIPTION_KEY)

    request = ai.text_request()

    request.lang = 'en' # optional, default value equal 'en'

    a = raw_input("Query: ")

    request.query = a
    
    if a == "QUIT":
        keepGoing = False
        break

    response = request.getresponse()
    data = json.loads(response.read())

    try:        
        if (data["result"]["metadata"]["intentName"] == "onOrOff"):
            onOff = onOrOff(onOff, data["result"]["parameters"]["onlineoffline"])
    finally:
        print "No Intent"
        
    print (data['result']["fulfillment"]['speech'])

