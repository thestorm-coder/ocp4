from views import GameResult, MainMenu, Menu, NewPlayer, PlayersMenu, TournamentsMenu
from managers import player_manager as pm, tournament_manager as tm


# def show_player_by_name_ctrl():



# def players_rankin_ctrl():
#     result = GameResult.show()
#     print(result)

# def player_edition_ctrl():
#     #     data2=



def add_player_ctrl():
    data = NewPlayer().show()
    pm.create(**data)


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
    # elif choice == 2:
    #     player_edition()
    # elif choice == 3:
    #     players_rankin_ctrl()
    # elif choice == 4:
    #     show_player_by_name_ctrl()
    # elif choice == 5:
    #     print("Retour")


def main_menu_ctrl():
    choice = MainMenu().show()

    if choice == 1:
        players_menu_ctrl()
    elif choice == 2:
        tournaments_menu_ctrl()
    elif choice == 3:
        print("Quitter le Menu")


main_menu_ctrl()
