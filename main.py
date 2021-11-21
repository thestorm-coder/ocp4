from views import MainMenu, Menu, NewPlayer, PlayersMenu, TournamentsMenu
from managers import player_manager as pm, tournament_manager as tm


def add_player_ctrl():
    data = NewPlayer().show()
    print(data)


def tournaments_menu_ctrl():
    choice = TournamentsMenu().show()
    if choice == 5:
        main_menu_ctrl()


def players_menu_ctrl():
    choice = PlayersMenu().show()
    if choice == 5:
        main_menu_ctrl()
    elif choice == 1:
        add_player_ctrl()


def main_menu_ctrl():
    choice = MainMenu().show()

    if choice == 1:
        players_menu_ctrl()
    elif choice == 2:
        tournaments_menu_ctrl()
    elif choice == 3:
        print("Quitter le Menu")


main_menu_ctrl()




# continuer à coder la naviagation entre les menus
# 