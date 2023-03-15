import json
import seedwork.presentacion.api as api
from flask import Blueprint, Response, request
from aplicacion.mapeadores import MapeadorRecepcionOrdenDTOJson
from aplicacion.servicios import ServicioRecepcionOrden

from aplicacion.queries.obtener_orden import ObtenerOrden
from aplicacion.comandos.crear_orden import CrearOrden

from seedwork.aplicacion.comandos import ejecutar_commando
from seedwork.aplicacion.queries import ejecutar_query

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
        
        print("**********POST recepcion_orden_asincrona --COMANDO: ", comando)
        print("\n")
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    
@bp.route('/orden', methods=('GET',))
@bp.route('/orden/<id>', methods=('GET',))
def dar_orden(id=None):
    if id:
        sr = ServicioRecepcionOrden()
        map_orden = MapeadorRecepcionOrdenDTOJson()
        
        return map_orden.dto_a_externo(sr.obtener_orden_por_id(id))
    else:
        return [{'message': 'GET!'}]

@bp.route('/orden-query', methods=('GET',))
@bp.route('/orden-query/<id>', methods=('GET',))
def dar_orden_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerOrden(id))
        map_orden = MapeadorRecepcionOrdenDTOJson()
        
        return map_orden.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]