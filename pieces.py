"""
    Module that contains the classes for all the pieces of chess
"""
from abc import ABCMeta, abstractmethod


class Piece(metaclass=ABCMeta):
    """Base class for all the other classes"""
    def __init__(self):
        self.model = None
        self.symbol = None
        self.colour = None
        self.moved = False
        self.position = None

    @abstractmethod
    def check_legal_move(self, position):
        """Return True if move is legal, False else"""
        pass

    def check_occupied_friendly(self, position):
        if self.model.board_state(position) is not None:
            if self.model.board_state(position).colour == self.model.currently_playing:
                return True
            else:
                return False
        else:
            return False


class Rook(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position
        self.moved = False

    def set_symbol(self):
        if self.model.show_symbols:
            if self.colour == 'white':
                return '\u265C'
            else:
                return '\u2656'
        else:
            if self.colour == 'white':
                return 'r'
            else:
                return 'R'

    def check_legal_move(self, position):
        pass


class Horse(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position

    def set_symbol(self):
        if self.model.show_symbols:
            if self.colour == 'white':
                return '\u265E'
            else:
                return '\u2658'
        else:
            if self.colour == 'white':
                return 'h'
            else:
                return 'H'

    def check_legal_move(self, position):
        pass


class Bishop(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position

    def set_symbol(self):
        if self.model.show_symbols:
            if self.colour == 'white':
                return '\u265D'
            else:
                return '\u2657'
        else:
            if self.colour == 'white':
                return 'b'
            else:
                return 'B'

    def check_legal_move(self, position):
        pass


class Pawn(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position
        self.moved = False

    def set_symbol(self):
        if self.model.show_symbols:
            if self.colour == 'white':
                return '\u265F'
            else:
                return '\u2659'
        else:
            if self.colour == 'white':
                return 'p'
            else:
                return 'P'

    def check_legal_move(self, position):
        allowed = []
        if self.colour == 'white':
            if self.check_occupied_friendly(self.position - 8):
                allowed.append(self.model.board_state[self.position - 8])
            if self.check_occupied_hostile(self.position - 9):
                allowed.append(self.model.board_state[self.position - 9])
            if self.check_occupied_hostile(self.position - 7):
                allowed.append(self.model.board_state[self.position - 7])
            if not self.moved:
                if self.check_occupied_friendly(self.position - 16):
                    allowed.append(self.model.board_state[self.position - 16])
        else:
            if self.check_occupied_friendly(self.position + 8):
                allowed.append(self.model.board_state[self.position + 8])
            if self.check_occupied_hostile(self.position + 9):
                allowed.append(self.model.board_state[self.position + 9])
            if self.check_occupied_hostile(self.position + 7):
                allowed.append(self.model.board_state[self.position + 7])
            if not self.moved:
                if self.check_occupied_friendly(self.position + 16):
                    allowed.append(self.model.board_state[self.position + 16])
        if position in allowed:
            return True
        else:
            return False


    def check_occupied_hostile(self, position):
        if self.model.board_state[position] is not None:
            if self.model.currently_playing == 'white':
                if self.model.board_state[position].color == 'black':
                    return True
            elif self.model.currently_playing == 'black':
                if self.model.board_state[position].color == 'white':
                    return True
            else:
                return False
        else:
            return False


class Queen(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position

    def set_symbol(self):
        if self.model.show_symbols:
            if self.colour == 'white':
                return '\u265B'
            else:
                return '\u2655'
        else:
            if self.colour == 'white':
                return 'q'
            else:
                return 'Q'

    def check_legal_move(self, position):
        pass


class King(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position
        self.moved = False

    def set_symbol(self):
        if self.model.show_symbols:
            if self.colour == 'white':
                return '\u265A'
            else:
                return '\u2654'
        else:
            if self.colour == 'white':
                return 'k'
            else:
                return 'K'

    def check_legal_move(self, wanted_position):
        allowed = [self.position - 1, self.position + 1, self.position ]
        for _ in [-1, 0, 1]:
            allowed.append(self.position + 8 + _)
            allowed.append(self.position - 8 + _)
        # Remove Spaces if occupied by friendly
