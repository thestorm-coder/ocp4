from pydantic import (
    BaseModel)

from pydantic.types import PositiveInt
from utils.utils import Result
from player_manager import player_manager as pm


class Match(BaseModel):
    """ cette class indique les vainquers de chaque parties"""
    player_1_Id: PositiveInt
    player_2_Id: PositiveInt
    score1: Result = None


    @property
    def score2(self):
        return Result(1.0-self.score1.value)
    
    @property
    def played(self):
        return self.score1 is not None

    def play(self, select_winner_view):
        if not self.played:
            self.score1 = select_winner_view(player1=pm.find_by_id(self.player_1_Id), player2=pm.find_by_id(self.player_2_Id)).show()