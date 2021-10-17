from models import player, round
from views import player_view
from controllers import launch_tournament, home_menu_controller
from utils import verify_response

class AddPlayers:
    """ Add players in a tournament"""

    def __init__(self, tournament=""):
        self.tournament = tournament
        self.view_get_information_player = player_view.PlayerView()
        self.informations_player = {}
        self.verification = False
        self.player_index = 1
        self.number_player_to_add = 8

    def __call__(self):
        if not self.tournament:
            response = self.view_get_information_player.ask_questions("Combien voulez-vous inscrire "
                                                                      "de personnes ?")
            try:
                self.number_player_to_add = int(response)
            except ValueError:
                self.view_get_information_player.display_informations("vous devez entrez un nombre")
                return AddPlayers()

        # add questions to the view to create the player
        self.view_get_information_player.add_questions("Nom du joueur:\n", "last_name", "required")
        self.view_get_information_player.add_questions("prénom du joueur:\n", "first_name", "required")
        self.view_get_information_player.add_questions("Date de naisance du joueur (jj-mm-aaaa):\n", "birthday", "date")
        self.view_get_information_player.add_questions("sexe du joueur (M/F):\n", "sexe", ['M', 'F'])
        self.view_get_information_player.add_questions("rang du joueur:\n", "ranking", int)

        while self.number_player_to_add:
        # ask question to manager
            self.view_get_information_player.display_informations(f"Entrez les informotions du joueur "
                                                                  f"{self.number_player_to_add}")
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
            new_player = player.Player(**self.informations_player)
            new_player.save_player()
            if self.tournament:
                self.tournament.add_players(new_player)

            self.number_player_to_add -= 1
            self.view_get_information_player.display_informations_player()
        self.view_get_information_player.display_informations("Tous les joueurs ont été ajoutés."
                                                      "Vous pouvez lancer votre tournoi")

        if self.tournament:
            return launch_tournament.LaunchTournament(self.tournament)
        else:
            return home_menu_controller.HomeMenuController

    def add_player_index(self):
        self.view_get_information_player.responses["index"] = self.player_index
        self.player_index += 1

    def save_players(self):
        db = TinyDB('db.json')
        players_table = db.table('players')
        players_table.insert_multiple(self.serialized_players)



