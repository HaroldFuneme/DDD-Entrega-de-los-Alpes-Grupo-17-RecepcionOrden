import os

import sqlalchemy

from flask import Flask, jsonify
from flask_swagger import swagger

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
    from config.db import init_db
    init_db(app)

    from config.db import db

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()

    # Importa Blueprints
    from . import recepcion_orden

    # # Registro de Blueprints
    app.register_blueprint(recepcion_orden.bp)

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
    