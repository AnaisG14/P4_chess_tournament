class DisplayMatches:
    """ Display all the matches of a round"""

    def __init__(self):
        pass

    def display_players(self, players):
        print("Les joueurs suivants participent à ce round :")
        for player in players:
            print(f"{player}; ")

    def display_score(self, players):
        print(f"Voici les scores à la fin de ce round")
        for player in players:
            print({player.last_name}, {player.first_name}, {player.score})

    def display_matches(self, matches):
        print(f"Voici les matches pour ce round")
        nb = 1
        for match in matches:
            print(f"Match {nb}: {match}")
            nb += 1

    def display_classement(self, results):
        print(f"Voici le classement pour ce tournoi:\n{results}")

    def ask_question(self, question):
        response = input(question)
        return response
