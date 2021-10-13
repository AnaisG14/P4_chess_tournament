class DisplayMatches:
    """ Display all the matches of a round"""

    def __init__(self):
        pass

    def display_players(self, players):
        print("Les joueurs suivants participent à ce round :")
        for player in players:
            print(f"{player.first_name}; ")

    def display_matches(self, matches):
        nb = 1
        for match in matches:
            print(f"Match {nb}: {match}")
            nb += 1

    def ask_question(self, question):
        response = input(question)
        return response
