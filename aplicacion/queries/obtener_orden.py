from seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from seedwork.aplicacion.queries import ejecutar_query as query
from infraestructura.repositorios import RepositorioOrdenes
from dataclasses import dataclass
from .base import OrdenQueryBaseHandler
from aplicacion.mapeadores import MapeadorOrden
from .base import OrdenQueryBaseHandler
import uuid

@dataclass
class ObtenerOrden(Query):
    id: str

class ObtenerOrdenHandler(OrdenQueryBaseHandler):

    def handle(self, query: ObtenerOrden) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
        orden =  self.fabrica_ordenes.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorOrden())
        return QueryResultado(resultado=orden)

@query.register(ObtenerOrden)
def ejecutar_query_obtener_reserva(query: ObtenerOrden):
    handler = ObtenerOrdenHandler()
    return handler.handle(query)