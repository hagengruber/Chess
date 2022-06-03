"""
    Module that contains the alpha-beta-pruning algorithm for the AI
"""
import math
import pieces
from evaluatePieces import Evaluate


# ToDo: Kommentieren

class AI:
    def __init__(self, model, view, color, enemy):
        self.model = model
        self.view = view
        self.color = color
        self.enemy = enemy  # Enemy Color
        self.count = 0

    def alpha_beta_pruning(self, state, depth, alpha, beta, ai_playing):

        self.count += 1

        if depth == 0 or not self.model.check_for_king():
            d = self.calculate_board_value(state)
            return d

        if ai_playing:
            ai_value = -math.inf
            self.model.currently_playing = "White"
            for next_move in self.get_possible_moves(self.enemy, state):

                x, y = next_move

                temp = self.model.get_copy_board_state(state)

                change_position = False

                try:

                    # print("Type: " + str(type(state[x])))
                    change_position = temp[x].position
                    temp[x].position = y
                    temp[y] = temp[x]
                    temp[x] = None
                except AttributeError:
                    pass

                value = self.alpha_beta_pruning(temp, depth - 1, alpha, beta, False)

                if change_position:
                    temp[y].position = change_position

                self.model.currently_playing = "Black"

                ai_value = max(ai_value, value)

                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return ai_value

        else:
            player_value = math.inf
            self.model.currently_playing = "Black"
            for next_move in self.get_possible_moves(self.color, state):

                x, y = next_move

                temp = self.model.get_copy_board_state(state)

                change_position = False

                try:

                    change_position = temp[x].position
                    temp[x].position = y
                    temp[y] = temp[x]
                    temp[x] = None
                except AttributeError:
                    pass

                value = self.alpha_beta_pruning(temp, depth - 1, alpha, beta, True)

                if change_position:
                    temp[y].position = change_position

                player_value = min(player_value, value)
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return player_value

    @staticmethod
    def calculate_board_value(current_game_state):

        ev = Evaluate(current_game_state)

        piece = ev.get_pieces_evaluate()

        pawn = ev.position_evaluate(pieces.Pawn, 100, ev.PAWN_TABLE)
        horse = ev.position_evaluate(pieces.Horse, 320, ev.HORSE_TABLE)
        bishop = ev.position_evaluate(pieces.Bishop, 330, ev.BISHOP_TABLE)
        rook = ev.position_evaluate(pieces.Rook, 500, ev.ROOK_TABLE)
        queen = ev.position_evaluate(pieces.Queen, 900, ev.QUEEN_TABLE)

        return piece + pawn + rook + horse + bishop + queen

    @staticmethod
    def get_possible_moves(color, state):

        move = []

        for i in state:
            try:
                if i.colour == color:
                    possible_move = i.check_legal_move(i.position, state, True)
                    if len(possible_move) > 0:
                        for a in possible_move:
                            if 0 < a < 64:
                                move.append([i.position, a])

            except AttributeError:
                continue

        return move

    def move(self):
        best_score = math.inf
        final_move = None

        state = self.model.get_copy_board_state()

        for next_move in self.get_possible_moves(self.color, state):

            temp = self.model.get_copy_board_state(state)

            x, y = next_move

            temp[y] = temp[x]
            temp[x] = None

            current_score = self.alpha_beta_pruning(temp, 3, -math.inf, math.inf, True)

            if current_score < best_score:
                best_score = current_score
                final_move = next_move

        x, y = final_move

        self.model.move_piece(x, y)
