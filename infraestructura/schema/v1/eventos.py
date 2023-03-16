import uuid
from pulsar.schema import *
from seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class OrdenCreadaPayload(Record):
    ordenId = String()
    user = String()
    user_address = String()
    items = list

class EventoOrdenCreada(EventoIntegracion):
    eventId = String(default=str(uuid.uuid4()))
    eventName = String(default="OrdenCreada")
    eventDataFormat = String(default="JSON")
    payload = OrdenCreadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)