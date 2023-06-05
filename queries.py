from connection import *
#from Comments_Module import *
#from UserManagement_module import *
import logging
from datetime import datetime
import mysql.connector
mydb=connect_db()
cursor=mydb.cursor()

###############################################################################

def user_add(name, email_id,hashed_password, contact):#add role after test3
        """This endpoint is used to add a new user to the system.
          It expects the user's name, email ID, contact information,
        and generates an OTP (One-Time Password) to be sent to the user's email address. The user's information, along with the hashed OTP, is then stored in the database."""
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside user_add function.....")
        query="select 1 from users where email_id=%s;"
        values=(email_id,)
        cursor.execute(query,values)
        id=cursor.fetchone()
        if not id:
               return jsonify({"error":"email already exists."}),400

        logging.debug(dt_string + " Adding the users details into the database...")
        query = "INSERT INTO users ( Name, Email_ID, password ,Contact) VALUES (%s, %s, %s,%s);" #add role after test
        values = ( name, email_id,hashed_password, contact)#add role after test
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string + " Details successfully updated into the database....")

        return jsonify({"message": "User created successfully."}), 200


##########################################################################################

def user_show():
            now = datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            logging.debug(dt_string + " Inside user_show function.....")
            logging.debug(dt_string+"showing all the users")
            query = "select user_id,name,email_id,contact,role from users;"
            cursor.execute(query)
            id=cursor.fetchall()
            user_list = []
            for project in id:
                    user_dict = {
                        'user_id': project[0],
                        'name': project[1],
                        'Email_id' : project[2],
                        'contact' : project[3],
                        "role" : project[4]
                    }
                    user_list.append(user_dict)
            logging.debug(dt_string + " returning a list of all users...")
            return jsonify(user_list),200

#################################################################################################

def user_assign(project_id,user_ID,role_in_project):
            """This endpoint is used to assign a user to a particular project. 
            It expects the project ID, user ID, and the user's role in the project.
              If the role is "Project manager," it returns a message indicating that there can only be one project manager per project. Otherwise, it adds the user to the project and returns a list of all users assigned to that project."""
            
            now = datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            logging.debug(dt_string + " Inside user_assign function.....")

            query="select * from project_details where project_id=%s"
            values=(project_id,)
            cursor.execute(query,values)
            a=cursor.fetchall()
            if not a:
                return jsonify({"error": "Invalid project_id"}), 400
            logging.debug(dt_string + " Inside user_assign ")

            
            query="select * from users where user_id=%s"
            values=(user_ID,)
            cursor.execute(query,values)
            a=cursor.fetchall()
            if not a:
                return jsonify({"error": "Invalid user_id"}), 400

            query = "select * from project_member where user_id=%s and project_id=%s;"
            values=(user_ID,project_id)
            cursor.execute(query,values)
            id=cursor.fetchone()
            if id:
                   return jsonify({"error":"User already associated with the project."}),400
            
            logging.debug(dt_string + " Associating the user with the requisite project...")
            query = "INSERT INTO project_member(project_id,user_id,role_in_project) VALUES(%s,%s,%s);"
            values = (project_id,user_ID,role_in_project)
            cursor.execute(query, values)
            mydb.commit()
            logging.debug(dt_string + " The user successfully associated with the project....")
            # to fetch id of newly added member and all user_ids
            #query = "select user_id, name ,roles,Email_id,contact from users where user_id in (select user_id from project_member where project_id=%s);"
            logging.debug(dt_string + " Getting a list of all users associated with the requisite project...")
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
            logging.debug(dt_string + " returning a list of all users...")
            return jsonify(user_list),200

############################################################################################

