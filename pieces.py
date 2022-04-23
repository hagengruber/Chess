"""
    Module that contains the classes for all the pieces of chess
"""
from abc import ABCMeta, abstractmethod


class Piece(metaclass=ABCMeta):
    """Base class for all the other classes"""
    def __init__(self):
        self.symbol = None
        self.colour = None
        self.moved = False
        self.position = None
        self.model = None

    @abstractmethod
    def check_legal_move(self, position):
        pass

    @abstractmethod
    def move(self, position):
        pass


class Rook(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.colour = colour
        self.symbol = self.set_symbol()
        self.model = model
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

    def move(self, position):
        pass


class Horse(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.colour = colour
        self.symbol = self.set_symbol()
        self.model = model
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

    def move(self, position):
        pass


class Bishop(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.colour = colour
        self.symbol = self.set_symbol()
        self.model = model
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

    def move(self, position):
        pass


class Pawn(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.colour = colour
        self.symbol = self.set_symbol()
        self.model = model
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
                return 'r'
            else:
                return 'R'

    def check_legal_move(self, position):
        pass

    def move(self, position):
        pass


class Queen(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.colour = colour
        self.symbol = self.set_symbol()
        self.model = model
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

    def move(self, position):
        pass


class King(Piece):
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.colour = colour
        self.symbol = self.set_symbol()
        self.model = model
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

    def check_legal_move(self, position):
        pass

    def move(self, position):
        if self.check_legal_move(position):
            return self.position, position
        else:
            raise IllegalMove()
