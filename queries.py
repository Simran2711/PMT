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

     


#    Shrishti


def user_add(name, email_id,hashed_password, contact):
        """This endpoint is used to add a new user to the system. It expects the user's name, email ID, contact information, and generates an OTP (One-Time Password) to be sent to the user's email address. The user's information, along with the hashed OTP, is then stored in the database."""
        query = "INSERT INTO users ( Name, Email_ID, password ,Contact) VALUES (%s, %s, %s,%s);"
        values = ( name, email_id,hashed_password, contact)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "User created successfully."}), 200


def user_assign(project_id,user_ID,role_in_project):
            """This endpoint is used to assign a user to a particular project. It expects the project ID, user ID, and the user's role in the project. If the role is "Project manager," it returns a message indicating that there can only be one project manager per project. Otherwise, it adds the user to the project and returns a list of all users assigned to that project."""
            query = "INSERT INTO project_member(project_id,user_id,role_in_project) VALUES (%s, %s,%s)"
            values = (project_id,user_ID,role_in_project)
            cursor.execute(query, values)
            mydb.commit()
            # to fetch id of newly added member and all user_ids
            #query = "select user_id, name ,roles,Email_id,contact from users where user_id in (select user_id from project_member where project_id=%s);"
            query = "select u.user_id, name ,role_in_project , email_id,contact from users u ,project_member m where u.user_id=m.user_id and project_id=%s"
            values = (project_id,)
            cursor.execute(query, values)
           
            id=cursor.fetchall()
            user_list = []
            for project in id:
                    user_dict = {
                        'user_id': project[0],
                        'name': project[1],
                        'roles_in_project': project[2],
                        'Email_id' : project[3],
                        'contact' : project[4]
                    }
                    user_list.append(user_dict)
            return jsonify(user_list)


def project_commentadd(project_id,description,user_id):
        """This endpoint is used to add a comment to a project. It expects the project ID, user ID, and the comment description. The comment is then stored in the database, and the newly added comment, along with other comments for that project, is returned."""
        query = "INSERT INTO comments(id,description,user_id,date) VALUES (%s, %s,%s,now())"
        values = (project_id,description,user_id)
        cursor.execute(query, values)
        mydb.commit()
        # to fetch newly added member comments
        query = "select * from comments where id=%s;"
        values = (project_id,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        comments_list = []
        for project in id:
                comments_dict = {
                    'comment_id': project[0],
                    'id': project[1],
                    'description': project[2],
                    'user_id' : project[3],
                    'date' : project[4]
                }
                comments_list.append(comments_dict)
        return jsonify(comments_list)
        

def issue_commentadd(issue_id,description,Name,user_id):
        """This endpoint is used to add a comment to an issue. It expects the issue ID, user ID, the author's name, and the comment description. The comment is then stored in the database, and the newly added comment, along with other comments for that issue, is returned."""
        query = "INSERT INTO comments(id,description,user_id,author_name,date) VALUES (%s, %s,%s,%s,now())"
        values = (issue_id,description,Name,user_id)
        cursor.execute(query, values)
        mydb.commit()
        # to fetch newly added member comments
        query = "select * from comments where id=%s;"
        values = (issue_id,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        comments_list = []
        for project in id:
                comments_dict = {
                    'comment_id': project[0],
                    'id': project[1],
                    'description': project[2],
                    'user_id' : project[3],
                    'author_name': project[4],
                    'date' : project[5]
                }
                comments_list.append(comments_dict)
        return jsonify(comments_list)
 
def displaycomments_projectswise(project_id):
        """This endpoint is used to display all the comments related to a specific project. It expects the project ID and retrieves all the comments associated with that project from the database. The comments are returned as a JSON response"""
        query = "select comment_id,user_id,description,author_name,date from comments where id=%s"
        values = (project_id,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        comments_list = []
        for project in id:
                comments_dict = {
                    'comment_id': project[0],
                    'user_id' : project[1],
                    'description': project[2],
                    'author_name' : project[3],
                    'date' : project[4]
                }
                comments_list.append(comments_dict)
        return jsonify(comments_list)


def displaycomments_issuewise(issue_id):
        """This endpoint is used to display all the comments related to a specific issue. It expects the project ID and issue ID and retrieves all the comments associated with that issue from the database. The comments are returned as a JSON response."""
        query = "select comment_id,user_id,description,author_name,date from comments where id = %s"
        values = (issue_id,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        comments_list = []
        for project in id:
                comments_dict = {
                    'comment_id': project[0],
                    'user_id' : project[1],
                    'description': project[2],
                    'author_name' : project[3],
                    'date' : project[4]
                }
                comments_list.append(comments_dict)
        return jsonify(comments_list)

# Shrishti