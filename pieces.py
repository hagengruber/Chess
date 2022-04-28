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
        if position in range(65):
            if self.model.board_state[position] is not None:
                if self.model.board_state[position].colour == self.model.currently_playing:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def check_occupied_hostile(self, position):
        if position in range(65):
            if self.model.board_state[position] is not None:
                if self.model.board_state[position].colour != self.model.currently_playing:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def check_occupied(self, position):
        if position in range(65):
            if self.check_occupied_hostile(position) or self.check_occupied_friendly(position):
                return True
            else:
                return False
        else:
            return False

    def check_linear(self):
        allowed = []
        space_to_check = self.position - 8
        while True:
            if space_to_check in range(65) and not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check - 8
            else:
                break
        space_to_check = self.position + 8
        while True:
            if space_to_check in range(65) and not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check + 8
            else:
                break
        space_to_check = self.position - 1
        while True:
            if space_to_check in range(65) and not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check - 1
            else:
                break
        space_to_check = self.position + 1
        while True:
            if space_to_check in range(65) and not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check + 1
            else:
                break
        return allowed

    def check_diagonal(self):
        allowed = []
        space_to_check = self.position - 9
        while True:
            if space_to_check in range(65) and not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check - 9
            else:
                break
        space_to_check = self.position + 9
        while True:
            if space_to_check in range(65) and not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check + 9
            else:
                break
        space_to_check = self.position - 7
        while True:
            if space_to_check in range(65) and not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check - 7
            else:
                break
        space_to_check = self.position + 7
        while True:
            if space_to_check in range(65) and not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check + 7
            else:
                break
        return allowed


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
        allowed = self.check_linear()
        if position in allowed:
            return True
        else:
            return False


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
        allowed = self.check_diagonal()
        if position in allowed:
            return True
        else:
            return False


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
            if not self.check_occupied(self.position - 8):
                allowed.append(self.position - 8)
            if self.check_occupied_hostile(self.position - 9):
                allowed.append(self.position - 9)
            if self.check_occupied_hostile(self.position - 7):
                allowed.append(self.position - 7)
            if not self.moved:
                if not self.check_occupied(self.position - 16):
                    allowed.append(self.position - 16)
        else:
            if not self.check_occupied(self.position + 8):
                allowed.append(self.position + 8)
            if self.check_occupied_hostile(self.position + 9):
                allowed.append(self.position + 9)
            if self.check_occupied_hostile(self.position + 7):
                allowed.append(self.position + 7)
            if not self.moved:
                if not self.check_occupied(self.position + 16):
                    allowed.append(self.position + 16)
        if position in allowed:
            return True
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
        pass
