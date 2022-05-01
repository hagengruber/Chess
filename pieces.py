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
        """Returns true if a given position exists and is occupied by a friendly piece"""
        if position in range(64):
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
        """Returns true if a given position exists and is occupied by a hostile piece"""
        if position in range(64):
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
        """Returns true if a given position exists and is occupied"""
        if position in range(64):
            if self.check_occupied_hostile(position) or self.check_occupied_friendly(position):
                return True
            else:
                return False
        else:
            return False

    def check_linear(self):
        """Returns a list of all free spaces north, east, west and south of a given space"""
        allowed = []
        space_to_check = self.position - 8
        while space_to_check in range(64):
            if not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check - 8
            else:
                break
        space_to_check = self.position + 8
        while space_to_check in range(64):
            if not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check + 8
            else:
                break
        space_to_check = self.position - 1
        while space_to_check in range(64):
            if not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check - 1
            else:
                break
        space_to_check = self.position + 1
        while space_to_check in range(64):
            if not self.check_occupied_friendly(space_to_check):
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
        """Returns a list of all free spaces northeast, southeast, southwest and northwest of a given space"""
        allowed = []
        space_to_check = self.position - 9
        while space_to_check in range(64):
            if not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check - 9
            else:
                break
        space_to_check = self.position + 9
        while space_to_check in range(64):
            if not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check + 9
            else:
                break
        space_to_check = self.position - 7
        while space_to_check in range(64):
            if not self.check_occupied_friendly(space_to_check):
                if self.check_occupied_hostile(space_to_check):
                    allowed.append(space_to_check)
                    break
                else:
                    allowed.append(space_to_check)
                    space_to_check = space_to_check - 7
            else:
                break
        space_to_check = self.position + 7
        while space_to_check in range(64):
            if not self.check_occupied_friendly(space_to_check):
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
    """Class for Rooks"""
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position
        self.moved = False

    def set_symbol(self):
        """Returns the Symbol the given piece should display"""
        if self.model.show_symbols:
            if self.colour == 'White':
                return '\u265C'
            else:
                return '\u2656'
        else:
            if self.colour == 'White':
                return 'r'
            else:
                return 'R'

    def check_legal_move(self, position):
        """Makes a list of all legal moves and returns True if the given position is part of them"""
        allowed = self.check_linear()
        if position in allowed:
            return True
        else:
            return False


class Horse(Piece):
    """Class for Horses"""
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position

    def set_symbol(self):
        """Returns the Symbol the given piece should display"""
        if self.model.show_symbols:
            if self.colour == 'White':
                return '\u265E'
            else:
                return '\u2658'
        else:
            if self.colour == 'White':
                return 'h'
            else:
                return 'H'

    def check_legal_move(self, position):
        """Makes a list of all legal moves and returns True if the given position is part of them"""
        allowed = []
        if not self.check_occupied_friendly(self.position - 17):
            allowed.append(self.position - 17)
        if not self.check_occupied_friendly(self.position - 15):
            allowed.append(self.position - 15)
        if not self.check_occupied_friendly(self.position - 10):
            allowed.append(self.position - 10)
        if not self.check_occupied_friendly(self.position - 6):
            allowed.append(self.position - 6)
        if not self.check_occupied_friendly(self.position + 17):
            allowed.append(self.position + 17)
        if not self.check_occupied_friendly(self.position + 15):
            allowed.append(self.position + 15)
        if not self.check_occupied_friendly(self.position + 10):
            allowed.append(self.position + 10)
        if not self.check_occupied_friendly(self.position + 6):
            allowed.append(self.position + 6)
        if position in allowed:
            return True
        else:
            return False


class Bishop(Piece):
    """Class for Bishops"""
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position

    def set_symbol(self):
        """Returns the Symbol the given piece should display"""
        if self.model.show_symbols:
            if self.colour == 'White':
                return '\u265D'
            else:
                return '\u2657'
        else:
            if self.colour == 'White':
                return 'b'
            else:
                return 'B'

    def check_legal_move(self, position):
        """Makes a list of all legal moves and returns True if the given position is part of them"""
        allowed = self.check_diagonal()
        if position in allowed:
            return True
        else:
            return False


class Pawn(Piece):
    """Class for Pawns"""
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position
        self.moved = False

    def set_symbol(self):
        """Returns the Symbol the given piece should display"""
        if self.model.show_symbols:
            if self.colour == 'White':
                return '\u265F'
            else:
                return '\u2659'
        else:
            if self.colour == 'White':
                return 'p'
            else:
                return 'P'

    def check_legal_move(self, position):
        """Makes a list of all legal moves and returns True if the given position is part of them"""
        allowed = []
        if self.colour == 'White':
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

    def upgrade(self):
        """Returns True if the Pawn is in an upgrade-position"""
        if self.colour == 'Black':
            if self.position in range(56, 63):
                return True
            else:
                return False
        else:
            if self.position in range(0, 7):
                return True
            else:
                return False


class Queen(Piece):
    """Class for Queens"""
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position

    def set_symbol(self):
        """Returns the Symbol the given piece should display"""
        if self.model.show_symbols:
            if self.colour == 'White':
                return '\u265B'
            else:
                return '\u2655'
        else:
            if self.colour == 'White':
                return 'q'
            else:
                return 'Q'

    def check_legal_move(self, position):
        """Makes a list of all legal moves and returns True if the given position is part of them"""
        allowed = self.check_linear() + self.check_diagonal()
        if position in allowed:
            return True
        else:
            return False


class King(Piece):
    """Class for Kings"""
    def __init__(self, colour, position, model):
        Piece.__init__(self)
        self.model = model
        self.colour = colour
        self.symbol = self.set_symbol()
        self.position = position
        self.moved = False

    def set_symbol(self):
        """Returns the Symbol the given piece should display"""
        if self.model.show_symbols:
            if self.colour == 'White':
                return '\u265A'
            else:
                return '\u2654'
        else:
            if self.colour == 'White':
                return 'k'
            else:
                return 'K'

    def check_legal_move(self, position):
        """Makes a list of all legal moves and returns True if the given position is part of them"""
        allowed = []
        if not self.check_occupied_friendly(self.position - 9):
            allowed.append(self.position - 9)
        if not self.check_occupied_friendly(self.position - 8):
            allowed.append(self.position - 8)
        if not self.check_occupied_friendly(self.position - 7):
            allowed.append(self.position - 7)
        if not self.check_occupied_friendly(self.position - 1):
            allowed.append(self.position - 1)
        if not self.check_occupied_friendly(self.position + 1):
            allowed.append(self.position + 1)
        if not self.check_occupied_friendly(self.position + 7):
            allowed.append(self.position + 7)
        if not self.check_occupied_friendly(self.position + 8):
            allowed.append(self.position + 8)
        if not self.check_occupied_friendly(self.position + 9):
            allowed.append(self.position + 9)
        if position in allowed:
            return True
        else:
            return False
