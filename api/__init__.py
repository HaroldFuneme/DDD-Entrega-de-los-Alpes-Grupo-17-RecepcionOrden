import os

from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger
from infraestructura.dto import Orden

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
    from infraestructura.dto import Orden

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'database-recepcion-orden.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #  # Inicializa la DB
    from config.db import init_db
    init_db(app)

    from config.db import db
    

    importar_modelos_alchemy()

    ## TEST DB
    with app.app_context():
        db.create_all()
        ord = Orden(user="usuario1")
        db.session.add(ord)
        db.session.commit()
        print(Orden.query.all())

    


    #  # Importa Blueprints
    # from . import cliente
    # from . import hoteles
    # from . import pagos
    # from . import precios_dinamicos
    # from . import vehiculos
    # from . import vuelos

    # # Registro de Blueprints
    # app.register_blueprint(cliente.bp)
    # app.register_blueprint(hoteles.bp)
    # app.register_blueprint(pagos.bp)
    # app.register_blueprint(precios_dinamicos.bp)
    # app.register_blueprint(vehiculos.bp)
    # app.register_blueprint(vuelos.bp)

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