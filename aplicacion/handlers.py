from seedwork.aplicacion.handlers import Handler
from infraestructura.despachadores import Despachador

class HandlerOrdenIntegracion(Handler):

    @staticmethod
    def handle_orden_creada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden-a')

    @staticmethod
    def handle_orden_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden-a')

    @staticmethod
    def handle_orden_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden-a')

    @staticmethod
    def handle_orden_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-orden-a')


    