def project_commentadd(project_id,description,user_id):
        """This endpoint is used to add a comment to a project.
          It expects the project ID, user ID, and the comment description. 
          The comment is then stored in the database, and the newly added comment, along with other comments for that project, is returned."""
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside project_commentadd function .....")
        logging.debug(dt_string +  " Adding comment to the project....")

        query = "select Name from users where user_id =%s"
        values = (user_id,)
        cursor.execute(query,values)
        a_name=cursor.fetchone()
        if not a_name:
            return jsonify({"error": "Invalid user_id"}), 400
        author_name=a_name[0]
        
        print(author_name)
        logging.debug(dt_string + "noted....")
        
        query = "INSERT INTO comments(id, description, user_id, author_name, date) VALUES (%s, %s, %s, %s, now())"
        values = (project_id, description, user_id, author_name)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug(dt_string + " Comment successfully added....")
        # to fetch newly added member comments
        logging.debug(dt_string + " getting all the comments associated with this project....")
        query = "select * from comments where id=%s;"
        values = (project_id,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        logging.debug(dt_string + " All comments fetched sucessfully....")
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
        logging.debug(dt_string + " returning all the comments associated with project.")
        return jsonify(comments_list),200


#######################################################################################

def issue_commentadd(issue_id,description,user_id):
        """This endpoint is used to add a comment to an issue.
          It expects the issue ID, user ID, the author's name, and the comment description. 
          The comment is then stored in the database, and the newly added comment, along with other comments for that issue, is returned."""
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside issue_commentadd function.....")
        logging.debug(dt_string + " Adding new comment to issue_id passed ", issue_id)

        query = "select Name from users where user_id =%s"
        values = (user_id,)
        cursor.execute(query, values)
        a_name=cursor.fetchone()
        if not a_name:
            return jsonify({"error": "Invalid user_id"}), 400
        author_name=a_name[0]

        query = "INSERT INTO comments(id,description,user_id,author_name,date) VALUES (%s, %s,%s,%s,now())"
        values = (issue_id,description,user_id,author_name)
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string + " Comment added sucessfully to issue_id ", issue_id)
        # to fetch newly added member comments
        logging.debug(dt_string + " Fetching all the comments related to issue ", issue_id)
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
        logging.debug(dt_string + " Returning the list of all the comments related to this issue...")
        return jsonify(comments_list),200

##############################################################################

