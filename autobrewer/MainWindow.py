from functools import partial

from loguru import logger
from PySide2 import QtGui, QtWidgets

from .GUI.BrewConfig import BrewConfig
from .GUI.BrewProgress import BrewStatus
from .GUI.CleaningScreen import CleaningScreen
from .GUI.DeviceStatus import DeviceStatus
from .GUI.MainMenu import MainMenu
from .osconfig import is_raspberry_pi


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.defineMainScreenUI()
        self.createStackedLayout()
        self.connections()

    #define size of whole screen
    def defineMainScreenUI(self):
        self.setObjectName("MainWindow")
        if is_raspberry_pi():
            self.showFullScreen()
        else:
            self.setFixedSize(1024,600)
        self.setWindowTitle("Auto Brewser System")

    #create stacked layout for different pages, add them to central widget
    def createStackedLayout(self):
        self.setCentralWidget(QtWidgets.QStackedWidget())
        self.menus = {"mainMenu": MainMenu(), "brewConfig": BrewConfig(), "brewStatus": BrewStatus(), "cleaningScreen": CleaningScreen(), "deviceStatus": DeviceStatus()}
        for menu in self.menus.values():
            self.centralWidget().addWidget(menu)
        #create instances of the screens and add them to the stacked layout here


    def connections(self):
        #see "goToMenu" function below. the 'lambda: ' statement is required for arcane reasons when calling a function that takes arguments
        #in a signal-slot connection like this
        self.menus["brewConfig"].BackButton.clicked.connect(partial(self.goToMenu, self.menus["mainMenu"]))
        self.menus["brewStatus"].ReturnToMenuButton.clicked.connect(partial(self.goToMenu, self.menus["mainMenu"]))
        self.menus["deviceStatus"].ReturnToMenuButton.clicked.connect(partial(self.goToMenu, self.menus["mainMenu"]))
        self.menus["cleaningScreen"].ReturnToMenuButton.clicked.connect(partial(self.goToMenu, self.menus["mainMenu"]))

        self.menus["brewConfig"].StartBrewButton.clicked.connect(partial(self.goToMenu, self.menus["brewConfig"]))
        self.menus["mainMenu"].EnterBrewConfigButton.clicked.connect(partial(self.goToMenu, self.menus["brewConfig"]))
        self.menus["mainMenu"].EnterCleanScreenButton.clicked.connect(partial(self.goToMenu, self.menus["cleaningScreen"]))
        self.menus["mainMenu"].EnterDeviceStatusScreen.clicked.connect(partial(self.goToMenu, self.menus["deviceStatus"]))
        logger.debug("Menu navigation buttons connected")


    #this just avoids having a million "switch to menu" functions. the menu passed to this function MUST already be in the stacked layout
    def goToMenu(self, menu):
        logger.info("UI switched to screen " + str(menu))
        self.centralWidget().setCurrentWidget(menu)
