from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
import datetime
from datetime import datetime
import logging
logging.basicConfig(level=logging.DEBUG)

file = open("myfile.txt","w")

app = Flask(__name__)
cors = CORS(app)



##############################################################################################################
                                        # login
###############################################################################################################


def pm_loginn():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for login api")
        logging.debug(dt_string,"Inside the Login api ")
        data = request.get_json()
        Email_ID = data['email_id']
        Password = data['password']
        cursor = mydb.cursor()
        logging.debug(dt_string,"Checking for valid email")
        query = "SELECT * FROM Users WHERE Email_ID=%s"
        values = (Email_ID,)
        cursor.execute(query, values)
        users = cursor.fetchone()
        logging.debug(dt_string,"Email Checking Query executed sucessfully")
        logging.debug(dt_string,"Query result is ",users)
        if not users:
            logging.debug(dt_string,"Email id is not valid")
            return jsonify({'error': 'Email id is not valid'}), 400
        else:
            flag=True
        logging.debug(dt_string,"Checking for valid password")
        query = "SELECT * FROM Users WHERE Password=%s"
        values = (Password,)
        cursor.execute(query, values)
        users = cursor.fetchone()
        logging.debug(dt_string,"Password Checking Query executed sucessfully")
        logging.debug(dt_string,"Query result is ",users)
        if not users:
            logging.debug(dt_string,"Password is not valid")
            return jsonify({'error': 'Password is not valid'}), 400
        else:
            flag2=True
        if flag==flag2==True:
            logging.debug(dt_string,"Email id and ppassword is valid")
            logging.debug(dt_string,"Login api execution completed no error occur")
            return jsonify({"Return": "login successful"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400



##############################################################################################################
                                        # CREATE PROJECT
###############################################################################################################


def create_projects():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for create roject api")
        logging.debug(dt_string,"Inside the create project api ")
        data = request.get_json()
        logging.debug(dt_string,"payload comming from frontend ",data)
        project_name = data['project_name']
        project_description = data['project_description']
        planned_sd = data['planned_sd']
        planned_ed = data['planned_ed']
        actual_sd = data['actual_sd']
        actual_ed = data['actual_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        status = data['status']
        project_lead = data['project_lead']
        client_name = data['client_name']
        risk = data['risk']
        mitigation = data['mitigation']
        logging.debug(dt_string,"Calling create project query function ")
        return create_project_query(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                                    planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation)

    except KeyError:
        # Handle missing key error
        return jsonify({'error': 'Missing key in the request'}), 400



################################################################################################################    
                                   # UPDATE PROJECT DETAILS
############################################################################################################### 


def update_projects():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for Update project api")
        logging.debug(dt_string+"Inside the update project api ")
        data = request.get_json()
        logging.debug(dt_string+"payload received from frontend is ", data)
        project_id = data['project_id']
        project_name = data['project_name']
        project_description = data['project_description']
        planned_sd = data['planned_sd']
        planned_ed = data['planned_ed']
        actual_sd = data['actual_sd']
        actual_ed = data['actual_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        status = data['status']
        project_lead = data['project_lead']
        client_name = data['client_name']
        risk = data['risk']
        mitigation = data['mitigation']
        logging.debug(dt_string+"Calling update project query function ")
        
        if not isinstance(project_id, int):
            return jsonify({'error': 'Invalid data type for project_id'}), 400
        if not isinstance(planned_hours, str):
            return jsonify({'error': 'Invalid data type for planned_hours'}), 400
        if not isinstance(actual_hours, str):
            return jsonify({'error': 'Invalid data type for actual_hours'}), 400
        
        
        return update_project_details(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                                      planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, project_id)

    except KeyError:
        # Handle missing key error
        return jsonify({'error': 'Missing key in the request'}), 400

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500

      

###################################### GET ALL PROJECT DETAILS ###################################


def get_cardprojectdetails():
    try:
        print("inside the function")
        cursor = mydb.cursor()
        query = "SELECT * FROM Project_Details;"
        cursor.execute(query)
        projects = cursor.fetchall()
        print(projects)
        print("query executed successfully")

        project_list = []
        for project in projects:
            project_dict = {
                'Project_name': project[0],
                'Planned_sd': project[1],
                'Planned_ed': project[2],
                'Actual_sd': project[3],
                'Actual_ed': project[4]
            }
            project_list.append(project_dict)

        return jsonify(project_list)
    except Exception as e:
        print("An error occurred:", str(e))
        return jsonify({'error': 'An error occurred while fetching project details'})
    finally:
        cursor.close()







def create_task():
    try:
        data = request.get_json()
        issue_id = data['issue_id']
        description = data['description']
        status = data['status']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        priority = data['priority']
       

       

        
        return createtask(issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours,priority)

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500



def update_task():
    try:
        data = request.get_json()
        task_id = data['task_id']
        issue_id = data['issue_id']
        description = data['description']
        status = data['status']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        priority = str(data['priority'])
        

        if not isinstance(task_id, int):
            return jsonify({'error': 'Invalid data type for task_id'}), 400
        if not isinstance(issue_id, int):
            return jsonify({'error': 'Invalid data type for issue_id'}), 400
      
        

        return updatetask(description, status, task_sd, task_ed, planned_hours, actual_hours,priority,task_id, issue_id)
    

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    


############################ DELETE TASK #################################

def delete_task():
    try:
        data = request.get_json()
        task_id = data['task_id']
        cursor = mydb.cursor()


      

        return deletetask(task_id)
        

    except KeyError as e:
        # Handle missing key in the request data
        logging.error("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except Exception as e:
        # Handle any other unexpected exceptions
        logging.error("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    






    
if __name__ == "__main__":
    app.run(debug=True,port=5000)
