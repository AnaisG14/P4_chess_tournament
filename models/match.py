from models import round, player

class MatchManager:
    """ serialize and deserialize players and save them into a tinyDB"""

    @classmethod
    def deserialize(cls, serialized_match):
        player1 = player.PlayerManager.deserialize(serialized_match['player1'])
        player2 = player.PlayerManager.deserialize(serialized_match['player2'])
        return {'player1': player1, 'player2': player2}


class Match:
    """ Instance of match"""
    manager = MatchManager()
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.match = (player1, player2)
        self.serialized_match = []

    def __str__(self):
        return f"{self.player1} contre {self.player2}"

    def __repr__(self):
        return f"{self.player1} contre {self.player2}"

    def serialize(self):
        player1 = self.player1.serialize()
        player2 = self.player2.serialize()
        self.serialized_match = {
            'player1': player1,
            'player2': player2,
            'match': (player1, player2)
        }
        return self.serialized_match

    @classmethod
    def get(cls, serialized_match):
        deserialized_match = cls.manager.deserialize(serialized_match)
        instance = cls(**deserialized_match)
        return instance

