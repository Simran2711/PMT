# Importing necessary modules and libraries.
from flask import Flask, jsonify, Request
from flask_cors import CORS, cross_origin
from connection import *
from queries import *
from issue import *
import logging

logging.basicConfig(level=logging.DEBUG)

# Creating a Flask application instance and enabling CORS (Cross-Origin Resource Sharing) for handling cross-origin requests.
app = Flask(__name__)
CORS(app, origins="*")

############################ CREATE ISSUE DETAILS #################################

# Defining an API endpoint (/create_issue) for creating a new issue. This endpoint expects a POST request.
@app.route('/create_issue', methods=['POST'])
def create_issue():
    # Call the create_issue function from the queries module with the required arguments
    return createissue()  
    

############################ UPDATE ISSUE DETAILS #################################

# Defining an API endpoint (/update_issue) for updating an existing issue. This endpoint expects a POST request.
@app.route('/update_issue', methods=['POST'])
def update_issue():
    # Call the update_issue function from the queries module with the required arguments
    return updateissue()  # Pass the necessary arguments
    

############################ DELETE ISSUE DETAILS #################################

# Defining an API endpoint (/delete_issue) for deleting an issue. This endpoint expects a POST request.
@app.route('/delete_issue', methods=['POST'])
def delete_issue():
    # Call the delete_issue function from the queries module with the required arguments
    return deleteissue()  # Pass the necessary arguments
    

############################ CREATE TASK #################################

@app.route('/create_task', methods=['POST'])
def create_task():
    # Call the create_task function from the queries module with the required arguments
    return createtask()  # Pass the necessary arguments
    

############################ UPDATE TASK #################################

@app.route('/update_task', methods=['POST'])
def update_task():
    # Call the update_task function from the queries module with the required arguments
    return updatetask()  # Pass the necessary arguments
    

############################ DELETE TASK #################################

@app.route('/delete_task', methods=['POST'])
def delete_task():
    # Call the delete_task function from the queries module with the required arguments
    return deletetask()  # Pass the necessary arguments
 
############################ CREATE DEFECT#################################

@app.route('/create_defect', methods=['POST'])
def create_defect():

    return createdefect()

############################ UPDATE TASK #################################

@app.route('/update_defect', methods=['POST'])
def update_defect():

    return updatedefect()

############################ DELETE DEFECT #################################

@app.route('/delete_defect', methods=['POST'])
def delete_defect():

    return deletedefect()


# Check if the current script is being run directly as the main module
if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
