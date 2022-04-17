from View import View
from Controller import Controller


class Model:
    def __init__(self):
        self.board_state = [[' '] * 8] * 8
        self.view = View()
        self.controller = Controller()

    def moin(self):
        pass
