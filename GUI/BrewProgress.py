from PySide2 import QtCore, QtGui, QtWidgets
from GUI.BrewProgressGUI import Ui_BrewStatus

class BrewStatus(QtWidgets.QWidget, Ui_BrewStatus):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connections()
        self.adjustUI()

    def connections(self):
        #add any connections that are internal to the functioning of this widget only
        self.AbortBrewButton.clicked.connect(self.abortBrew)
        self.PauseResumeButton.clicked.connect(self.pauseResumeBrew)

    def adjustUI(self):
        self.PauseResumeButton.setCheckable(True)
        self.PauseResumeButton.setText("Pause")

    def abortBrew(self):
        ## This function should stop the machine, return it to a neutral state with no liquid.
        ## Then take the user back to the main menu when finished.
        self.CurrentTaskLabel.setText("Aborting Brew Cycle . . .")
        self.PauseResumeButton.setEnabled(False)
        self.AbortBrewButton.setEnabled(False)

    def pauseResumeBrew(self):
        ## This should pause the current brewing process.
        ## Primarily pumps and liquid transfers should be stopped.
        ## Heaters should remain operational to preserve the integrity of the brew.
        if self.PauseResumeButton.isChecked():
            self.PauseResumeButton.setText("Resume")
        else:
            self.PauseResumeButton.setText("Pause")

    def resetBrewScreen(self):
        ## This will reset the screen to the default layout.
        self.PauseResumeButton.setText("Pause")
        self.PauseResumeButton.setChecked(False)
        self.PauseResumeButton.setEnabled(True)
        self.AbortBrewButton.setEnabled(True)
