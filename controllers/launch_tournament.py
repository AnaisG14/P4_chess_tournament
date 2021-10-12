from models import round

class LaunchTournament:
    """ Générer les paires de joueurs"""
    def __init__(self, tournament):
        self.tournament = tournament
        self.players = []

    def __call__(self, round):
        self.players = round
        print(f"les joueurs sont {self.players}")