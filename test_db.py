from models import tournament, player, round
from controllers import launch_tournament

information_tournament1 = {"tournament_name": "Tournois Paris",
                          "tournament_place": "Sens",
                          "rounds_number": 4,
                          "time_controller": "bullet",
                          "manager_description": "test pour un premier tournois",
                          "start_date": "04/10/2021",
                           "end_date": "05/10/2021",
                            'rounds_name': [],
                            'rounds': [],
                            'players': [],
                            'results': []
                          }
tournois1 = tournament.Tournament(**information_tournament1)

dict_joueur1 = {"first_name" : "Anais",
                "last_name" : "Gatard",
                "birthday" : "14-05-1977",
                "sexe" : "F",
                "ranking" : 12,
                "score":0
                }

dict_joueur2 = {"first_name" : "Fred",
                "last_name" : "Lesire",
                "birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 13,
                "score": 0
                }
dict_joueur3 = {"first_name" : "Guillaume",
                "last_name" : "Esnault",
                "birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 26,
                "score": 0
                }
dict_joueur4 = {"first_name" : "Jean",
                "last_name" : "Dupont",
                "birthday" : "01-06-1969",
                "sexe" : "M",
                "ranking" : 4,
                "score": 0
                }
dict_joueur5 = {"first_name" : "Paul",
                "last_name" : "Demarre",
                "birthday" : "12-06-1973",
                "sexe" : "M",
                "ranking" : 22,
                "score": 0
                }
dict_joueur6 = {"first_name" : "Christelle",
                "last_name" : "Adam",
                "birthday" : "29-12-1986",
                "sexe" : "F",
                "ranking" : 16,
                "score": 0
                }
dict_joueur7 = {"first_name" : "Laure",
                "last_name" : "Laure",
                "birthday" : "18-07-2008",
                "sexe" : "F",
                "ranking" : 15,
                "score": 0
                }
dict_joueur8 = {"first_name" : "Jérémi",
                "last_name" : "Sno",
                "birthday" : "07-04-2004",
                "sexe" : "M",
                "ranking" : 29,
                "score": 0
                }
Anais = player.Player(**dict_joueur1)
Fred = player.Player(**dict_joueur2)
Guillaume = player.Player(**dict_joueur3)
Jean = player.Player(**dict_joueur4)
Paul = player.Player(**dict_joueur5)
Christelle = player.Player(**dict_joueur6)
Laure = player.Player(**dict_joueur7)
Jeremi = player.Player(**dict_joueur8)

tournois1.add_players(Anais)
tournois1.add_players(Fred)
tournois1.add_players(Guillaume)
tournois1.add_players(Jean)
tournois1.add_players(Paul)
tournois1.add_players(Christelle)
tournois1.add_players(Laure)
tournois1.add_players(Jeremi)

print("créer un round")
round1 = round.Round(tournois1, "round1")

print("creation des matches")
round1.generate_first_pairs()
print(round1)

print("enregistrement des scores")
print(f"Dupont gagne contre Adam")
Jean.modify_score(Jean.score + 1)
print(f"le nouveau score de Jean est {Jean.score}")
print(f"Demarre gagne contre Gatard")
Paul.modify_score(Paul.score + 1)
print(f"Lesire fait nul contre Esnault")
Fred.modify_score(Fred.score + 0.5)
Guillaume.modify_score(Guillaume.score + 0.5)
print(f"Sno gagne contre Laure")
Jeremi.modify_score(Jeremi.score + 1)
round1.add_end_time()
print(f"round1 terminé à {round1.datetime_end}")
print("nouveau round")
round2 = round.Round(tournois1,"Round2")
tournois1.add_rounds(round2)
print("relance des matches")
round2.generate_pairs()
print(round2.matches)

serialized_anais = Anais.serialize()
print(serialized_anais)
info_anais_bis = player.PlayerManager.deserialize(serialized_anais)
print(f"type info_anais_bis: {type(info_anais_bis)}")
anais_bis = player.Player.get(info_anais_bis)
# anais_bis = player.Player(**info_anais_bis)
print(anais_bis)
anais_bis.save_player()

serialized_tournois1 = tournois1.serialized()
print(serialized_tournois1)
tournois1.save_tournament()

tournois2 = tournament.Tournament.get(serialized_tournois1)
print(f"test réussi: \n {tournois2}")

# app = launch_tournament.LaunchTournament(tournois2)
# app()

test = tournament.TournamentManager.get_all_from_db()
for tournament in test:
    print(tournament['tournament_name'])

