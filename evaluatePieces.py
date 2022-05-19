from time import sleep
import pieces
import math

class Evaluate:

    def __init__(self, current_game_state):
        self.current_game_state = current_game_state

    PAWN_TABLE = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [5, 10, 10, -20, -20, 10, 10, 5],
        [5, -5, -10, 0, 0, -10, -5, 5],
        [0, 0, 0, 20, 20, 0, 0, 0],
        [5, 5, 10, 25, 25, 10, 5, 5],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    HORSE_TABLE = [
        [-50, -40, -30, -30, -30, -30, -40, -50],
        [-40, -20, 0, 5, 5, 0, -20, -40],
        [-30, 5, 10, 15, 15, 10, 5, -30],
        [-30, 0, 15, 20, 20, 15, 0, -30],
        [-30, 5, 15, 20, 20, 15, 0, -30],
        [-30, 0, 10, 15, 15, 10, 0, -30],
        [-40, -20, 0, 0, 0, 0, -20, -40],
        [-50, -40, -30, -30, -30, -30, -40, -50]
    ]

    BISHOP_TABLE = [
        [-20, -10, -10, -10, -10, -10, -10, -20],
        [-10, 5, 0, 0, 0, 0, 5, -10],
        [-10, 10, 10, 10, 10, 10, 10, -10],
        [-10, 0, 10, 10, 10, 10, 0, -10],
        [-10, 5, 5, 10, 10, 5, 5, -10],
        [-10, 0, 5, 10, 10, 5, 0, -10],
        [-10, 0, 0, 0, 0, 0, 0, -10],
        [-20, -10, -10, -10, -10, -10, -10, -20]
    ]

    ROOK_TABLE = [
        [0, 0, 0, 5, 5, 0, 0, 0],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [-5, 0, 0, 0, 0, 0, 0, -5],
        [5, 10, 10, 10, 10, 10, 10, 5],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    QUEEN_TABLE = [
        [-20, -10, -10, -5, -5, -10, -10, -20],
        [-10, 0, 5, 0, 0, 0, 0, -10],
        [-10, 5, 5, 5, 5, 5, 0, -10],
        [0, 0, 5, 5, 5, 5, 0, -5],
        [-5, 0, 5, 5, 5, 5, 0, -5],
        [-10, 0, 5, 5, 5, 5, 0, -10],
        [-10, 0, 0, 0, 0, 0, 0, -10],
        [-20, -10, -10, -5, -5, -10, -10, -20]
    ]

    def get_pieces_evaluate(self):

        black = 0
        white = 0

        for i in self.current_game_state:

            if type(i) is pieces.Rook:

                if i.colour == "White":
                    white += 500
                else:
                    black += 500

            if type(i) is pieces.Pawn:
                if i.colour == "White":
                    white += 100
                else:
                    black += 100

            if type(i) is pieces.Horse:
                if i.colour == "White":
                    white += 320
                else:
                    black += 320

            if type(i) is pieces.Bishop:
                if i.colour == "White":
                    white += 330
                else:
                    black += 330

            if type(i) is pieces.King:
                if i.colour == "White":
                    white += 20000
                else:
                    black += 20000

            if type(i) is pieces.Queen:
                if i.colour == "White":
                    white += 900
                else:
                    black += 900

        return white - black

    def position_evaluate(self, pieces_type, color, piece_val, lookup):
        white = 0
        black = 0
        count = 0

        for i in self.current_game_state:
            if type(i) is pieces_type:
                if i.colour == color:
                    white += piece_val
                else:
                    y = math.floor(count/8)
                    x = count - (y * 7) - y
                    black += lookup[7-x][y]
            count += 1
        return white-black
