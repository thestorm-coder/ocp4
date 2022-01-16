from typing import List
from utils.utils import Name
from pydantic import (
    BaseModel)
from datetime import datetime

from models.match import Match


class Round(BaseModel):
    """cette class décrit le fonctionnement d'un round"""
    name: Name
    matchs: List[Match] = []
    start_date: datetime = datetime.today()
    end_date: datetime = None

    def play(self, select_winner_view):
        for match in self.matchs:
            match.play(select_winner_view)