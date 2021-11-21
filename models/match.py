from pydantic import (
    BaseModel)

from pydantic.types import PositiveInt
from models.winner import Winner


class Match(BaseModel):
    """ cette class indique les vainquers de chaque parties"""
    player_1_Id: PositiveInt
    player_2_Id: PositiveInt
    winner: Winner
