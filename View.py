import os


class View:
    def __init__(self):
        self.model = None

    # Updates the board to show the changes that have been made
    def update_board(self):
        pass

    # Clears the Console
    @staticmethod
    def clear_console():
        if os.name in ['nt', 'dos']:
            command = 'cls'
        else:
            command = 'clear'
        os.system(command)

    # Show the starting menu
    def print_menu(self):

        # ToDo: Vorschlag diskutieren
        # Vorschlag:
        # pip install pyfiglet
        # import pyfiglet
        # print(pyfiglet.figlet_format("Let's  Play  Chess"))

        b = u"\u2588"
        nb = ' '
        self.clear_console()
        print('\n' + nb + 3*b + nb + b + nb + b + nb + 3*b + nb + 3*b + nb + 3*b)
        print(nb + b + 3*nb + b + nb + b + nb + b + 3*nb + b + 3*nb + b)
        print(nb + b + 3*nb + 3*b + nb + 3*b + nb + 3*b + nb + 3*b)
        print(nb + b + 3*nb + b + nb + b + nb + b + 5*nb + b + 3*nb + b)
        print(nb + 3*b + nb + b + nb + b + nb + 3*b + nb + 3*b + nb + 3*b + '\n')
        print('Welcome to TicTacToe! Please enter a number to choose an option :)')
        print('(1)PlayerVsPlayer   (2)PlayerVsBot   (3)LoadGame   (4)Exit')
        self.model.controller.get_menu_choice()
