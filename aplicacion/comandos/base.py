from seedwork.aplicacion.comandos import ComandoHandler
from infraestructura.fabricas import FabricaRepositorio
from dominio.fabricas import FabricaOrden

class CrearOrdenBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_ordenes: FabricaOrden = FabricaOrden()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_ordenes(self):
        return self._fabrica_ordenes    
    