import json

import jsonpath
import requests as requests


url = "https://reqres.in/api/users"

data = {
    "name": "arun",
    "job": "leader"
}
#or
file = open('/Users/surendrakumar.tv/PycharmProjects/PythonPytestAPI/user.json','r')
json_input = file.read()


request_data = json.loads(json.dumps(data))

response = requests.post(url, request_data)
json_response = response.json()
print("Response code:",response.status_code)
print("Response length:",response.headers.get("Content-Length"))

print(json_response)

id = jsonpath.jsonpath(json_response,"id")
name = jsonpath.jsonpath(json_response,"name")
job = jsonpath.jsonpath(json_response, "job")

print(id[0])
print(name[0])
print(job[0])
