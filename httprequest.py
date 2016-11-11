import requests
import json
from datetime import datetime, timedelta
import dateutil.parser

########1.
# send json that includes token and github to endpoint, using http post request
url = "http://challenge.code2040.org/api/register"
jsondata = {"token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe", "github": "https://github.com/MadisonHe19/apiPractice"}
header = {"content-type": "application/json"}

# response object
response = requests.post(url, json = jsondata, headers = header)

#*******************************************************************************************************************

########2. send json to server and server should return string. Reverse string then send back
url = "http://challenge.code2040.org/api/reverse"
jsondata = { "token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe" }
header = {"content-type": "application/json"}

#response object
response = requests.post(url, json = jsondata, headers = header)

#reversed string
reversedString = response.text[::-1]

url = "http://challenge.code2040.org/api/reverse/validate"
jsondata = { "token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe", "string" : reversedString}
header = {"content-type": "application/json"}

response = requests.post(url, json = jsondata, headers = header)


#*******************************************************************************************************************

########3. server will send dict with string and array of strings. Find string in array and return index.
url = "http://challenge.code2040.org/api/haystack"
jsondata = { "token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe"}
header = {"content-type": "application/json"}

#response object
response = requests.post(url, json = jsondata, headers = header)

#convert json data to dictionary
received = json.loads(response.text)
indexOf = None

#search array for string and return index
for x in range(len(received["haystack"])):
    if received["needle"] == received["haystack"][x]:
        indexOf = x
        break

#resend found index to server
url = "http://challenge.code2040.org/api/haystack/validate"
jsondata = {"token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe", "needle": indexOf}
response = requests.post(url, json = jsondata, headers = header)

#*******************************************************************************************************************

#4 server will send string(a prefix) and array of strings. Return array of strings without prefix
url = "http://challenge.code2040.org/api/prefix"
jsondata = { "token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe"}
response = requests.post(url, json = jsondata, headers = header)

received = json.loads(response.text)
newlist = []

for x in received["array"]:
    if received["prefix"] != x[ :len(received["prefix"])]:
        newlist.append(x)

url = "http://challenge.code2040.org/api/prefix/validate"
jsondata = { "token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe", "array": newlist}
response = requests.post(url, json = jsondata, headers = header)

#*******************************************************************************************************************


#5. server sends json with datestamp and interval for seconds. I must return datestamp in same format and add intervals to it
url = "http://challenge.code2040.org/api/dating"
jsondata = { "token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe"}
response = requests.post(url, json = jsondata, headers = header)

received = json.loads(response.text)

def computeIso8601(received):
    #convert iso 8601 string to datetime object
    newTime = dateutil.parser.parse(received["datestamp"])
    #x = datetime.strptime( "2007-03-04T21:08:12", "%Y-%m-%dT%H:%M:%SZ" )

    #create timedelta object
    interval = received["interval"]
    addedTime = timedelta(0,interval)

    #create new variable to hold new time( add timedelta object and datetime object to create new datetime object)
    newIso =  newTime + addedTime

    #remove timezone info from end of new isoformat and append Z to keep format consistent
    newIso = newIso.replace(tzinfo=None).isoformat() + "Z"
    return newIso

url = "http://challenge.code2040.org/api/dating/validate"
jsondata = { "token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe","datestamp": computeIso8601(received)}
response = requests.post(url, json = jsondata, headers = header)
