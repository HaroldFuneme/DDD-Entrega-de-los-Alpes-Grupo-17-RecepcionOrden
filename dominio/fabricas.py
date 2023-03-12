from dataclasses import dataclass
from .entidades import Orden
from dominio.excepciones import TipoObjetoNoExisteEnDominioOrdenesExcepcion
from seedwork.dominio.entidades import Entidad
from seedwork.dominio.fabricas import Fabrica

from seedwork.dominio.repositorios import Mapeador


@dataclass
class _FabricaOrden(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        print("__FabricaOrden OBJ INPUT: ", obj)
        print("__FabricaOrden MAPEADOR INPUT: ", mapeador)
        print("__FabricaOrden ISINSTANCE: ", isinstance(obj, Entidad))
        print("\n")
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            orden: Orden = mapeador.dto_a_entidad(obj)
            ## reglas para correctitud del objeto Orden del dominio
            return orden


@dataclass
class FabricaOrden(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        print("FabricaOrden OBJ INPUT: ", obj)
        print("FabricaOrden MAPEADOR INPUT: ", mapeador)
        print("\n")
        if mapeador.obtener_tipo() == Orden.__class__:
            fabrica_orden = _FabricaOrden()
            print("FabricaOrden DTO or ENTIDAD: ", fabrica_orden)
            print("\n")
            return fabrica_orden.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioOrdenesExcepcion()