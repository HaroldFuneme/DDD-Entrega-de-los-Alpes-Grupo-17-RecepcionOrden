from aplicacion.dto import OrdenDTO
from dominio.entidades import Orden
from infraestructura.fabricas import FabricaRepositorio
from seedwork.aplicacion.servicios import Servicio


class ServicioRecepcionOrden(Servicio):

    def __init__(self):
        self._fabrica_orden: FabricaRepositorio = FabricaRepositorio()
        #self._fabrica_vuelos: FabricaVuelos = FabricaVuelos()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_orden
    
    # @property
    # def fabrica_vuelos(self):
    #     return self._fabrica_vuelos

    def crear_recepcion_orden(self, recepcion_orden_dto: OrdenDTO) -> OrdenDTO:
        # orden: Orden = self._fabrica_orden.crear_objeto(recepcion_orden_dto, Mapeadororden())

        # repositorio = self.fabrica_repositorio.crear_objeto(Repositorioordens.__class__)
        # repositorio.agregar(orden)

        # return self.fabrica_vuelos.crear_objeto(orden, Mapeadororden())
        return recepcion_orden_dto

