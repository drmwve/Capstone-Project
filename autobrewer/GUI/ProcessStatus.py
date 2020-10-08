from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .BrewProgressGUI import Ui_BrewStatus
from ..ExecutionHandler import executionhandler
from datetime import timedelta


class ProcessStatus(QtWidgets.QWidget, Ui_BrewStatus):

    nextStepRequest = QtCore.Signal()
    stopProcessRequest = QtCore.Signal()
    manualOverrideRequest = QtCore.Signal()
    returnUserToMenu = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.adjustUI()
        self.connections()
        

    def connections(self):
        # add any connections that are internal to the functioning of this widget only
        self.AbortBrewButton.clicked.connect(self.abortBrew)
        self.ManualBrewButton.clicked.connect(self.manualOverride)
        self.NextBrewStepButton.clicked.connect(self.nextStep)
        self.delayTimer.timeout.connect(self.delayManualControl)
        self.updateTimer.timeout.connect(self.updateETA)
        self.abortTimer.timeout.connect(self.resetProgressScreen)

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
        logger.info("User requested to abort brew.")
        self.stopProcessRequest.emit()
        self.abortTimer.start(self.remainingProcessTime)

    def manualOverride(self):
        if self.ManualBrewButton.isChecked():
            logger.info("User requested manual control over process.")
            self.NextBrewStepButton.setEnabled(True)
            self.manualOverrideRequest.emit()
        else:
            logger.info("User requested to disable manual control over process.")
            
            self.manualOverrideRequest.emit()
            self.NextBrewStepButton.setEnabled(False)

    def resetProgressScreen(self):
        ## This will reset the screen to the default layout.
        self.ManualBrewButton.setChecked(False)
        self.ManualBrewButton.setEnabled(True)
        self.NextBrewStepButton.setEnabled(False)
        self.AbortBrewButton.setEnabled(True)
        self.updateTimer.stop()
        self.abortTimer.stop()
        self.CurrentTaskProgressBar.setValue(0)
        self.ETALabel.setText("Hold onto your biscuits")
        self.CurrentTaskLabel.setText("Getting ready . . .")
        logger.debug("Progress screen has been reset")
        ## Returns user to the main menu after the abort process finishes.
        self.returnUserToMenu.emit()

    def nextStep(self):
        logger.info("User requested to advance process to next step.")
        self.nextStepRequest.emit()
        self.ManualBrewButton.setEnabled(False)
        self.NextBrewStepButton.setEnabled(False)
        self.AbortBrewButton.setEnabled(False)
        self.delayTimer.start(2000)

    def delayManualControl(self):
        self.ManualBrewButton.setEnabled(True)
        self.NextBrewStepButton.setEnabled(True)
        self.AbortBrewButton.setEnabled(True)
        self.delayTimer.stop()

    def startUpdateTimer(self, totalprocesstime):
        self.totalProcessTime = totalprocesstime
        self.remainingProcessTime = self.totalProcessTime
        self.resetProgressScreen()
        self.CurrentTaskProgressBar.setRange(-self.totalProcessTime, 0)
        self.updateTimer.start(1000)

    def processComplete(self):
        logger.debug("Caught process complete")
        self.updateTimer.stop()
        self.CurrentTaskProgressBar.setValue(0)
        self.CurrentTaskLabel.setText("Process Complete")
        self.ETALabel.setText("")

    def updateLabel(self, label: str):
        self.CurrentTaskLabel.setText(label)

    def updateETA(self):
        self.remainingProcessTime -= 1
        self.ETALabel.setText(
            "ETA: "
            + str(timedelta(seconds=int(self.remainingProcessTime)))
        )
        self.CurrentTaskProgressBar.setValue(-self.remainingProcessTime)
        logger.debug("UPDATED ETA")