from ast import List
from config.db import db
from dominio.repositorios import RepositorioOrdenes, RepositorioProveedores
from infraestructura.dto import Orden, Item
from dominio.fabricas import FabricaOrden
from .dto import Orden as OrdenDTO
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
        orden_dto = self.fabrica_ordenes.crear_objeto(orden, MapeadorOrden())
        db.create_all()
    
        items: Item = []
        for i in orden.items:
            items.append(i)
        #ord = Orden(user=orden.user, user_address=orden.user.address, items=items)


        # item1 = Item(item='pantalon1')
        # item2 = Item(item='pantalon2')
        # item3 = Item(item='pantalon3')
        # db.session.add(ord)
        # db.session.add(item1)
        # db.session.add(item2)
        # db.session.add(item3)
        # db.session.commit()
        # for item in orden.items:
        #     db.session.add(item)

        db.session.add(orden_dto)
        db.session.commit()

    def actualizar(self, orden: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, orden_id: UUID):
        # TODO
        raise NotImplementedError
