from tinydb import TinyDB

class PlayerManager:
    """ serialize and deserialize players and save them into a tinyDB"""

    @classmethod
    def deserialize(cls, serialized_player):
        """ deserialize method"""
        first_name = serialized_player['first_name']
        last_name = serialized_player['last_name']
        birthday = serialized_player['birthday']
        sexe = serialized_player['sexe']
        ranking = serialized_player['ranking']
        score = serialized_player['score']
        return {'first_name': first_name, 'last_name': last_name, 'birthday': birthday, 'sexe': sexe,
                'ranking': ranking, 'score': score}

#     @classmethod
#     def save(cls):
#         data_to_save = cls.serialize()
#         db = TinyDB('db.json')
#         players_table = db.table('players')
#         players_table.insert(data_to_save)

class Player:
    """ Creation of player """
    manager = PlayerManager()
    def __init__(self, first_name, last_name, birthday, sexe, ranking, score=0):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sexe = sexe
        self.ranking = ranking
        self.tournaments_participation = []
        self.score = score

    def modify_ranking(self, new_ranking):
        self.ranking = new_ranking

    def modify_score(self, new_score):
        self.score = new_score

    def add_tournament(self, tounrnament_name):
        self.tournaments_participation.append(tounrnament_name)

    def serialize(self):
        # self.manager.serialize(self)
        self.serialized_player = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'sexe': self.sexe,
            'ranking': self.ranking,
            'score': self.score
        }
        return self.serialized_player

    def save_player(self):
        # self.manager.save()
        serialized_player = self.serialize()
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert(serialized_player)

    @classmethod
    def get(cls, serialized_player):
        deserialized_player = cls.manager.deserialize(serialized_player)
        instance = cls(**deserialized_player)
        return instance

    def __str__(self):
        return f"{self.last_name} {self.first_name}: rang({self.ranking}), score({self.score})"

    def __repr__(self):
        return f"{self.last_name} {self.first_name}: rang({self.ranking}), score({self.score})"
