from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
import smtplib
import random
import logging
from datetime import datetime
from flask_bcrypt import Bcrypt

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')
bcrypt = Bcrypt(app)

###########################################################################################################
                        #to add new user(authority of  alpha user)
###########################################################################################################

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside add usder API.....")
        data = request.get_json()
        
        logging.debug(dt_string + " Taking Some inputs.....")
        
        name = data['name']
        
        email_id = data['email_id']
        
        contact = data['contact']
        

        def send_otp_email(receiver_email, otp):
            
            logging.debug(dt_string + " Entered send_otp_email function....")
            
            sender_email = "pratik@infobellit.com"  # Replace with your email address
            
            password = "mzygirleuqcwzwtk"  # Replace with your email password

            message = f"Subject: login credentials for Project Management Tool\n\n Your Username is your email.\nYour password is: {otp}"
            
            logging.debug(dt_string + " Sending email....")
            
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                
                server.login(sender_email, password)
                
                server.sendmail(sender_email, receiver_email, message)
            

        def generate_otp(length=6):
            
            logging.debug(dt_string + " Entered into generate_otp function....")
            
            digits = "0123456789abcdefghijklmnopqrstuvwxyz"
            
            otp = ""
            
            for _ in range(length):
            
                otp += random.choice(digits)
            
            logging.debug(dt_string + " OTP generated sucessfully....")
            
            return otp

        # Example usage
        email = email_id  # Replace with the recipient's email address
        
        logging.debug(dt_string + " calling generate_otp function...")
        
        otp = generate_otp()
        
        logging.debug(dt_string + " calling send_otp_email function....")
        
        send_otp_email(email, otp)
        
        print("OTP sent successfully!")


        # Hash the password
        logging.debug(dt_string + " Encrypting the generated password....")
       
        hashed_password = bcrypt.generate_password_hash(otp).decode('utf-8')

        logging.debug(dt_string + " calling user_add function to update the database....")

        return user_add(name, email_id,hashed_password, contact)

    except KeyError as e:
        # Handle missing key in the request data
        #print(dt_string + " Missing key in request data: " + str(e))
        
        return jsonify({"error": str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        print(" Database error: " + str(err))
        
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        print(" An error occurred: " + str(e))
        
        return jsonify({"error": "An error occurred: " + str(e)}), 500


############################################################################################################
                            # API to Assign a user to a particular project    
############################################################################################################



@app.route('/assign_user', methods=['POST'])
def assign_user():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " Inside assign user api...")
        data = request.get_json()
        
        logging.debug(dt_string + " Accepting some values....")

        project_id=data['project_id']
        
        user_ID =data["user_ID"]
        
        role_in_project = data["role_in_project"]
        
        logging.debug(dt_string + " checking if the project manager role already existing or not since tere can be only one project manager per project....")
        
        if(role_in_project=='Project manager'):
            
            return jsonify({"error":"Their can only be one Project manager per project"}),400
        
        else:
            
            logging.debug(dt_string + " calling user_assign function to update the databse....")
            
            return user_assign(project_id,user_ID,role_in_project)

    except KeyError as e:
        # Handle missing key in the request data
        
        #print("Missing key in request data: " + str(e))
        
        return jsonify({"error": str(e)}), 400

    except mysql.connector.Error as err:
        # Handle MySQL database-related errors
        
        print("Database error: " + str(err))
        
        return jsonify({"error": "Database error: " + str(err)}), 500

    except Exception as e:
        # Handle any other unexpected exceptions
        
        print("An error occurred: " + str(e))
        
        return jsonify({"error": "An error occurred: " + str(e)}), 500
    

