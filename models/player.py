from pydantic import (
    BaseModel, PositiveInt)
from datetime import date
from utils.utils import Name, Gender


class Player(BaseModel):
    """Cette class décrit les carractéristiques d'un joueur"""
    id: PositiveInt
    last_name: Name
    first_name: Name
    birth_date: date
    gender: Gender
    rank: PositiveInt

    def __str__(self) -> str:
        return f"{self.id}, {self.last_name}, {self.first_name}, {self.rank}"
