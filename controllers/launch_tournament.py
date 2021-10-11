from models import round

class LaunchTournament:
    """ Générer les paires de joueurs"""
    def __init__(self, tournament_name):
        self.tournament_name = tournament_name
        self.players = []

    def __call__(self, round):
        self.players = round
        print(f"les joueurs sont {self.players}")