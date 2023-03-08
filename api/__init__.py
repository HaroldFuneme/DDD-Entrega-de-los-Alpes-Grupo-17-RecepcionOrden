import os

import sqlalchemy


from infraestructura.dto import db

from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger
from infraestructura.dto import Orden

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    import infraestructura.dto

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)



    # # Configuracion de BD
    #app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database-recepcion-orden.db')
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database_recepcion_orden.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa la DB
    # from config.db import init_db
    # db= init_db(app)

    #importar_modelos_alchemy()
    ## TEST DB
    

    #  # Importa Blueprints
    # from . import vuelos

    # # Registro de Blueprints
    # app.register_blueprint(vuelos.bp)
    from api.recepcion_orden import recepcion_orden_bp

    app.register_blueprint(recepcion_orden_bp)

    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "Microservicio RecepcionOrden"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
    