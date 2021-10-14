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
        response = ""
        while response != "o":
            response = self.rounds_view.ask_question("Pour générer les matches, taper 'o'.")
            if response == "q":
                exit()
        self.round.generate_first_pairs()
        self.rounds_view.display_matches(self.round.matches)
        self.tournament.add_rounds(self.round)

        response_score = self.rounds_view.ask_question("Tapez une touche pour entrez les scores ou 'q' pour quitter")
        if response_score == "q":
            exit()
        else:
            for match in self.round.matches:
                score1 = self.rounds_view.ask_question(f"Score de {match.player1}")
                score2 = self.rounds_view.ask_question(f"Score de {match.player2}")
                match.player1.modify_ranking(score1)
                match.player2.modify_ranking(score2)




