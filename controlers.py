from os import name
from views import MainMenu, NewPlayer, PlayersMenu, TournamentsMenu, Table, NewTournament
from player_manager import player_manager as pm
from tounament_manager import tournament_manager as tm
from views import UpdatePlayerRank, SelectItem, SelectPlayer1Score

# def reports_ctrl():
    
def list_of_tournaments_ctrl():
    Table(title="Liste des tournois", item=sorted(tm.find_all(), key=lambda x: x.tournament)).show()
    tournaments_menu_ctrl()


def play_tournament_ctrl():
    tournament_id = SelectItem(title="Choisir un tournoi", items=tm.find_all()).show()
    tournament = tm.find_by_id(tournament_id)
    tournament.play(select_winner_view=SelectPlayer1Score, manager=tm)
    tournaments_menu_ctrl()


def create_tournament_ctrl():
    data = NewTournament().show()
    data["rounds"] = [{"name": f'round {nb}'} for nb in range(1, data["rounds_number"]+1)]
    data["players"] = [SelectItem(title="Choix de joueur", items=pm.find_all()).show() for _ in range(data["players_number"])]
    tm.create(save=True, **data)
    tournaments_menu_ctrl()


def list_player_by_name_ctrl():
    Table(title="Nom des joueurs", items=sorted(pm.find_all(), key=lambda x: x.last_name)).show()
    players_menu_ctrl()


def list_player_by_rank_ctrl():
    Table(title="Liste des joueurs", items=sorted(pm.find_all(), key=lambda x: x.rank)).show()
    players_menu_ctrl()


def edit_player_ctrl():
    form_data = UpdatePlayerRank().show()
    player_id = form_data["id"]
    player = pm.find_by_id(player_id)
    player.rank = form_data["rank"]
    pm.save_item(player_id)
    players_menu_ctrl()


def add_player_ctrl():
    data = NewPlayer().show()
    pm.create(save=True, **data)
    players_menu_ctrl()


def tournaments_menu_ctrl():
    choice = TournamentsMenu().show()
    if choice == 5:
        main_menu_ctrl()
    elif choice == 1:
        create_tournament_ctrl()
    elif choice == 2:
        play_tournament_ctrl()
    elif choice == 3:
        list_of_tournaments_ctrl()
    elif choice == 4:
        reports_ctrl()


def players_menu_ctrl():
    choice = PlayersMenu().show()
    if choice == 5:
        main_menu_ctrl()
    elif choice == 1:
        add_player_ctrl()
    elif choice == 2:
        edit_player_ctrl()
    elif choice == 3:
        list_player_by_rank_ctrl()
    elif choice == 4:
        list_player_by_name_ctrl()


def main_menu_ctrl():
    choice = MainMenu().show()

    if choice == 1:
        players_menu_ctrl()
    elif choice == 2:
        tournaments_menu_ctrl()
    elif choice == 3:
        print("Quitter le Menu")


main_menu_ctrl()
