from utils.manager import Manager
from models.tournament import Tournament
tournament_manager = Manager(item_type=Tournament)
# tournament_manager.load_from_json("mocks/tournaments.json")