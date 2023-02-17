import json

import jsonpath
import requests as requests

# API url
url = "https://reqres.in/api/users?page=2"

# Send get request
response = requests.get(url)

#Display response content

"""
print("response:",response.json())
print("headers:",response.headers)
print("Status code:",response.status_code)
"""

#Parse response to Json format

json_response = json.loads(response.text)
#or
json_response = response.json()

#print(json_response)

#Fetch value using json path

pages = jsonpath.jsonpath(json_response,"total_pages")
print(pages[0])

assert pages[0] == 2

first_name_list = jsonpath.jsonpath(json_response,"data[*].first_name")

print(first_name_list)