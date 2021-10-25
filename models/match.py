from models import round, player

class MatchManager:
    """ serialize and deserialize players and save them into a tinyDB"""

    @classmethod
    def deserialize(cls, serialized_match):
        serialized_player1 = serialized_match[0]
        serialized_player2 = serialized_match[1]
        return {'match': [[player.PlayerManager.deserialize(serialized_player1[0]), serialized_player1[1]],
                          [player.PlayerManager.deserialize(serialized_player2[0]), serialized_player2[1]]]
                }


class Match:
    """ Instance of match"""
    manager = MatchManager()
    def __init__(self, player1, player2):
        """ player1 = [player, score]"""
        # self.player1 = player1
        # self.player2 = player2
        self.match = (player1, player2)

    def __str__(self):
        # return f"{self.player1} contre {self.player2}"
        return f"{self.match[0]} contre {self.match[1]}"

    def __repr__(self):
        # return f"{self.player1} contre {self.player2}"
        return f"{self.match[0]} contre {self.match[1]}"

    def serialize(self):
        serialized_player1 = self.match[0][0].serialize()
        serialized_player2 = self.match[1][0].serialize()
        self.serialized_match = {
            'match': [[serialized_player1, self.match[0][1]],
                      [serialized_player2, self.match[1][1]]]
                      }
        return self.serialized_match

    @classmethod
    def get(cls, serialized_match):
        deserialized_match = cls.manager.deserialize(serialized_match)
        instance = cls(deserialized_match['player1'], deserialized_match['player2'])
        return instance

