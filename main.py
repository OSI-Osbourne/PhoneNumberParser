import sys

import Controller.Validator
import Model.TelNumber
from ui.MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.btnCancelOpt.clicked.connect(self.close)
        self.btnOptInput.clicked.connect(self.initInput)
        self.btnResetInput.clicked.connect(self.refresh)

    def initInput(self):
        inputNumber = self.inputTelNr.text()
        full_number = ''

        model = Model.TelNumber.TelNumber(inputNumber)
        model.cc = model.cc.replace('(', '')
        model.cc = model.cc.replace(')', '')

        # country code (cc)
        if model.cc == '0':
            model.cc = '+49'
            self.outOptCC.setText("DE")
            full_number += "+49 "

        elif model.cc.startswith('00'):
            model.cc = model.cc.replace('00', '+')
            self.outOptCC.setText(model.cc)
            full_number += model.cc + ' '
        else:
            self.outOptCC.setText(model.cc)
            full_number += model.cc + ' '


        model.cc = Controller.Validator.replace_cc(model.cc)
        self.outOptCC.setText(model.cc)

        model.region = model.region.replace('(', '')
        model.region = model.region.replace(')', '')


        # region number
        self.outOptRegion.setText(model.region)
        full_number += model.region + ' '

        # primary number
        self.outOptPrimary.setText(model.primary)
        full_number += model.primary

        # extension
        if model.extension == '':
            self.outOptExt.setText('─')
        else:
            self.outOptExt.setText(model.extension)
            full_number += '-' + model.extension

        # full phone number
        self.outStructTelNr.setText(full_number)

        # success
        if not model.valid:
            self.lblStatus.setText('Telefonnummer konnte nicht formatiert werden!')
        else:
            self.lblStatus.setText('Telefonnummer erfolgreich formatiert!')

    def refresh(self):
        self.inputTelNr.setText("")
        self.outStructTelNr.setText("")
        self.outOptCC.setText("")
        self.outOptRegion.setText("")
        self.outOptPrimary.setText("")
        self.outOptExt.setText("")
        self.lblStatus.setText("")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
