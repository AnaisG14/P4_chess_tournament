from tinydb import TinyDB

class ManagementDB:
    """ to create, save or get on tiny_db"""
    def __init__(self):
        self.db = TinyDB('db.json')
        self.tournaments_table = self.db.table('tournaments')
        self.players_table = self.db.table('players')

    def get(self, table):
        if table == "tournaments":
            return self.tournaments_table.all()
        elif table == "players":
            return self.players_table.all()

    def save(self, table, to_save):
        if table == "tournaments":
            self.tournaments_table.insert(to_save)
        elif table == "players":
            self.players_table.insert(to_save)



