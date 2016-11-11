import requests
import json

########1.
# send json that includes token and github to endpoint, using http post request

url = "http://challenge.code2040.org/api/register"
jsondata = {"token": "afa5d2bbbd8c9e0fb41eaf1cc1fd28fe", "github": "https://github.com/MadisonHe19/apiPractice"}
header = {"content-type": "application/json"}

# response object
r = requests.post(url, json = jsondata, headers = header)


########2.
