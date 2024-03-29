"""
    Module for displaying the current state of the game to the user
"""
import os


class View:
    """Class that handles everything for the module"""
    def __init__(self):
        self.model = None
        self.last_board = None

    def update_board(self, state=""):
        """Updates the board to show recent movement"""
        self.clear_console()

        if state == "":
            state = self.model.board_state

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
                if state[i*8 + j] is not None:
                    if state[i*8 + j] != self.last_board[i*8 + j]:
                        row += '\u2502\x1b[6;30;42m' + ' ' + state[i*8 + j].symbol + ' \x1b[0m'
                    else:
                        row += '\u2502' + ' ' + state[i * 8 + j].symbol + ' '
                else:
                    if state[i * 8 + j] != self.last_board[i * 8 + j]:
                        row += '\u2502\x1b[6;30;42m' + '   \x1b[0m'
                    else:
                        row += '\u2502' + '   '

            row += '\u2502'
            print(row)
            if i != 7:
                print(box_middle)
        print(box_bottom)

        self.last_board = self.model.get_copy_board_state()

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
        print('Welcome to Chess! :)\n')
        print('-Consider increasing the font size to make the board bigger and thus easier to see')
        print('-Enter a move by giving the coordinates of the starting point and the goal point (Example: A3D6)')
        print('-During a match you can enter "q" to quit, "s" to save or "m" to go back to the menu\n')
        print('(1)PlayerVsPlayer   (2)PlayerVsBot   (3)LoadGame   (4)Exit')
        self.model.controller.get_menu_choice()
