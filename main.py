from Model import Model
from View import View

if __name__ == 'main':
    model = Model(View())
    model.view.model = model
