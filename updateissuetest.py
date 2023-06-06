import json
import unittest
import requests


class UpdateIssue(unittest.TestCase):
    API_ENDPOINT = "http://127.0.0.1:5000/update_issue"



    def test_update_issue_api_testing_by_giving_missing_parameter(self):
        print("#" * 50)
        print("Test case id: TMP01")
        print("Test case name: Missing parameter")
        print("Inside the Test Case")

        # Prepare the data for updating the issue with missing parameter
        data = {
            "issue_id": 3000,
            "issue_name": "New Issue Name"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint to update the issue
        r = requests.post(url=self.API_ENDPOINT, data=json.dumps(data), headers=headers)

        # Print the response status code
        print("Response status code:", r.status_code)

        # Get the response content as JSON
        response_data = r.json()

        # Print the JSON response
        print("Response content:", response_data)
        print("")

        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(r.status_code, 400)
        # Assert the response error message
        #self.assertEqual(response_data["error"], "Missing required parameter(s)")

    

    def test_update_issue_api_testing_by_giving_non_existent_parameter(self):
        print("#" * 50)
        print("Test case id: TNE02")
        print("Test case name: Non-existent issue ID")
        print("Inside the Test Case")

        # Prepare the data for updating the issue with non-existent issue ID
        data = {
            "issue_id": 999,
            "issue_name": "New Issue Name",
            "description": "Updated issue description"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint to update the issue
        r = requests.post(url=self.API_ENDPOINT, data=json.dumps(data), headers=headers)

        # Print the response status code
        print("Response status code:", r.status_code)

        # Get the response content as JSON
        response_data = r.json()

        # Print the JSON response
        print("Response content:", response_data)
        print("")

        # Assert that the response status code is 404 (Not Found)
        self.assertEqual(r.status_code, 400)
        # Assert the response error message
        self.assertEqual(response_data["error"], "Issue not found")


    def test_update_issue_api_testing_by_giving_valid_parameter(self):
        print("#" * 50)
        print("Test case id: TVU03")
        print("Test case name: Valid update")
        print("Inside the Test Case")

        # Prepare the data for updating the issue
        data = {
            "issue_id": 3013,
            "issue_name": "New Issue Name",
            "description": "Updated issue description"
        }

        # Set the headers for the request
        headers = {'Content-type': 'application/json'}

        # Send a POST request to the API endpoint to update the issue
        r = requests.post(url=self.API_ENDPOINT, data=json.dumps(data), headers=headers)

        # Print the response status code
        print("Response status code:", r.status_code)

        # Get the response content as JSON
        response_data = r.json()

        # Print the JSON response
        print("Response content:", response_data)
        print("")

        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code, 200)
        # Assert the response message
        self.assertEqual(response_data["message"], "Issue Updated Successfully")

    
   


if __name__ == '__main__':
    unittest.main()
