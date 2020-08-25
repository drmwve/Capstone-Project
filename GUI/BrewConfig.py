from PyQt5 import QtCore, QtGui, QtWidgets
from BrewConfigGUI import Ui_BrewConfigWindow

class BrewConfig(object):

    ## Global Variables
    ## Default display values and settings.
    ## These need to be imported to the brewing program.


    def __init__(self, MainWindow):
        self.GUICode = Ui_BrewConfigWindow()
        self.GUICode.setupUi(MainWindow)
        self.HopCartridges = 5
        self.MashTunTemperature = 160
        self.Hop1Timing = 5
        self.Hop2Timing = 10
        self.Hop3Timing = 20
        self.Hop4Timing = 30
        self.Hop5Timing = 50
        self.connections()


    def connections(self):
        self.GUICode.MashTempDecrease.clicked.connect(self.DecreaseMashTemp)
        self.GUICode.MashTempIncrease.clicked.connect(self.IncreaseMashTemp)
        self.GUICode.MashTempEntry.setText(str(self.MashTunTemperature))
        self.GUICode.HopCartridgeSelectEntry.setText(str(self.HopCartridges))
        self.GUICode.HopCartridgeSelectDecrease.clicked.connect(self.DecreaseCartridgeSelect)
        self.GUICode.HopCartridgeSelectIncrease.clicked.connect(self.IncreaseCartridgeSelect)
        self.GUICode.Hop1Decrease.clicked.connect(self.DecreaseHop1)
        self.GUICode.Hop1Entry.setText(str(self.Hop1Timing))
        self.GUICode.Hop1Increase.clicked.connect(self.IncreaseHop1)
        self.GUICode.Hop2Entry.setText(str(self.Hop2Timing))
        self.GUICode.Hop2Increase.clicked.connect(self.IncreaseHop2)
        self.GUICode.Hop2Decrease.clicked.connect(self.DecreaseHop2)
        self.GUICode.Hop3Entry.setText(str(self.Hop3Timing))
        self.GUICode.Hop3Increase.clicked.connect(self.IncreaseHop3)
        self.GUICode.Hop3Decrease.clicked.connect(self.DecreaseHop3)
        self.GUICode.Hop4Entry.setText(str(self.Hop4Timing))
        self.GUICode.Hop4Increase.clicked.connect(self.IncreaseHop4)
        self.GUICode.Hop4Decrease.clicked.connect(self.DecreaseHop4)
        self.GUICode.Hop5Entry.setText(str(self.Hop5Timing))
        self.GUICode.Hop5Increase.clicked.connect(self.IncreaseHop5)
        self.GUICode.Hop5Decrease.clicked.connect(self.DecreaseHop5)

        self.GUICode.StartBrewButton.clicked.connect(self.StartBrewing)
        self.GUICode.BackButton.clicked.connect(self.ReturnToMenu)

    ## Defining button functions
    def IncreaseMashTemp(self):

        self.MashTunTemperature += 1
        self.GUICode.MashTempEntry.setText(str(self.MashTunTemperature))

    def DecreaseMashTemp(self):
        self.MashTunTemperature -= 1
        self.GUICode.MashTempEntry.setText(str(self.MashTunTemperature))

    def IncreaseCartridgeSelect(self):

        if self.HopCartridges < 5:
            self.HopCartridges += 1
            self.GUICode.HopCartridgeSelectEntry.setText(str(self.HopCartridges))
        if self.HopCartridges == 5:
            self.GUICode.Hop5Entry.setHidden(False)
            self.GUICode.Hop5Increase.setHidden(False)
            self.GUICode.Hop5Decrease.setHidden(False)
            UseHop5 = 1
        if self.HopCartridges == 4:
            self.GUICode.Hop4Entry.setHidden(False)
            self.GUICode.Hop4Increase.setHidden(False)
            self.GUICode.Hop4Decrease.setHidden(False)
            UseHop4 = 1
        if self.HopCartridges == 3:
            self.GUICode.Hop3Entry.setHidden(False)
            self.GUICode.Hop3Increase.setHidden(False)
            self.GUICode.Hop3Decrease.setHidden(False)
            UseHop3 = 1
        if self.HopCartridges == 2:
            self.GUICode.Hop2Entry.setHidden(False)
            self.GUICode.Hop2Increase.setHidden(False)
            self.GUICode.Hop2Decrease.setHidden(False)
            UseHop2 = 1

    def DecreaseCartridgeSelect(self):

        if self.HopCartridges > 1:
            self.HopCartridges -= 1
            self.GUICode.HopCartridgeSelectEntry.setText(str(self.HopCartridges))
        if self.HopCartridges == 4:
            self.GUICode.Hop5Entry.setHidden(True)
            self.GUICode.Hop5Increase.setHidden(True)
            self.GUICode.Hop5Decrease.setHidden(True)
            UseHop5 = 0
        if self.HopCartridges == 3:
            self.GUICode.Hop4Entry.setHidden(True)
            self.GUICode.Hop4Increase.setHidden(True)
            self.GUICode.Hop4Decrease.setHidden(True)
            UseHop4 = 0
        if self.HopCartridges == 2:
            self.GUICode.Hop3Entry.setHidden(True)
            self.GUICode.Hop3Increase.setHidden(True)
            self.GUICode.Hop3Decrease.setHidden(True)
            UseHop3 = 0
        if self.HopCartridges == 1:
            self.GUICode.Hop2Entry.setHidden(True)
            self.GUICode.Hop2Increase.setHidden(True)
            self.GUICode.Hop2Decrease.setHidden(True)
            UseHop2 = 0

    def IncreaseHop1(self):
        if self.Hop1Timing < 60:
            self.Hop1Timing += 5
            self.GUICode.Hop1Entry.setText(str(self.Hop1Timing))

    def DecreaseHop1(self):
        if self.Hop1Timing > 1:
            self.Hop1Timing -= 5
            self.GUICode.Hop1Entry.setText(str(self.Hop1Timing))

    def IncreaseHop2(self):
        if self.Hop2Timing < 60:
            self.Hop2Timing += 5
            self.GUICode.Hop2Entry.setText(str(self.Hop2Timing))

    def DecreaseHop2(self):
        if self.Hop2Timing > 1:
            self.Hop2Timing -= 5
            self.GUICode.Hop2Entry.setText(str(self.Hop2Timing))

    def IncreaseHop3(self):
        if self.Hop3Timing < 60:
            self.Hop3Timing += 5
            self.GUICode.Hop3Entry.setText(str(self.Hop3Timing))

    def DecreaseHop3(self):
        if self.Hop3Timing > 1:
            self.Hop3Timing -= 5
            self.GUICode.Hop3Entry.setText(str(self.Hop3Timing))

    def IncreaseHop4(self):
        if self.Hop4Timing < 60:
            self.Hop4Timing += 5
            self.GUICode.Hop4Entry.setText(str(self.Hop4Timing))

    def DecreaseHop4(self):
        if self.Hop4Timing > 1:
            self.Hop4Timing -= 5
            self.GUICode.Hop4Entry.setText(str(self.Hop4Timing))

    def IncreaseHop5(self):
        if self.Hop5Timing < 60:
            self.Hop5Timing += 5
            self.GUICode.Hop5Entry.setText(str(self.Hop5Timing))

    def DecreaseHop5(self):
        if self.Hop5Timing > 1:
            self.Hop5Timing -= 5
            self.GUICode.Hop5Entry.setText(str(self.Hop5Timing))

    def StartBrewing(self):
        ## This function should connect to Husam's brewing program
        print("I don't work yet!")

    def ReturnToMenu(self):
        ## This will take the user back to the main menu, aborting the brew.
        print("I don't work yet either!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ## GUI Setup
    ## Define and set main window
    MainWindow.setObjectName("BrewConfigWindow")
    MainWindow.resize(1024, 600)
    MainWindow.setMinimumSize(QtCore.QSize(1024, 600))
    MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
    MainWindow.setWindowTitle("Brew Configuration")

    actualUI = BrewConfig(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())