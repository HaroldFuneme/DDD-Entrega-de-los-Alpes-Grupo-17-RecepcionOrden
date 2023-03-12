from .dto import OrdenDTO, ItemDTO 
from dominio.entidades import Orden, Item
from seedwork.aplicacion.dto import Mapeador as AppMap
from seedwork.dominio.repositorios import Mapeador as RepMap
from .dto import OrdenDTO
from flask import jsonify 


class MapeadorRecepcionOrdenDTOJson(AppMap):

    def externo_a_dto(self, externo: dict)-> OrdenDTO: 
        print("MapeadorRecepcionOrdenDTOJson EventId: ", externo.get('eventId'))
        print("\n")
        event_id = externo.get('eventId')
        event_name = externo.get('eventName')
        event_data_format = externo.get('eventDataFormat')
        user = externo.get('user')
        user_address = externo.get('user_addres')
      
        items: list[ItemDTO] = list()
        for itin in externo.get('items', list()):
            items.append(itin)
        orden_dto =  OrdenDTO(event_id, event_name+'-T', event_data_format, user, user_address, items)
        print("MapeadorRecepcionOrdenDTOJson EXTERNO TO DTO: ", orden_dto)
        print("\n")
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
        print("MapeadorRecepcionOrdenDTOJson DTO TO EXTERNO: ", dto)
        print("\n")
        return dto.__dict__

class MapeadorOrden(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_orden(self, orden_dto: OrdenDTO) -> Orden:
        return orden_dto

    def obtener_tipo(self) -> type:
        return Orden.__class__


    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        print("MAP_API ENTIDAD TO DTO  --- ENTIDAD:  ", entidad)
        print("\n")
        print("MAP_API ENTIDAD TO DTO  --- DTO:  ", OrdenDTO(entidad.user, entidad.user_address, entidad.items))
        print("\n")
        return OrdenDTO(entidad.user, entidad.user_address, entidad.items)

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        print("MAP_API DTO TO ENTIDAD -- DTO:  ", dto)
        orden = Orden()
        orden.items = list()

        #items_dto: list[any] = dto.items
        #orden = Orden(user=dto.user, user_address=dto.user_address, items=dto.items)
        orden = Orden(user=dto.user, user_address=dto.user_address)
        orden.items = [Item(item=item_dto) for item_dto in dto.items]
        
        print("MAP_API DTO TO ENTIDAD -- ENTIDAD:  ", orden)
        print("\n")
        return orden
