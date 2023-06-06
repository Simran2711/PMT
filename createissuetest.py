import requests
import json
import unittest



class Createissue(unittest.TestCase):

 


    def test_create_issue_api_testing_by_giving_missing_parameter(self):
        print("#"*50)
        print("Test case id: TCIA01")
        print("Test case name: Checking for missing parameter ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000/create_issue"
        
        # Prepare the data for the new user
        data = {"Issue_name":"fyufjfhv"}


        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint to add the new user
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        
        print("response error code we got",r.status_code)
        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print("response content we got",pastebin_url)
        print(" ")

        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code,400)




    def test_create_issue_api_testing_by_giving_right_parameter(self):
        print("#"*50)
        print("Test case id: TCIA02")
        print("Test case name: Checking for Right Parameter ")
        print("Inside the Test Case ")
        # Define the API endpoint for adding a new user
        API_ENDPOINT_post = "http://127.0.0.1:5000/create_issue"
        

        # Prepare the data for the new user
        data = {"Issue_name":"demo", "Description":"detail"}


        # Set the headers for the request
        headers = {'Content-type': 'application/json'}
        

        # Send a POST request to the API endpoint to add the new user
        r = requests.post(url=API_ENDPOINT_post, data=json.dumps(data), headers=headers)

        # Print the response status code
        print("response error code we got",r.status_code)

        # Get the response content as JSON
        pastebin_url = r.json()

        # Print the JSON response
        print("response content we got",pastebin_url)
        print(" ")

        # Assert that the response status code is 200 (OK)
        self.assertEqual(r.status_code, 200)

    

if __name__ == "__main__":
    unittest.main()
