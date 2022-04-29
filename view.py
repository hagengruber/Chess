"""
    Module for displaying the current state of the game to the user
"""
import os


class View:
    """Class that handles everything for the module"""
    def __init__(self):
        self.model = None

    def update_board(self):
        """Updates the board to show recent movement"""
        self.clear_console()
        box_top = ' \u250C' + '\u2500\u2500\u2500\u252C'*7 + '\u2500\u2500\u2500\u2510'
        box_middle = ' \u251C' + '\u2500\u2500\u2500\u253C'*7 + '\u2500\u2500\u2500\u2524'
        box_bottom = ' \u2514' + '\u2500\u2500\u2500\u2534'*7 + '\u2500\u2500\u2500\u2518'
        print(self.model.currently_playing + ' is currently playing!')
        print('   1   2   3   4   5   6   7   8')
        print(box_top)
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(8):
            row = letters[i]
            for j in range(8):
                if self.model.board_state[i*8 + j] is not None:
                    row += '\u2502' + ' ' + self.model.board_state[i*8 + j].symbol + ' '
                else:
                    row += '\u2502' + '   '
            row += '\u2502'
            print(row)
            if i != 7:
                print(box_middle)
        print(box_bottom)

    @staticmethod
    def clear_console():
        """Clear the console of unnecessary stuff"""
        if os.name in ['nt', 'dos']:
            command = 'cls'
        else:
            command = 'clear'
        os.system(command)

    def print_menu(self):
        """Display the starting menu and tell 'model' to ask the user what he wants to do"""
        block = '\u2588'
        no_block = ' '
        self.clear_console()
        print('\n' + no_block + 3*block + no_block + block + no_block + block + no_block + 3*block
              + no_block + 3*block + no_block + 3*block)
        print(no_block + block + 3*no_block + block + no_block + block + no_block + block
              + 3*no_block + block + 3*no_block + block)
        print(no_block + block + 3*no_block + 3*block + no_block + 3*block + no_block
              + 3*block + no_block + 3*block)
        print(no_block + block + 3*no_block + block + no_block + block + no_block + block
              + 5*no_block + block + 3*no_block + block)
        print(no_block + 3*block + no_block + block + no_block + block + no_block + 3*block
              + no_block + 3*block + no_block + 3*block + '\n')
        print('Welcome to Chess! Please enter a number to choose an option :)')
        print('(1)PlayerVsPlayer   (2)PlayerVsBot   (3)LoadGame   (4)Exit')
        self.model.controller.get_menu_choice()
