from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .BrewProgressGUI import Ui_BrewStatus
from ..ExecutionHandler import executionhandler
from datetime import timedelta


class BrewStatus(QtWidgets.QWidget, Ui_BrewStatus):

    nextBrewStepSignal = QtCore.Signal()
    abortBrewSignal = QtCore.Signal()
    manualOverrideSignal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.adjustUI()
        self.connections()
        

    def connections(self):
        # add any connections that are internal to the functioning of this widget only
        self.AbortBrewButton.clicked.connect(self.abortBrew)
        self.ManualBrewButton.clicked.connect(self.manualBrewing)
        self.NextBrewStepButton.clicked.connect(self.nextBrewingStep)
        self.delayTimer.timeout.connect(self.delayManualControl)
        self.updateTimer.timeout.connect(self.updateETA)
        #self.abortTimer.timeout.connect(brewStatus.resetBrewScreen)

    def adjustUI(self):
        self.ManualBrewButton.setCheckable(True)
        self.ManualBrewButton.setText("Manual Control")
        self.NextBrewStepButton.setEnabled(False)
        self.abortTimer=QtCore.QTimer()
        self.delayTimer=QtCore.QTimer()
        self.updateTimer=QtCore.QTimer()
        
    def abortBrew(self):
        ## This function should stop the machine, return it to a neutral state with no liquid.
        ## Then take the user back to the main menu when finished.
        self.CurrentTaskLabel.setText("Aborting Brew Cycle . . .")
        self.ManualBrewButton.setEnabled(False)
        self.AbortBrewButton.setEnabled(False)
        self.abortTimer.start(executionhandler.process.currentstep.estimatedtime)
        logger.info("User requested to abort brew.")
        self.abortBrewSignal.emit()

    def manualBrewing(self):
        if self.ManualBrewButton.isChecked():
            logger.info("User requested manual control over brewing cycle.")
            self.NextBrewStepButton.setEnabled(True)
            self.manualOverrideSignal.emit()
        else:
            logger.info("User requested to disable manual control over brewing cycle.")
            
            self.manualOverrideSignal.emit()
            self.NextBrewStepButton.setEnabled(False)

    def resetBrewScreen(self):
        ## This will reset the screen to the default layout.

        self.ManualBrewButton.setChecked(False)
        self.ManualBrewButton.setEnabled(True)
        self.NextBrewStepButton.setEnabled(False)
        self.AbortBrewButton.setEnabled(True)


    def nextBrewingStep(self):
        logger.info("User requested to advance brewing to next step.")
        self.nextBrewStepSignal.emit()
        self.ManualBrewButton.setEnabled(False)
        self.NextBrewStepButton.setEnabled(False)
        self.AbortBrewButton.setEnabled(False)
        self.delayTimer.start(2000)

    def delayManualControl(self):
        self.ManualBrewButton.setEnabled(True)
        self.NextBrewStepButton.setEnabled(True)
        self.AbortBrewButton.setEnabled(True)
        self.delayTimer.stop()

    def updateETA(self):
        self.ETALabel.setText(
            "ETA: "
            + str(timedelta(seconds=int(executionhandler.process.currentstep.estimatedtime / 1000)))
        )
        self.CurrentTaskProgressBar.setValue(executionhandler.process.currentstep.estimatedtime)
        self.CurrentTaskLabel.setText(str(executionhandler.process.currentstep))
        self.updateTimer.start(1000)
        logger.debug("UPDATED ETA")




brewStatus = BrewStatus()