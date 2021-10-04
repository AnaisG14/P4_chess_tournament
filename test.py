from Models import tournament_model
from Views import tournament_view
from Controllers import create_tournament
"""
information_tournament = {"tournament_name": "Tournois test",
                          "tournament_place": "Sens",
                          "rounds_number": 4,
                          "rounds_list": ["round1", "round2", "round3"],
                          "players_index" : [1, 2, 3, 4, 5, 6, 7, 8],
                          "time_controller": "bullet",
                          "manager_description": "test pour un premier tournois",
                          "tournament_date": ("04/10/2021", "05/10/2021")
                          }

tournois = tournament_model.TournamentModel(information_tournament)
print(tournois.tournament_name)
print(tournois.players_index[2])
print(tournois)
"""
"""
info_tournois = tournament_view.TournamentView()
info_tournois.add_questions("quel est votre nom", "nom")
info_tournois.add_questions("quel est votre age", "age")
info_tournois.ask_questions()
print(info_tournois)
tournois2 = tournament_model.TournamentModel(info_tournois.informations_tournament)
print(tournois2)
"""

app = create_tournament.CreateTournament()
app()
print(app)
