from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from GUI.CleaningScreenGUI import Ui_CleaningScreen
from datetime import timedelta


class CleaningScreen(QtWidgets.QWidget, Ui_CleaningScreen):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cleanRunningElements = [self.PauseResumeCleanButton, self.AbortCleanButton, self.CurrentCleanTaskLabel, self.CleanETALabel, self.CurrentCleanTaskProgressBar]
        self.adjustUI()
        self.connections()

    def connections(self):
        #add any connections that are internal to the functioning of this widget only
        self.AbortCleanButton.clicked.connect(self.abortClean)
        self.PauseResumeCleanButton.clicked.connect(self.pauseResumeClean)
        self.StartCleaningButton.clicked.connect(self.startClean)
        self.abortTimer.timeout.connect(self.resetCleanScreen)
        self.cleaningTimer.timeout.connect(self.resetCleanScreen)
        self.updateTimer.timeout.connect(self.updateETA)

    def adjustUI(self):
        self.abortTimer=QtCore.QTimer()
        self.updateTimer=QtCore.QTimer()
        self.cleaningTimer=QtCore.QTimer()
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
        self.abortTimer.start(15000)
        self.CurrentCleanTaskProgressBar.setRange(-15000, 0)
        self.cleaningTimer.stop()
        self.updateETA()
        


    def pauseResumeClean(self):
        ## This should pause the current brewing process.
        ## For the cleaning cycle it should be safe to disable all functions.
        ## (Pumps, heaters, etc.)

        if self.PauseResumeCleanButton.isChecked():
            ## Pauses process
            logger.info("User requested to pause clean.")
            self.PauseResumeCleanButton.setText("Resume")
            self.cleaningTimer.setInterval(self.cleaningTimer.remainingTime())
            self.cleaningTimer.stop()
        else:
            ## Restarts process
            logger.info("User requested to resume cleaning.")
            self.PauseResumeCleanButton.setText("Pause")
            self.cleaningTimer.start()

    def startClean(self):

        ## Reshow hidden elements that are now relevent and hide start button
        logger.info("Starting cleaning cycle.")
        for i in range(len(self.cleanRunningElements)):
            self.cleanRunningElements[i].setHidden(False)
        self.StartCleaningButton.setHidden(True)

        self.CurrentCleanTaskLabel.setText("This should update the user on what's happening . . .")
        self.cleaningTimer.start(3.6e+6)
        self.CurrentCleanTaskProgressBar.setRange(-3.6e+6, 0)
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
        self.abortTimer.stop()
        self.cleaningTimer.stop()

    def updateETA(self):
        if self.abortTimer.isActive() == True:
            self.CleanETALabel.setText("ETA: "+str(timedelta(seconds=int(self.abortTimer.remainingTime()/1000))))
            self.CurrentCleanTaskProgressBar.setValue(-self.abortTimer.remainingTime())
            self.updateTimer.start(1000)
        elif self.cleaningTimer.isActive() == True:
            self.CleanETALabel.setText("ETA: "+str(timedelta(seconds=int(self.cleaningTimer.remainingTime()/1000))))
            self.CurrentCleanTaskProgressBar.setValue(-self.cleaningTimer.remainingTime())
            self.updateTimer.start(1000)