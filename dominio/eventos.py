from __future__ import annotations
from dataclasses import dataclass, field
from seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class OrdenCreada(EventoDominio):
    id_orden: uuid.UUID = None
    eventDataFormat:  str = None
    eventName: str = None
    user: str = None
    user_address: str = None
    eventId: int = None
    eventos = []
    items = []
    
@dataclass
class OrdenCancelada(EventoDominio):
    id_orden: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class OrdenAprobada(EventoDominio):
    id_orden: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class OrdenPagada(EventoDominio):
    id_orden: uuid.UUID = None
    fecha_actualizacion: datetime = None