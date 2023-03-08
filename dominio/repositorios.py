from abc import ABC
from seedwork.dominio.repositorios import Repositorio

class RepositorioOrdenes(Repositorio, ABC):
    ...

class RepositorioProveedores(Repositorio, ABC):
    ...