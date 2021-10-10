class PlayerModel:
    """ Creation of player """

    def __init__(self, dict_player, score=0):
        self.attribut_player = dict_player
        for key, value in dict_player.items():
            setattr(self, key, value)
        self.tournaments_participation = []
        self.score = score

    def modify_ranking(self, new_ranking):
        self.attribut_player["ranking"] = new_ranking

    def modifiy_score(self, new_score):
        self.score = new_score

    def add_tournament(self, tounrnament_name):
        self.tournaments_participation.append(tounrnament_name)

    def save_player(self):
        pass

    def __str__(self):
        return str(self.attribut_player)

    def __repr__(self):
        for key, value in self.attribut_player.items():
            print(f"{key}: {value}")