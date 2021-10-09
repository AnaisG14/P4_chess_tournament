from models import tournament_model

class RoundModel:
    """ Model for a round"""

    def __init__(self, tournament_model, round_name, players):
        self.round_name = round_name
        self.round_players = []
        for player in players:
            self.round_players.append((player.last_name, player.ranking))
        self.matches = []

    def add_players(self, player):
        self.round_players.append(player)

    def generate_pairs(self):
        # classer les joueurs en fonction de leur rang
        pass

    def __str__(self):
        return str(self.round_players)

    def __repr__(self):
        return str(self.round_players)
