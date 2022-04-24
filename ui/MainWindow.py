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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 150, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnOptInput = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOptInput.sizePolicy().hasHeightForWidth())
        self.btnOptInput.setSizePolicy(sizePolicy)
        self.btnOptInput.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnOptInput.setFont(font)
        self.btnOptInput.setObjectName("btnOptInput")
        self.horizontalLayout.addWidget(self.btnOptInput)
        self.btnResetInput = QtWidgets.QPushButton(self.centralwidget)
        self.btnResetInput.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnResetInput.setFont(font)
        self.btnResetInput.setObjectName("btnResetInput")
        self.horizontalLayout.addWidget(self.btnResetInput)
        self.btnCancelOpt = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelOpt.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnCancelOpt.setFont(font)
        self.btnCancelOpt.setObjectName("btnCancelOpt")
        self.horizontalLayout.addWidget(self.btnCancelOpt)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 75, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.lblOutOptCC = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOutOptCC.sizePolicy().hasHeightForWidth())
        self.lblOutOptCC.setSizePolicy(sizePolicy)
        self.lblOutOptCC.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutOptCC.setFont(font)
        self.lblOutOptCC.setAutoFillBackground(False)
        self.lblOutOptCC.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblOutOptCC.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutOptCC.setObjectName("lblOutOptCC")
        self.gridLayout.addWidget(self.lblOutOptCC, 0, 0, 1, 1)
        self.lblOutOptRegion = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOutOptRegion.sizePolicy().hasHeightForWidth())
        self.lblOutOptRegion.setSizePolicy(sizePolicy)
        self.lblOutOptRegion.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutOptRegion.setFont(font)
        self.lblOutOptRegion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblOutOptRegion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutOptRegion.setObjectName("lblOutOptRegion")
        self.gridLayout.addWidget(self.lblOutOptRegion, 0, 1, 1, 1)
        self.lblOutOptPrimary = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOutOptPrimary.sizePolicy().hasHeightForWidth())
        self.lblOutOptPrimary.setSizePolicy(sizePolicy)
        self.lblOutOptPrimary.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutOptPrimary.setFont(font)
        self.lblOutOptPrimary.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblOutOptPrimary.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutOptPrimary.setObjectName("lblOutOptPrimary")
        self.gridLayout.addWidget(self.lblOutOptPrimary, 0, 2, 1, 1)
        self.lblOutOptExt = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOutOptExt.sizePolicy().hasHeightForWidth())
        self.lblOutOptExt.setSizePolicy(sizePolicy)
        self.lblOutOptExt.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutOptExt.setFont(font)
        self.lblOutOptExt.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblOutOptExt.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutOptExt.setObjectName("lblOutOptExt")
        self.gridLayout.addWidget(self.lblOutOptExt, 0, 3, 1, 1)
        self.outOptCC = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outOptCC.sizePolicy().hasHeightForWidth())
        self.outOptCC.setSizePolicy(sizePolicy)
        self.outOptCC.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outOptCC.setFont(font)
        self.outOptCC.setAutoFillBackground(False)
        self.outOptCC.setFrameShape(QtWidgets.QFrame.Box)
        self.outOptCC.setText("")
        self.outOptCC.setAlignment(QtCore.Qt.AlignCenter)
        self.outOptCC.setObjectName("outOptCC")
        self.gridLayout.addWidget(self.outOptCC, 1, 0, 1, 1)
        self.outOptRegion = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outOptRegion.sizePolicy().hasHeightForWidth())
        self.outOptRegion.setSizePolicy(sizePolicy)
        self.outOptRegion.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outOptRegion.setFont(font)
        self.outOptRegion.setAutoFillBackground(False)
        self.outOptRegion.setFrameShape(QtWidgets.QFrame.Box)
        self.outOptRegion.setText("")
        self.outOptRegion.setAlignment(QtCore.Qt.AlignCenter)
        self.outOptRegion.setObjectName("outOptRegion")
        self.gridLayout.addWidget(self.outOptRegion, 1, 1, 1, 1)
        self.outOptPrimary = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outOptPrimary.sizePolicy().hasHeightForWidth())
        self.outOptPrimary.setSizePolicy(sizePolicy)
        self.outOptPrimary.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outOptPrimary.setFont(font)
        self.outOptPrimary.setAutoFillBackground(False)
        self.outOptPrimary.setFrameShape(QtWidgets.QFrame.Box)
        self.outOptPrimary.setText("")
        self.outOptPrimary.setAlignment(QtCore.Qt.AlignCenter)
        self.outOptPrimary.setObjectName("outOptPrimary")
        self.gridLayout.addWidget(self.outOptPrimary, 1, 2, 1, 1)
        self.outOptExt = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outOptExt.sizePolicy().hasHeightForWidth())
        self.outOptExt.setSizePolicy(sizePolicy)
        self.outOptExt.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outOptExt.setFont(font)
        self.outOptExt.setAutoFillBackground(False)
        self.outOptExt.setFrameShape(QtWidgets.QFrame.Box)
        self.outOptExt.setText("")
        self.outOptExt.setAlignment(QtCore.Qt.AlignCenter)
        self.outOptExt.setObjectName("outOptExt")
        self.gridLayout.addWidget(self.outOptExt, 1, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 50, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblIn = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblIn.sizePolicy().hasHeightForWidth())
        self.lblIn.setSizePolicy(sizePolicy)
        self.lblIn.setMinimumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblIn.setFont(font)
        self.lblIn.setAlignment(QtCore.Qt.AlignCenter)
        self.lblIn.setObjectName("lblIn")
        self.gridLayout_2.addWidget(self.lblIn, 0, 0, 1, 1)
        self.inputTelNr = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputTelNr.sizePolicy().hasHeightForWidth())
        self.inputTelNr.setSizePolicy(sizePolicy)
        self.inputTelNr.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputTelNr.setFont(font)
        self.inputTelNr.setAlignment(QtCore.Qt.AlignCenter)
        self.inputTelNr.setObjectName("inputTelNr")
        self.gridLayout_2.addWidget(self.inputTelNr, 0, 1, 1, 1)
        self.lblOutStruct = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOutStruct.sizePolicy().hasHeightForWidth())
        self.lblOutStruct.setSizePolicy(sizePolicy)
        self.lblOutStruct.setMinimumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lblOutStruct.setFont(font)
        self.lblOutStruct.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutStruct.setObjectName("lblOutStruct")
        self.gridLayout_2.addWidget(self.lblOutStruct, 1, 0, 1, 1)
        self.outStructTelNr = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outStructTelNr.sizePolicy().hasHeightForWidth())
        self.outStructTelNr.setSizePolicy(sizePolicy)
        self.outStructTelNr.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.outStructTelNr.setFont(font)
        self.outStructTelNr.setFrameShape(QtWidgets.QFrame.Box)
        self.outStructTelNr.setFrameShadow(QtWidgets.QFrame.Plain)
        self.outStructTelNr.setText("")
        self.outStructTelNr.setAlignment(QtCore.Qt.AlignCenter)
        self.outStructTelNr.setObjectName("outStructTelNr")
        self.gridLayout_2.addWidget(self.outStructTelNr, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
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
        self.btnOptInput.setText(_translate("MainWindow", "Optimieren"))
        self.btnResetInput.setText(_translate("MainWindow", "Zurücksetzen"))
        self.btnCancelOpt.setText(_translate("MainWindow", "Abbrechen"))
        self.lblOutOptCC.setText(_translate("MainWindow", "Ländervorwahl:"))
        self.lblOutOptRegion.setText(_translate("MainWindow", "Ortsvortwahl:"))
        self.lblOutOptPrimary.setText(_translate("MainWindow", "Rufnummer:"))
        self.lblOutOptExt.setText(_translate("MainWindow", "Durchwahl:"))
        self.lblIn.setText(_translate("MainWindow", "Bitte Telefonnummer hier eintragen:"))
        self.lblOutStruct.setText(_translate("MainWindow", "Strukturierte Telefonnummer:"))
