from seedwork.dominio.repositorios import Mapeador

class MapeadorOrden(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_orden_dto(self, itinerarios_dto: list):
        itin_dict = dict()