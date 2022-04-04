import Controller.Validator
import Controller.Parser
import ui.MainWindow

class TelNumber:
    def __init__(self, number):
        self.number = number
        self.cc = ""
        self.region = ""
        self.primary = ""
        self.extension = ""
        self.full_number = ""
        Controller.Validator.validate(self.number)



