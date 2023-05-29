from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt

app = Flask(__name__)
cors = CORS(app)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohan@91196",
    database="pmt",
    port=3306
)
cursor = mydb.cursor()


############################################################
############################################################


@app.route('/GetWorkFlow', methods=['POST'])
def GetWorkFlow():
        data = request.get_json()
        wf=data["wf"]
        curent_state=data["curr"]
        prev_state=data["prev"]
        next_state=data["succ"]
        query = "insert into workflow values(%s,%s,%s,%s)"
        values=(wf,prev_state,curent_state,next_state)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"done":"Data inserted succesfully"})


@app.route('/StatusUpdate', methods=['POST'])
def StatusUpdate():
        data = request.get_json()
        status=data["status"]
        cursor = mydb.cursor()
        query = "select status from task where task_id=1001;"
        cursor.execute(query,)
        current_state=cursor.fetchone()
        for i in current_state:
              c_state=i
              
        print("current state=",c_state)
        print("state inserted by user=",status)
        
        query = "select prev_state,next_state from workflow where current_state=%s"
        values=(str(c_state),)
        cursor.execute(query,values)    
        succ_state=cursor.fetchall()
        print(succ_state)
        print(type(succ_state))
        for k in succ_state:
            for j in k:
                if j.lower()==status.lower():
                        print("match")
                        print(status)
                        query = "update task set status=%s where task_id=%s"
                        values=(status,1001)
                        cursor.execute(query, values)
                        mydb.commit()
                        return jsonify({"message": "update successfull"})
        else:
               print("not present")
               return jsonify({"message": "violating workflow"})

@app.route('/GetWorkflowIssue', methods=['POST'])
def GetWorkflowIssue():
        data = request.get_json()
        issue=data["issueid"]
        wfn=data["wfn"]
        cursor = mydb.cursor()
        query = "insert into issueworkflow_connection(issue_id,workflow_name) values(%s,%s);"
        values = (issue,wfn)
        cursor.execute(query, values)
        mydb.commit()
        return jsonify({"message": "workflow assigned to task successfully"})
        

      







if __name__ == "__main__":
    app.run(debug=True)