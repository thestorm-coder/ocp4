from utils.manager import Manager
from models.player import Player
from models.tournament import Tournament
player_manager = Manager(item_type=Player)
player_manager.load_from_json("mocks/players.json")
tournament_manager = Manager(item_type=Tournament)
tournament_manager.load_from_json("mocks/tournaments.json")