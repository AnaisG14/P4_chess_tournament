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
        return {'first_name': first_name, 'last_name': last_name,
                'birthday': birthday, 'sexe': sexe,
                'ranking': ranking}

    @classmethod
    def get_all_from_db(cls):
        db = TinyDB('db.json')
        tournament_players = db.table('players')
        return tournament_players.all()

#     @classmethod
#     def save(cls):
#         data_to_save = cls.serialize()
#         db = TinyDB('db.json')
#         players_table = db.table('players')
#         players_table.insert(data_to_save)

class Player:
    """ Creation of player """
    manager = PlayerManager()
    def __init__(self, first_name, last_name, birthday, sexe, ranking):
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.sexe = sexe
        self.ranking = ranking
        self.tournaments_participation = []
        # self.score = score

    def modify_ranking(self, new_ranking):
        self.ranking = new_ranking

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
        }
        return self.serialized_player

    def save_player(self):
        # self.manager.save()
        serialized_player = self.serialize()
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert(serialized_player)

    @classmethod
    def get(cls, deserialized_player=""):
        if not deserialized_player:
            deserialized_players = cls.manager.get_all_from_db()
            for item in deserialized_players:
                deserialized_player = cls.manager.deserialize(item)
        return cls(**deserialized_player)

    def __str__(self):
        return f"{self.last_name} {self.first_name}: rang({self.ranking})"

    def __repr__(self):
        return f"{self.last_name} {self.first_name}: rang({self.ranking})"
