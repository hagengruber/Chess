"""
    @Author: Schamberger Sandro: 22102471
    @Author: Hagengruber Florian: 22101608
    @Author: Joiko Christian:
"""
from model import Model


if __name__ == "__main__":
    model = Model()
    model.controller.model = model
    model.view.model = model
    model.view.print_menu()
    model.controller.get_menu_choice()

"""
TODO:
    -Add Tips, Rules, Options (however you want to call it) to allow user to change whether or not he wants to use
     symbols or not, tell him the rules/possibilities of this chess version (Castling etc. is possible) and to give tips
     (H is horse, Change Font-Size because symbols are very small) [Format of Input!]
    -Add Save Option
    -Fix Bug that other pieces that are not Horses can jump over other pieces (Only happened once by KI with Pawn)
    -Add comments to algorithm.py and evaluatePieces.py
    -Test the game to find more bugs!
"""