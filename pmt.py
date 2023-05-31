from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')





##############################################################################################################
                                        # CREATE PROJECT
###############################################################################################################


@app.route('/create_project', methods=['POST'])
def create_project():
        data = request.get_json()
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

        return create_project_query(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation)
        



from flask import request, jsonify

@app.route('/projects', methods=['POST'])
def create_project():
    try:
        data = request.get_json()
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
        

        # Perform database insertion or other logic here

        response = {
            'status': 'success',
            'message': 'Project created successfully'
        }
        return jsonify(response), 200

    except KeyError as e:
        response = {
            'status': 'error',
            'message': f'Missing required field: {str(e)}'
        }
        return jsonify(response), 400

    except Exception as e:
        response = {
            'status': 'error',
            'message': f'An error occurred: {str(e)}'
        }
        return jsonify(response), 500


################################################################################################################    
                                   # UPDATE PROJECT DETAILS
############################################################################################################### 

@app.route('/update_project', methods=['POST'])
def update_project():
    data = request.get_json()
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

    return update_project_details(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, project_id)
    

##############################################################################################################    
                                     #ADD A NEW TEAM MEMBER
############################################################################################################## 



from flask_bcrypt import Bcrypt
import bcrypt
bcrypt = Bcrypt(app)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email_id = data['email_id']
    contact = data['contact']
    roles = data['roles']

    import smtplib
    import random

    def send_otp_email(receiver_email, otp):
            sender_email = "pratik@infobellit.com"  # Replace with your email address
            password = "mzygirleuqcwzwtk"  # Replace with your email password

            message = f"Subject: login credentials for Project Management Tool\n\n Your Username is your email.\nYour password is: {otp}"

            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

    def generate_otp(length=6):
        digits = "0123456789abcdefghijklmnopqrstuvwxyz"
        otp = ""
        for _ in range(length):
            otp += random.choice(digits)

        return otp

        # Example usage
    email = email_id  # Replace with the recipient's email address

    otp = generate_otp()
    send_otp_email(email, otp)
    print("OTP sent successfully!")

        # Hash the password
    hashed_password = bcrypt.generate_password_hash(otp).decode('utf-8')
    return create_user_query(name, email_id, hashed_password, contact, roles)
    

    


############################################################
#                       workflow module                    #
############################################################


@app.route('/GetWorkFlow', methods=['POST'])
def GetWorkFlow():
    try:
        data = request.get_json()
        wf = data["wf"]
        current_state = data["curr"]
        prev_state = data["prev"]
        next_state = data["succ"]
        query = "INSERT INTO workflow VALUES (%s, %s, %s, %s)"
        values = (wf, prev_state, current_state, next_state)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"done": "Data inserted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/StatusUpdate', methods=['POST'])
def StatusUpdate():
    try:
        data = request.get_json()
        status = data["status"]
        cursor = mydb.cursor()
        query = "SELECT status FROM task WHERE task_id = 1001"
        cursor.execute(query)
        current_state = cursor.fetchone()[0]
        print("current state =", current_state)
        print("state inserted by user =", status)
        
        query = "SELECT prev_state, next_state FROM workflow WHERE current_state = %s"
        values = (current_state,)
        cursor.execute(query, values)
        succ_state = cursor.fetchall()
        print(succ_state)
        print(type(succ_state))
        
        for k in succ_state:
            for j in k:
                if j.lower() == status.lower():
                    print("match")
                    print(status)
                    query = "UPDATE task SET status = %s WHERE task_id = %s"
                    values = (status, 1001)
                    cursor.execute(query, values)
                    mydb.commit()
                    return jsonify({"message": "Update successful"})
        
        print("not present")
        return jsonify({"message": "Violating workflow"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/GetWorkflowIssue', methods=['POST'])
def GetWorkflowIssue():
    try:
        data = request.get_json()
        issue = data["issueid"]
        wfn = data["wfn"]
        cursor = mydb.cursor()
        query = "INSERT INTO issueworkflow_connection (issue_id, workflow_name) VALUES (%s, %s)"
        values = (issue, wfn)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"message": "Workflow assigned to task successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})




@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.get_json()
        Task_ID = data['Task_ID']
        issue_id = data['issue_id']
        description = data['description']
        status = data['status']
        task_sd = data['task_sd']
        task_ed = data['task_ed']
        planned_hours = data['planned_hours']
        actual_hours = data['actual_hours']
        priority = data['priority']
        
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO task (Task_ID,issue_id, description, Status, task_SD, task_ED, planned_Hours, actual_Hours, priority) "
                    "VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)",
                    (Task_ID, issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours, priority))
        mydb.commit()

        task_id = cursor.lastrowid

        response = {
            'status': 'success',
            'message': 'Task created successfully',
            'task_id': task_id
        }
        return jsonify(response)
    except KeyError as e:
        response = {
            'status': 'error',
            'message': f'Missing required field: {str(e)}'
        }
        return jsonify(response), 400




 
if __name__ == "__main__":
    app.run(debug=True,port=5000)
