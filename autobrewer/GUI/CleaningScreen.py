from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .CleaningScreenGUI import Ui_CleaningScreen
from datetime import timedelta


class CleaningScreen(QtWidgets.QWidget, Ui_CleaningScreen):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cleanRunningElements = [self.NextCleanStepButton, self.ManualCleanButton, self.AbortCleanButton, self.CurrentCleanTaskLabel, self.CleanETALabel, self.CurrentCleanTaskProgressBar]
        self.adjustUI()
        self.timers = [self.updateTimer, self.actionTimer]
        self.connections()

    def connections(self):
        #add any connections that are internal to the functioning of this widget only
        self.AbortCleanButton.clicked.connect(self.abortClean)
        self.ManualCleanButton.clicked.connect(self.manualCleaning)
        self.StartCleaningButton.clicked.connect(self.startClean)
        self.actionTimer.timeout.connect(self.resetCleanScreen)
        self.updateTimer.timeout.connect(self.updateETA)
        self.NextCleanStepButton.clicked.connect(self.nextCleaningStep)

    def adjustUI(self):
        self.updateTimer=QtCore.QTimer()
        self.actionTimer=QtCore.QTimer()
        self.ManualCleanButton.setCheckable(True)
        self.ManualCleanButton.setText("Manual Control")
        self.NextCleanStepButton.setEnabled(False)
        ## Hide UI elements that don't have a purpose until cleaning starts.
        for i in range(len(self.cleanRunningElements)):
            self.cleanRunningElements[i].setVisible(False)

    def abortClean(self):
        ## This function should stop the machine, return it to a neutral state with no liquid.
        ## Then take the user back to the main menu when finished.
        logger.info("User requested to abort clean.")
        self.CurrentCleanTaskLabel.setText("Aborting Cleaning Cycle . . .")
        self.ManualCleanButton.setEnabled(False)
        self.AbortCleanButton.setEnabled(False)
        self.actionTimer.stop()
        self.actionTimer.start(15000)
        self.CurrentCleanTaskProgressBar.setRange(-15000, 0)
        self.updateETA()



    def manualCleaning(self):
        if self.ManualCleanButton.isChecked():
            ## Enables next step button
            logger.info("User requested manual control over cleaning cycle.")
            self.NextCleanStepButton.setEnabled(True)
        else:
            ## Restarts process
            logger.info("User requested to disable manual control over cleaning cycle.")
            self.NextCleanStepButton.setEnabled(False)

    def startClean(self):

        ## Reshow hidden elements that are now relevent and hide start button
        logger.info("Starting cleaning cycle.")
        for i in range(len(self.cleanRunningElements)):
            self.cleanRunningElements[i].setHidden(False)
        self.StartCleaningButton.setHidden(True)
        self.CurrentCleanTaskLabel.setText("This should update the user on what's happening . . .")
        self.actionTimer.start(3.6e+6)
        self.CurrentCleanTaskProgressBar.setRange(-3.6e+6, 0)
        self.updateETA()

    def resetCleanScreen(self):
        ## This will reset the screen to the default layout.
        for i in range(len(self.cleanRunningElements)):
            self.cleanRunningElements[i].setHidden(True)
        self.ManualCleanButton.setText("Pause")
        self.StartCleaningButton.setHidden(False)
        self.ManualCleanButton.setChecked(False)
        self.CurrentCleanTaskLabel.setText("What am I doing?")
        self.ManualCleanButton.setEnabled(True)
        self.AbortCleanButton.setEnabled(True)
        self.CleanETALabel.setText("ETA: 84 Years")
        self.actionTimer.stop()

    def updateETA(self):
        self.CleanETALabel.setText("ETA: "+str(timedelta(seconds=int(self.actionTimer.remainingTime()/1000))))
        self.CurrentCleanTaskProgressBar.setValue(-self.actionTimer.remainingTime())
        self.updateTimer.start(1000)

    def nextCleaningStep(self):
        logger.info("User requested to advance cleaning to next step.")
        pass