# API url
import requests as requests

url = "https://reqres.in/api/users/2"

# Send get request
response = requests.delete(url)

# fetch response code
print(response.status_code)
assert 204 == response.status_code
