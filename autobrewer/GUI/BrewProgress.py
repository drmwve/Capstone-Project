from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .BrewProgressGUI import Ui_BrewStatus


class BrewStatus(QtWidgets.QWidget, Ui_BrewStatus):

    nextBrewStepSignal = QtCore.Signal()
    abortBrewSignal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connections()
        self.adjustUI()

    def connections(self):
        # add any connections that are internal to the functioning of this widget only
        self.AbortBrewButton.clicked.connect(self.abortBrew)
        self.ManualBrewButton.clicked.connect(self.manualBrewing)
        self.NextBrewStepButton.clicked.connect(self.nextBrewingStep)

    def adjustUI(self):
        self.ManualBrewButton.setCheckable(True)
        self.ManualBrewButton.setText("Manual Control")
        self.NextBrewStepButton.setEnabled(False)

    def abortBrew(self):
        ## This function should stop the machine, return it to a neutral state with no liquid.
        ## Then take the user back to the main menu when finished.
        self.CurrentTaskLabel.setText("Aborting Brew Cycle . . .")
        self.ManualBrewButton.setEnabled(False)
        self.AbortBrewButton.setEnabled(False)
        logger.info("User requested to abort brew.")
        self.abortBrewSignal.emit()


    def manualBrewing(self):
        if self.ManualBrewButton.isChecked():
            logger.info("User requested manual control over brewing cycle.")
            self.NextBrewStepButton.setEnabled(True)
        else:
            logger.info("User requested to disable manual control over brewing cycle.")
            self.NextBrewStepButton.setEnabled(False)

    def resetBrewScreen(self):
        ## This will reset the screen to the default layout.
        self.ManualBrewButton.setText("Pause")
        self.ManualBrewButton.setChecked(False)
        self.ManualBrewButton.setEnabled(True)
        self.ManualBrewButton.setEnabled(True)

    def nextBrewingStep(self):
        logger.info("User requested to advance brewing to next step.")
        self.nextBrewStepSignal.emit()
        pass