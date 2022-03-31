import sys

from ui.MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
