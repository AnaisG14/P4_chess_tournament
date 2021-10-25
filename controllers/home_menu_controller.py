from models import home_menu
from views import home_menu_view
from controllers import create_tournament, add_players, report_actors, launch_tournament, report_tournaments

class HomeMenuController:
    """ Display HomeMenu, ask a choice to the user and return a controller"""
    def __init__(self):
        self.home_menu = home_menu.HomeMenu()
        self.menu_view = home_menu_view.HomeMenuView(self.home_menu)

    def __call__(self):
        self.home_menu.add_item("auto", "Créer et lancer un tournoi", create_tournament.CreateTournament())
        self.home_menu.add_item("auto", "Poursuivre un tournoi sauvegardé", launch_tournament.LaunchTournament)
        self.home_menu.add_item("", "---- Les joueurs ----")
        self.home_menu.add_item("auto", "Ajouter des joueurs", add_players.AddPlayers())
        self.home_menu.add_item("auto", "Afficher la liste des joueurs", report_actors.ReportActors())
        self.home_menu.add_item("", "---- Les tournois ----")
        self.home_menu.add_item("auto", "Afficher la liste des tournois", report_tournaments.ReportTournament())
        self.home_menu.add_item("auto", "Afficher la liste des rounds d'un tournoi", "tournament_report.TournamentReport()")
        self.home_menu.add_item("auto", "Afficher la liste des matches d'un tournoi", "tournament_report.TournamentReport()")
        return self.menu_view.user_choice()



