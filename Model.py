from View import View
from Controller import Controller


class Model:
    def __init__(self):
        self.board_state = [[' '] * 8] * 8
        self.view = View()
        self.controller = Controller()
        self.show_symbols = True

    def reset_board(self):
        if self.show_symbols:
            self.reset_with_symbols()
        else:
            self.reset_with_letters()

    def reset_with_symbols(self):
        self.board_state[0][0] = '\u265C'
        self.board_state[0][1] = '\u265D'
        self.board_state[0][2] = '\u265E'
        self.board_state[0][3] = '\u265B'
        self.board_state[0][4] = '\u265A'
        self.board_state[0][5] = '\u265E'
        self.board_state[0][6] = '\u265D'
        self.board_state[0][7] = '\u265C'
        for i in range(8):
            self.board_state[1][i] = '\u265F'
        self.board_state[7][0] = '\u2656'
        self.board_state[7][1] = '\u2657'
        self.board_state[7][2] = '\u2658'
        self.board_state[7][3] = '\u2655'
        self.board_state[7][4] = '\u2654'
        self.board_state[7][5] = '\u2658'
        self.board_state[7][6] = '\u2657'
        self.board_state[7][7] = '\u2656'
        for i in range(8):
            self.board_state[6][i] = '\u2659'

    def reset_with_letters(self):
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

