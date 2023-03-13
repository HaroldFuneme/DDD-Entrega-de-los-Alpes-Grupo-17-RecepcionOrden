"""DTOs para la capa de infrastructura del dominio de RecepcionOrden

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de RecepcionOrden

"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table, text
import uuid
from config.db import db

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os


Base = db.declarative_base()

# Definición de la tabla de asociación
orden_item_association = db.Table('orden_item_association',
    db.Column('id_orden', db.Integer, db.ForeignKey('ordenes.id'), primary_key=True),
    db.Column('id_item', db.Integer, db.ForeignKey('items.id'), primary_key=True)
)
class Orden(db.Model):
    __tablename__ = "ordenes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_orden = db.Column(db.String(36), nullable=False, unique=True)
    user = db.Column(db.String(128), nullable=False)
    user_address = db.Column(db.String(128), nullable=False)
    items = db.relationship('Item', secondary=orden_item_association, backref='ordenes')

    def __init__(self, user, user_address, items=[]):
        self.id_orden = str(uuid.uuid4())
        self.user = user
        self.user_address = user_address
        self.items = items

    # ##TODO BORRAR
    # def __repr__(self):
    #     return "USER::  {}  {}  {}  {}   => {}".format(self.id, self.id_orden, self.user, self.user_address, self.items)

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)    
    id_item = db.Column(db.String(36), nullable=False, unique=True)
    item = db.Column(db.String(128), nullable=False)


    def __init__(self, item):
        self.id_item = str(uuid.uuid4())
        self.item = item

    # ##TODO BORRAR
    # def __repr__(self):
    #     return "ITEM::  {}  {}  {}".format(self.id, self.id_item, self.item)