def displaycomments_projectswise(project_id):
        """This endpoint is used to display all the comments related to a specific project. 
        It expects the project ID and retrieves all the comments associated with that project from the database. 
        The comments are returned as a JSON response"""

        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside displaycomments_projectwise function.....")
        logging.debug(dt_string + " Fetching all the comments related to this project with project_id ",project_id)
        query = "select comment_id,user_id,description,author_name,date from comments where id=%s;"
        values = (project_id,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        if(id is None):
                return jsonify({"error":"no project found with this project_id"}),400
        
        logging.debug(dt_string + " All the comments if exists fetched sucessfuly ....")
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
        if(len(comments_list)==0 ):
            return jsonify({"error":"no matching results"}),400
        else:
            logging.debug(dt_string + " returning the list of all comments for the project with project_id ", project_id)
            return jsonify(comments_list),200
        

############################################################################################

def displaycomments_issuewise(issue_id):
        """This endpoint is used to display all the comments related to a specific issue. 
        It expects the project ID and issue ID and retrieves all the comments associated with that issue from the database.
          The comments are returned as a JSON response."""
        
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside displaycomments_issuewise function.....")
        logging.debug(dt_string +  " Fetching all the comments related to the issue with issue_id ",issue_id)
        query = "select comment_id,user_id,description,author_name,date from comments where id = %s"
        values = (issue_id,)
        cursor.execute(query, values)
        id=cursor.fetchall()
        if(id is None):
                return jsonify({"error":"no issue found with this issue_id"}),400

        logging.debug(dt_string + " All comments fetched sucessfully...")
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

        if(len(comments_list)==0 ):
            return jsonify({"error":"no matching results"}),400
        else:
            logging.debug(dt_string + " Returning all the comments related to issueId ",issue_id)
            return jsonify(comments_list),200

####################################################################################

def updateprojectwise_comments(user_id, description, comment_id, project_id):
    """
    Updates a project-wise comment in the database.

    Args:
        user_id (int): The ID of the user making the comment.
        description (str): The updated comment description.
        author_name (str): The author's name.
        comment_id (int): The ID of the comment to be updated.
        project_id (int): The ID of the project.

    Returns:
        list: A list of dictionaries representing the updated comments for the project, each containing the comment details.

    Raises:
        Exception: If there is an error executing the SQL queries.
    """

    now = datetime.now()
    dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
    logging.debug(dt_string + " Inside updateprojectwise_comments function.....")
    logging.debug(dt_string + "fetching the author name based on user_id")
    # Fetch the author_name from the users table

    query = "SELECT Name FROM users WHERE user_id = %s"
    values = (user_id,)
    cursor.execute(query, values)
    a_name=cursor.fetchone()
    if not a_name:
            return jsonify({"error": "Invalid user_id"}), 400
    author_name=a_name[0]  # Assign the fetched result to a variable
    logging.debug(dt_string + " The author name fetched sucessfully.... ")
    # Update the comment
    logging.debug(dt_string + " Updating the comment...")
    query="select * from comments where comment_id=%s "
    values=(comment_id,)
    cursor.execute(query,values)
    a=cursor.fetchone()
    if not a:
            return jsonify({"error": "Invalid comment_id"}), 400
    logging.debug(dt_string + " Updating the comment")
    query = "UPDATE comments SET description = %s, user_id = %s, author_name = %s , date=now() WHERE comment_id = %s;"
    values = (description, user_id, author_name, comment_id)
    cursor.execute(query, values)
    mydb.commit()
    logging.debug(dt_string + " Comment updated sucessfully...")

    # Retrieve the updated comments for the project
    logging.debug(dt_string + " Fetching all the comments along with the upade")
    query = "SELECT comment_id, user_id, description, author_name, date FROM comments WHERE id = %s"
    values = (project_id,)
    cursor.execute(query, values)

    updated_comments = cursor.fetchall()
    logging.debug(dt_string + " All comments fetched successfully....")
    comments_list = []
    for project in updated_comments:
        comments_dict = {
            'comment_id': project[0],
            'user_id': project[1],
            'description': project[2],
            'author_name': project[3],
            'date': project[4]
        }
        comments_list.append(comments_dict)

    logging.debug(dt_string + " Returing the list of all comments...")
    return jsonify(comments_list)

##########################################################################

def updateissuewise_comments(user_id,description,comment_id,issue_id):
                """Update an issue comment with the provided details.

                Args:
                user_id (int): The ID of the user updating the comment.
                description (str): The updated comment description.
                comment_id (int): The ID of the comment to update.
                issue_id (int): The ID of the issue associated with the comment.

                Returns:
                A JSON response containing the updated comment details.

                Raises:
                Exception: If an error occurs during the update process.
                """
        
                now = datetime.now()
                dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
                logging.debug(dt_string + " Inside updateissuewise_comments API.....")

                logging.debug(dt_string + " fetching name from the given the user_id")
                
                query = "select Name from users where user_id =%s"
                values = (user_id,)
                cursor.execute(query, values)
                a_name=cursor.fetchone()
                if not a_name:
                        return jsonify({"error": "Invalid user_id"}), 400
                author_name=a_name[0]  # Assign the fetched result to a variable
                logging.debug(dt_string + " Assigned the fetched name to author name.")
                logging.debug(dt_string + " Updating the comment related details into the databse....")

                query="select * from comments where comment_id=%s "
                values=(comment_id,)
                cursor.execute(query,values)
                a=cursor.fetchone()
                if not a:
                    return jsonify({"error": "Invalid comment_id"}), 400

                query = "update comments set description=%s,user_id=%s,author_name=%s where comment_id=%s;"
                values = (description,user_id,author_name,comment_id)
                cursor.execute(query, values)
                mydb.commit()
                logging.debug(dt_string + " updation done successfully....")
                logging.debug(dt_string + " Fetching all the comments ...")
                query = "select comment_id,user_id,description,author_name,date from comments where id = %s"
                values = (issue_id,)
                cursor.execute(query, values)

                id=cursor.fetchall()
                logging.debug(dt_string + " Comments fetched successfully....")
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
                logging.debug(dt_string + " Returning the comments list for the issue with issue_id ",issue_id)
                return jsonify(comments_list)

#######################################################################################

def delete_comments(comment_id):
            """it deletes a comment based on comment_id"""
            now = datetime.now()
            dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
            logging.debug(dt_string + " Inside delete_comments function.....")
            
            query="select * from comments where comment_id=%s "
            values=(comment_id,)
            cursor.execute(query,values)
            a=cursor.fetchone()
            if not a:
                    return jsonify({"error": "Invalid comment_id"}), 400

            query = "delete from comments where comment_id=%s;"
            values= (comment_id,)
            cursor.execute(query,values)
            mydb.commit()
            
            return jsonify({"msg":"Comment deleted sucessfully"}),200

