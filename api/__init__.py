import os

import sqlalchemy

from flask import Flask, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def registrar_handlers():
    import aplicacion

def importar_modelos_alchemy():
    import infraestructura.dto

def comenzar_consumidor():
    import threading
    import infraestructura.consumidores as ordenes

        # Suscripción a eventos
    threading.Thread(target=ordenes.suscribirse_a_eventos).start()

        # Suscripción a comandos
    threading.Thread(target=ordenes.suscribirse_a_comandos).start()

def create_app(configuracion={}):

    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # # Configuracion de BD
    #app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database-recepcion-orden.db')
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database_recepcion_orden.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = '9d58f98f-3ae8-4149-a09f-3a8c2012e32c'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['TESTING'] = configuracion.get('TESTING')

    # Inicializa la DB
    from config.db import init_db
    init_db(app)

    from config.db import db

    importar_modelos_alchemy()
    registrar_handlers()

    with app.app_context():
        db.create_all()
        if not app.config.get('TESTING'):
            comenzar_consumidor()

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
    