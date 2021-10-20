from models import round, tournament
from views import display_matches, tournament_view

class LaunchTournament:
    """ Générer les paires de joueurs"""
    def __init__(self, tournament_instance=""):
        self.tournament_view = tournament_view.TournamentView()
        self.choice = ""
        if tournament_instance:
            self.tournament = tournament_instance
        else:
            self.tournament = tournament.Tournament.get(self.get_tournament_in_progress())
        self.rounds_name = tournament.rounds_name
        self.rounds_view = display_matches.DisplayMatches()
        self.verification = False

    def __call__(self):
        while len(self.tournament.rounds) < len(self.tournament.rounds_number):
            if not self.tournament.rounds:
                self.wait_response("lancer le premier round.")
                self.generate_first_round()
            self.generate_rounds(f"Round {self.tournament.rounds_name[len(self.tournament.rounds)+1]}")
            results = self.tournament.display_results()
            self.rounds_view.display_classement(results)

    def get_tournament_in_progress(self):
        tournament_data = tournament.Tournament.get_tournament_in_progress()
        self.choice = self.tournament_view.display_tournament_in_progress(tournament_data)
        if self.choice in tournament_data.keys():
            return tournament_data[self.choice]

    def generate_first_round(self):
        new_round = round.Round(self.tournament, self.tournament.rounds_name[0])
        new_round.generate_first_pairs()
        self.rounds_view.display_matches(new_round.matches)
        self.tournament.add_rounds(new_round)
        self.wait_response("entrer les scores")
        new_round.add_end_time()
        self.add_score(new_round)


    def add_score(self, round):
        for match in round.matches:
            while not self.verification:
                score1 = self.rounds_view.ask_question(f"Score de {match.player1}")
                test_score = self.verify_score(score1)
                if test_score == True:
                    self.verification = True
                else:
                    print(test_score)
            self.verification = False
            while not self.verification:
                score2 = self.rounds_view.ask_question(f"Score de {match.player2}")
                test_score = self.verify_score(score2)
                if test_score == True:
                    self.verification = True
                else:
                    print(test_score)
            self.verification = False
            match.player1.modify_score(match.player1.score + float(score1))
            match.player2.modify_score(match.player2.score + float(score2))
        self.rounds_view.display_score(self.tournament.players)

    def verify_score(self, score_to_test):
        try:
            float(score_to_test)
        except ValueError:
            return f"vous devez entrer un nombre"
        else:
            return True

    def generate_rounds(self, round_name):
        new_round = round.Round(self.tournament, round_name)
        self.wait_response("lancer le round suivant.")
        new_round.generate_pairs()
        self.rounds_view.display_matches(new_round.matches)
        self.tournament.add_rounds(new_round)
        self.wait_response("entrer les scores")
        new_round.add_end_time()
        self.add_score(new_round)
        self.wait_response("Enregistrer")
        self.tournament.save_tournament()


    def wait_response(self, question):
        response = self.rounds_view.ask_question(f"Tapez 'q' pour quitter ou 'entrez' pour {question}")
        if response == "q":
            exit()
        else:
            return




