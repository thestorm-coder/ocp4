import re
from enum import Enum


class Name(str):
    """ cette class permet d'afficher le nom du tournois """
    def __new__(cls, value):
        if not re.match(r"^[A-Za-z\- 'éèàùë]{2,20}$", value):
            raise ValueError("Le prénom est incorrect")
        return str.__new__(str, value)


class Gender(Enum):
    """ cette class permet de définir le genre d'une personne """
    Male = "H"
    Female = "F"


class TimeControl(Enum):
    Bullet = "Bullet"
    Blitz = "Blitz"
    FastMove = "FastMove"


class Description(str):
    def __new__(cls, value):
        if not re.match(r"^[A-Za-z\- 'éèàùë]{2,40}$", value):
            raise ValueError("Le prénom est incorrect")
        return str.__new__(str, value)
