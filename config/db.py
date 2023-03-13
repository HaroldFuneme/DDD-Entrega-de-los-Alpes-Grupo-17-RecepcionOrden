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


# def database_connection(config, basedir=os.path.abspath(os.path.dirname(__file__))) -> str:
#     if not isinstance(config,dict):
#         raise DatabaseConfigException
    
#     if config.get('TESTING', False) == True:
#         return f'sqlite:///{os.path.join(basedir, "database-recepcion-orden.db")}'
#     else:
#         return f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}/recepcion_orden'



    # # Definición de la tabla de asociación
    # orden_item_association = db.Table('orden_item_association',
    #     db.Column('orden_id', db.Integer, db.ForeignKey('ordenes.id'), primary_key=True),
    #     db.Column('item_id', db.Integer, db.ForeignKey('items.id'), primary_key=True)
    # )
    # class Orden(db.Model):
    #     __tablename__ = "ordenes"
    #     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #     id_orden = db.Column(db.String(36), nullable=False, unique=True)
    #     user = db.Column(db.String(128), nullable=False)
    #     user_address = db.Column(db.String(128), nullable=False)
    #     items = db.relationship('Item', secondary=orden_item_association, backref='ordenes')

    #     def __init__(self, user, user_address, items=[]):
    #         self.id_orden = str(uuid5.uuid4())
    #         self.user = user
    #         self.user_address = user_address
    #         self.items = items

    #     ##TODO BORRAR
    #     def __repr__(self):
    #         return "USER::  {}  {}  {}  {}   => {}".format(self.id, self.id_orden, self.user, self.user_address, self.items)

    # class Item(db.Model):
    #     __tablename__ = "items"
    #     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #     id_item = db.Column(db.String(36), nullable=False, unique=True)
    #     item = db.Column(db.String(128), nullable=False)

    #     def __init__(self, item):
    #         self.id_item = str(uuid5.uuid4())
    #         self.item = item

    #     ##TODO BORRAR
    #     def __repr__(self):
    #         return "ITEM::  {}  {}  {}".format(self.id, self.id_item, self.item)



