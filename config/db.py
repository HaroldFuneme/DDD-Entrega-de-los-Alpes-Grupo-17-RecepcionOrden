from uuid import uuid5
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

import os

db = None

def init_db(app: Flask):
    global db 
    db = SQLAlchemy(app)

DB_USERNAME = os.getenv('DB_USERNAME', default="root")
DB_PASSWORD = os.getenv('DB_PASSWORD', default="adminadmin")
DB_HOSTNAME = os.getenv('DB_HOSTNAME', default="localhost")

class DatabaseConfigException(Exception):
    def __init__(self, message='Configuration file is Null or malformed'):
        self.message = message
        super().__init__(self.message)




