import os


class View:
    def __init__(self):
        self.model = None

    # Updates the board to show the changes that have been made
    def update_board(self):
        self.clear_console()
        box_top = '\u250C' + '\u2500\u2500\u2500\u252C'*7 + '\u2500\u2500\u2500\u2510'
        box_middle = '\u251C' + '\u2500\u2500\u2500\u253C'*7 + '\u2500\u2500\u2500\u2524'
        box_bottom = '\u2514' + '\u2500\u2500\u2500\u2534'*7 + '\u2500\u2500\u2500\u2518'
        print(box_top)
        for i in range(8):
            row = ''
            for j in range(8):
                row += '\u2502' + ' ' + self.model.board_state[i][j] + ' '
            row += '\u2502'
            print(row)
            if i != 7:
                print(box_middle)
        print(box_bottom)

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
        b = '\u2588'
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
