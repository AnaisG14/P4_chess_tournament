from models import tournament_model, tournament_list, player_model, players_list,\
    round_model, match_model, classement_model, rapport_model

# test tournament_model
information_tournament1 = {"tournament_name": "Tournois test",
                          "tournament_place": "Sens",
                          "rounds_number": 4,
                          "time_controller": "bullet",
                          "manager_description": "test pour un premier tournois",
                          "start_date": "04/10/2021",
                           "end_date": "05/10/2021"
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
dict_joueur4 = {"index" : 4,
                "first_name" : "Jean",
                "last_name" : "Dupont",
                "date_of_birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 4
                }
dict_joueur5 = {"index" : 5,
                "first_name" : "Paul",
                "last_name" : "Demarre",
                "date_of_birthday" : "12-06-1973",
                "sexe" : "M",
                "ranking" : 22
                }
dict_joueur6 = {"index" : 6,
                "first_name" : "Christelle",
                "last_name" : "Adam",
                "date_of_birthday" : "29-12-1986",
                "sexe" : "F",
                "ranking" : 16
                }
dict_joueur7 = {"index" : 7,
                "first_name" : "Laure",
                "last_name" : "Laure",
                "date_of_birthday" : "18-07-2008",
                "sexe" : "F",
                "ranking" : 15
                }
dict_joueur8 = {"index" : 8,
                "first_name" : "Jérémi",
                "last_name" : "Sno",
                "date_of_birthday" : "07-04-2004",
                "sexe" : "M",
                "ranking" : 29
                }
Anais = player_model.PlayerModel(dict_joueur1)
Fred = player_model.PlayerModel(dict_joueur2)
Guillaume = player_model.PlayerModel(dict_joueur3)
Jean = player_model.PlayerModel(dict_joueur4)
Paul = player_model.PlayerModel(dict_joueur5)
Christelle = player_model.PlayerModel(dict_joueur6)
Laure = player_model.PlayerModel(dict_joueur7)
Jeremi = player_model.PlayerModel(dict_joueur8)
print("affichage des joueurs")
print(Anais)
print(Fred)
print("modification du rang d'un joueur")
Fred.modify_ranking(11)
print(Fred)
print("ajout des joueurs au tournoi1")
tournois1.add_players(Anais)
tournois1.add_players(Fred)
tournois1.add_players(Guillaume)
tournois1.add_players(Jean)
tournois1.add_players(Paul)
tournois1.add_players(Christelle)
tournois1.add_players(Laure)
tournois1.add_players(Jeremi)

print("ajout des joueurs au tournoi2")
tournois2.add_players(Anais)
for player in tournois1.players:
    print(player)
for player in tournois2.players:
    print(player)

print("créer un round")
round1 = round_model.RoundModel(tournois1.tournament_name, "round1", tournois1.players)
tournois1.add_rounds(round1)
for player in round1.round_players:
    print(player)

print("creation des matches")
round1.generate_first_pairs()
print(round1)

print("enregistrement des scores")
print(f"Dupont gagne contre Adam")
Jean.modifiy_score(Jean.score + 1)
print(f"le nouveau score de Jean est {Jean.score}")
print(f"Demarre gagne contre Gatard")
Paul.modifiy_score(Paul.score + 1)
print(f"Lesire fait nul contre Esnault")
Fred.modifiy_score(Fred.score + 0.5)
Guillaume.modifiy_score(Guillaume.score + 0.5)
print(f"Sno gagne contre Laure")
Jeremi.modifiy_score(Jeremi.score + 1)
round1.add_end_time()
print(f"round1 terminé à {round1.datetime_end}")
print("nouveau round")
round2 = round_model.RoundModel(tournois1.tournament_name,"Round2", tournois1.players)
tournois1.add_rounds(round2)
print("relance des matches")
round2.generate_pairs()
print(round2.matches)

print("tournois1")
print(tournois1)
print("classement")
classement = classement_model.ClassementModel(tournois1)
classement.display_results()
print(classement)

# test rapports
rapport1 = rapport_model.RapportModel(liste_tournois)
rapport1.list_actors("name")
print(f"Affichage par nom:\n{rapport1.actors}")
rapport1.list_actors("score")
print(f"Affichage par score:\n{rapport1.actors}")
print(f"liste des joueurs du tounois1 par nom")
list_player = rapport1.list_players(tournois1, "name")
for player in list_player:
    print(player)
print(f"liste des joueurs du tounois1 par score")
list_player = rapport1.list_players(tournois1, "score")
for player in list_player:
    print(player)
print(f"liste des tournois")
list_tournament = rapport1.list_tournament()
for tournament in list_tournament:
    print(tournament)
print(f"liste des rounds du tournois1")
rounds = rapport1.list_rounds(tournois1)
for round in rounds:
    print(round)
print(f"liste des matches du tournois1")
matches = rapport1.list_matches(tournois1)
for match in matches:
    print(match)



