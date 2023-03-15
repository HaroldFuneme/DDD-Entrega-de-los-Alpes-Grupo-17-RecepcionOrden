from dataclasses import dataclass
from aplicacion.comandos.base import CrearOrdenBaseHandler

from seedwork.aplicacion.comandos import Comando
from seedwork.aplicacion.comandos import ejecutar_commando as comando
from aplicacion.dto import OrdenDTO, ItemDTO
from aplicacion.mapeadores import MapeadorOrden
from dominio.entidades import Orden
from infraestructura.repositorios import RepositorioOrdenes
from seedwork.infraestructura.uow import UnidadTrabajoPuerto

@dataclass
class CrearOrden(Comando):
    event_id: int
    event_name: str
    event_data_format: str
    user: str
    user_address: str
    items: 'list[ItemDTO]'


class CrearOrdenHandler(CrearOrdenBaseHandler):
    
    def handle(self, comando: CrearOrden):
        print("CrearOrdenHandler COMANDO: ", comando)
        print("\n")
        orden_dto = OrdenDTO(comando.event_id, comando.event_name, comando.event_data_format, comando.user, comando.user_address)

        orden: Orden = self.fabrica_ordenes.crear_objeto(orden_dto, MapeadorOrden())
        orden.crear_orden(orden)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, orden)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearOrden)
def ejecutar_comando_crear_reserva(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)