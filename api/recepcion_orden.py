import json
import seedwork.presentacion.api as api
from flask import Blueprint, Response, request
from aplicacion.mapeadores import MapeadorRecepcionOrdenDTOJson
from aplicacion.servicios import ServicioRecepcionOrden

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

        # return recepcion_orden.dto_a_externo(dto_final)
        return recepcion_orden_dto
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
    

