from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
from workflow import *
import datetime
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

def getwf():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for GetWorkFlow api")
        logging.debug(dt_string+" Inside the GetWorkFlowr api ")
        data = request.get_json()
        logging.debug(dt_string+" payload received from frontend is ", data)
        wf = data["wf"]
        current_state = data["curr"]
        prev_state = data["prev"]
        next_state = data["succ"]
        query = "INSERT INTO workflow VALUES (%s, %s, %s, %s)"
        values = (wf, prev_state, current_state, next_state)
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string+" Query Exectued successfully ")
        logging.debug(dt_string+" GetWorkFlow API is executed successfully")
        return jsonify({"done": "Data inserted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

def statusupdate():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call for StatusUpdate api")
        logging.debug(dt_string+" Inside the StatusUpdate api ")
        data = request.get_json()
        status = data["status"]
        logging.debug(dt_string+" payload received from frontend is ", data)
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
        logging.debug(dt_string + " Querry is executed successfully ")
        logging.debug(dt_string + " result of query ",succ_state)
        print(succ_state)
        print(type(succ_state))
        
        for k in succ_state:
            for j in k:
                if j.lower() == status.lower():
                    logging.debug(dt_string + " checking for enter workflow is match with previous or next state ")
                    print("match")
                    print(status)
                    query = "UPDATE task SET status = %s WHERE task_id = %s"
                    values = (status, 1001)
                    cursor.execute(query, values)
                    logging.debug(dt_string + " Update status Querry is executed successfully ")
                    mydb.commit()
                    return jsonify({"message": "Update successful"})
        
        print("not present")
        return jsonify({"message": "Violating workflow"})
    except Exception as e:
        return jsonify({"error": str(e)})

def getworkflowussue():
    try:
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string + " User has made a call for get workfflow module api")
        logging.debug(dt_string+" Inside the get workfflow api ")       
        data = request.get_json()
        logging.debug(dt_string+" payload recived from frontend is ",data)
        issue = data["issueid"]
        wfn = data["wfn"]
        cursor = mydb.cursor()
        query = "INSERT INTO issueworkflow_connection (issue_id, workflow_name) VALUES (%s, %s)"
        values = (issue, wfn)
        cursor.execute(query, values)
        mydb.commit()
        logging.debug(dt_string+" querry executed successfully" )
        return jsonify({"message": "Workflow assigned to task successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})