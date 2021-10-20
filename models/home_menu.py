from models import tournament

class HomeMenu():
    """ Model for the home menu """

    def __init__(self):
        self.menu_entries = {}
        self.auto_key = 1

    def add_item(self, key, entries, controller):
        """ Add item to the menu"""
        if key == "auto":
            key = str(self.auto_key)
            self.auto_key += 1
        self.menu_entries[key] = (entries, controller)
        return

    def select_tournament(self):
        tournament_data = tournament.Tournament.get_tournament_in_db()
        return f"{tournament_data['tournament_name']} à {tournament_data['place']} du " \
               f"{tournament_data['start_date']} au {tournament_data['end_date']}"


    def __repr__(self):
        return f"{self.menu_entries}"






