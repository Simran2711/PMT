from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
from pmt import *
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

    
if __name__ == "__main__":
    app.run(debug=True,port=5000)