"""
    Module for getting and processing input from the user
"""
from algorithm import AI
import json
import sys
import os
import pathlib
from pieces import *


def get_files(i):
    if i == 1:
        return pathlib.Path().absolute()
    else:
        dirPath = pathlib.Path().absolute()
        return [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]


class Controller:
    """Class that handles everything for the module"""

    def __init__(self, view):
        self.model = None
        self.view = view
        self.ai = None

    def get_menu_choice(self):
        """Gets input from user and processes the input"""
        selection = input()

        if selection == '1':
            self.model.reset_pieces()
            # initializes the previous board of the view
            self.view.last_board = self.model.get_copy_board_state()

            self.model.view.update_board()
            self.model.ai = False
            self.get_movement_choice()

            self.model.currently_playing = 'Black'

            while self.model.check_for_king():

                self.get_movement_choice()
                if self.model.currently_playing == 'White':
                    self.model.currently_playing = 'Black'
                else:
                    self.model.currently_playing = 'White'
            print(self.model.currently_playing + ' lost because his king died!')

        elif selection == '2':
            self.model.reset_pieces()
            # initializes the previous board of the view
            self.view.last_board = self.model.get_copy_board_state()

            self.model.view.update_board()
            ai = AI(self.model, self.view, "Black", "White")
            self.model.ai = True
            self.get_movement_choice()

            self.model.currently_playing = 'Black'

            ai.move()
            self.model.currently_playing = 'White'

            while self.model.check_for_king():
                if self.model.currently_playing == 'Black':
                    ai.move()
                else:
                    self.get_movement_choice()

                if self.model.currently_playing == 'White':
                    self.model.currently_playing = 'Black'
                else:
                    self.model.currently_playing = 'White'
            print(self.model.currently_playing + ' lost because his king died!')

        elif selection == '3':
            self.load()
            self.view.update_board()

        elif selection == '4':
            self.model.view.clear_console()
            sys.exit()

        elif selection == '5':
            # ToDo: Rules + Options
            pass

        else:
            print('Your choice is not valid! Please try again!')
            self.get_menu_choice()

    def get_movement_choice(self):
        choice = input('Please enter your desired Move: ').upper()

        if choice == "Q":
            sys.exit()

        if choice == "S":
            self.save()
            self.view.clear_console()
            self.view.print_menu()
            self.get_menu_choice()

        if len(choice) < 4:
            print('Your Choice is not valid. Please try again!')
            self.get_movement_choice()
        else:
            lines = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            columns = ['1', '2', '3', '4', '5', '6', '7', '8']
            start_pos = choice[:2]
            goal_pos = choice[-2:]
            if start_pos[0] in lines and goal_pos[0] in lines and start_pos[1] in columns and goal_pos[1] in columns:
                self.model.move_piece(self.model.correlation[start_pos], self.model.correlation[goal_pos])
            else:
                print('Your Choice is not valid. Please try again!')
                self.get_movement_choice()

    # Board aktuellen spieler und ob KI spielt View Symbol
    def save(self):
        GameSave = {'currently_playing': str(self.model.currently_playing),
                    'show_symbols': self.model.show_symbols,
                    'board_state': {},
                    'Ai': False}

        if self.model.ai:
            GameSave.update({'Ai': True})

        dict = {}
        for i in range(63):
            if self.model.board_state[i] is not None:
                lol = self.model.board_state[i].__doc__.split(" ")
                dict.update({str(i): {'piece': lol[2],
                                      'colour': str(self.model.board_state[i].colour),
                                      'moved': self.model.board_state[i].moved,
                                      'position': self.model.board_state[i].position}})
            else:
                dict.update({str(i): {'piece': None,
                                      'symbol': None,
                                      'colour': None,
                                      'moved': None,
                                      'position': None}})

        GameSave['board_state'].update(dict)

        path = str(get_files(1))
        name = "\\GameSave.json"

        with open(path + name, "w") as json_file:
            json.dump(GameSave, json_file)

    def load(self):
        files = get_files(2)
        name = 'GameSave.json'  # ggf Namen ändern

        if name in files:  # Parameter eintragen fürs testen
            with open("GameSave.json", "r") as Data:  # Parameter eintragen fürs testen
                GameSave = json.load(Data)
                # den aktuellen spieler abfragen

                self.model.currently_playing = GameSave['currently_playing']
                self.model.show_symbols = GameSave['show_symbols']
                if 'Ai' in GameSave:
                    self.ai = True

                for i in range(63):
                    if GameSave['board_state'][str(i)]['piece'] == 'None':  # Moved wird nicht übernommen
                        self.model.board_state[i] = None

                    else:
                        if GameSave['board_state'][str(i)]['piece'] == 'Rooks':
                            self.model.board_state[i] = Rook(GameSave['board_state'][str(i)]['colour'], i, self.model)
                        if GameSave['board_state'][str(i)]['piece'] == 'Horses':
                            self.model.board_state[i] = Horse(GameSave['board_state'][str(i)]['colour'], i, self.model)
                        if GameSave['board_state'][str(i)]['piece'] == 'Bishops':
                            self.model.board_state[i] = Bishop(GameSave['board_state'][str(i)]['colour'], i, self.model)
                        if GameSave['board_state'][str(i)]['piece'] == 'Queens':
                            self.model.board_state[i] = Queen(GameSave['board_state'][str(i)]['colour'], i, self.model)
                        if GameSave['board_state'][str(i)]['piece'] == 'Kings':
                            self.model.board_state[i] = King(GameSave['board_state'][str(i)]['colour'], i, self.model)
                        if GameSave['board_state'][str(i)]['piece'] == 'Pawns':
                            self.model.board_state[i] = Pawn(GameSave['board_state'][str(i)]['colour'], i, self.model)

        else:
            print("Es ist kein Spiel gespeichert")

        self.view.last_board = self.model.get_copy_board_state()
