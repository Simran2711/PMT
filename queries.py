from connection import *
from datetime import datetime
import logging


mydb=connect_db()
cursor=mydb.cursor()

############################ CREATE ISSUE DETAILS #################################

def create_issue(Issue_name, Description):
        query = "INSERT INTO issue_details (issue_name, description) VALUES (%s, %s)"
        values = (Issue_name, Description)
        cursor.execute(query, values)
        mydb.commit()
    
        
        logging.debug("Issue created: issue_name={}, description={}".format(Issue_name, Description))
        return jsonify({"message": "Issue created successfully"}), 200


########################### UPDATE ISSUE DETAILS #################################

def updateissues(issue_name, description, issue_id):
   

        query = "UPDATE issue_details SET issue_name = %s,description = %s WHERE issue_id=%s"
        values = (issue_name, description, issue_id)
        cursor.execute(query, values)
        mydb.commit()

        return jsonify({"message": "Issue Updated Successfully"}), 200



############################ DELETE ISSUE DETAILS #################################

def deleteissue(issue_id):
        
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

        
        logging.debug("Issue deleted: issue_id={}".format(issue_id))
        return jsonify({"message": "Issue Deleted successfully"}), 200

############################ CREATE TASK #################################

def createtask(issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours,priority):
        
        query = "INSERT INTO task (issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours,priority)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Task created: issue_id={}, description={}, status={}, task_sd={}, task_ed={}, planned_hours={}, actual_hours={}, priority={}".format(issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours, priority))
        return jsonify({"message": "Task created successfully"}), 200

############################ UPDATE TASK #################################

def updatetask(description, status, task_sd, task_ed, planned_hours, actual_hours,priority,task_id, issue_id):
        
        query = "UPDATE task SET description = %s,status = %s,task_sd=%s, task_ed=%s, planned_hours=%s, actual_hours=%s, priority=%s WHERE task_id=%s and issue_id=%s"
        values = (description, status, task_sd, task_ed, planned_hours, actual_hours,priority,task_id, issue_id)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Task updated: task_id={}, issue_id={}, description={}, status={}, task_sd={}, task_ed={}, planned_hours={}, actual_hours={}, priority={}".format(task_id, issue_id, description, status, task_sd, task_ed, planned_hours, actual_hours, priority))
        return jsonify({"message": "Task updated successfully"}), 200

############################ DELETE TASK #################################

def deletetask(task_id):
        
        query = "DELETE FROM task WHERE task_id = %s"
        values = (task_id,)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Task deleted: task_id={}".format(task_id))
        return jsonify({"message": "Task Deleted successfully"}), 200

############################ CREATE DEFECT #################################

def createdefect(issue_id, description, status,severity, defect_sd, defect_ed, planned_hours, actual_hours):

        query = "INSERT INTO defect (issue_id, description, status, severity, defect_sd, defect_ed, planned_hours, actual_hours) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (issue_id, description, status,severity, defect_sd, defect_ed, planned_hours, actual_hours)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Defect created: issue_id={}, description={}, status={}, severity={}, defect_sd={}, defect_ed={}, planned_hours={}, actual_hours={}".format(issue_id, description, status, defect_sd, defect_ed, planned_hours, actual_hours))
        return jsonify({"message": "Defect created successfully"}), 200

############################ UPDATE DEFECT #################################

def updatedefect(description, status, severity, defect_sd, defect_ed, planned_hours, actual_hours,defect_id, issue_id):
        
        query = "UPDATE defect SET description = %s,status = %s,severity = %s, defect_sd=%s, defect_ed=%s, planned_hours=%s, actual_hours=%s WHERE defect_id=%s and issue_id=%s"
        values = (description, status,severity, defect_sd, defect_ed, planned_hours, actual_hours,defect_id, issue_id)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Defect updated: defect_id={}, issue_id={}, description={}, status={},severity={} ,defect_sd={}, defect_ed={}, planned_hours={}, actual_hours={}".format(defect_id, issue_id, description, status,severity, defect_sd, defect_ed, planned_hours, actual_hours))
        return jsonify({"message": "Defect updated successfully"}), 200

############################ DELETE DEFECT #################################

def deletedefect(defect_id):
        
        query = "DELETE FROM defect WHERE defect_id = %s"
        values = (defect_id,)
        cursor.execute(query, values)
        mydb.commit()

        logging.debug("Defect deleted: defect_id={}".format(defect_id))
        return jsonify({"message": "Defect Deleted successfully"}), 200
