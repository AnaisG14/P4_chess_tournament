from models import player, round
from views import player_view
from controllers import launch_tournament
from utils import verify_response

class AddPlayers:
    """ Add players in a tournament"""

    def __init__(self, tournament):
        self.tournament = tournament
        self.view_get_information_player = player_view.PlayerView()
        self.informations_player = {}
        self.verification = False
        self.player_index = 1

    def __call__(self):
        # add questions to the view to create the player
        self.view_get_information_player.add_questions("Nom du joueur:\n", "last_name", "required")
        self.view_get_information_player.add_questions("prénom du joueur:\n", "first_name", "required")
        self.view_get_information_player.add_questions("Date de naisance du joueur (jj-mm-aaaa):\n", "birthday", "date")
        self.view_get_information_player.add_questions("sexe du joueur (M/F):\n", "sexe", ['M', 'F'])
        self.view_get_information_player.add_questions("rang du joueur:\n", "ranking", int)

        nb = 8
        while nb:
        # ask question to manager
            self.view_get_information_player.display_informations(f"Entrez les informotions du joueur {nb}")
            self.add_player_index()
            for question in self.view_get_information_player.questions:
                self.verification = False
                while not self.verification:
                    response = self.view_get_information_player.ask_questions(question[0])
                    test_response = verify_response.verify_response(question, response)
                    if test_response == True:
                        self.verification = True
                        self.informations_player[question[1]] = response
                    else:
                        print(test_response)
            self.tournament.add_players(player.Player(**self.informations_player))
            nb -= 1
            self.view_get_information_player.display_informations_player()
        self.view_get_information_player.display_informations("Tous les joueurs ont été ajoutés."
                                                      "Vous pouvez lancer votre tournoi")

        return launch_tournament.LaunchTournament(self.tournament)

    def add_player_index(self):
        self.view_get_information_player.responses["index"] = self.player_index
        self.player_index += 1



