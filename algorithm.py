"""
    Module that contains the alpha-beta-pruning algorithm for the AI
"""
import math
import pieces
from time import sleep
from evaluatePieces import Evaluate


class AI:
    def __init__(self, model, view, color, enemy):
        self.model = model
        self.view = view
        self.color = color
        self.enemy = enemy  # Enemy Color
        self.count = 0

    def alpha_beta_pruning(self, state, depth, alpha, beta, ai_playing):

        self.count += 1
        # self.view.update_board(state)

        if depth == 0 or not self.model.check_for_king():
            d = self.calculate_board_value(state)
            return d

        if ai_playing:
            ai_value = -math.inf
            self.model.currently_playing = "White"
            for next_move in self.get_possible_moves(self.enemy, state):

                # ToDO - Weitermachen: Erster Move hier: 40, 32 - F1, E2
                # Im anderen Algorithmus b2 b3
                # Schauen woran das liegt und danach den Algorithmus weiter vergleichen

                # print("Other Moves: " + str(len(self.get_possible_moves(self.enemy, state))))
                # print(self.get_possible_moves(self.enemy, state))
                # print("Next Move: " + str(next_move))

                # save_board = self.model.get_copy_board_state(state)
                x, y = next_move
                # old_pos = self.model.board_state[x].position

                # print("Vorher: X: " + str(state[x]) + " Y: " + str(state[y]))

                # self.model.currently_playing = "White"

                change_position = False

                try:

                    # print("Type: " + str(type(state[x])))
                    change_position = state[x].position
                    state[x].position = y
                    state[y] = state[x]
                    state[x] = None
                except AttributeError:
                    pass

                # print("Nachher: X: " + str(state[x]) + " Y: " + str(state[y]))

                # self.model.move_piece(x, y, False)

                # self.model.currently_playing = "Black"

                temp = self.model.get_copy_board_state(state)

                value = self.alpha_beta_pruning(temp, depth - 1, alpha, beta, False)

                if change_position:
                    state[y].position = change_position

                self.model.currently_playing = "Black"

                ai_value = max(ai_value, value)

                # self.model.board_state[y].moved = False
                # self.model.board_state[y].position = old_pos
                # self.model.board_state = save_board

                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return ai_value

        else:
            player_value = math.inf
            self.model.currently_playing = "Black"
            for next_move in self.get_possible_moves(self.color, state):

                # print("Own Moves: " + str(len(self.get_possible_moves(self.color, state))))
                # print(self.get_possible_moves(self.color, state))

                # save_board = self.model.get_copy_board_state(state)
                x, y = next_move

                # old_pos = self.model.board_state[x].position
                # self.model.currently_playing = "White"

                change_position = False

                try:

                    # print("Type: " + str(type(state[x])))
                    change_position = state[x].position
                    state[x].position = y
                    state[y] = state[x]
                    state[x] = None
                except AttributeError:
                    pass

                # self.model.move_piece(x, y, False)
                # self.model.currently_playing = "Black"

                temp = self.model.get_copy_board_state(state)

                value = self.alpha_beta_pruning(temp, depth - 1, alpha, beta, True)

                if change_position:
                    state[y].position = change_position

                # self.model.board_state[y].moved = False
                # self.model.board_state[y].position = old_pos
                # self.model.board_state = save_board

                player_value = min(player_value, value)
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return player_value

    def calculate_board_value(self, current_game_state):

        ev = Evaluate(current_game_state)

        piece = ev.get_pieces_evaluate()

        pawn = ev.position_evaluate(pieces.Pawn, self.color, 100, ev.PAWN_TABLE)
        rook = ev.position_evaluate(pieces.Rook, self.color, 500, ev.ROOK_TABLE)
        horse = ev.position_evaluate(pieces.Horse, self.color, 320, ev.HORSE_TABLE)
        bishop = ev.position_evaluate(pieces.Bishop, self.color, 330, ev.BISHOP_TABLE)
        queen = ev.position_evaluate(pieces.Queen, self.color, 900, ev.QUEEN_TABLE)

        return piece + pawn + rook + horse + bishop + queen

    def get_possible_moves(self, color, state):

        # if state is None:
            # state = self.model.board_state

        move = []

        for i in state:
            try:
                if i.colour == color:
                    # print("Figur: " + i.colour + " " + str(i.position) + " " + str(type(i)))
                    possible_move = i.check_legal_move(i.position, state, True)
                    if len(possible_move) > 0:
                        for a in possible_move:
                            if 0 < a < 64:
                                move.append([i.position, a])

            except AttributeError:
                continue

        return move

    def move(self):
        best_score = None
        final_move = None

        state = self.model.get_copy_board_state()

        for next_move in self.get_possible_moves(self.color, state):

            temp = self.model.get_copy_board_state(state)
            # save_board = self.model.get_copy_board_state()

            x, y = next_move

            # old_pos = self.model.board_state[x].position

            temp[y] = temp[x]
            temp[x] = None

            # self.model.move_piece(x, y, False)

            # self.model.board_state[y].moved = False
            # self.model.board_state[y].position = old_pos

            current_score = self.alpha_beta_pruning(temp, 3, -math.inf, math.inf, True)
            # print("COUNT: " + str(self.count) + " SCORE: " + str(current_score))

            if best_score is None:
                best_score = current_score
                final_move = next_move

            elif current_score > best_score:
                best_score = current_score
                final_move = next_move

            # self.model.board_state = save_board
            # del save_board

        x, y = final_move

        # print(final_move)
        # sleep(50)

        self.model.move_piece(x, y)
