from models import round, tournament
from views import display_matches, tournament_view

class LaunchTournament:
    """ Générer les paires de joueurs"""
    def __init__(self, tournament_instance=""):
        self.tournament_view = tournament_view.TournamentView()
        if tournament_instance:
            self.tournament = tournament_instance
        else:
            self.tournament = tournament.Tournament.get(self.get_tournament_in_progress())
        # self.rounds_name = self.tournament.rounds_name
        self.rounds_view = display_matches.DisplayMatches()
        self.verification = False

    def __call__(self):
        while len(self.tournament.rounds) < int(self.tournament.rounds_number):
            if not self.tournament.rounds:
                self.wait_response("lancer le premier round.")
                self.generate_first_round()
            players_score = self.tournament.rounds[-1].round_players
            self.generate_rounds(f"Round {self.tournament.rounds_name[len(self.tournament.rounds)]}", players_score)
        results = self.tournament.display_results(self.round_players)
        self.rounds_view.display_classement(results)

    def get_tournament_in_progress(self):
        tournament_data = tournament.Tournament.get_tournament_in_progress()
        choice = self.tournament_view.display_tournament_in_progress(tournament_data)
        return tournament_data[int(choice)]
        # if int(choice) in range(len(tournament_data)):
        #     return tournament_data[choice]
        # else:
        #     print("entrez un choix valide")

    def generate_first_round(self):
        players_with_score = [[player, 0] for player in self.tournament.players]

        new_round = round.Round(self.tournament, self.tournament.rounds_name[0],
                                players_with_score)
        new_round.generate_first_pairs()
        self.rounds_view.display_matches(new_round.matches)
        self.tournament.add_rounds(new_round)
        print(f"new_round: {new_round}")
        print(f"instance: {self.tournament.rounds}")
        self.wait_response("entrer les scores")
        new_round.add_end_time()
        self.add_score(new_round)
        self.round_players = new_round.round_players

    def add_score(self, round):
        for match in round.matches:
            while not self.verification:
                score1 = self.rounds_view.ask_question(f"Score de {match.match[0][0]}")
                test_score = self.verify_score(score1)
                if test_score == True:
                    self.verification = True
                else:
                    print(test_score)
            self.verification = False
            while not self.verification:
                score2 = self.rounds_view.ask_question(f"Score de {match.match[1][0]}")
                test_score = self.verify_score(score2)
                if test_score == True:
                    self.verification = True
                else:
                    print(test_score)
            self.verification = False
            match.match[0][1] += float(score1)
            match.match[1][1] += float(score2)
        self.rounds_view.display_score(round.matches)

    def verify_score(self, score_to_test):
        try:
            float(score_to_test)
        except ValueError:
            return f"vous devez entrer un nombre"
        else:
            return True

    def generate_rounds(self, round_name, round_players):
        new_round = round.Round(self.tournament, round_name, round_players)
        new_round.matches = []
        self.wait_response("lancer le round suivant.")
        print(new_round.round_name)
        new_round.generate_pairs()
        self.rounds_view.display_matches(new_round.matches)
        self.tournament.add_rounds(new_round)
        print(f"new_round: {new_round}")
        print(f"instance: {self.tournament.rounds}")
        self.wait_response("entrer les scores")
        new_round.add_end_time()
        self.add_score(new_round)
        self.round_players = new_round.round_players
        # self.wait_response("Enregistrer")
        # self.tournament.save_tournament()


    def wait_response(self, question):
        response = self.rounds_view.ask_question(f"Tapez 'q' pour quitter ou 'entrez' pour {question}")
        if response == "q":
            exit()
        else:
            return




