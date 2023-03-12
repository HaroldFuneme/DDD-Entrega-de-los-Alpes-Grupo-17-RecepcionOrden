from aplicacion.dto import OrdenDTO
from aplicacion.mapeadores import MapeadorOrden
from dominio.entidades import Orden
from seedwork.aplicacion.servicios import Servicio
from dominio.fabricas import FabricaOrden
from infraestructura.fabricas import FabricaRepositorio
from dominio.repositorios import RepositorioOrdenes


class ServicioRecepcionOrden(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_orden: FabricaOrden = FabricaOrden()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_orden
    
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    

    def crear_recepcion_orden(self, recepcion_orden_dto: OrdenDTO) -> OrdenDTO:

        orden: Orden = self._fabrica_orden.crear_objeto(recepcion_orden_dto, MapeadorOrden())
        print("\nOrden generada por fabrica de orden para SAVE DB: ", orden)
        print("\n")

        ## VERIFICAR
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
        print("RepositorioOrdenes generada por fabrica de repositorio: ", repositorio)
        print("\n")
        repositorio.agregar(orden)

        #return res
        return self._fabrica_orden.crear_objeto(orden, MapeadorOrden())

