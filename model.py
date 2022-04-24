"""
    Module for managing and manipulating data
"""
from view import View
from controller import Controller
from pieces import Rook, Horse, Bishop, Pawn, King, Queen


# noinspection PyTypeChecker
class Model:
    """Class that handles everything for the module"""

    def __init__(self):
        self.board_state = list(None for _ in range(65))
        self.view = View()
        self.controller = Controller()
        self.show_symbols = True
        self.correlation = {'A1': (0, 0), 'A2': (0, 1), 'A3': (0, 2), 'A4': (0, 3),
                            'A5': (0, 4), 'A6': (0, 5), 'A7': (0, 6), 'A8': (0, 7),
                            'B1': (1, 0), 'B2': (1, 1), 'B3': (1, 2), 'B4': (1, 3),
                            'B5': (1, 4), 'B6': (1, 5), 'B7': (1, 6), 'B8': (1, 7),
                            'C1': (2, 0), 'C2': (2, 1), 'C3': (2, 2), 'C4': (2, 3),
                            'C5': (2, 4), 'C6': (2, 5), 'C7': (2, 6), 'C8': (2, 7),
                            'D1': (3, 0), 'D2': (3, 1), 'D3': (3, 2), 'D4': (3, 3),
                            'D5': (3, 4), 'D6': (3, 5), 'D7': (3, 6), 'D8': (3, 7),
                            'E1': (4, 0), 'E2': (4, 1), 'E3': (4, 2), 'E4': (4, 3),
                            'E5': (4, 4), 'E6': (4, 5), 'E7': (4, 6), 'E8': (4, 7),
                            'F1': (5, 0), 'F2': (5, 1), 'F3': (5, 2), 'F4': (5, 3),
                            'F5': (5, 4), 'F6': (5, 5), 'F7': (5, 6), 'F8': (5, 7),
                            'G1': (6, 0), 'G2': (6, 1), 'G3': (6, 2), 'G4': (6, 3),
                            'G5': (6, 4), 'G6': (6, 5), 'G7': (6, 6), 'G8': (6, 7),
                            'H1': (7, 0), 'H2': (7, 1), 'H3': (7, 2), 'H4': (7, 3),
                            'H5': (7, 4), 'H6': (7, 5), 'H7': (7, 6), 'H8': (7, 7)}
        self.pieces = []  # to speed up piece_search later?
        self.currently_playing = 'white'

    def reset_pieces(self):
        """Reset the board using symbols"""
        model = self
        self.board_state[0] = Rook('black', 0, model)
        self.board_state[1] = Horse('black', 1, model)
        self.board_state[2] = Bishop('black', 2, model)
        self.board_state[3] = Queen('black', 3, model)
        self.board_state[4] = King('black', 4, model)
        self.board_state[5] = Bishop('black', 5, model)
        self.board_state[6] = Horse('black', 6, model)
        self.board_state[7] = Rook('black', 7, model)
        for i in range(8):
            self.board_state[8 + i] = Pawn('black', i, model)
        self.board_state[56] = Rook('white', 56, model)
        self.board_state[57] = Horse('white', 57, model)
        self.board_state[58] = Bishop('white', 58, model)
        self.board_state[59] = Queen('white', 59, model)
        self.board_state[60] = King('white', 60, model)
        self.board_state[61] = Bishop('white', 61, model)
        self.board_state[62] = Horse('white', 62, model)
        self.board_state[63] = Rook('white', 63, model)
        for i in range(8):
            self.board_state[48 + i] = Pawn('white', i, model)

    def move_piece(self, start_pos, goal_pos):
        start_line, start_column = start_pos
        goal_line, goal_column = goal_pos
        moved_piece = self.board_state[start_line][start_column]
        killed_piece = self.board_state[goal_line][goal_column]
        if moved_piece is not None and moved_piece.colour == self.currently_playing:
            if self.board_state[start_line][start_column].check_legal_move(goal_pos):
                self.board_state[goal_line][goal_column] = moved_piece
                if killed_piece is not None:
                    self.pieces.remove(killed_piece)
            else:
                print('Sorry, this move is not legal. Please try again!')
                self.get_movement_choice()
        else:
            print('There is no piece of your color on this space. Please try again!')
            self.get_movement_choice()

    def get_movement_choice(self):
        pass
    # Get input, change with correlation and call move_piece function to move the piece
    # if Piece at wanted position
