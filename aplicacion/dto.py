from typing import List
from seedwork.aplicacion.dto import DTO
from dataclasses import dataclass


@dataclass(frozen=True)
class ItemDTO(DTO):
    item: str


@dataclass(frozen=True)
class OrdenDTO(DTO):
    event_id: int
    event_name: str
    event_data_format: str
    user: str
    user_address: str
    items: List[ItemDTO] = None
