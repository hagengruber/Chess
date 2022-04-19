import sys


class Controller:
    def __init__(self):
        self.model = None

    def get_menu_choice(self):
        selection = input()
        if selection == '1':
            self.model.view.update_board()
        elif selection == '2':
            pass
        elif selection == '3':
            pass
        elif selection == '4':
            self.model.view.clear_console()
            sys.exit()
        else:
            print('Your choice is not valid! Please try again!')
            self.get_menu_choice()
