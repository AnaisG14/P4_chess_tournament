# Séquence de l'application
#   - menu d'accueil
#       1- Se connecter
#       2- commencer une partie
#       3- reprendre une partie en cours
#       4- consulter le palmarès de résultats
#       5- consulter le classement

# Class des controllers
class ApplicationController:
    """Controleur principale qui lance l'application et instancie le premier controller"""
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuControllers()
        while self.controller:
            self.controller = self.controller()

class HomeMenuControllers:
    """Séquence d'accueil qui va implémenter le menu principal.
    Il fait appel à la vue et sur la base du menu sélectionné, il passe la main à un autre controller"""

    def __init__(self):
        self.menu = Menu() # vient d'un modèle menu
        self.view = HomeMenuView(self.menu) # affichage du menu importé depuis les vues

    def __call__(self):
        """ méthode utilisée dès que la fonction est appelée"""
        # création du menu
        self.menu.add("auto", "se connecter", ConnectionMenuController()) # ajoute des entrées au menu
        self.menu.add("auto", "commencer une partie", NewGameController()) # ajoute des entrées au menu
        self.menu.add("q", "Quitter", EndScreenController()) # ajoute des entrées au menu

        # demander à la vue d'afficher le menu et de collecter la réponse
        user_choice = self.view.get_user_choice()

        # retourner le controller associé au choix de l'utilistateur au controleur principal
        return  user_choice.handler # appel le controleur de nouveau jeu

class ConnectionMenuControllers:
    """ Séquence de connection"""
    def __call__(self):
        return # controller suivant

class SignupMenuController:
    """ Séquence(controller) d'inscription"""

class NewGameController:
    """ Séquence (controller) de gestion de démarrage de la partie"""
    pass

class OngoingGame:
    """ Gestion de la partie en cours"""
    pass

class RankingController:
    """Gestion du classement"""
    pass

class EndScreenController:
    pass

# exemples Class des views
class HomeMenuView:
    """ Affichage du Menu et demander un choix en utilisant un modèle menu"""
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        """ afficher le menu"""
        print("Accueil du jeu")
        for key, option in self.menu.entrie.items():
            print(f"{key} : {option}")

    def get_user_choice(self):
        self._display_menu()

        # afficher le menu à l'utilisateur

        # demander à l'utilisateur de faire un choix
        choice = input(">>")
        # valider le choix de l'utilisateur
        if choice in self.menu:
            return self.menu[choice]
        # retourner le choix de l'utilsateur


# exemples Class des models
class MenuEntry:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler

    def __repr__(self):
        return str(self.option)

class Menu:
    def __init__(self):
        self.entries = {}
        self._autokey = 1

    def __add__(self, key, option, handler):
        if key == "auto":
            key = str(self._autokey)
            self._autokey +=1
        self.entries[str(key)] = MenuEntry(option, handler)

    def __contains__(self):
        return str(choice) in self.entries

    def __getitem__(self, choice):
        pass

if __name__ == "__main__":
    app = ApplicationController()
    app.start()