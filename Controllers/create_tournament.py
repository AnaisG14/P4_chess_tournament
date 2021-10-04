from Models import tournament_model
from Views import tournament_view

class CreateTournament:
    """ Create tournament with user informations"""
    def __init__(self):
        self.informations_tournament = tournament_view.TournamentView()
        self.tournament = tournament_model.TournamentModel(self.informations_tournament.informations_tournament)

    def __call__(self):
        print("création du tournoi")
        # save questions
        self.informations_tournament.add_questions("Donnez un nom au tournois à créer",
                                                   "tournament_name")
        self.informations_tournament.add_questions("Indiquez le lieu de votre tournois",
                                                   "tournament_place")
        self.informations_tournament.add_questions("Indiquez le nombre de round (par défaut 4)",
                                                   "rounds_number",
                                                   "int(response)")
        self.informations_tournament.add_questions("Quel sera le controleur de temps",
                                                   "time_controller",
                                                   "response in ['bullet', 'blitz', 'coup rapide']")
        self.informations_tournament.add_questions("Description du tournois facultatif",
                                                   "manager_description")
        self.informations_tournament.add_questions("Date de début",
                                                   "stard_date")
        self.informations_tournament.add_questions("Date de fin",
                                                   "end_date")

        # ask question to user
        self.informations_tournament.ask_questions()

    def __str__(self):
        return str(self.tournament)

