

from ast import List
from dataclasses import dataclass, field

from sqlalchemy import Column, ForeignKey, Integer
from dominio.eventos import OrdenCreada
from seedwork.dominio.entidades import AgregacionRaiz, Entidad
from sqlalchemy.orm import relationship


@dataclass
class Orden(AgregacionRaiz):
    eventId: str = None
    eventName: str = None
    eventDataFormat: str = None
    user: str = None
    user_address: str = None
    items: list = field(default_factory=list)

    def crear_orden(self, orden):
        print("Entidad CREAR_ORDEN --ORDEN: ", orden)
        print("\n")
        self.eventId = orden.eventId
        self.eventName = orden.eventName
        self.eventDataFormat = orden.eventDataFormat
        self.user = orden.user
        self.user_address = orden.user_address
        self.items = orden.items

        self.agregar_evento(OrdenCreada(eventName=self.eventName, eventDataFormat=self.eventDataFormat, user=self.user, user_address=self.user_address ))
        # TODO Agregar evento de compensación
@dataclass
class Item():
    item: str
