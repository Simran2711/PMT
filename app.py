# Importing necessary modules and libraries.

from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS, cross_origin
import bcrypt
from flask_bcrypt import bcrypt

# Creating a Flask application instance and enabling CORS (Cross-Origin Resource Sharing) for handling cross-origin requests.
app = Flask(__name__)
cors = CORS(app)

# Establishing a connection to the MySQL database using the mysql.connector module and configuring the connection parameters.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="pmt",
)

# Create a cursor to execute SQL queries
cursor = mydb.cursor()

############################ CREATE PROJECT DETAILS #################################

#Defining an API endpoint (/create_project) for creating a new project. This endpoint expects a POST request.

@app.route('/create_project', methods=['POST'])
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

        cursor = mydb.cursor()
        query = "INSERT INTO project_details (Project_Name, Project_Description, Planned_SD, Planned_ED,Actual_SD, Actual_ED, Planned_Hours, Actual_Hours, Status, Project_Lead, Client_Name,Risk, Mitigation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Project created successfully"}), 200

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


############################ UPDATE PROJECT DETAILS #################################

# Defining an API endpoint (/update) for updating an existing project. This endpoint expects a POST request.

@app.route('/update', methods=['POST'])
def update_project():
    try:
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
        cursor = mydb.cursor()
        query = "UPDATE project_details SET project_name = %s, project_description = %s, planned_sd = %s, planned_ed = %s,actual_sd = %s,actual_ed = %s,planned_hours = %s,actual_hours =%s,status = %s,project_lead = %s,client_name = %s,risk = %s,mitigation = %s where project_id = %s"
        values = (project_name, project_description, planned_sd, planned_ed, actual_sd, actual_ed,
                  planned_hours, actual_hours, status, project_lead, client_name, risk, mitigation, project_id)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"message": "Project updated successfully"}), 200

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


############################ DELETE PROJECT DETAILS #################################

# Defining an API endpoint (/delete_proj) for deleting a project. This endpoint expects a POST request.

@app.route('/delete_proj', methods=['POST'])
def delete_project():
    try:
        data = request.get_json()
        project_id = data['project_id']
        cursor = mydb.cursor()

        # Delete related records from project_member table
        member_query = "DELETE FROM project_member WHERE project_id = %s"
        values = (project_id,)
        cursor.execute(member_query, values)

        # Delete related records from issue_member table
        issue_query = "DELETE FROM issue_member WHERE project_id = %s"
        cursor.execute(issue_query, values)

        # Delete related records from project_workflow table
        projwf_query = "DELETE FROM projectworkflow_connection WHERE project_id = %s"
        cursor.execute(projwf_query, values)

        # Delete project details from project_details table
        query = "DELETE FROM project_details WHERE project_id = %s"
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Project Deleted successfully"}), 200

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


############################ CREATE ISSUE DETAILS #################################

# Defining an API endpoint (/create_issue) for creating a new issue. This endpoint expects a POST request.

@app.route('/create_issue', methods=['POST'])
def create_issue():
    try:
        data = request.get_json()
        issue_name = data['issue_name']
        description = data['description']

        cursor = mydb.cursor()
        query = "INSERT INTO issue_details (issue_name, description) VALUES (%s, %s)"
        values = (issue_name, description)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Issue created successfully"}), 200

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


############################ UPDATE ISSUE DETAILS #################################

# Defining an API endpoint (/update_issue) for updating an existing issue. This endpoint expects a POST request.

@app.route('/update_issue', methods=['POST'])
def update_issue():
    try:
        data = request.get_json()
        issue_id = data['issue_id']
        issue_name = data['issue_name']
        description = data['description']

        cursor = mydb.cursor()
        query = "UPDATE issue_details SET issue_name = %s,description = %s WHERE issue_id=%s"
        values = (issue_name, description, issue_id)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"message": "Issue Updated successfully"}), 200

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


############################ DELETE ISSUE DETAILS #################################

# Defining an API endpoint (/delete_issue) for deleting an issue. This endpoint expects a POST request.

@app.route('/delete_issue', methods=['POST'])
def delete_issue():
    try:
        data = request.get_json()
        issue_id = data['issue_id']
        cursor = mydb.cursor()

        # Delete related records from issue_member table
        member_query = "DELETE FROM issue_member WHERE issue_id = %s"
        values = (issue_id,)
        cursor.execute(member_query, values)

        # Delete related records from defect table
        defect_query = "DELETE FROM defect WHERE issue_id = %s"
        cursor.execute(defect_query, values)

        # Delete related records from Task table
        task_query = "DELETE FROM task WHERE issue_id = %s"
        cursor.execute(task_query, values)

        # Delete related records from file table
        file_query = "DELETE FROM file WHERE issue_id = %s"
        cursor.execute(file_query, values)

        # Delete related records from issue_workflow table
        issuewf_query = "DELETE FROM issueworkflow_connection WHERE issue_id = %s"
        cursor.execute(issuewf_query, values)

        # Delete project details from issue_details table
        query = "DELETE FROM issue_details WHERE issue_id = %s"
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Issue Deleted successfully"}), 200

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


# Check if the current script is being run directly as the main module
if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)


