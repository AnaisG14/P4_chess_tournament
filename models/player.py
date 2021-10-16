class Player:
    """ Creation of player """

    def __init__(self, last_name, first_name, birthday, sexe, ranking, score=0):
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

    def save_player(self):
        pass

    def __str__(self):
        return f"{self.last_name} {self.first_name}: rang({self.ranking}), score({self.score})"

    def __repr__(self):
        return f"{self.last_name} {self.first_name}: rang({self.ranking}), score({self.score})"
