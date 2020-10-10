from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .ProcessStatusGUI import Ui_ProcessStatus
from ..ExecutionHandler import executionhandler
from datetime import timedelta


class ProcessStatus(QtWidgets.QWidget, Ui_ProcessStatus):

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
        self.StopProcessButton.clicked.connect(self.stopProcess)
        self.ManualControlButton.clicked.connect(self.manualOverride)
        self.NextStepButton.clicked.connect(self.nextStep)
        self.delayTimer.timeout.connect(self.delayManualControl)
        self.updateTimer.timeout.connect(self.updateETA)
        self.stopTimer.timeout.connect(self.resetProgressScreen)

    def adjustUI(self):
        self.ManualControlButton.setCheckable(True)
        self.NextStepButton.setEnabled(False)
        self.stopTimer=QtCore.QTimer()
        self.delayTimer=QtCore.QTimer()
        self.updateTimer=QtCore.QTimer()
        
    def stopProcess(self):
        ## This function should stop the machine, return it to a neutral state with no liquid.
        ## Then take the user back to the main menu when finished.
        self.CurrentTaskLabel.setText("Stopping Process . . .")
        self.ManualControlButton.setEnabled(False)
        self.StopProcessButton.setEnabled(False)
        logger.info("User requested to stop the current process.")
        self.stopProcessRequest.emit()
        self.stopTimer.start(self.remainingProcessTime)

    def manualOverride(self):
        if self.ManualControlButton.isChecked():
            logger.info("User requested manual control over process.")
            self.NextStepButton.setEnabled(True)
            self.manualOverrideRequest.emit()
        else:
            logger.info("User requested to disable manual control over process.")
            
            self.manualOverrideRequest.emit()
            self.NextStepButton.setEnabled(False)

    def resetProgressScreen(self):
        ## This will reset the screen to the default layout.
        self.ManualControlButton.setChecked(False)
        self.ManualControlButton.setEnabled(True)
        self.NextStepButton.setEnabled(False)
        self.StopProcessButton.setEnabled(True)
        self.updateTimer.stop()
        self.stopTimer.stop()
        self.CurrentTaskProgressBar.setValue(0)
        self.ETALabel.setText("Hold onto your biscuits")
        self.CurrentTaskLabel.setText("Getting ready . . .")
        logger.debug("Progress screen has been reset")
        ## Returns user to the main menu after the stop process finishes.
        self.returnUserToMenu.emit()

    def nextStep(self):
        logger.info("User requested to advance process to next step.")
        self.nextStepRequest.emit()
        self.ManualControlButton.setEnabled(False)
        self.NextStepButton.setEnabled(False)
        self.StopProcessButton.setEnabled(False)
        self.delayTimer.start(2000)

    def delayManualControl(self):
        self.ManualControlButton.setEnabled(True)
        self.NextStepButton.setEnabled(True)
        self.StopProcessButton.setEnabled(True)
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
        self.remainingProcessTime = 0
        self.returnUserToMenu.emit()

    def updateLabel(self, label: str):
        self.CurrentTaskLabel.setText(label)

    def updateETA(self):
        if self.remainingProcessTime > 0:
            self.remainingProcessTime -= 1
            self.ETALabel.setText(
                "ETA: "
                + str(timedelta(seconds=int(self.remainingProcessTime)))
            )
            self.CurrentTaskProgressBar.setValue(-self.remainingProcessTime)
            logger.debug("UPDATED ETA")