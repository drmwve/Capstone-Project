from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .CleaningScreenGUI import Ui_CleaningScreen
from datetime import timedelta


class CleaningScreen(QtWidgets.QWidget, Ui_CleaningScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cleanRunningElements = [
            self.PauseResumeCleanButton,
            self.AbortCleanButton,
            self.CurrentCleanTaskLabel,
            self.CleanETALabel,
            self.CurrentCleanTaskProgressBar,
        ]
        self.adjustUI()
        self.timers = [self.updateTimer, self.actionTimer]
        self.connections()

    def connections(self):
        # add any connections that are internal to the functioning of this widget only
        self.AbortCleanButton.clicked.connect(self.abortClean)
        self.PauseResumeCleanButton.clicked.connect(self.pauseResumeClean)
        self.StartCleaningButton.clicked.connect(self.startClean)
        self.actionTimer.timeout.connect(self.resetCleanScreen)
        self.updateTimer.timeout.connect(self.updateETA)

    def adjustUI(self):
        self.updateTimer = QtCore.QTimer()
        self.actionTimer = QtCore.QTimer()
        self.PauseResumeCleanButton.setCheckable(True)
        self.PauseResumeCleanButton.setText("Pause")
        ## Hide UI elements that don't have a purpose until cleaning starts.
        for i in range(len(self.cleanRunningElements)):
            self.cleanRunningElements[i].setHidden(True)

    def abortClean(self):
        ## This function should stop the machine, return it to a neutral state with no liquid.
        ## Then take the user back to the main menu when finished.
        logger.info("User requested to abort clean.")
        self.CurrentCleanTaskLabel.setText("Aborting Cleaning Cycle . . .")
        self.PauseResumeCleanButton.setEnabled(False)
        self.AbortCleanButton.setEnabled(False)
        self.actionTimer.stop()
        self.actionTimer.start(15000)
        self.CurrentCleanTaskProgressBar.setRange(-15000, 0)
        self.updateETA()

    def pauseResumeClean(self):
        ## This should pause the current brewing process.
        ## For the cleaning cycle it should be safe to disable all functions.
        ## (Pumps, heaters, etc.)

        if self.PauseResumeCleanButton.isChecked():
            ## Pauses process
            logger.info("User requested to pause clean.")
            self.PauseResumeCleanButton.setText("Resume")
            self.actionTimer.setInterval(self.actionTimer.remainingTime())
            self.actionTimer.stop()
            self.updateTimer.stop()
        else:
            ## Restarts process
            logger.info("User requested to resume cleaning.")
            self.PauseResumeCleanButton.setText("Pause")
            self.actionTimer.start()
            self.updateTimer.start()

    def startClean(self):

        ## Reshow hidden elements that are now relevent and hide start button
        logger.info("Starting cleaning cycle.")
        for i in range(len(self.cleanRunningElements)):
            self.cleanRunningElements[i].setHidden(False)
        self.StartCleaningButton.setHidden(True)
        self.CurrentCleanTaskLabel.setText(
            "This should update the user on what's happening . . ."
        )
        self.actionTimer.start(3.6e6)
        self.CurrentCleanTaskProgressBar.setRange(-3.6e6, 0)
        self.updateETA()

    def resetCleanScreen(self):
        ## This will reset the screen to the default layout.
        for i in range(len(self.cleanRunningElements)):
            self.cleanRunningElements[i].setHidden(True)
        self.PauseResumeCleanButton.setText("Pause")
        self.StartCleaningButton.setHidden(False)
        self.PauseResumeCleanButton.setChecked(False)
        self.CurrentCleanTaskLabel.setText("What am I doing?")
        self.PauseResumeCleanButton.setEnabled(True)
        self.AbortCleanButton.setEnabled(True)
        self.CleanETALabel.setText("ETA: 84 Years")
        self.actionTimer.stop()

    def updateETA(self):
        self.CleanETALabel.setText(
            "ETA: "
            + str(timedelta(seconds=int(self.actionTimer.remainingTime() / 1000)))
        )
        self.CurrentCleanTaskProgressBar.setValue(-self.actionTimer.remainingTime())
        self.updateTimer.start(1000)
