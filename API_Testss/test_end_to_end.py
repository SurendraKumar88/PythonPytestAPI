import ast
import json

import jsonpath
import requests


class TestEndToEnd:
    student_id = 0
    def test_create_student(self):
        url = "https://thetestingworldapi.com/api/studentsDetails"

        print("url:",url)

        request_data = TestEndToEnd().payload_createStudent()
        payload = json.loads(json.dumps(request_data))

        print("request_data:",payload)

        response = requests.post(url,payload)
        assert response.status_code == 201

        print("response:",response.json())

        TestEndToEnd.student_id = jsonpath.jsonpath(response.json(),"id")[0]
        print(TestEndToEnd.student_id)

    def test_add_technical_details_to_student(self):
        url = "https://thetestingworldapi.com/api/technicalskills"
        print("url:", url)

        #request_data = str(TestEndToEnd().payload_Add_technicalDetails())
        #req_data = request_data.replace("ID",str(TestEndToEnd.student_id)).replace(str(-999),str(TestEndToEnd.student_id))
        #payload = json.loads(json.dumps(ast.literal_eval(req_data)))

        #or

        request_data = TestEndToEnd().payload_Add_technicalDetails()
        payload = json.loads((json.dumps(request_data)))
        payload['id'] = TestEndToEnd.student_id
        payload['st_id'] = str(TestEndToEnd.student_id)

        print("request_data:", payload)

        response = requests.post(url, payload)
        assert response.status_code == 200

        print("response:", response.json())

        status = jsonpath.jsonpath(response.json(),"status")[0]
        assert status == "true"

    def test_add_address(self):
        url = "https://thetestingworldapi.com/api/addresses"
        print("url:", url)

        request_data = TestEndToEnd().payload_add_address()
        payload = json.loads(json.dumps(request_data))
        payload['stId'] = str(TestEndToEnd.student_id)

        print("request_data:", payload)

        response = requests.post(url, payload)
        assert response.status_code == 200

        print("response:", response.json())
        status = jsonpath.jsonpath(response.json(), "status")[0]
        assert status == "true"

    def test_fetch_final_student_details(self):
        url = "https://thetestingworldapi.com/api/FinalStudentDetails/"+str(TestEndToEnd.student_id)
        print("url:", url)

        response = requests.get(url)
        assert response.status_code == 200

        print("response:", response.json())























#Payloads
    def payload_createStudent(self):
        payload = {
                     "first_name": "surendra1",
                     "middle_name": "kumar",
                     "last_name": "tv",
                     "date_of_birth": "07-11-1993"
                    }

        return payload

    def payload_Add_technicalDetails(self):
        payload = {
                      "id": -999,
                      "language": [
                        "Java",
                        "Python"
                      ],
                      "yearexp": "7",
                      "lastused": "2021",
                      "st_id": "ID"
                    }
        return payload

    def payload_add_address(self):
        payload = {
                      "Permanent_Address": {
                        "House_Number": "sample string 1",
                        "City": "sample string 2",
                        "State": "sample string 3",
                        "Country": "sample string 4",
                        "PhoneNumber": [
                          {
                            "Std_Code": "sample string 1",
                            "Home": "sample string 2",
                            "Mobile": "sample string 3"
                          },
                          {
                            "Std_Code": "sample string 1",
                            "Home": "sample string 2",
                            "Mobile": "sample string 3"
                          }
                        ]
                      },
                      "Current_Address": {
                        "House_Number": "sample string 1",
                        "City": "sample string 2",
                        "State": "sample string 3",
                        "Country": "sample string 4",
                        "PhoneNumber": [
                          {
                            "Std_Code": "sample string 1",
                            "Home": "sample string 2",
                            "Mobile": "sample string 3"
                          },
                          {
                            "Std_Code": "sample string 1",
                            "Home": "sample string 2",
                            "Mobile": "sample string 3"
                          }
                        ]
                      },
                      "stId": "ID"
                    }

        return payload