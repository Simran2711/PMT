from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS,cross_origin
import bcrypt
from flask_bcrypt import bcrypt
from connection import *
from queries import *
from Comments_Module import *
from UserManagement_module import *
import datetime
from datetime import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

file = open("myfile.txt","w")

app = Flask(__name__)
cors = CORS(app)
CORS(app, origins='*')

@app.route('/add_user', methods=['POST'])
def add_user():
    return ({"msg":"done"})

@app.route('/assign_user', methods=['POST'])
def assign_user():
   return ({"msg":"done"})

@app.route('/add_project_comment', methods=['POST'])
def add_project_comment():
           return ({"msg":"done"})

@app.route('/add_issue_comment', methods=['POST'])
def add_issue_comment():
    return ({"msg":"done"})

@app.route('/display_projectwise_comments', methods=['POST'])
def display_projectwise_comments():
    return ({"msg":"done"})

@app.route('/display_issuewise_comments', methods=['POST'])
def display_issuewise_comments():
    return ({"msg":"done"})

@app.route('/update_projectwise_comments', methods=['POST'])
def update_projectwise_comments():
    return ({"msg":"done"})

@app.route('/update_issuewise_comments', methods=['POST'])
def update_issuewise_comments():
    return ({"msg":"done"})

if __name__ == "__main__":
    app.run(debug=True,port=5000)