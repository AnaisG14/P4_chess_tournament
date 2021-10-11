
class HomeMenuView:
    def __init__(self, menu_model):
        # menu est d du type HomeMenu
        self.menu_view = menu_model
        self.keys = []
        self.choice = True

    def display_menu(self):
        """ Display the menu """
        print("Que voulez-vous faire ?")
        for key, value in self.menu_view.menu_entries.items():
            print(f"{str(key)}- {value[0]}")

    def user_choice(self):
        for key in self.menu_view.menu_entries.keys():
            self.keys.append(key)
        self.display_menu()
        while self.choice not in self.keys:
            self.choice = input("Que voulez-vous faire ? Entrez le numero correspondant")
        return self.menu_view.menu_entries[self.choice][1]
