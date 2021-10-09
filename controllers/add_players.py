from models import player_model, round_model, players_list
from views import player_view
from controllers import launch_tournament
import datetime
import copy

class AddPlayers:
    """ Add players in a tournament"""

    def __init__(self):
        self.player_informations = player_view.PlayerView()
        self.verification = False
        self.player_index = 1
        self.player_list = players_list.PlayersList()
        self.player_in_round = round_model.RoundModel("round1")
        self.launch_tournament = launch_tournament.LaunchTournament("tournoi1")

    def __call__(self):
        # add questions the view to create the player
        self.player_informations.add_questions("Nom du joueur:\n", "last_name", "required")
        self.player_informations.add_questions("prénom du joueur:\n", "surname", "required")
        self.player_informations.add_questions("Date de naisance du joueur (jj-mm-aaaa):\n", "birthday", "date")
        self.player_informations.add_questions("sexe du joueur (M/F):\n", "sexe", ['M', 'F'])
        self.player_informations.add_questions("rang du joueur:\n", "ranking", int)

        nb = 2
        while nb:
        # ask question to manager
            self.player_informations.display_informations(f"Entrez les informotions du joueur {nb+1}")
            self.add_player_index()
            for question in self.player_informations.questions:
                self.verification = False
                while self.verification == False:
                    response = self.player_informations.ask_questions(question[0])
                    self.verify_response(question, response)
            player = player_model.PlayerModel(self.player_informations.informations_player)
            self.player_list.add_player(player)
            self.player_in_round.add_players((player.name, player.ranking))
            nb -= 1
        self.player_informations.display_informations("Votre joueur a bien été ajouté.")
        self.player_informations.display_informations("Tous les joueurs ont été ajoutés."
                                                      "Vous pouvez lancer votre tournoi")

        return self.launch_tournament(self.player_in_round)

    def add_player_index(self):
        self.player_informations.informations_player["index"] = self.player_index
        self.player_index += 1

    def verify_response(self, question, response):
        """ verify response before save it in the dictionnary """
        if question[2]:
            condition = question[2]
            if condition == int:
                try:
                    response = int(response)
                    if type(response) == condition:
                        self.player_informations.informations_player[question[1]] = response
                        self.verification = True
                except ValueError:
                    print(f"vous devez indiquer un nombre")
            elif type(condition) == list:
                if response in condition:
                    self.player_informations.informations_player[question[1]] = response
                    self.verification = True
                else:
                    print("vous devez choisir votre réponse dans la liste proposée")
            elif condition == "date":
                date = response.split("-")
                try:
                    response = datetime.date(int(date[2]), int(date[1]), int(date[0]))
                    self.player_informations.informations_player[question[1]] = response
                    self.verification = True
                except ValueError:
                    print("vérifier que le nombre de mois est entre 1 et 12 et que le nombre de jours"
                          "est entre 1 et 31")
                except TypeError:
                    print("les éléments de la date doivent être des chiffres séparés par un tiret")
                except IndexError:
                    print("les éléments de la date doivent être des chiffres séparés par un tiret")
            elif condition == "required":
                if response:
                    self.player_informations.informations_player[question[1]] = response
                    self.verification = True
                else:
                    print("Vous devez entrer une réponse")
            else:
                pass
        else:
            self.player_informations.informations_player[question[1]] = response
            self.verification = True


