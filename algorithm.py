"""
    Module that contains the alpha-beta-pruning algorithm for the AI
"""
import math
from tqdm import tqdm
import pieces
from evaluatePieces import Evaluate


class AI:
    """Handles the behavior of the AI"""

    def __init__(self, model, view, color, enemy):
        self.model = model
        self.view = view
        self.color = color
        self.enemy = enemy  # Enemy Color

    def alpha_beta_pruning(self, state, depth, alpha, beta, ai_playing):
        """Returns the score of the current board"""

        # calcs the score of the current board
        if depth == 0 or not self.model.check_for_king():
            return self.calculate_board_value(state)

        if ai_playing:
            ai_value = -math.inf
            self.model.currently_playing = "White"
            # calcs the score of every possible move
            for next_move in self.get_possible_moves(self.enemy, state):

                x_move, y_move = next_move

                temp = self.model.get_copy_board_state(state)

                change_position = None

                try:

                    # print("Type: " + str(type(state[x])))
                    change_position = temp[x_move].position
                    temp[x_move].position = y_move
                    temp[y_move] = temp[x_move]
                    temp[x_move] = None
                except AttributeError:
                    pass

                # calcs the score of the current board
                value = self.alpha_beta_pruning(temp, depth - 1, alpha, beta, False)

                if change_position is not None:
                    temp[y_move].position = change_position

                self.model.currently_playing = "Black"

                # White want the score as high as possible
                ai_value = max(ai_value, value)

                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return ai_value

        player_value = math.inf
        self.model.currently_playing = "Black"
        for next_move in self.get_possible_moves(self.color, state):

            x_move, y_move = next_move

            temp = self.model.get_copy_board_state(state)

            change_position = None

            try:

                change_position = temp[x_move].position
                temp[x_move].position = y_move
                temp[y_move] = temp[x_move]
                temp[x_move] = None
            except AttributeError:
                pass

            value = self.alpha_beta_pruning(temp, depth - 1, alpha, beta, True)

            if change_position is not None:
                temp[y_move].position = change_position

            # Black wants the score as low as possible
            player_value = min(player_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return player_value

    @staticmethod
    def calculate_board_value(current_game_state):
        """Evaluate the current Board"""

        evaluate = Evaluate(current_game_state)

        piece = evaluate.get_pieces_evaluate()

        pawn = evaluate.position_evaluate(pieces.Pawn, 100, evaluate.PAWN_TABLE)
        horse = evaluate.position_evaluate(pieces.Horse, 320, evaluate.HORSE_TABLE)
        bishop = evaluate.position_evaluate(pieces.Bishop, 330, evaluate.BISHOP_TABLE)
        rook = evaluate.position_evaluate(pieces.Rook, 500, evaluate.ROOK_TABLE)
        queen = evaluate.position_evaluate(pieces.Queen, 900, evaluate.QUEEN_TABLE)

        return piece + pawn + rook + horse + bishop + queen

    @staticmethod
    def get_possible_moves(color, state):
        """Get all possible moves of the color"""

        move = []

        for i in state:
            try:
                if i.colour == color:
                    possible_move = i.check_legal_move(i.position, state, True)
                    if len(possible_move) > 0:
                        for moves in possible_move:
                            if 0 < moves < 64:
                                move.append([i.position, moves])

            except AttributeError:
                continue

        return move

    def move(self):
        """
        Main function
        Calcs the best move for the AI moves
        """

        print("AI thinks...")

        best_score = math.inf
        final_move = None

        # The current board self.model.board_state shouldn't be overwritten
        # Therefore state is a copy of the Value and not a copy of the Instance
        state = self.model.get_copy_board_state()
        possible_moves = self.get_possible_moves(self.color, state)

        output = tqdm(total=len(possible_moves))

        # Calcs every possible move of the AI
        for next_move in possible_moves:

            temp = self.model.get_copy_board_state(state)

            x_move, y_move = next_move
            change_position = None

            try:

                # if a pieces got the attribute position, it has to be saved and changed
                change_position = temp[x_move].position
                temp[x_move].position = y_move
                temp[y_move] = temp[x_move]
                temp[x_move] = None
            except AttributeError:
                pass

            # calcs the score of the current move
            current_score = self.alpha_beta_pruning(temp, 3, -math.inf, math.inf, True)

            if change_position is not None:
                temp[y_move].position = change_position

            if current_score < best_score:
                best_score = current_score
                final_move = next_move

            output.update()

        output.close()

        x_move, y_move = final_move
        print(str(x_move) + " " + str(y_move))

        self.model.move_piece(x_move, y_move)
