import json

import jsonpath
import requests as requests

url = "https://reqres.in/api/users/2"

file = open("/Users/surendrakumar.tv/PycharmProjects/PythonPytestAPI/user_update.json","r")

request = file.read()
request_data = json.loads(request)

response = requests.put(url,request_data)

response_data = response.json()
print(response_data)

name  = jsonpath.jsonpath(response_data,"name")
job = jsonpath.jsonpath(response_data,"job")

print(name[0])
print(job[0])