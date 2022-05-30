'''
Created 25 March 2022

'''

from modelCalc import Model
from viewCalc import View


class Controller:
    def __init__(self):
        self.modelCalc = Model()
        self.viewCalc = View(self)

    def main(self):
        self.viewCalc.main()

    
    def on_button_click(self, caption):
        result = self.modelCalc.calculate(caption)

        self.viewCalc.value_var.set(result)

if __name__ == '__main__':
    calculator = Controller()
    calculator.main()



