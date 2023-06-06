from connection import *
# MySQL configuration


mydb=connect_db()
cursor=mydb.cursor()




def user_add(name, email_id,hashed_password, contact):
        """This endpoint is used to add a new user to the system. It expects the user's name, email ID, contact information, and generates an OTP (One-Time Password) to be sent to the user's email address. The user's information, along with the hashed OTP, is then stored in the database."""
        query = "INSERT INTO users ( Name, Email_ID, password ,Contact) VALUES (%s, %s, %s,%s);"
        values = ( name, email_id,hashed_password, contact)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"message": "User created successfully."}), 200




def create_project_query(project_name, project_description, 
                   planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, 
                  client_name, risk, mitigation):
        cursor = mydb.cursor()
        query = "INSERT INTO project_details (Project_Name, Project_Description, Planned_SD, Planned_ED,Actual_SD, Actual_ED, Planned_Hours, Actual_Hours, Status, Project_Lead, Client_Name, Risk, Mitigation) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Project created successfully"}), 200




def update_project_details(project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, project_id):
        cursor = mydb.cursor()
        query = "UPDATE project_details SET project_name = %s, project_description = %s, planned_sd = %s, planned_ed = %s,actual_sd = %s,actual_ed = %s,planned_hours = %s,actual_hours =%s,status = %s,project_lead = %s,client_name = %s,risk = %s,mitigation = %s where project_id = %s"
        values = (project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, project_id)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"message": "Project updated successfully"}), 200



############################ CREATE TASK #################################

def createtask(issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours,priority):
        
        query = "INSERT INTO task (issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours,priority)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Task created successfully"}), 200

############################ UPDATE TASK #################################

def updatetask(description, status, task_sd, task_ed, planned_hours, actual_hours,priority,task_id, issue_id):
        
        query = "UPDATE task SET description = %s,status = %s,task_sd=%s, task_ed=%s, planned_hours=%s, actual_hours=%s, priority=%s WHERE task_id=%s and issue_id=%s"
        values = (description, status, task_sd, task_ed, planned_hours, actual_hours,priority,task_id, issue_id)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Task updated successfully"}), 200

############################ DELETE TASK #################################

def deletetask(task_id):
        
        query = "DELETE FROM task WHERE task_id = %s"
        values = (task_id,)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"message": "Task Deleted successfully"}), 200