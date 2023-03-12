

from ast import List
from dataclasses import dataclass, field

from sqlalchemy import Column, ForeignKey, Integer
from seedwork.dominio.entidades import AgregacionRaiz, Entidad
from sqlalchemy.orm import relationship


@dataclass
class Orden(AgregacionRaiz):
    user: str = None
    user_address: str = None
    items: list = field(default_factory=list)
@dataclass
class Item():
    item: str
