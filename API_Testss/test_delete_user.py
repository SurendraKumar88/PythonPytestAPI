
import requests as requests

class TestDeleteUser:
    def test_deleteuser(self):

        url = "https://reqres.in/api/users/2"

        # Send get request
        response = requests.delete(url)

        # fetch response code
        print(response.status_code)
        assert 204 == response.status_code
