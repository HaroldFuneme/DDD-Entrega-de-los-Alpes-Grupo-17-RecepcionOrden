from dataclasses import dataclass
from infraestructura.dto import Orden
from dominio.excepciones import TipoObjetoNoExisteEnDominioOrdenesExcepcion
from seedwork.dominio.entidades import Entidad
from seedwork.dominio.fabricas import Fabrica

from seedwork.dominio.repositorios import Mapeador


@dataclass
class _FabricaOrden(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            orden: Orden = mapeador.dto_a_entidad(obj)
            return orden


@dataclass
class FabricaOrden(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        print("Type of Mapeador Dominio: ", mapeador.obtener_tipo())
        print("Type of Mapeador Dominio: ", Orden.__class__)
        print("OBJ From service: ", obj)
        if mapeador.obtener_tipo() == Orden.__class__:
            fabrica_orden = _FabricaOrden()
            print("Obj generate form Fabrica type ORDEN: ", fabrica_orden.crear_objeto(obj, mapeador))
            return fabrica_orden.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioOrdenesExcepcion()