import os
from typing import Any, List, Tuple
from datetime import date
from utils.utils import Gender, TimeControl
from models.player import Player
from utils.utils import Result


class View:
    """Cette classe a pour but d'afficher un titre et un contenu"""
    def __init__(self, title: str, content: str = "", blocking: bool = False):
        self.title = title
        self.content = content
        self.blocking = blocking

    def show(self):
        os.system("reset")
        print(self.title.upper())
        print("-"*len(self.title))
        print(self.content)
        if self.blocking:
            input("\nVeuillez appuyer sur entrée pour continuer !")


class Menu(View):
    """cette classe permet à l'utilisateur de faire un choix parmi une liste de choix"""
    def __init__(self, title: str, choices: List[Tuple[str, Any]]):
        content = "\n".join([f"{nb}) {choice}" for nb, choice in enumerate(choices, start=1)])
        self.choices = choices
        super().__init__(title, content)

    def show(self):
        """ cette méthode permet à l'utilisateur de faire un choix parmi une liste de choix"""
        super().show()
        while True:
            try:
                user_number = int(input("\nVeuillez entrer votre choix: "))
                if 0 < user_number <= len(self.choices):
                    return self.choices[user_number-1][1]
            except ValueError:
                print("Oops!  ce n'est pas un nombre.  veuillez essayer à nouveau")


class Form(View):
    """"cette classe permet à l'utilisateur de renseigner des champs dont les valeurs lui sont retournées
    sous forme de dictionnaire"""
    def __init__(self, title: str, fields: List[Tuple[str, str, Any]]):
        self.fields = fields
        super().__init__(title=title)

    def show(self):
        """cette méthode permet à l'utilisateur de remplir un ensemble de champ et de les retourner
        sous forme de dictionnaire"""
        data = {}
        super().show()
        for field_name, field_description, field_type in self.fields:
            while True:
                try:
                    data[field_name] = field_type(input(f"Quel est votre {field_description} ? "))
                    break
                except ValueError:
                    pass
        return self.post_process(data)

    def post_process(self, data):
        return data


class UpdatePlayerRank(Form):
    """ cette class permet d'éditer le classement d'un joueur"""
    def __init__(self):
        super().__init__(title="Edition d'un joueur", fields=[
            ("id", "Identifiant", int),
            ("rank", "Classement", int)])

    def post_process(self, data):
        return data


class Table(View):
    """ cette class permet de lister tous les joueurs """
    def __init__(self, title: str, items: List):
        content = "\n".join([str(item) for item in items])
        super().__init__(title, content=content, blocking=True)


class MainMenu(Menu):
    """ cette class permet d'afficher le menu principal """
    def __init__(self):
        super(). __init__(title="Tournois d'echec", choices=[
            ("Gestion des joueurs", 1),
            ("Gestion des tournois", 2),
            ("Quitter", 3),
            ])


class ReportTournament(Menu):
    """ Cette class affiche le rapport du tournoi"""
    def __init__(self):
        super().__init__(title="Repport", choices=[
            ("Information du tournoi", 1),
            ("tableau des scores", 2),
            ("résultat des matches", 3)
            ("retour", 4),
            ])


class ListView(View):
    """ cette class permet d'afficher une liste de vues """
    def __init__(self, title: str, items: List[Any]):
        super().__init__(title=title, content="\n".join([str(item) for item in items]), blocking=True)


class ScorBoard(View):
    """ cette class a pour but d'afficher le score des matches """
    def __init__(self, title: str, items: List[Any]):
        super().__init__(title=title, content="\n".join([str(item) for item in items]), blocking=True)


class GameResult(View):
    """ cette class a pour but d'afficher le résultat des matches """
    def __init__(self, title: str, items: List[Any]):
        super().__init__(title=title, content="\n".join([str(item) for item in items]), blocking=True)


class NewTournament(Form):
    """ cette class permet de créer un nouveau tournois"""
    def __init__(self):
        super().__init__(title="Nouveau tournois", fields=[
            ("name", "Nom du tournoi", str),
            ("location", "lieux", str),
            ("rounds_number", "nombre de rounds", int),
            ("players_number", "nombre de joueurs", int),
            ("description", "description", str),
            ("time_control","règle", TimeControl),
            ])


class NewPlayer(Form):
    """ cette class permet la création d'un joueur """
    def __init__(self):
        super().__init__(title="Création d'un nouveau joueur", fields=[
            ("first_name", "Prénom", str),
            ("last_name", "Nom", str),
            ("birth_date_year", "année de naissance", int),
            ("birth_date_month", "mois de naissance", int),
            ("birth_date_day", "jour de naissance", int),
            ("gender", "Sexe", Gender),
            ("rank", "Position", int)
            ])

    def post_process(self, data):
        data["birth_date"] = date(year=data["birth_date_year"], month=data["birth_date_month"], day=data["birth_date_day"])
        return data


class PlayersMenu(Menu):
    def __init__(self):
        super().__init__(title="Gestion des Joeurs", choices=[
            ("Créer un joueur", 1),
            ("éditer un joueur", 2),
            ("Lister les joueurs par classement", 3),
            ("Lister les joueurs par nom", 4)
            ("Retour", 5),
            ])


class TournamentsMenu(Menu):
    def __init__(self):
        super().__init__(title="Gestion des tournois", choices=[
            ("Créer un tournoi",1),
            ("Jouer un tournoi", 2),
            ("Lister les tournois", 3),
            ("Afficher les rapports d'un tournoi", 4),
            ("Retour", 5),
            ])


class SelectItem(Menu):
    def __init__(self, title: str, items: List[Any]):
        choices = [
            (str(item), item.id) for item in items]
        super().__init__(title=title, choices=choices)


class SelectPlayer1Score(Menu):
    """ cette class permet de définir un vainqeur """
    def __init__(self, player1: Player, player2: Player):
        super().__init__(title="Choix du gagnant", choices=[
            (str(player1), Result.Win),
            (str(player2), Result.Lose),
            ("égalité", Result.Draw),
        ])
