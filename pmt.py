from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
import smtplib
import random

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')


###########################################################################################################
                        #to add new user(authority of  alpha user)
###########################################################################################################

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        name = data['name']
        email_id = data['email_id']
        contact = data['contact']
        
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

        return user_add(name, email_id,hashed_password, contact)

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print("Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500


############################################################################################################
                            # API to Assign a user to a particular project    
############################################################################################################



@app.route('/assign_user', methods=['POST'])
def assign_user():
    try:
        data = request.get_json()
        project_id=data['project_id']
        user_ID =data["user_ID"]
        role_in_project = data["role_in_project"]
        if(role_in_project=='Project manager'):
            return jsonify({"message":"Their can only be one Project manager per project"})
        else:
            return user_assign(project_id,user_ID,role_in_project)

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print("Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    

#################################################################################3
                    #API to add comment to project
##################################################################################3



@app.route('/add_project_comment', methods=['POST'])
def add_project_comment():
    try:
        data = request.get_json()
        project_id=data['project_id']
        user_id =data["user_id"]
        description=data["description"]

        return project_commentadd(project_id,description,user_id)

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print("Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    


#######################################################################################
                # Add comment to issue
#######################################################################################

@app.route('/add_issue_comment', methods=['POST'])
def add_issue_comment():
    try:
        data = request.get_json()
        issue_id=data['issue_id']
        user_id =data["user_id"]
        description=data["description"]
        Name = data["Name"]

        return issue_commentadd(issue_id,description,Name,user_id)

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print("Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500


##################################################################################################
                #api to display the comments related to a project 
##################################################################################################
@app.route('/display_projectwise_comments', methods=['POST'])
def display_projectwise_comments():
    try:
        data = request.get_json()
        project_id= data["project_id"]
        #user_id =data["user_id"]

      

        return displaycomments_projectswise(project_id)

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print("Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500


################################################################################################
                    #api to display the comments related to a issue
################################################################################################
@app.route('/display_issuewise_comments', methods=['POST'])
def display_issuewise_comments():
    try:
        data = request.get_json()
        project_id= data["project_id"]
        issue_id=data["issue_id"]
        #user_id =data["user_id"]

        return displaycomments_issuewise(issue_id)

    except KeyError as e:
        # Handle missing key in the request data
        print("Missing key in request data: " + str(e))
        return jsonify({"error": "Missing key in request data: " + str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print("Database error: " + str(err))
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print("An error occurred: " + str(e))
        return jsonify({"error": "An error occurred: " + str(e)}), 500