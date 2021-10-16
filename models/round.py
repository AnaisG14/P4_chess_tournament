from datetime import datetime
from operator import attrgetter
from models import match

class Round:
    """ Model for a round"""

    def __init__(self,tournament, round_name):
        """ player is an attibut of tournament model"""
        self.tournament = tournament
        self.round_name = round_name
        self.round_players = tournament.players
        self.matches = []
        self.datetime_start = datetime.now()
        self.datetime_end = ""

    def add_match(self, match):
        self.matches.append(match)

    def generate_first_pairs(self):
        # classer les joueurs en fonction de leur rang
        global match
        list_players_sorted = sorted(self.round_players, key=attrgetter("ranking"))
        number_of_pairs = len(self.round_players)/2
        nb = 0
        while nb < number_of_pairs:
            player1 = list_players_sorted[nb]
            player2 = list_players_sorted[int(nb + number_of_pairs)]
            self.add_match(match.Match(player1, player2))
            nb += 1

    def generate_pairs(self):
        # classer les joueurs en fonction de leur score puis de leur rang
        global match
        list_players_sorted = sorted(self.round_players, key=attrgetter("score", "ranking"))
        print(list_players_sorted)
        nb = 0
        while nb < len(self.round_players):
            player1 = list_players_sorted[nb]
            player2 = list_players_sorted[nb+1]
            self.add_match(match.Match(player1, player2))
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