# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(1024, 600)
        MainMenu.setMinimumSize(QtCore.QSize(1024, 600))
        MainMenu.setMaximumSize(QtCore.QSize(1024, 600))
        self.MainMenuLayout = QtWidgets.QGridLayout(MainMenu)
        self.MainMenuLayout.setObjectName("MainMenuLayout")
        self.EnterCleanScreenButton = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.EnterCleanScreenButton.sizePolicy().hasHeightForWidth()
        )
        self.EnterCleanScreenButton.setSizePolicy(sizePolicy)
        self.EnterCleanScreenButton.setMinimumSize(QtCore.QSize(800, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.EnterCleanScreenButton.setFont(font)
        self.EnterCleanScreenButton.setObjectName("EnterCleanScreenButton")
        self.MainMenuLayout.addWidget(self.EnterCleanScreenButton, 1, 0, 1, 1)
        self.EnterBrewConfigButton = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.EnterBrewConfigButton.sizePolicy().hasHeightForWidth()
        )
        self.EnterBrewConfigButton.setSizePolicy(sizePolicy)
        self.EnterBrewConfigButton.setMinimumSize(QtCore.QSize(800, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.EnterBrewConfigButton.setFont(font)
        self.EnterBrewConfigButton.setObjectName("EnterBrewConfigButton")
        self.MainMenuLayout.addWidget(self.EnterBrewConfigButton, 0, 0, 1, 1)
        self.EnterDeviceStatusScreen = QtWidgets.QPushButton(MainMenu)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.EnterDeviceStatusScreen.sizePolicy().hasHeightForWidth()
        )
        self.EnterDeviceStatusScreen.setSizePolicy(sizePolicy)
        self.EnterDeviceStatusScreen.setMinimumSize(QtCore.QSize(800, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.EnterDeviceStatusScreen.setFont(font)
        self.EnterDeviceStatusScreen.setObjectName("EnterDeviceStatusScreen")
        self.MainMenuLayout.addWidget(self.EnterDeviceStatusScreen, 2, 0, 1, 1)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Form"))
        self.EnterCleanScreenButton.setText(_translate("MainMenu", "Cleaning"))
        self.EnterBrewConfigButton.setText(_translate("MainMenu", "Start Brewing"))
        self.EnterDeviceStatusScreen.setText(_translate("MainMenu", "Device Status"))
