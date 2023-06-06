# Importing necessary modules and libraries.
from flask import Flask, jsonify, Request
from flask_cors import CORS, cross_origin
from connection import *
from queries import *

from workflow import *
from Filter import *
import datetime
from datetime import datetime
from issue import *
from pmt import *

import logging
logging.basicConfig(level=logging.DEBUG)

# Creating a Flask application instance and enabling CORS (Cross-Origin Resource Sharing) for handling cross-origin requests.
app = Flask(__name__)

CORS(app, origins="*")

cors = CORS(app)


############################################################
#                       authentication module                    #
############################################################
from flask_bcrypt import Bcrypt
import bcrypt
bcrypt = Bcrypt(app)



@app.route('/GetWorkFlow', methods=['POST'])
def GetWorkFlow():
    return getwf()

@app.route('/StatusUpdate', methods=['POST'])
def StatusUpdate():
    return statusupdate()
  
  
@app.route('/GetWorkflowIssue', methods=['POST'])
def GetWorkflowIssue():
    return getworkflowussue()


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
    



############################################################
#                       Issue module                       #
############################################################


@app.route('/IssueByMonth', methods=['POST'])
def IssueByMonth():
    return IssueFilterationMonth()

@app.route('/IssueByWeek', methods=['POST'])
def IssueByWeek():
    return IssueFilterationWeek()

@app.route('/IssueByQuarter', methods=['POST'])
def IssueByQuarterly():
    return IssueFilterationQuarterly()

@app.route('/DetailedIssue', methods=['GET'])
def DetailedIssue():
    return DetailedIssueFilteration()

  
  
  

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

@app.route('/login', methods=['POST'])
def pm_login():
    return pm_loginn()



@app.route('/create_project', methods=['POST'])
def create_project():
    return create_projects()



@app.route('/update_project', methods=['POST'])
def update_project():
    return update_projects() 


@app.route('/create_tasks', methods=['POST'])
def create_tasks():
    return create_task() 

@app.route('/update_tasks', methods=['POST'])
def update_tasks():
    return update_task() 

    
if __name__ == "__main__":
    app.run(debug=True,port=5000)

