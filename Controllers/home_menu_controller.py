from Models import home_menu_model
from Views import home_menu_view
from Controllers import create_tournament, add_players, view_reports

class HomeMenuController:
    """ Display HomeMenu and ask a choice to the user"""
    def __init__(self):
        self.home_menu = home_menu_model.HomeMenuModel()
        self.menu_view = home_menu_view.HomeMenuView(self.home_menu)

    def __call__(self):
        self.home_menu.add_item("auto", "Créer un tournoi", create_tournament.CreateTournament())
        self.home_menu.add_item("auto", "Ajouter des joueurs", add_players.AddPlayers())
        self.home_menu.add_item("auto", "Afficher les rapports", view_reports.ViewReports())

        return self.menu_view.user_choice()

