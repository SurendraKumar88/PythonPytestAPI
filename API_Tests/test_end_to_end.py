import json

import jsonpath
import requests


class TestEndToEnd():

    def test_create_student(self):
        url = "https://thetestingworldapi.com/api/studentsDetails"

        request_data = TestEndToEnd().payload_createStudent()
        payload = json.loads(json.dumps(request_data))

        response = requests.post(url,payload)
        assert response.status_code == 201

        student_id = jsonpath.jsonpath(response.json(),"id")[0]
        print(student_id)










    def payload_createStudent(self):
        payload = {
                     "first_name": "surendra1",
                     "middle_name": "kumar",
                     "last_name": "tv",
                     "date_of_birth": "07-11-1993"
                    }

        return payload