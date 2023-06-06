from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
from workflow import *
from Filter import *

import datetime
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

file = open("myfile.txt","w")

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')

############################################################
#                       workflow module                    #
############################################################


@app.route('/GetWorkFlow', methods=['POST'])
def GetWorkFlow():
    return getwf()

@app.route('/StatusUpdate', methods=['POST'])
def StatusUpdate():
    return statusupdate()


@app.route('/GetWorkflowIssue', methods=['POST'])
def GetWorkflowIssue():
    return getworkflowussue()

############################################################
#                       Issue module                       #
############################################################


@app.route('/IssueByMonth', methods=['POST'])
def IssueByMonth():
    return IssueFilterationMonth()

@app.route('/IssueByWeek', methods=['POST'])
def IssueByWeek():
    return IssueFilterationWeek()

@app.route('/IssueByQuarter', methods=['POST'])
def IssueByQuarterly():
    return IssueFilterationQuarterly()

@app.route('/DetailedIssue', methods=['GET'])
def DetailedIssue():
    return DetailedIssueFilteration()

if __name__ == "__main__":
    app.run(debug=True,port=5000)