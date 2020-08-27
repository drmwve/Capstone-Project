from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.CleaningScreenGUI import Ui_CleaningScreen

class CleaningScreen(QtWidgets.QWidget, Ui_CleaningScreen):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cleanRunningElements = [self.PauseResumeCleanButton, self.AbortCleanButton, self.CurrentCleanTaskLabel, self.CleanETALabel, self.CurrentCleanTaskProgressBar]
        self.connections()
        self.adjustUI()

    def connections(self):
        #add any connections that are internal to the functioning of this widget only
        self.AbortCleanButton.clicked.connect(self.abortClean)
        self.PauseResumeCleanButton.clicked.connect(self.pauseResumeClean)
        self.StartCleaningButton.clicked.connect(self.startClean)

    def adjustUI(self):
        self.PauseResumeCleanButton.setCheckable(True)
        self.PauseResumeCleanButton.setText("Pause")
        ## Hide UI elements that don't have a purpose until cleaning starts.
        for i in range(len(self.cleanRunningElements)):
            self.cleanRunningElements[i].setHidden(True)

    def abortClean(self):
        ## This function should stop the machine, return it to a neutral state with no liquid.
        ## Then take the user back to the main menu when finished.
        self.CurrentCleanTaskLabel.setText("Aborting Cleaning Cycle . . .")

    def pauseResumeClean(self):
        ## This should pause the current brewing process.
        ## For the cleaning cycle it should be safe to disable all functions.
        ## (Pumps, heaters, etc.)
        if self.PauseResumeCleanButton.isChecked():
            self.PauseResumeCleanButton.setText("Resume")
        else:
            self.PauseResumeCleanButton.setText("Pause")

    def startClean(self):

        ## Reshow hidden elements that are now relevent and hide start button
        for i in range(len(self.cleanRunningElements)):
            self.cleanRunningElements[i].setHidden(False)
        self.StartCleaningButton.setHidden(True)
