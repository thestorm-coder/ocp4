from typing import List
from models.match import Match
from pydantic import (
    BaseModel, PositiveInt)
from utils.utils import TimeControl, Description, Name
from datetime import datetime
from models.round import Round
from player_manager import player_manager as pm


class Tournament(BaseModel):
    "cette classe décrit le déroulé d'un tournoi"
    id: PositiveInt
    name: Name
    location: Name
    start_date: datetime = datetime.today()
    end_date: datetime = None
    rounds: List[Round]
    players: List[PositiveInt]
    time_control: TimeControl
    description: Description = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup()

    def setup(self):
        if len(self.rounds[0].matchs) == 0:
            players = [pm.find_by_id(player_id) for player_id in self.players]
            players.sort(key=lambda x: x.rank, reverse=True)
            group1 = players[:len(players)//2]
            group2 = players[len(players)//2:]
            self.rounds[0].matchs = [Match(player_1_Id=p1.id, player_2_Id=p2.id) for p1, p2 in zip(group1, group2)]

    def matches_to_play(self):
        matches = []
        for round in self.rounds:
            for match in round.matchs:
                if match.played:
                    matches.append(match)
        return matches

    def play(self, select_winner_view, manager):
        for round in self.rounds:
            if round.end_date is not None:
                continue
            self.setup_next_round(round)
            round.play(select_winner_view)
            round.end_date = datetime.today()
            manager.save_item(self.id)

