import requests
import json

########1.
# send json that includes token and github to endpoint, using http post request
url = "http://challenge.code2040.org/api/register"
jsondata = {"token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe", "github": "https://github.com/MadisonHe19/apiPractice"}
header = {"content-type": "application/json"}

# response object
response = requests.post(url, json = jsondata, headers = header)

*******************************************************************************************************************

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


*******************************************************************************************************************

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

*******************************************************************************************************************

#4 server will send string(a prefix) and array of strings. Return array of strings without prefix
