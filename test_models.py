from models import tournament_model, tournament_list, player_model, players_list, round_model

# test tournament_model
information_tournament1 = {"tournament_name": "Tournois test",
                          "tournament_place": "Sens",
                          "rounds_number": 4,
                          "time_controller": "bullet",
                          "manager_description": "test pour un premier tournois",
                          "tournament_date": ("04/10/2021", "05/10/2021")
                          }
information_tournament2 = {"tournament_name": "Autre tournois test",
                          "tournament_place": "Paris",
                          "rounds_number": 3,
                          "time_controller": "blizt",
                          "manager_description": "deuxième tournoi",
                          "start_date": "04/11/2021",
                           "end_date": "05/11/2021"
                          }
print("creation de 2 tournois et d'une liste de tournoi")
tournois1 = tournament_model.TournamentModel(information_tournament1)
tournois2 = tournament_model.TournamentModel(information_tournament2)
liste_tournois = tournament_list.TournamentList()
print("affichage du nom premier tournoi")
print(tournois1.tournament_name)
print("affichage du 2nd tournoi")
print(tournois2)
print("ajout des tournoi à la liste créée")
liste_tournois.add_tournament(tournois1)
liste_tournois.add_tournament(tournois2)
print("affichage du nom des tournois de la liste")
for tournoi in liste_tournois.tournaments:
    print(tournoi.tournament_name)
print("affichage de tous les tournois de la liste")
print(liste_tournois)

# test player_model et list_player
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
dict_joueur3 = {"index" : 3,
                "first_name" : "Guillaume",
                "last_name" : "Esnault",
                "date_of_birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 26
                }
dict_joueur4 = {"index" : 3,
                "first_name" : "Jean",
                "last_name" : "Dupont",
                "date_of_birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 4
                }
Anais = player_model.PlayerModel(dict_joueur1)
Fred = player_model.PlayerModel(dict_joueur2)
Guillaume = player_model.PlayerModel(dict_joueur3)
Jean = player_model.PlayerModel(dict_joueur4)
print("affichage des joueurs")
print(Anais)
print(Fred)
print("modification du rang d'un joueur")
Fred.modify_ranking(11)
print(Fred)
print("ajout des joueurs à un tournoi")
tournois1.add_players(Anais)
tournois1.add_players(Fred)
tournois1.add_players(Guillaume)
tournois1.add_players(Jean)
tournois2.add_players(Anais)
for player in tournois1.players:
    print(player)
for player in tournois2.players:
    print(player)

print("créer un round")
round1 = round_model.RoundModel(tournois1.tournament_name, "round1", tournois1.players)
for player in round1.round_players:
    print(player)