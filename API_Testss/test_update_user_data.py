import json

import jsonpath
import requests as requests

class TestUpdateUserData:
    def test_update_userdata(self):
        url = "https://reqres.in/api/users/2"

        #file = open("/Users/surendrakumar.tv/PycharmProjects/PythonPytestAPI/user_update.json", "r")
        #request = file.read()
        #request_data = json.loads(request)

        #or

        request = TestUpdateUserData().update_single_user_request_data()
        request_data = json.loads(json.dumps(request))

        response = requests.put(url,request_data)

        response_data = response.json()
        print(response_data)

        name  = jsonpath.jsonpath(response_data,"name")
        job = jsonpath.jsonpath(response_data,"job")

        print(name[0])
        print(job[0])

        # Request Data

    def update_single_user_request_data(self):
        request_data = {
            "name": "arun_update",
            "job": "leader_update"
        }

        return request_data