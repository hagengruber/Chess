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

    @abstractmethod
    def check_legal_move(self, position):
        pass

    @abstractmethod
    def move(self, position):
        pass


class Rook(Piece):
    def __init__(self, symbol, colour, position):
        Piece.__init__(self)
        self.symbol = symbol
        self.colour = colour
        self.position = position

    def check_legal_move(self, position):
        pass

    def move(self, position):
        pass


class Horse(Piece):
    def __init__(self, symbol, colour, position):
        Piece.__init__(self)
        self.symbol = symbol
        self.colour = colour
        self.position = position

    def check_legal_move(self, position):
        pass

    def move(self, position):
        pass


class Bishop(Piece):
    def __init__(self, symbol, colour, position):
        Piece.__init__(self)
        self.symbol = symbol
        self.colour = colour
        self.position = position

    def check_legal_move(self, position):
        pass

    def move(self, position):
        pass


class Queen(Piece):
    def __init__(self, symbol, colour, position):
        Piece.__init__(self)
        self.symbol = symbol
        self.colour = colour
        self.position = position

    def check_legal_move(self, position):
        pass

    def move(self, position):
        pass


class King(Piece):
    def __init__(self, symbol, colour, position):
        Piece.__init__(self)
        self.symbol = symbol
        self.colour = colour
        self.position = position

    def check_legal_move(self, position):
        pass

    def move(self, position):
        if self.check_legal_move(position):
            return self.position, position
        else:
            raise IllegalMove()
