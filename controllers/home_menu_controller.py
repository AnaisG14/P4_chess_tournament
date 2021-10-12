from models import home_menu
from views import home_menu_view
from controllers import create_tournament, add_players, view_reports, launch_tournament


class HomeMenuController:
    """ Display HomeMenu and ask a choice to the user"""
    def __init__(self):
        self.home_menu = home_menu.HomeMenu()
        self.menu_view = home_menu_view.HomeMenuView(self.home_menu)

    def __call__(self):
        self.home_menu.add_item("auto", "Créer un tournoi", create_tournament.CreateTournament())
        # self.home_menu.add_item("auto", "Ajouter des joueurs", add_players.AddPlayers(""))
        # self.home_menu.add_item("auto", "Lancer le tournoi", launch_tournament.LaunchTournament("en attente"))
        # self.home_menu.add_item("auto", "Afficher les rapports", view_reports.ViewReports())

        return self.menu_view.user_choice()

