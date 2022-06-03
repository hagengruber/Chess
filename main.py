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
