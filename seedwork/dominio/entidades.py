
from dataclasses import dataclass, field
from .mixins import ValidarReglasMixin
from .reglas import IdEntidadEsInmutable
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
    ...


@dataclass
class Locacion(Entidad):
    def __str__(self) -> str:
        ...