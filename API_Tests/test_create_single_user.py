import json

import jsonpath
import requests as requests







class TestCreateSingleUser:

    def test_create_single_user(self):
        url = "https://reqres.in/api/users"
        payload = TestCreateSingleUser().create_single_user_request_data()
        request_data = json.loads(json.dumps(payload))

        response = requests.post(url, request_data)
        json_response = response.json()
        print("Response code:", response.status_code)
        print("Response length:", response.headers.get("Content-Length"))

        id = jsonpath.jsonpath(json_response, "id")
        name = jsonpath.jsonpath(json_response, "name")
        job = jsonpath.jsonpath(json_response, "job")

        print(id[0])
        print(name[0])
        print(job[0])

        assert id[0] != 0

    # Request Data
    def create_single_user_request_data(self):
        request_data = {
        "name": "arun",
        "job": "leader"
        }

        return request_data







