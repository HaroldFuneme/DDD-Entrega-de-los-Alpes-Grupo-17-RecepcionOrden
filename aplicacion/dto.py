from typing import List
from seedwork.aplicacion.dto import DTO
from dataclasses import dataclass


@dataclass(frozen=True)
class OrdenDTO(DTO):
    event_id: int
    event_name: str
    event_data_format: str
    user: str
    user_addres: str
    items: List[str]

    def __init__(self, event_id: int, event_name: str, event_data_format: str, user: str, user_addres: str, items: List[str]) -> None:
        self.event_id = event_id
        self.event_name = event_name
        self.event_data_format = event_data_format
        self.user = user
        self.user_addres = user_addres
        self.items = items