"""DTOs para la capa de infrastructura del dominio de RecepcionOrden

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de RecepcionOrden

"""
from config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table
import uuid

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))
#Base = db.declarative_base()
app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database-recepcion-orden.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Orden(db.Model):
    __tablename__ = "ordenes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_orden = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    user = db.Column(db.String(128), nullable=False, primary_key=True)

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_item = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    item = db.Column(db.String(128), nullable=False, primary_key=True)


##TODO BORRAR
def __repr__(self):
    return "{}-{}-{}".format(self.id, self.id_orden, self.user)
