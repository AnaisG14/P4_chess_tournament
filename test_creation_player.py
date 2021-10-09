from models import player_model, round_model, players_list
from views import player_view
from controllers import add_players

# test player_model
dict_joueur1 = {"index" : 1,
                "first_name" : "Anais",
                "last_name" : "Gatard",
                "date_of_birthday" : "14-05-1977",
                "sexe" : "F",
                "ranking" : 12
                }

dict_joueur2 = {"index" : 2,
                "first_name" : "Fred",
                "last_name" : "Lesire",
                "date_of_birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 13
                }

joueur1 = player_model.PlayerModel(dict_joueur1)
joueur2 = player_model.PlayerModel(dict_joueur2)

print(joueur1)
print(joueur2)

joueur2.modify_ranking(11)
print(joueur2)

# test player_view
player_view = player_view.PlayerView()
player_view.add_questions("nom","name", "required")
player_view.ask_questions(player_view.questions)

# test add_players
players = add_players.AddPlayers()
players()
list_players = players_list.PlayersList()
for player in list_players.players:
    print(f"joueur = {player.name}")