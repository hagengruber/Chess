"""
    Module for getting and processing input from the user
"""
import sys


class Controller:
    """Class that handles everything for the module"""
    def __init__(self):
        self.model = None

    def get_menu_choice(self):
        """Gets input from user and processes the input"""
        selection = input()
        if selection == '1':
            self.model.reset_pieces()
            self.model.view.update_board()
            self.get_movement_choice()
            self.model.currently_playing = 'Black'
            while self.model.check_for_king():
                self.model.view.update_board()
                self.get_movement_choice()
                if self.model.currently_playing == 'White':
                    self.model.currently_playing = 'Black'
                else:
                    self.model.currently_playing = 'White'
            print(self.model.currently_playing + ' lost because his king died!')
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

    def get_movement_choice(self):
        choice = input('Please enter your desired Move: ')
        lines = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        columns = ['1', '2', '3', '4', '5', '6', '7', '8']
        start_pos = choice[:2]
        goal_pos = choice[-2:]
        if start_pos[0] in lines and goal_pos[0] in lines and start_pos[1] in columns and goal_pos[1] in columns:
            self.model.move_piece(self.model.correlation[start_pos], self.model.correlation[goal_pos])
        else:
            print('Your Choice is not valid. Please try again!')
            self.get_movement_choice()
