from models import round, player

class MatchManager:
    """ serialize and deserialize players and save them into a tinyDB"""
    @classmethod
    def get(cls, deserialized_match):
        """ get information of players using deserialize method"""
        match = Match(**deserialized_match)
        return match

class Match:
    """ Instance of match"""
    manager = MatchManager()
    def __init__(self, player1, player2):
        # player = list ([last_name, ranking], score)
        self.player1 = player1
        self.player2 = player2
        self.match = (player1, player2)
        self.serialized_match = []

    def __str__(self):
        return f"{self.player1} contre {self.player2}"

    def __repr__(self):
        return f"{self.player1} contre {self.player2}"

    def serialized(self):
        player1 = self.player1.serialize()
        player2 = self.player2.serialize()
        self.serialized_match = {
            'player1': player1,
            'player2': player2,
            'match': (player1, player2)
        }
        return self.serialized_match

    @classmethod
    def deserialized_match(cls, serialized_match):
        player1 = player.Player.deserialize(serialized_match['player1'])
        player2 = player.Player.deserialize(serialized_match['player2'])
        return {'player1': player1, 'player2': player2}

    @classmethod
    def get(cls, serialized_match):
        deserialized_match = cls.deserialized_match(serialized_match)
        instance = cls.manager.get(deserialized_match)
        return instance

