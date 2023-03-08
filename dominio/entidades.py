

from ast import List
from dataclasses import dataclass, field
from seedwork.dominio.entidades import AgregacionRaiz


@dataclass
class Orden(AgregacionRaiz):
    user = ''
    user_address = ''
    items = []

@dataclass
class Item(AgregacionRaiz):
    item = ''