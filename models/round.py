from datetime import datetime
from operator import attrgetter
from models import round, match, player

class RoundManager:
    """ serialize and deserialize players and save them into a tinyDB"""

    @classmethod
    def deserialize(cls, serialized_round):
        round_name = serialized_round['round_name']
        round_players = serialized_round['round_players']
        recreate_round_players = []
        for serialized_player in round_players:
            deserialized_player = player.PlayerManager.deserialize(serialized_player)
            recreate_player = player.Player.get(deserialized_player)
            recreate_round_players.append(recreate_player)
        matches = serialized_round['matches']
        recreate_matches = []
        for serialized_match in matches:
            deserialized_match = match.MatchManager.deserialize(serialized_match)
            recreate_match = match.Match.get(deserialized_match)
            recreate_matches.append(recreate_match)

        datetime_start = serialized_round['datetime_start']
        datetime_end = serialized_round['datetime_end']
        return {'round_name':round_name,
                'round_players': recreate_round_players,
                'matches': recreate_matches,
                'datetime_start': datetime_start,
                'datetime_end': datetime_end
                }


    @classmethod
    def get(cls, deserialized_round):
        """ get information of players using deserialize method"""
        round = Round(**deserialized_round)
        return round

class Round:
    """ Model for a round"""
    manager = RoundManager()
    def __init__(self,tournament, round_name):
        """ player is an attibut of tournament model"""
        self.tournament = tournament
        self.round_name = round_name
        self.round_players = tournament.players
        self.serialized_round_players = []
        self.matches = []
        self.serialized_matches = []
        self.datetime_start = datetime.now()
        self.datetime_end = ""
        self.serialized_datetime_start = f"{self.datetime_start}"
        self.serialized_datetime_end = f"{self.datetime_end}"

    def add_match(self, match):
        self.matches.append(match)

    def generate_first_pairs(self):
        # classer les joueurs en fonction de leur rang
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
        essais = 0
        list_players_sorted = sorted(self.round_players, key=attrgetter("score", "ranking"))
        print(list_players_sorted)
        while list_players_sorted:
            player1 = list_players_sorted.pop(0)
            player2 = list_players_sorted[0]
            test_pair = self.verify_pairs(player1, player2)
            if test_pair == "ok":
                player2 = list_players_sorted.pop(0)
                self.add_match(match.Match(player1, player2))
            else:
                try:
                    player2 = list_players_sorted.pop(1)
                except IndexError:
                    list_players_sorted = sorted(self.round_players, key=attrgetter("score", "ranking"))
                    if essais == 0:
                        list_players_sorted[1], list_players_sorted[2] = list_players_sorted[2], list_players_sorted[1]
                    if essais == 1:
                        list_players_sorted[2], list_players_sorted[3] = list_players_sorted[3], list_players_sorted[2]
                    if essais == 2:
                        list_players_sorted[3], list_players_sorted[4] = list_players_sorted[4], list_players_sorted[3]
                    if essais == 3:
                        list_players_sorted[1], list_players_sorted[3] = list_players_sorted[3], list_players_sorted[1]
                    if essais == 4:
                        list_players_sorted[2], list_players_sorted[4] = list_players_sorted[4], list_players_sorted[2]
                    if essais == 5:
                        return "Impossible d'associer les joueurs"
                    essais += 1
                    self.matches.clear()
                else:
                    self.add_match(match.Match(player1, player2))

    def verify_pairs(self, player1, player2):
        for round in self.tournament.rounds:
            for match in round.matches:
                if player1 in match.match:
                    if player2 in match.match:
                        return "impossible"
        return "ok"

    def add_end_time(self):
        self.datetime_end = datetime.now()

    def serialize(self):
        for match in self.matches:
            serialized_match = match.serialize()
            self.serialized_matches.append(serialized_match)
        for player in self.round_players:
            serialized_player = player.serialize()
            self.serialized_round_players.append(serialized_player)
        self.serialized_round = {
            'round_name': self.round_name,
            'round_players': self.serialized_round_players,
            'matches': self.serialized_matches,
            'datetime_start': self.serialized_datetime_start,
            'datetime_end': self.serialized_datetime_end,
        }
        return self.serialized_round


    @classmethod
    def get(cls, serialized_round):
        deserialized_round = cls.manager.deserialize(serialized_round)
        instance = cls.manager.get(deserialized_round)
        return instance

    def __str__(self):
        return f"nom du tournoi: {self.round_name}\n" \
               f"Joueurs participants: {self.round_players}\n" \
               f"Matches: {self.matches}\n" \
               f"Heure début {self.datetime_start}"

    def __repr__(self):
        return f"nom du tournoi: {self.round_name}\n" \
               f"Joueurs participants: {self.round_players}\n" \
               f"Matches: {self.matches}"