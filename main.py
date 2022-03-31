import sys

from ui.MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

#if __name__ == '__main__':
#    app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
