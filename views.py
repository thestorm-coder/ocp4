import os
from typing import Any, List, Tuple
from models.player import Player


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
    def __init__(self, title, choices):
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
                    return user_number
            except ValueError:
                print("Oops!  ce n'est pas un nombre.  veuillez essayer à nouveau")


class Form(View):
    """"cette classe permet à l'utilisateur de renseigner des champs dont les valeurs lui sont retournées sous forme de dictionnaire""" 
    def __init__(self, title: str, fields: List[Tuple[str, str]]):
        self.fields = fields
        super().__init__(title=title)

    def show(self):
        """cette méthode permet à l'utilisateur de remplir un ensemble de champ et de les retourner sous forme de dictionnaire"""
        data = {}
        super().show()
        for field_name, field_description in self.fields:
            data[field_name] = input(f"Quel est votre {field_description} ? ")
        return data


class MainMenu(Menu):
    """ cette class permet d'afficher le menu principal """
    def __init__(self):
        super(). __init__(title="Tournois d'echec", choices=["Gestion des joueurs", "Gestion des tournois", "Quitter"])


class TournamentList(Menu):
    """ Cette class a pour but d'afficher l'historique des tournoi"""
    def __init__(self):
        super().__init__(title="Liste des tournois", choices=["Tournoi 1", "tounoi 2", "tounroi 3", "tournoi 4", "retour"])


class ReportTournament(Menu):
    """ Cette class affiche le rapport du tournoi"""
    def __init__(self):
        super().__init__(title="Repport", choices=["Information du tournoi", "tableau des scores", "résultat des matches", "retour"])


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
    def __init__(self, title: str, items: List[Any]):
        super().__init__(title=title, content="\n".join([str(item) for item in items]), blocking=True)


class NewPlayer(Form):
    """ cette class permet l'inscription d'un joueur """
    def __init__(self):
        super().__init__(title="Création d'un nouveau joueur", fields=[("first_name", "Prénom"), ("last_name", "Nom"), ("birth_date", "Date de naissance"), ("gender", "Sexe"), ("rank", "Position")])


class PlayersMenu(Menu):
    def __init__(self):
        super().__init__(title="Gestion des Joeurs", choices=["Créer un joueur", "éditer un joueur", "Lister les joueurs par classement", "Lister les joueurs par nom", "Retour"])


class TournamentsMenu(Menu):
    def __init__(self):
        super().__init__(title="Gestion des tournois", choices=["Créer un tournoi", "Jouer un tournoi", "Lister les tournois", "Afficher les rapports d'un tournoi", "Retour"])
