"""
    Module that contains the alpha-beta-pruning algorithm for the AI
"""
from model import Model
from math import inf
class AI:
    def __init__(self, model):
        self.model = model

    def alpha_beta_pruning(self, current_game_state, depth, alpha, beta, ai_playing):
        if depth == 0 or not self.model.check_for_king(# Give team, add default value):
            return self.calculate_board_value(current_game_state)
        if ai_playing:
            ai_value = inf
            for next in states: # All ai-pieces * their possible move options??
                value = alpha_beta_pruning(next, depth - 1, alpha, beta, False)
                ai_value = max(ai_value, value)
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return ai_value
        else:
            player_value = -inf
            for next in states # All player-pieces * their possible move options??
                value = alpha_beta_pruning(next, depth - 1, alpha, beta, True)
                player_value = min(player_value, value)
                beta = min(beta, value)
                if beta <= alpha:
                    break
                return player_value

    def calculate_board_value(self):
        pass # Pieces need a Value assigned to them which can be added up to calculate a value for a game-state!
            # Maybe make lists that contain only white and only black pieces?
            # If change is made, adapt king check and piece removal from move