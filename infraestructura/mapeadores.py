from seedwork.dominio.repositorios import Mapeador
from .dto import Orden as OrdenDTO
from .dto import Item as ItemDTO
from dominio.entidades import Orden

class MapeadorOrden(Mapeador):
    
    def obtener_tipo(self) -> type:
        return Orden.__class__

    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        print("MAP_INFRA  ENTIDAD TO DTO  --- ENTIDAD:  ", entidad)
        print("\n")

        orden_dto = OrdenDTO(user=entidad.user, user_address=entidad.user_address)
        #orden = Orden(user='destino@acme.com', user_address='Call 45 45 90', items=['item1','item2', 'item3'])
        items_dto = []
        for item in orden_dto.items:
            items_dto.append(ItemDTO(item=item))
        orden_dto.items = items_dto


        print("MAP_INFRA  ENTIDAD TO DTO  --- DTO:  ", orden_dto)
        print("\n")
        return orden_dto

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        print("MAP_INFRA DTO TO ENTIDAD  --- ENTIDAD:  ", dto)
        print("\n")
        orden = Orden(dto.user, dto.user_address, dto.items)
        print("MAP_INFRA DTO TO ENTIDAD  --- DTO:  ", orden)
        print("\n")
        return orden