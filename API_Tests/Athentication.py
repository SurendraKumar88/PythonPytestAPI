import json
import requests

URL = "http://192.168.0.34/comGpsGate/api/v.1/applications/40/tokens"

headers = {
"accept": "application/json",
"Content-Type": "application/json"
}

params = {
"username": "your user name",
"password": "your password"
}

resp = requests.post(URL, headers = headers ,data=json.dumps(params))
tk = json.loads(resp.text)['token']

if resp.status_code != 200:
    print('error: ' + str(resp.status_code))
else:
    print('token: ' + str(tk))
    print('Success')