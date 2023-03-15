
from dataclasses import dataclass, field
from .mixins import ValidarReglasMixin
from .reglas import IdEntidadEsInmutable
from .eventos import EventoDominio
from .excepciones import IdDebeSerInmutableExcepcion
from datetime import datetime
import uuid

@dataclass
class Entidad:
    user: str =  ""
    user_address: str = ""
    items = [] 

    @property
    def orden_id(self):
        return self.orden_id
        

@dataclass
class AgregacionRaiz(Entidad, ValidarReglasMixin):
    eventos: 'list[EventoDominio]' = field(default_factory=list)

    def agregar_evento(self, evento: EventoDominio):
        self.eventos.append(evento)
    
    def limpiar_eventos(self):
        self.eventos = list()


@dataclass
class Locacion(Entidad):
    def __str__(self) -> str:
        ...