import Controller.Validator
import ui.MainWindow

class TelNumber:
    def __init__(self, number):
        self.number = number
        self.opt_number = Controller.Validator.validate(number)
        self.cc = self.opt_number[0]
        self.region = self.opt_number[1]
        self.primary = self.opt_number[2]
        self.extension = ""
        self.full_number = ""



