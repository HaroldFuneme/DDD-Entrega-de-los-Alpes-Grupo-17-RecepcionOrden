import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from infraestructura.schema.v1.eventos import EventoOrdenCreada
from infraestructura.schema.v1.comandos import ComandoCrearOrden
from seedwork.infraestructura import utils

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://34.121.180.145:6650')
        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-orden-a', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='eda-sub-eventos', schema=AvroSchema(EventoOrdenCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().payload}')

            #consumidor.acknowledge(mensaje)     

        cliente.close()
    except:
        logging.error('ERRORP: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://34.121.180.145:6650')
        #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-orden-a', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='eda-sub-comandos', schema=AvroSchema(ComandoCrearOrden))

        while True:
            mensaje = consumidor.receive()
            print(f'Comando recibido: {mensaje.value().data}')

            #consumidor.acknowledge(mensaje)     
            
        cliente.close()
    except:
        logging.error('ERRORP: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()