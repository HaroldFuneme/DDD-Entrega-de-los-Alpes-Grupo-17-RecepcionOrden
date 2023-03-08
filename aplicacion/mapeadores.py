from seedwork.aplicacion.dto import Mapeador as AppMap
from .dto import OrdenDTO
from flask import jsonify 


class MapeadorRecepcionOrdenDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        print(externo.get('eventId'))
        event_id = externo.get('eventId')
        event_name = externo.get('eventName')
        event_data_format = externo.get('eventDataFormat')
        user = externo.get('user')
        user_addres = externo.get('user_addres')
        items = []
        for itin in externo.get('items', list()):
            items.append(itin)
        orden_dto =  OrdenDTO(event_id, event_name+'-T', event_data_format, user, user_addres, items)
        return jsonify(orden_dto.__dict__)

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__
