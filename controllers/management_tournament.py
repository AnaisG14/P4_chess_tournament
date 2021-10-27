from models import tournament, player
from views import home_menu_view
from controllers import launch_tournament, add_players

class ManagementTournament:
    """ affichage des éléments des tournois"""

    def __init__(self):
        self.all_tournaments = tournament.TournamentManager.get_all()
        self.all_players = player.PlayerManager.get_all()
        self.menu_tournament_view = home_menu_view.TournamentList
        self.key = 1

    def selecte_tournament(self):
        tournament_entries = {}
        keys = []
        for tournament in self.all_tournaments:
            tournament_entries[self.key] = tournament
            keys.append(self.key)
            self.key += 1
        response = ""
        while response not in keys:
            response = self.menu_tournament_view.choice_tournament(tournament_entries)
            try:
                response = int(response)
            except ValueError:
                print("Vous devez entrer un nombre")
            else:
                return tournament_entries[response]

    def get_tournament_in_progress(self):
        tournament_in_progress = {}
        keys = []
        key = 1
        for each_tournament in self.all_tournaments:
            if not each_tournament.results:
                tournament_in_progress[key] = each_tournament
                keys.append(key)
                key += 1
        response = ""
        while response not in keys:
            response = self.menu_tournament_view.choice_tournament_in_progress(tournament_in_progress)
            try:
                response = int(response)
            except ValueError:
                print("Vous devez entrer un nombre")
            else:
                tournament_get = tournament_in_progress.pop(response)
                self.all_tournaments = [value for value in tournament_in_progress.values()]
                tournament.TournamentManager.save_all(self.all_tournaments)
                return tournament_get


    def __call__(self):
        tournament_in_progress = self.get_tournament_in_progress()
        if tournament_in_progress.players:
            return launch_tournament.LaunchTournament(tournament_in_progress)
        else:
            return add_players.AddPlayers(tournament_in_progress)



