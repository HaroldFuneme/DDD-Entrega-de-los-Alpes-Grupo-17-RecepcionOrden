from ast import List
from config.db import db
from dominio.repositorios import RepositorioOrdenes, RepositorioProveedores
from dominio.entidades import Orden
from .dto import Item as ItemDTO
from .dto import Orden as OrdenDTO
from dominio.fabricas import FabricaOrden
from .mapeadores import MapeadorOrden
from uuid import UUID

class RepositorioProveedoresSQLite(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Orden:
        # TODO
        raise NotImplementedError

    def obtener_todos(self) -> List:
        ...

    def agregar(self, entity: Orden):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    

class RepositorioOrdenesSQLite(RepositorioOrdenes):

    def __init__(self):
        self._fabrica_ordenes: FabricaOrden = FabricaOrden()

    @property
    def fabrica_ordenes(self):
        return self._fabrica_ordenes

    def obtener_por_id(self, id: UUID) -> Orden:
        reserva_dto = db.session.query(OrdenDTO).filter_by(id=str(id)).one()
        return self.fabrica_ordenes.crear_objeto(reserva_dto, MapeadorOrden())

    def obtener_todos(self):
        # TODO
        raise NotImplementedError

    def agregar(self, orden: any):
        print("RepositorioOrdenesSQLite obj para agregar DB: ", orden)
        print("\n")
   
        item_dto = []
        for item in orden.items:
            item_dt = Item(item=item.item)
            db.session.add(item_dt)
            item_dto.append(item_dt)

        ord = Orden(user=orden.user, user_address=orden.user_address, items=item_dto)
        db.session.add(ord)
        print("RepositorioOrdenesSQLite obj agregado a DB: ", ord)
        print("\n")

        db.session.commit()

    def actualizar(self, orden: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, orden_id: UUID):
        # TODO
        raise NotImplementedError
