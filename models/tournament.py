from typing import List
from pydantic import (
    BaseModel, PositiveInt)
from utils.utils import TimeControl, Description, Name
from datetime import datetime
from models.round import Round


class Tournament(BaseModel):
    "cette classe décrit le déroulé d'un tournoi"
    id: PositiveInt
    name: Name
    location: Name
    start_date: datetime = datetime.today()
    end_date: datetime = None
    rounds: List[Round] = []
    number_of_rounds: PositiveInt
    players: List[PositiveInt]
    time_control: TimeControl
    description: Description


# print(Tournament(name="Mortel combat", location="Paris", round=3, start_date= "2021-09-12 10:12",
# player="Toto",time_control=20, description="cette manche sera la dernière"))
