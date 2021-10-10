from datetime import datetime
from models import match_model

class RoundModel:
    """ Model for a round"""

    def __init__(self,tournament_name, round_name, players):
        """ player is an attibut of tournament model"""
        self.round_name = f"{round_name} de {tournament_name}"
        self.round_players = []
        for player in players:
            self.round_players.append([(player.last_name, player.ranking), player.score])
        self.matches = []
        self.datetime_start = datetime.now()
        self.datetime_end = ""

    def add_players(self, player):
        self.round_players.append(player)

    def add_match(self, match_model):
        self.matches.append(match_model)

    def generate_first_pairs(self):
        # classer les joueurs en fonction de leur rang
        self.round_players.sort(key=lambda x: x[0][1])
        number_of_pairs = len(self.round_players)/2
        nb = 0
        while nb < number_of_pairs:
            player1 = self.round_players[nb]
            player2 = self.round_players[int(nb + number_of_pairs)]
            match = match_model.MatchModel(player1, player2)
            self.add_match(match)
            nb += 1

    def generate_pairs(self):
        # classer les joueurs en fonction de leur score puis de leur rang
        self.round_players.sort(key=lambda x: (x[1], x[0][1]))
        nb = 0
        while nb < len(self.round_players):
            player1 = self.round_players[nb]
            player2 = self.round_players[nb+1]
            match = match_model.MatchModel(player1, player2)
            self.add_match(match)
            nb += 2

    def add_end_time(self):
        self.datetime_end = datetime.now()

    def __str__(self):
        return f"nom du tournoi: {self.round_name}\n" \
               f"Joueurs participants: {self.round_players}\n" \
               f"Matches: {self.matches}\n" \
               f"Heure début {self.datetime_start}"

    def __repr__(self):
        return f"nom du tournoi: {self.round_name}\n" \
               f"Joueurs participants: {self.round_players}\n" \
               f"Matches: {self.matches}"