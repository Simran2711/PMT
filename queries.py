from connection import *
from pmt import *

# mydb = mysql.connector.connect(
#      host="localhost",
#      user="root",
#      password="postgres",
#      database="pmt",
  
#  )
# cursor = mydb.cursor()
mydb=connect_db()
cursor=mydb.cursor()




def create_user_query(name, email_id, hashed_password, contact, roles):
      
        cursor = mydb.cursor()
        query = "INSERT INTO users ( Name, Email_ID, password ,Contact, roles) VALUES (%s, %s, %s,%s,%s);"
        values = (name, email_id, hashed_password, contact, roles)
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

     


    