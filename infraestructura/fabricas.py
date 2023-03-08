from attr import dataclass
from seedwork.dominio.fabricas import Fabrica
from seedwork.dominio.repositorios import Repositorio
from dominio.repositorios import RepositorioOrdenes, RepositorioProveedores
from .repositorios import RepositorioOrdenesSQLite, RepositorioProveedoresSQLite
#from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioOrdenes.__class__:
            return RepositorioOrdenesSQLite()
        elif obj == RepositorioProveedores.__class__:
            return RepositorioProveedoresSQLite()
        else:
            raise "ExcepcionFabrica()"