from functools import partial

from PySide2 import QtWidgets
from loguru import logger

from .GUI.BrewConfig import BrewConfig
from .GUI.ProcessStatus import ProcessStatus
from .GUI.CleaningScreen import CleaningScreen
from .GUI.DeviceStatus import DeviceStatus
from .GUI.MainMenu import MainMenu
from .utils import IS_RASPBERRY_PI
from .Process import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.defineMainScreenUI()
        self.createStackedLayout()
        self.connections()

    # define size of whole screen
    def defineMainScreenUI(self):
        self.setObjectName("MainWindow")
        if IS_RASPBERRY_PI:
            self.showFullScreen()
        else:
            self.setFixedSize(1024, 600)
        self.setWindowTitle("Auto Brewer System")

    # create stacked layout for different pages, add them to central widget
    def createStackedLayout(self):
        self.setCentralWidget(QtWidgets.QStackedWidget())
        self.menus = {
            "mainMenu": MainMenu(),
            "brewConfig": BrewConfig(),
            "processStatus": ProcessStatus(),
            "cleaningScreen": CleaningScreen(),
            "deviceStatus": DeviceStatus(),
        }
        for menu in self.menus.values():
            self.centralWidget().addWidget(menu)
        # create instances of the screens and add them to the stacked layout here

    def connections(self):
        # see "goToMenu" function below. the partial statement is required for arcane reasons when calling a function that takes arguments
        # in a signal-slot connection like this
        self.menus["brewConfig"].BackButton.clicked.connect(
            partial(self.goToMenu, self.menus["mainMenu"])
        )
        self.menus["processStatus"].DeviceStatusButton.clicked.connect(
            partial(self.goToMenu, self.menus["deviceStatus"])
        )
        self.menus["deviceStatus"].ReturnToMenuButton.clicked.connect(
            partial(self.goToMenu, self.menus["mainMenu"])
        )
        self.menus["cleaningScreen"].ReturnToMenuButton.clicked.connect(
            partial(self.goToMenu, self.menus["mainMenu"])
        )
        self.menus["cleaningScreen"].StartCleaningButton.clicked.connect(
            partial(self.goToMenu, self.menus["processStatus"])
        )
        self.menus["cleaningScreen"].FlushSystemButton.clicked.connect(
            partial(self.goToMenu, self.menus["processStatus"])
        )
        self.menus["brewConfig"].StartBrewButton.clicked.connect(
            partial(self.goToMenu, self.menus["processStatus"])
        )
        self.menus["mainMenu"].EnterBrewConfigButton.clicked.connect(
            partial(self.goToMenu, self.menus["brewConfig"])
        )
        self.menus["mainMenu"].EnterCleanScreenButton.clicked.connect(
            partial(self.goToMenu, self.menus["cleaningScreen"])
        )
        self.menus["mainMenu"].EnterDeviceStatusScreen.clicked.connect(
            partial(self.goToMenu, self.menus["deviceStatus"])
        )
        self.menus["deviceStatus"].ProcessStatusButton.clicked.connect(
            partial(self.goToMenu, self.menus["processStatus"])
        )
        logger.debug("Menu navigation buttons connected")

    # this just avoids having a million "switch to menu" functions. the menu passed to this function MUST already be in the stacked layout
    def goToMenu(self, menu):
        logger.info("Switched to screen " + str(menu))
        self.centralWidget().setCurrentWidget(menu)
