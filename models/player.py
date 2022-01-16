from pydantic import (
    BaseModel, PositiveInt)
from datetime import date

from pydantic.types import constr
from utils.utils import Gender



class Player(BaseModel):
    """Cette class décrit les carractéristiques d'un joueur"""
    id: PositiveInt
    last_name: constr(strict=True, to_lower=True, strip_whitespace=True, min_length=2, max_length=50)
    first_name: constr(strict=True, to_lower=True, strip_whitespace=True, min_length=2, max_length=50)
    birth_date: date
    gender: Gender
    rank: PositiveInt

    def __str__(self) -> str:
        return f"{self.id}, {self.last_name.upper()}, {self.first_name.capitalize()}, {self.rank}"
