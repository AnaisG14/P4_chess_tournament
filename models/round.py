from datetime import datetime
from models import round, match, player, tournament

class RoundManager:
    """ serialize and deserialize players and save them into a tinyDB"""

    @classmethod
    def deserialize(cls, serialized_round):
        round_name = serialized_round['round_name']
        matches = serialized_round['matches']
        recreate_matches = []
        for serialized_match in matches:
            recreate_matches.append(match.Match.get(serialized_match))

        datetime_start = serialized_round['datetime_start']
        datetime_end = serialized_round['datetime_end']
        return {'round_name': round_name,
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

    def __init__(self, round_name, matches=[], datetime_start=None, datetime_end=""):
        self.round_name = round_name
        self.matches = matches
        self.serialized_matches = []
        if datetime_start:
            self.datetime_start = datetime_start
        else:
            self.datetime_start = datetime.now()
        self.datetime_end = datetime_end
        self.serialized_datetime_start = str(self.datetime_start)
        self.serialized_datetime_end = str(self.datetime_end)


    def add_match(self, match):
        self.matches.append(match)

    def add_end_time(self):
        self.datetime_end = datetime.now()

    def serialize(self):
        for match in self.matches:
            serialized_match = match.serialize()
            self.serialized_matches.append(serialized_match)
        self.serialized_round = {
            'round_name': self.round_name,
            'matches': self.serialized_matches,
            'datetime_start': self.serialized_datetime_start,
            'datetime_end': self.serialized_datetime_end,
        }
        return self.serialized_round

    @classmethod
    def get(cls, serialized_round):
        deserialized_round = cls.manager.deserialize(serialized_round)
        instance = cls(**deserialized_round)
        return instance

    def __str__(self):
        return f"nom du tournoi: {self.round_name}\n" \
               f"Matches: {self.matches}\n" \
               f"Heure début {self.datetime_start}"

    def __repr__(self):
        return f"nom du tournoi: {self.round_name}\n" \
               f"Matches: {self.matches}"