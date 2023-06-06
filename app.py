from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *

from pmt import *

from Comments_Module import *
from UserManagement_module import *
import datetime
from datetime import datetime

import logging
logging.basicConfig(level=logging.DEBUG)

file = open("myfile.txt","w")

app = Flask(__name__)
cors = CORS(app)


############################################################
#                       authentication module                    #
############################################################
from flask_bcrypt import Bcrypt
import bcrypt
bcrypt = Bcrypt(app)


@app.route('/login', methods=['POST'])
def pm_login():
    return pm_loginn()



@app.route('/create_project', methods=['POST'])
def create_project():
    return create_projects()



@app.route('/update_project', methods=['POST'])
def update_project():
    return update_projects() 


@app.route('/create_tasks', methods=['POST'])
def create_tasks():
    return create_task() 

@app.route('/update_tasks', methods=['POST'])
def update_tasks():
    return update_task() 


CORS(app, origins='*')

@app.route('/add_user', methods=['POST'])
def add_user():
    return adduser()

    

@app.route('/assign_user', methods=['POST'])
def assign_user():
   return assignuser()
   

@app.route('/add_project_comment', methods=['POST'])
def add_project_comment():
    return add_projectcomment()
   

@app.route('/add_issue_comment', methods=['POST'])
def add_issue_comment():
    return add_issuecomment()
    

@app.route('/display_projectwise_comments', methods=['POST'])
def display_projectwise_comments():
    
      return  display_projectwisecomments()
    

@app.route('/display_issuewise_comments', methods=['POST'])
def display_issuewise_comments():
        return display_issuewisecomments()
        

@app.route('/update_projectwise_comments', methods=['POST'])
def update_projectwise_comments():
    return update_projectwisecomments()
   

@app.route('/update_issuewise_comments', methods=['POST'])
def update_issuewise_comments():
    return update_issuewisecomments()
    
@app.route('/show_user', methods=['POST'])
def show_user():
    return showuser()


@app.route('/deletecomment', methods=['POST'])
def deletecomment():
    return delete_comment()

if __name__ == "__main__":
    app.run(debug=True,port=5000)
