from connection import *
from app import *
from datetime import datetime
import logging

mydb=connect_db()
cursor=mydb.cursor()