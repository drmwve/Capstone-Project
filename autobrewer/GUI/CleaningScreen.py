from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget
from loguru import logger
from .CleaningScreenGUI import Ui_CleaningScreen


class CleaningScreen(QWidget, Ui_CleaningScreen):

    startCleaningSignal = Signal()
    flushSystemSignal = Signal()

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