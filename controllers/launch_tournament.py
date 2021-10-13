from models import round
from views import display_matches

class LaunchTournament:
    """ Générer les paires de joueurs"""
    def __init__(self, tournament):
        self.tournament = tournament
        self.rounds_name = tournament.rounds_name
        self.round = round.Round(tournament, tournament.rounds_name[0])
        self.rounds_view = display_matches.DisplayMatches()

    def __call__(self):
        self.rounds_view.display_players(self.tournament.players)
        response = self.rounds_view.ask_question("Pour générer les matches, taper 'O'. "
                                                 "Pour quitter, n'importe quelle touche")
        if response == "O":
            self.round.generate_first_pairs()
            self.rounds_view.display_matches(self.round.matches)
        else:
            exit()

