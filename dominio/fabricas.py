from dataclasses import dataclass
from dominio.entidades import Orden
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

            # self.validar_regla(MinimoUnItinerario(reserva.itinerarios))
            # [self.validar_regla(RutaValida(ruta)) for itin in reserva.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return orden


@dataclass
class FabricaOrden(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Orden.__class__:
            fabrica_orden = _FabricaOrden()
            return fabrica_orden.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioOrdenesExcepcion()