from utils import connexion_db
from models import tournament, player

class ManagementTournament:
    """ affichage des éléments des tournois"""

    def __init__(self):
        self.all_tournaments = tournament.Tournament.get()
        self.get_db_players = connexion_db.ManagementDB().get('players')
        self.all_players = [player.Player.get(item) for item in self.get_db_players]

