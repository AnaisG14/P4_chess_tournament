class ClassementModel:
    """ Classement of player at the end of a tournament"""

    def __init__(self, tournament):
        self.players = tournament.players
        self.results = []

    def display_results(self):
        for player in self.players:
            self.results.append((player.last_name, player.score))
        self.results.sort(key=lambda x: x[1], reverse=True)

    def __str__(self):
        display_results = ""
        nb = 1
        for player in self.results:
            display_results += f"{nb}-{player}\n"
            nb += 1
        return display_results

