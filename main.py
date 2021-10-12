import sys
from controllers import home_menu_controller

class ApplicationController:
    """ Launch the software"""
    def __init__(self):
        self.controller = None

    def run(self):
        self.controller = home_menu_controller.HomeMenuController()
        while self.controller:
            self.controller = self.controller()

def main():
    app = ApplicationController()
    app.run()

if __name__ == '__main__':
    sys.exit(main())

# créer un tournoi

# Ajouter 8 joueurs

# Lancer le tournoi

# Générer les pairs pour le premier tour

# entrez les résultats du premier tour