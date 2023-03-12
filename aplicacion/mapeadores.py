from infraestructura.dto import Orden
from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
from .dto import OrdenDTO
from flask import jsonify 


class MapeadorRecepcionOrdenDTOJson(AppMap):

    def externo_a_dto(self, externo: dict)-> OrdenDTO: 
        print("EventId: ", externo.get('eventId'))
        event_id = externo.get('eventId')
        event_name = externo.get('eventName')
        event_data_format = externo.get('eventDataFormat')
        user = externo.get('user')
        user_addres = externo.get('user_addres')
      
        items = []
        for itin in externo.get('items', list()):
            items.append(itin)
        orden_dto =  OrdenDTO(event_id, event_name+'-T', event_data_format, user, user_addres, items)
        return orden_dto
        #return jsonify(orden_dto.__dict__)

        # OrdenCreadaEvent = {
        #     'eventId': event_id,
        #     'eventName': event_name,
        #     'eventDataFormat': event_data_format,
        #     'payload': {
        #     'ordenId': '',
        #     'user': user,
        #     'user_addres': user_addres,
        #     'items': items,
        #     }

        # }
        # return OrdenCreadaEvent

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__

class MapeadorOrden(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_orden(self, orden_dto: OrdenDTO) -> Orden:
        return Orden(orden_dto.user, orden_dto.user_addres)

    def obtener_tipo(self) -> type:
        return Orden.__class__


    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        return OrdenDTO()

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        # print("DTO FROM MAPEADOR:  ", dto)
        # orden = Orden(dto.user, dto.user_addres, dto.items)
        # print("ORDEN CREATED FROM MAPEADOR:  ", dto)
        return dto
