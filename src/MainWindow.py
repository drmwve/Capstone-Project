from PySide2 import QtGui, QtWidgets
from loguru import logger
from functools import partial
from GUI.BrewConfig import BrewConfig
from GUI.BrewProgress import BrewStatus
from GUI.CleaningScreen import CleaningScreen
from GUI.DeviceStatus import DeviceStatus
from GUI.MainMenu import MainMenu


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.defineMainScreenUI()
        self.createStackedLayout()
        self.connections()

    #define size of whole screen
    def defineMainScreenUI(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(1024,600)
        self.setWindowTitle("Auto Brewser System")
        ## Uncomment next line to enable fullscreen, disabled for when testing on bigger screens.
        #self.showFullScreen()

    #create stacked layout for different pages, add them to central widget
    def createStackedLayout(self):
        self.setCentralWidget(QtWidgets.QStackedWidget())

        self.mainMenu = MainMenu()
        self.brewConfigScreen = BrewConfig()
        self.brewStatusScreen = BrewStatus()
        self.cleaningScreen = CleaningScreen()
        self.deviceStatusScreen = DeviceStatus()
        menus = [self.mainMenu, self.brewConfigScreen, self.BrewStatusScreen, self.CleaningScreen, self.DeviceStatusScreen]
        #menus = [MainMenu(), BrewConfig(), BrewStatus(), CleaningScreen(), DeviceStatus()]
        #(self.mainMenu, self.brewConfigScreen, self.brewStatusScreen, self.cleaningScreen, self.deviceStatusScreen) = menus
        for menu in menus:
            self.centralWidget().addWidget(menu)
        #create instances of the screens and add them to the stacked layout here


    def connections(self):
        #see "goToMenu" function below. the 'lambda: ' statement is required for arcane reasons when calling a function that takes arguments
        #in a signal-slot connection like this
        self.brewConfigScreen.BackButton.clicked.connect(partial(self.goToMenu, self.mainMenu))
        self.brewStatusScreen.ReturnToMenuButton.clicked.connect(partial(self.goToMenu, self.mainMenu))
        self.deviceStatusScreen.ReturnToMenuButton.clicked.connect(partial(self.goToMenu, self.mainMenu))
        self.cleaningScreen.ReturnToMenuButton.clicked.connect(partial(self.goToMenu, self.mainMenu))

        self.brewconfigScreen.StartBrewButton.clicked.connect(partial(self.goToMenu, self.BrewStatusScreen))
        self.mainMenu.EnterBrewConfigButton.clicked.connect(partial(self.goToMenu, self.brewConfigScreen))
        self.mainMenu.EnterCleanScreenButton.clicked.connect(partial(self.goToMenu, self.CleaningScreen))
        self.mainMenu.EnterDeviceStatusScreen.clicked.connect(partial(self.goToMenu, self.DeviceStatusScreen))
        logger.info("Menu navigation buttons connected")


    #this just avoids having a million "switch to menu" functions. the menu passed to this function MUST already be in the stacked layout
    def goToMenu(self, menu):
        logger.info("UI switched to screen " + str(menu))
        self.centralWidget().setCurrentWidget(menu)
