# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblIn = QtWidgets.QLabel(self.centralwidget)
        self.lblIn.setGeometry(QtCore.QRect(80, 70, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblIn.setFont(font)
        self.lblIn.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIn.setObjectName("lblIn")
        self.inputTelNr = QtWidgets.QLineEdit(self.centralwidget)
        self.inputTelNr.setGeometry(QtCore.QRect(360, 70, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputTelNr.setFont(font)
        self.inputTelNr.setAlignment(QtCore.Qt.AlignCenter)
        self.inputTelNr.setObjectName("inputTelNr")
        self.btnOptInput = QtWidgets.QPushButton(self.centralwidget)
        self.btnOptInput.setGeometry(QtCore.QRect(125, 500, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnOptInput.setFont(font)
        self.btnOptInput.setObjectName("btnOptInput")
        self.btnCancelOpt = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelOpt.setGeometry(QtCore.QRect(525, 500, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnCancelOpt.setFont(font)
        self.btnCancelOpt.setObjectName("btnCancelOpt")
        self.btnResetInput = QtWidgets.QPushButton(self.centralwidget)
        self.btnResetInput.setGeometry(QtCore.QRect(325, 500, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnResetInput.setFont(font)
        self.btnResetInput.setObjectName("btnResetInput")
        self.outStructTelNr = QtWidgets.QLabel(self.centralwidget)
        self.outStructTelNr.setGeometry(QtCore.QRect(360, 140, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outStructTelNr.setFont(font)
        self.outStructTelNr.setFrameShape(QtWidgets.QFrame.Box)
        self.outStructTelNr.setFrameShadow(QtWidgets.QFrame.Plain)
        self.outStructTelNr.setText("")
        self.outStructTelNr.setAlignment(QtCore.Qt.AlignCenter)
        self.outStructTelNr.setObjectName("outStructTelNr")
        self.lblOutStruct = QtWidgets.QLabel(self.centralwidget)
        self.lblOutStruct.setGeometry(QtCore.QRect(80, 140, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutStruct.setFont(font)
        self.lblOutStruct.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutStruct.setObjectName("lblOutStruct")
        self.lblOutOptCC = QtWidgets.QLabel(self.centralwidget)
        self.lblOutOptCC.setGeometry(QtCore.QRect(40, 250, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutOptCC.setFont(font)
        self.lblOutOptCC.setAutoFillBackground(False)
        self.lblOutOptCC.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblOutOptCC.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutOptCC.setObjectName("lblOutOptCC")
        self.lblOutOptRegion = QtWidgets.QLabel(self.centralwidget)
        self.lblOutOptRegion.setGeometry(QtCore.QRect(230, 250, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutOptRegion.setFont(font)
        self.lblOutOptRegion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblOutOptRegion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutOptRegion.setObjectName("lblOutOptRegion")
        self.lblOutOptPrimary = QtWidgets.QLabel(self.centralwidget)
        self.lblOutOptPrimary.setGeometry(QtCore.QRect(420, 250, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutOptPrimary.setFont(font)
        self.lblOutOptPrimary.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblOutOptPrimary.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutOptPrimary.setObjectName("lblOutOptPrimary")
        self.lblOutOptExt = QtWidgets.QLabel(self.centralwidget)
        self.lblOutOptExt.setGeometry(QtCore.QRect(610, 250, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutOptExt.setFont(font)
        self.lblOutOptExt.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblOutOptExt.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutOptExt.setObjectName("lblOutOptExt")
        self.outOptRegion = QtWidgets.QLabel(self.centralwidget)
        self.outOptRegion.setGeometry(QtCore.QRect(230, 320, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outOptRegion.setFont(font)
        self.outOptRegion.setAutoFillBackground(False)
        self.outOptRegion.setFrameShape(QtWidgets.QFrame.Box)
        self.outOptRegion.setText("")
        self.outOptRegion.setAlignment(QtCore.Qt.AlignCenter)
        self.outOptRegion.setObjectName("outOptRegion")
        self.outOptCC = QtWidgets.QLabel(self.centralwidget)
        self.outOptCC.setGeometry(QtCore.QRect(40, 320, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outOptCC.setFont(font)
        self.outOptCC.setAutoFillBackground(False)
        self.outOptCC.setFrameShape(QtWidgets.QFrame.Box)
        self.outOptCC.setText("")
        self.outOptCC.setAlignment(QtCore.Qt.AlignCenter)
        self.outOptCC.setObjectName("outOptCC")
        self.outOptExt = QtWidgets.QLabel(self.centralwidget)
        self.outOptExt.setGeometry(QtCore.QRect(610, 320, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outOptExt.setFont(font)
        self.outOptExt.setAutoFillBackground(False)
        self.outOptExt.setFrameShape(QtWidgets.QFrame.Box)
        self.outOptExt.setText("")
        self.outOptExt.setAlignment(QtCore.Qt.AlignCenter)
        self.outOptExt.setObjectName("outOptExt")
        self.outOptPrimary = QtWidgets.QLabel(self.centralwidget)
        self.outOptPrimary.setGeometry(QtCore.QRect(420, 320, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outOptPrimary.setFont(font)
        self.outOptPrimary.setAutoFillBackground(False)
        self.outOptPrimary.setFrameShape(QtWidgets.QFrame.Box)
        self.outOptPrimary.setText("")
        self.outOptPrimary.setAlignment(QtCore.Qt.AlignCenter)
        self.outOptPrimary.setObjectName("outOptPrimary")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telefonnummer optimieren"))
        self.lblIn.setText(_translate("MainWindow", "Bitte Telefonnummer hier eintragen:"))
        self.btnOptInput.setText(_translate("MainWindow", "Optimieren"))
        self.btnCancelOpt.setText(_translate("MainWindow", "Abbrechen"))
        self.btnResetInput.setText(_translate("MainWindow", "Zurücksetzen"))
        self.lblOutStruct.setText(_translate("MainWindow", "Strukturierte Telefonnummer:"))
        self.lblOutOptCC.setText(_translate("MainWindow", "Ländervorwahl:"))
        self.lblOutOptRegion.setText(_translate("MainWindow", "Ortsvortwahl:"))
        self.lblOutOptPrimary.setText(_translate("MainWindow", "Rufnummer:"))
        self.lblOutOptExt.setText(_translate("MainWindow", "Durchwahl:"))