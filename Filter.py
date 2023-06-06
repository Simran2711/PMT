from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
from workflow import *
from collections import defaultdict
import datetime
from datetime import datetime
import logging
mydb=connect_db()
cursor=mydb.cursor()

logging.basicConfig(level=logging.DEBUG)

from datetime import datetime, timedelta

# Get the current date



def IssueFilterationMonth():
    try:
        current_date = datetime.now()
        last_month_date = current_date - timedelta(days=current_date.day)
        last_month_date = last_month_date.replace(day=1)

# Calculate the last week's date
        last_week_date = current_date - timedelta(weeks=1)
        last_quarter_date = current_date.replace(month=((current_date.month - 1) // 3) * 3 + 1, day=1) - timedelta(days=1)

# Print the results
        print("Last current date:", current_date.date())
        print("Last month's date:", last_month_date.date())
        print("Last week's date:", last_week_date.date())
        print("Last quarter's date:", last_quarter_date.date())
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for Filteration Month api")
        logging.debug(dt_string+" Inside the Filteratio Month api ")
        data = request.get_json()
        logging.debug(dt_string+" payload received from frontend is ")
        print(data)
        project_id = data["project_id"]
        print(project_id)
        if type(project_id) is not int:
            return jsonify({"Error": "Wrong data type of project id"}), 400
        query1 = "SELECT count(i.issue_id) FROM issue_member i INNER JOIN task t ON i.issue_id = t.issue_id WHERE project_id=%s and (t.task_sd between %s and %s);"
        values = (project_id,str(last_month_date.date()),str(current_date.date()))
        cursor.execute(query1, values)
        list1=cursor.fetchall()
        query2 = "SELECT count(i.issue_id) FROM issue_member i INNER JOIN defect d ON i.issue_id = d.issue_id where project_id=%s and (d.defect_sd between %s and %s);"
        values = (project_id,str(last_month_date.date()),str(current_date.date()))
        cursor.execute(query2, values)
        list2=cursor.fetchall()
        task=list1[0]
        print("task =", task)
        defect=list2[0]
        print("defect =", defect)
        issue=task[0]+defect[0]
        print("issue =",issue)
        logging.debug(dt_string+" Query Exectued successfully ")
        logging.debug(dt_string+" issue_Number API is executed successfully")
        return jsonify({"Issue":issue}), 200 
    
    except Exception as e:
        return jsonify({"error": "bad values"}), 400
    
def IssueFilterationWeek():
    try:
        current_date = datetime.now()
        last_month_date = current_date - timedelta(days=current_date.day)
        last_month_date = last_month_date.replace(day=1)

# Calculate the last week's date
        last_week_date = current_date - timedelta(weeks=1)
        last_quarter_date = current_date.replace(month=((current_date.month - 1) // 3) * 3 + 1, day=1) - timedelta(days=1)

# Print the results
        print("Last current date:", current_date.date())
        print("Last month's date:", last_month_date.date())
        print("Last week's date:", last_week_date.date())
        print("Last quarter's date:", last_quarter_date.date())
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for Filteration Week api")
        logging.debug(dt_string+" Inside the Filteratio Week api ")
        data = request.get_json()
        logging.debug(dt_string+" payload received from frontend is ")
        print(data)
        project_id = data["project_id"]
        print(project_id)
        if type(project_id) is not int:
            return jsonify({"Error": "Wrong data type of project id"}), 400
        query1 = "SELECT count(i.issue_id) FROM issue_member i INNER JOIN task t ON i.issue_id = t.issue_id WHERE project_id=%s and (t.task_sd between %s and %s);"
        values = (project_id,str(last_week_date.date()),str(current_date.date()))
        cursor.execute(query1, values)
        list1=cursor.fetchall()
        query2 = "SELECT count(i.issue_id) FROM issue_member i INNER JOIN defect d ON i.issue_id = d.issue_id where project_id=%s and (d.defect_sd between %s and %s);"
        values = (project_id,str(last_week_date.date()),str(current_date.date()))
        cursor.execute(query2, values)
        list2=cursor.fetchall()
        task=list1[0]
        print("task =", task)
        defect=list2[0]
        print("defect =", defect)
        issue=task[0]+defect[0]
        print("issue =",issue)
        logging.debug(dt_string+" Query Exectued successfully ")
        logging.debug(dt_string+" issue_Number API is executed successfully")
        return jsonify({"Issue":issue}), 200 
    
    except Exception as e:
        return jsonify({"error": "bad values"}), 400

def IssueFilterationQuarterly():
    try:
        current_date = datetime.now()
        last_month_date = current_date - timedelta(days=current_date.day)
        last_month_date = last_month_date.replace(day=1)

# Calculate the last week's date
        last_week_date = current_date - timedelta(weeks=1)
        last_quarter_date = current_date.replace(month=((current_date.month - 1) // 3) * 3 + 1, day=1) - timedelta(days=1)

# Print the results
        print("Last current date:", current_date.date())
        print("Last month's date:", last_month_date.date())
        print("Last week's date:", last_week_date.date())
        print("Last quarter's date:", last_quarter_date.date())
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for Filteration Quarter api")
        logging.debug(dt_string+" Inside the Filteratio api ")
        data = request.get_json()
        logging.debug(dt_string+" payload received from frontend is ")
        print(data)
        project_id = data["project_id"]
        print(project_id)
        if type(project_id) is not int:
            return jsonify({"Error": "Wrong data type of project id"}), 400
        query1 = "SELECT count(i.issue_id) FROM issue_member i INNER JOIN task t ON i.issue_id = t.issue_id WHERE project_id=%s and (t.task_sd between %s and %s);"
        values = (project_id,str(last_quarter_date.date()),str(current_date.date()))
        cursor.execute(query1, values)
        list1=cursor.fetchall()
        query2 = "SELECT count(i.issue_id) FROM issue_member i INNER JOIN defect d ON i.issue_id = d.issue_id where project_id=%s and (d.defect_sd between %s and %s);"
        values = (project_id,str(last_quarter_date.date()),str(current_date.date()))
        cursor.execute(query2, values)
        list2=cursor.fetchall()
        task=list1[0]
        print("task =", task)
        defect=list2[0]
        print("defect =", defect)
        issue=task[0]+defect[0]
        print("issue =",issue)
        logging.debug(dt_string+" Query Exectued successfully ")
        logging.debug(dt_string+" issue_Number API is executed successfully")
        return jsonify({"Issue":issue}), 200 
    
    except Exception as e:
        return jsonify({"error": "bad values"}), 400
    

def DetailedIssueFilteration():
    try:
        current_date = datetime.now()
        last_month_date = current_date - timedelta(days=current_date.day)
        last_month_date = last_month_date.replace(day=1)

# Calculate the last week's date
        last_week_date = current_date - timedelta(weeks=1)
        last_quarter_date = current_date.replace(month=((current_date.month - 1) // 3) * 3 + 1, day=1) - timedelta(days=1)

# Print the results
        print("Last current date:", current_date.date())
        print("Last month's date:", last_month_date.date())
        print("Last week's date:", last_week_date.date())
        print("Last quarter's date:", last_quarter_date.date())
        now = datetime.now()
        dt_string = str(now.strftime("%d/%m/%Y %H:%M:%S"))
        logging.debug(dt_string+" User has made a call for Filteration Quarter api")
        logging.debug(dt_string+" Inside the Filteratio api ")
        query1 = "SELECT i.project_id,count(i.issue_id) FROM issue_member i INNER JOIN task t ON i.issue_id = t.issue_id WHERE t.task_sd between %s and %s group by i.project_id;"
        values = (str(last_month_date.date()),str(current_date.date()))
        cursor.execute(query1, values)
        M_task=cursor.fetchall()
        query2 = "SELECT i.project_id,count(i.issue_id) FROM issue_member i INNER JOIN defect d ON i.issue_id = d.issue_id where d.defect_sd  between %s and %s group by i.project_id;;"
        values = (str(last_month_date.date()),str(current_date.date()))
        cursor.execute(query2, values)
        M_defect=cursor.fetchall()
        result_M_defect = {key: value for key, value in M_defect}
        #print(result_M_defect)
        result_M_task = {key: value for key, value in M_task}
        #print(result_M_task)
        Issue_Month = defaultdict(int)
        for key, value in result_M_defect.items():
            Issue_Month[key] += value
        for key, value in result_M_task.items():
            Issue_Month[key] += value
           # print(dict(Issue_Month))
        print(Issue_Month)
        query3 = "SELECT i.project_id,count(i.issue_id) FROM issue_member i INNER JOIN task t ON i.issue_id = t.issue_id WHERE t.task_sd between %s and %s group by i.project_id;"
        values = (str(last_week_date.date()),str(current_date.date()))
        cursor.execute(query3, values)
        W_task=cursor.fetchall()
        query4 = "SELECT i.project_id,count(i.issue_id) FROM issue_member i INNER JOIN defect d ON i.issue_id = d.issue_id where d.defect_sd  between %s and %s group by i.project_id;;"
        values = (str(last_week_date.date()),str(current_date.date()))
        cursor.execute(query4, values)
        W_defect=cursor.fetchall()
        result_W_defect = {key: value for key, value in W_defect}
        #print(result_W_defect)
        result_W_task = {key: value for key, value in W_task}
        #print(result_W_task)
        Issue_Week = defaultdict(int)
        for key, value in result_W_defect.items():
            Issue_Week[key] += value
        for key, value in result_W_task.items():
           Issue_Week[key] += value
        print(Issue_Week)
        query5 = "SELECT i.project_id,count(i.issue_id) FROM issue_member i INNER JOIN task t ON i.issue_id = t.issue_id WHERE t.task_sd between %s and %s group by i.project_id;"
        values = (str(last_quarter_date.date()),str(current_date.date()))
        cursor.execute(query5, values)
        Q_task=cursor.fetchall()
        query5 = "SELECT i.project_id,count(i.issue_id) FROM issue_member i INNER JOIN defect d ON i.issue_id = d.issue_id where d.defect_sd  between %s and %s group by i.project_id;;"
        values = (str(last_quarter_date.date()),str(current_date.date()))
        cursor.execute(query5, values)
        Q_defect=cursor.fetchall()
        result_Q_defect = {key: value for key, value in Q_defect}
        #print(result_W_defect)
        result_Q_task = {key: value for key, value in Q_task}
        #print(result_W_task)
        Issue_Quarterly = defaultdict(int)
        for key, value in result_Q_defect.items():
            Issue_Quarterly[key] += value
        for key, value in result_Q_task.items():
           Issue_Quarterly[key] += value
        print(Issue_Quarterly)
        logging.debug(dt_string+" Query Exectued successfully ")
        logging.debug(dt_string+" issue_Number API is executed successfully")
        return jsonify({"Monthly":Issue_Month,"Weekly":Issue_Week,"Quarterly":Issue_Quarterly}), 200 
    
    except Exception as e:
        return jsonify({"error": "bad values"}), 400