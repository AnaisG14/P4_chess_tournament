from Models import tournament_model
from Views import tournament_view, home_menu_view
from Controllers import home_menu_controller
import datetime

class CreateTournament:
    """ Create tournament with user informations"""
    def __init__(self):
        self.informations_tournament = tournament_view.TournamentView()
        self.tournament = tournament_model.TournamentModel(self.informations_tournament.informations_tournament)
        self.home_menu = home_menu_controller.HomeMenuController()

    def __call__(self):
        print("création du tournoi")

        # save questions
        self.informations_tournament.add_questions("Donnez un nom au tournois à créer:\n",
                                                   "tournament_name",
                                                   "required")
        self.informations_tournament.add_questions("Indiquez le lieu de votre tournois:\n",
                                                   "tournament_place",
                                                   "required")
        self.informations_tournament.add_questions("Indiquez le nombre de rounds (par défaut 4):\n",
                                                   "rounds_number",
                                                   int,
                                                   4)
        self.informations_tournament.add_questions("Quel sera le contrôleur de temps (bullet, blitz, coup rapide):\n",
                                                   "time_controller",
                                                   ['bullet', 'blitz', 'coup rapide'])
        self.informations_tournament.add_questions("Description du tournois facultatif:\n",
                                                   "manager_description")
        self.informations_tournament.add_questions("Date de début (aaaa-mm-dd):\n",
                                                   "start_date",
                                                   "date")
        self.informations_tournament.add_questions("Date de fin (aaaa-mm-dd):\n",
                                                   "end_date"
                                                   "date")

        # ask question to user
        for question in self.informations_tournament.questions:
            self.verification = False
            while self.verification == False:
                response = self.informations_tournament.ask_questions(question[0])
                if not response:
                    response = question[3]
                self.verify_response(question, response)

        print("Votre tournoi a bien été créé. Que voulez-vous faire maintenant")
        return self.home_menu

    def verify_response(self, question, response):
        """ verify response before save it in the dictionnary """
        if question[2]:
            condition = question[2]
            if condition == int:
                try:
                    response = int(response)
                    if type(response) == condition:
                        self.informations_tournament.informations_tournament[question[1]] = response
                        self.verification = True
                except ValueError:
                    print(f"vous devez indiquer un nombre")
            elif type(condition) == list:
                if response in condition:
                    self.informations_tournament.informations_tournament[question[1]] = response
                    self.verification = True
                else:
                    print("vous devez choisir votre réponse dans la liste proposée")
            elif condition == "date":
                date = response.split("-")
                try:
                    response = datetime.date(int(date[0]), int(date[1]), int(date[2]))
                    self.informations_tournament.informations_tournament[question[1]] = response
                    self.verification = True
                except ValueError:
                    print("vérifier que le nombre de mois est entre 1 et 12 et que le nombre de jours"
                          "est entre 1 et 31")
                except TypeError:
                    print("les éléments de la date doivent etre des chiffres séparés par un tiret")
            elif condition == "required":
                if response:
                    self.informations_tournament.informations_tournament[question[1]] = response
                    self.verification = True
                else:
                    print("Vous devez entrer une réponse")
            else:
                pass
        else:
            self.informations_tournament.informations_tournament[question[1]] = response
            self.verification = True

    def __str__(self):
        return str(self.tournament)

