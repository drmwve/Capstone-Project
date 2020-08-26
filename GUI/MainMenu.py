# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainMenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.setWindowModality(QtCore.Qt.WindowModal)
        MainMenu.setEnabled(True)
        MainMenu.resize(1024, 600)
        MainMenu.setMinimumSize(QtCore.QSize(1024, 600))
        MainMenu.setMaximumSize(QtCore.QSize(1024, 600))
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.EnterBrewConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterBrewConfigButton.setMinimumSize(QtCore.QSize(0, 60))
        self.EnterBrewConfigButton.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EnterBrewConfigButton.setFont(font)
        self.EnterBrewConfigButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EnterBrewConfigButton.setFlat(False)
        self.EnterBrewConfigButton.setObjectName("EnterBrewConfigButton")
        self.gridLayout.addWidget(self.EnterBrewConfigButton, 0, 0, 1, 1)
        self.EnterSanitationCycleButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterSanitationCycleButton.setMinimumSize(QtCore.QSize(0, 60))
        self.EnterSanitationCycleButton.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EnterSanitationCycleButton.setFont(font)
        self.EnterSanitationCycleButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EnterSanitationCycleButton.setFlat(False)
        self.EnterSanitationCycleButton.setObjectName("EnterSanitationCycleButton")
        self.gridLayout.addWidget(self.EnterSanitationCycleButton, 1, 0, 1, 1)
        self.EnterStatusScreen = QtWidgets.QPushButton(self.centralwidget)
        self.EnterStatusScreen.setEnabled(True)
        self.EnterStatusScreen.setMinimumSize(QtCore.QSize(0, 60))
        self.EnterStatusScreen.setMaximumSize(QtCore.QSize(800, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EnterStatusScreen.setFont(font)
        self.EnterStatusScreen.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.EnterStatusScreen.setFlat(False)
        self.EnterStatusScreen.setObjectName("EnterStatusScreen")
        self.gridLayout.addWidget(self.EnterStatusScreen, 2, 0, 1, 1)
        MainMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menubar.setObjectName("menubar")
        MainMenu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "MainMenu"))
        self.EnterBrewConfigButton.setText(_translate("MainMenu", "Start a new brew"))
        self.EnterSanitationCycleButton.setText(_translate("MainMenu", "Run sanitation cycle"))
        self.EnterStatusScreen.setText(_translate("MainMenu", "Device status"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
