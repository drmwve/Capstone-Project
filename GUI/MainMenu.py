from PyQt5 import QtCore, QtGui, QtWidgets
from BrewConfig import *

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        
        ## Defining button functions
        def EnterBrewScreen(BrewScreen):
            ## Work in progress, takes you to the brew screen.
            ## Doesn't allow you to go back and forth more than once.
            self.BrewScreen = BrewScreen
            self.BrewScreen=QtWidgets.QMainWindow()
            self.ui=Ui_BrewConfigWindow()
            self.ui.setupUi(self.BrewScreen)
            self.BrewScreen.show()
            MainMenu.close()

        def EnterCleanScreen():
            print("I don't go anywhere yet...")

        def EnterStatusScreen():
            print("Same.")

        ## GUI Setup
        ## Define main window
        MainMenu.setObjectName("MainMenu")
        MainMenu.setWindowModality(QtCore.Qt.WindowModal)
        MainMenu.setEnabled(True)
        MainMenu.resize(1024, 600)
        MainMenu.setMinimumSize(QtCore.QSize(1024, 600))
        MainMenu.setMaximumSize(QtCore.QSize(1024, 600))
        ## Uncomment next line to enable fullscreen, disabled for when testing on bigger screens.
        #BrewConfigWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.MainMenuLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.MainMenuLayout.setObjectName("MainMenuLayout")

        ## Font Settings
        font = QtGui.QFont()
        font.setPointSize(12)

        ## Start a brew button
        self.EnterBrewConfigButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterBrewConfigButton.setMinimumSize(QtCore.QSize(0, 60))
        self.EnterBrewConfigButton.setMaximumSize(QtCore.QSize(800, 60))
        self.EnterBrewConfigButton.setFont(font)
        self.EnterBrewConfigButton.setObjectName("EnterBrewConfigButton")
        self.MainMenuLayout.addWidget(self.EnterBrewConfigButton, 0, 0, 1, 1)
        self.EnterBrewConfigButton.setText("Start a new brew")
        self.EnterBrewConfigButton.clicked.connect(EnterBrewScreen)

        ## Cleaning cycle button
        self.EnterSanitationCycleButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterSanitationCycleButton.setMinimumSize(QtCore.QSize(0, 60))
        self.EnterSanitationCycleButton.setMaximumSize(QtCore.QSize(800, 60))
        self.EnterSanitationCycleButton.setFont(font)
        self.EnterSanitationCycleButton.setObjectName("EnterSanitationCycleButton")
        self.MainMenuLayout.addWidget(self.EnterSanitationCycleButton, 1, 0, 1, 1)
        self.EnterSanitationCycleButton.setText("Run sanitation cycle")
        self.EnterSanitationCycleButton.clicked.connect(EnterCleanScreen)

        ## Status screen button
        self.EnterStatusScreenButton = QtWidgets.QPushButton(self.centralwidget)
        self.EnterStatusScreenButton.setMinimumSize(QtCore.QSize(0, 60))
        self.EnterStatusScreenButton.setMaximumSize(QtCore.QSize(800, 60))
        self.EnterStatusScreenButton.setFont(font)
        self.EnterStatusScreenButton.setObjectName("EnterStatusScreenButton")
        self.MainMenuLayout.addWidget(self.EnterStatusScreenButton, 2, 0, 1, 1)
        self.EnterStatusScreenButton.setText("Device status")
        self.EnterStatusScreenButton.clicked.connect(EnterStatusScreen)

        ## Finalize layout
        MainMenu.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec_())
