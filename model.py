"""
    Module for managing and manipulating data
"""
from view import View
from controller import Controller


class Model:
    """Class that handles everything for the module"""

    def __init__(self):
        self.board_state = [[' '] * 8 for _ in range(9)]
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
        self.pieces = [] # to speed up piece_search later?
        self.currently_playing = 'white'

    def reset_pieces(self):
        """Resets the pieces to their starting position"""
        if self.show_symbols:
            self.reset_with_symbols()
        else:
            self.reset_with_letters()

    def reset_with_symbols(self):
        """Reset the board using symbols"""
        self.board_state[0][0] = '\u265C'
        self.board_state[0][1] = '\u265E'
        self.board_state[0][2] = '\u265D'
        self.board_state[0][3] = '\u265B'
        self.board_state[0][4] = '\u265A'
        self.board_state[0][5] = '\u265D'
        self.board_state[0][6] = '\u265E'
        self.board_state[0][7] = '\u265C'
        for i in range(8):
            self.board_state[1][i] = '\u265F'
        self.board_state[7][0] = '\u2656'
        self.board_state[7][1] = '\u2658'
        self.board_state[7][2] = '\u2657'
        self.board_state[7][3] = '\u2655'
        self.board_state[7][4] = '\u2654'
        self.board_state[7][5] = '\u2657'
        self.board_state[7][6] = '\u2658'
        self.board_state[7][7] = '\u2656'
        for i in range(8):
            self.board_state[6][i] = '\u2659'

    def reset_with_letters(self):
        """Reset the board using letters"""
        self.board_state[0][0] = 'R'
        self.board_state[0][1] = 'H'
        self.board_state[0][2] = 'B'
        self.board_state[0][3] = 'Q'
        self.board_state[0][4] = 'K'
        self.board_state[0][5] = 'B'
        self.board_state[0][6] = 'H'
        self.board_state[0][7] = 'R'
        for i in range(8):
            self.board_state[1][i] = 'P'
        self.board_state[7][0] = 'r'
        self.board_state[7][1] = 'h'
        self.board_state[7][2] = 'b'
        self.board_state[7][3] = 'q'
        self.board_state[7][4] = 'k'
        self.board_state[7][5] = 'b'
        self.board_state[7][6] = 'h'
        self.board_state[7][7] = 'r'
        for i in range(8):
            self.board_state[6][i] = 'p'

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
