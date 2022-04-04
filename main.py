import sys

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
        Model.TelNumber.TelNumber(inputNumber)
        self.outOptCC.setText("1")
        self.outOptRegion.setText("1")
        self.outOptPrimary.setText("1")
        self.outOptExt.setText("1")
        self.outStructTelNr.setText("1")

    def refresh(self):
        self.inputTelNr.setText("")
        self.outStructTelNr.setText("")
        self.outOptCC.setText("")
        self.outOptRegion.setText("")
        self.outOptPrimary.setText("")
        self.outOptExt.setText("")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()