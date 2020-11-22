from PySide2.QtCore import Signal, QTimer
from PySide2.QtWidgets import QWidget
from loguru import logger
from .ProcessStatusGUI import Ui_ProcessStatus
from datetime import timedelta


class ProcessStatus(QWidget, Ui_ProcessStatus):

    nextStepRequest = Signal()
    stopProcessRequest = Signal()
    manualOverrideRequest = Signal()
    returnUserToMenu = Signal()

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
        self.stopTimer=QTimer()
        self.delayTimer=QTimer()
        self.updateTimer=QTimer()
        
    def stopProcess(self):
        ## This function should stop the machine, return it to a neutral state with no liquid.
        ## Then take the user back to the main menu when finished.
        logger.info("User requested to stop the current process.")
        self.stopProcessRequest.emit()
        self.updateTimer.stop()
        self.stopTimer.stop()
        self.ETALabel.setText("Return to main menu to start a new process.")
        self.CurrentTaskLabel.setText("Process Stopped")
        self.CurrentTaskProgressBar.setHidden(True)
        self.processScreenEnd(True)

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
        self.processScreenEnd(False)
        self.CurrentTaskProgressBar.setHidden(False)
        self.updateTimer.stop()
        self.stopTimer.stop()
        self.CurrentTaskProgressBar.setValue(0)
        self.ETALabel.setText("Hold onto your biscuits")
        self.CurrentTaskLabel.setText("Getting ready . . .")
        logger.debug("Progress screen has been reset")

    def nextStep(self):
        logger.info("User requested to advance process to next step.")
        self.nextStepRequest.emit()
        self.NextStepButton.setEnabled(False)
        self.StopProcessButton.setEnabled(False)
        self.delayTimer.start(250)

    def delayManualControl(self):
        self.NextStepButton.setEnabled(True)
        self.StopProcessButton.setEnabled(True)
        self.delayTimer.stop()

    def startUpdateTimer(self, totalprocesstime):
        self.totalProcessTime = totalprocesstime
        self.remainingProcessTime = self.totalProcessTime
        self.resetProgressScreen()
        self.CurrentTaskProgressBar.setRange(-self.totalProcessTime, 0)
        self.CurrentTaskProgressBar.setValue(-self.totalProcessTime)
        self.updateTimer.start(1000)

    def processComplete(self):
        logger.debug("Caught process complete")
        self.updateTimer.stop()
        self.CurrentTaskProgressBar.setValue(0)
        self.CurrentTaskLabel.setText("Process Complete")
        self.ETALabel.setText("")
        self.remainingProcessTime = 0
        self.processScreenEnd(True)

    # sets the screen to allow the user to return to main menu after a process is stopped or completes
    def processScreenEnd(self, state: bool):
        if state:
            self.ManualControlButton.setHidden(True)
            self.NextStepButton.setHidden(True)
            self.StopProcessButton.setText("Main Menu")
            try:
                self.StopProcessButton.clicked.disconnect(self.stopProcess)
            except:
                pass
            self.StopProcessButton.clicked.connect(self.returnUserToMenu)
        else:
            self.ManualControlButton.setHidden(False)
            self.NextStepButton.setHidden(False)
            self.StopProcessButton.setText("Stop Process")
            self.StopProcessButton.clicked.connect(self.stopProcess)
            try:
                self.StopProcessButton.clicked.disconnect(self.returnUserToMenu)
            except:
                pass

    def updateLabel(self, label: str):
        self.CurrentTaskLabel.setText(label)

    def updateremainingtime(self, time: int):
        self.remainingProcessTime = time
        self.updateETA(decrement=False)

    def updateETA(self, decrement=True):
        if self.remainingProcessTime > 0:
            if decrement:
                self.remainingProcessTime -= 1
            self.ETALabel.setText(
                "ETA: "
                + str(timedelta(seconds=int(self.remainingProcessTime)))
            )
            self.CurrentTaskProgressBar.setValue(-self.remainingProcessTime)