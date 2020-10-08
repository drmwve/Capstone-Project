from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .CleaningScreenGUI import Ui_CleaningScreen
from datetime import timedelta


class CleaningScreen(QtWidgets.QWidget, Ui_CleaningScreen):

    startCleaningSignal = QtCore.Signal()
    flushSystemSignal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.adjustUI()
        self.connections()

    def connections(self):
        # add any connections that are internal to the functioning of this widget only
        self.StartCleaningButton.clicked.connect(self.startClean)
        self.FlushSystemButton.clicked.connect(self.flushSystem)

    def adjustUI(self):
        pass

    def startClean(self):
        ## Reshow hidden elements that are now relevent and hide start button
        logger.info("User requested to start cleaning cycle.")
        self.startCleaningSignal.emit()

    def flushSystem(self):
        logger.info("User requested to flush system.")
        self.flushSystemSignal.emit()