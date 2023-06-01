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

file = open("myfile.txt","w")

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')


############################################################
#                       workflow module                    #
############################################################


@app.route('/GetWorkFlow', methods=['POST'])
def GetWorkFlow():
    getwf()
    return ({"msg":"done"})



@app.route('/StatusUpdate', methods=['POST'])
def StatusUpdate():
    statusupdate()
    return ({"msg":"done"})


@app.route('/GetWorkflowIssue', methods=['POST'])
def GetWorkflowIssue():
    getworkflowussue()
    return ({"msg":"done"})
    
if __name__ == "__main__":
    app.run(debug=True,port=5000)