import json
import seedwork.presentacion.api as api
from flask import Blueprint, Response, request
from aplicacion.mapeadores import MapeadorRecepcionOrdenDTOJson
from aplicacion.servicios import ServicioRecepcionOrden
from aplicacion.comandos.crear_orden import CrearOrden

from seedwork.aplicacion.comandos import ejecutar_commando

from seedwork.dominio.excepciones import ExcepcionDominio


bp = api.crear_blueprint('recepcion-orden', '/recepcion')
#recepcion_orden_bp = Blueprint('recepcion_orden_bp', __name__)

@bp.route('/orden', methods=['POST'])
def recepcion_orden():
    try:
        recepcion_orden_dict = request.json
     
        map_recepcion_orden = MapeadorRecepcionOrdenDTOJson()
        recepcion_orden_dto = map_recepcion_orden.externo_a_dto(recepcion_orden_dict)

        sr = ServicioRecepcionOrden()
        dto_final = sr.crear_recepcion_orden(recepcion_orden_dto)

        return map_recepcion_orden.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    

@bp.route('/orden-comando', methods=['POST'])
def recepcion_orden_asincrona():
    try:
        recepcion_orden_dict = request.json
     
        map_recepcion_orden = MapeadorRecepcionOrdenDTOJson()
        recepcion_orden_dto = map_recepcion_orden.externo_a_dto(recepcion_orden_dict)

        comando = CrearOrden(
            recepcion_orden_dto.event_id,
            recepcion_orden_dto.event_name,
            recepcion_orden_dto.event_data_format,
            recepcion_orden_dto.user,
            recepcion_orden_dto.user_address,
            recepcion_orden_dto.items
        )
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    