from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.BrewConfigGUI import Ui_BrewConfigWindow
## These variables set if a given hop dispenser should be used.
## i.e. if == 0 then that hop dispenser is not loaded or selected by the user.
## These should be imported to the brewing program to use or not use specific hop cups.
## Hop 1 is always used (How can you brew without hops???)
UseHop2 = 1
UseHop3 = 1
UseHop4 = 1
UseHop5 = 1
class BrewConfig(QtWidgets.QWidget,Ui_BrewConfigWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #global variables aren't great, especially in a multithreaded application.
        #These are local variables which will be transmitted to the logic code using a signal or by initiation of the logic code class

        self.HopCartridges = 5
        self.MashTunTemperature = 160
        self.hopTiming = [5,10,20,30,50]
        self.hopEntry = [self.Hop1Entry, self.Hop2Entry, self.Hop3Entry, self.Hop4Entry, self.Hop5Entry]

        self.Hop1Timing = 5
        self.Hop2Timing = 10
        self.Hop3Timing = 20
        self.Hop4Timing = 30
        self.Hop5Timing = 50
        self.connections()


    def connections(self):
        self.MashTempDecrease.clicked.connect(self.DecreaseMashTemp)
        self.MashTempIncrease.clicked.connect(self.IncreaseMashTemp)
        self.MashTempEntry.setText(str(self.MashTunTemperature))
        self.HopCartridgeSelectEntry.setText(str(self.HopCartridges))
        self.HopCartridgeSelectDecrease.clicked.connect(self.DecreaseCartridgeSelect)
        self.HopCartridgeSelectIncrease.clicked.connect(self.IncreaseCartridgeSelect)
        self.Hop1Decrease.clicked.connect(self.DecreaseHop1)
        self.Hop1Entry.setText(str(self.Hop1Timing))
        self.Hop1Increase.clicked.connect(self.IncreaseHop1)
        self.Hop2Entry.setText(str(self.Hop2Timing))
        self.Hop2Increase.clicked.connect(self.IncreaseHop2)
        self.Hop2Decrease.clicked.connect(self.DecreaseHop2)
        self.Hop3Entry.setText(str(self.Hop3Timing))
        self.Hop3Increase.clicked.connect(self.IncreaseHop3)
        self.Hop3Decrease.clicked.connect(self.DecreaseHop3)
        self.Hop4Entry.setText(str(self.Hop4Timing))
        self.Hop4Increase.clicked.connect(self.IncreaseHop4)
        self.Hop4Decrease.clicked.connect(self.DecreaseHop4)
        self.Hop5Entry.setText(str(self.Hop5Timing))
        self.Hop5Increase.clicked.connect(self.IncreaseHop5)
        self.Hop5Decrease.clicked.connect(self.DecreaseHop5)

        self.StartBrewButton.clicked.connect(self.StartBrewing)

    ## Defining button functions
    def IncreaseMashTemp(self):

        self.MashTunTemperature += 1
        self.MashTempEntry.setText(str(self.MashTunTemperature))

    def DecreaseMashTemp(self):
        self.MashTunTemperature -= 1
        self.MashTempEntry.setText(str(self.MashTunTemperature))

    def IncreaseCartridgeSelect(self):

        if self.HopCartridges < 5:
            self.HopCartridges += 1
            self.HopCartridgeSelectEntry.setText(str(self.HopCartridges))

        for index in range(self.HopCartridges):
            pass


        if self.HopCartridges == 5:
            self.Hop5Entry.setHidden(False)
            self.Hop5Increase.setHidden(False)
            self.Hop5Decrease.setHidden(False)
            UseHop5 = 1
        if self.HopCartridges == 4:
            self.Hop4Entry.setHidden(False)
            self.Hop4Increase.setHidden(False)
            self.Hop4Decrease.setHidden(False)
            UseHop4 = 1
        if self.HopCartridges == 3:
            self.Hop3Entry.setHidden(False)
            self.Hop3Increase.setHidden(False)
            self.Hop3Decrease.setHidden(False)
            UseHop3 = 1
        if self.HopCartridges == 2:
            self.Hop2Entry.setHidden(False)
            self.Hop2Increase.setHidden(False)
            self.Hop2Decrease.setHidden(False)
            UseHop2 = 1

    def DecreaseCartridgeSelect(self):

        if self.HopCartridges > 1:
            self.HopCartridges -= 1
            self.HopCartridgeSelectEntry.setText(str(self.HopCartridges))
        if self.HopCartridges == 4:
            self.Hop5Entry.setHidden(True)
            self.Hop5Increase.setHidden(True)
            self.Hop5Decrease.setHidden(True)
            UseHop5 = 0
        if self.HopCartridges == 3:
            self.Hop4Entry.setHidden(True)
            self.Hop4Increase.setHidden(True)
            self.Hop4Decrease.setHidden(True)
            UseHop4 = 0
        if self.HopCartridges == 2:
            self.Hop3Entry.setHidden(True)
            self.Hop3Increase.setHidden(True)
            self.Hop3Decrease.setHidden(True)
            UseHop3 = 0
        if self.HopCartridges == 1:
            self.Hop2Entry.setHidden(True)
            self.Hop2Increase.setHidden(True)
            self.Hop2Decrease.setHidden(True)
            UseHop2 = 0

    def increaseHop(self, index):
        if self.hopTiming[index] < 60:
            self.hopTiming[index] +=5
            self.hopEntry[index].setText(str(self.hopTiming[index]))

    def IncreaseHop1(self):
        if self.Hop1Timing < 60:
            self.Hop1Timing += 5
            self.Hop1Entry.setText(str(self.Hop1Timing))

    def DecreaseHop1(self):
        if self.Hop1Timing > 1:
            self.Hop1Timing -= 5
            self.Hop1Entry.setText(str(self.Hop1Timing))

    def IncreaseHop2(self):
        if self.Hop2Timing < 60:
            self.Hop2Timing += 5
            self.Hop2Entry.setText(str(self.Hop2Timing))

    def DecreaseHop2(self):
        if self.Hop2Timing > 1:
            self.Hop2Timing -= 5
            self.Hop2Entry.setText(str(self.Hop2Timing))

    def IncreaseHop3(self):
        if self.Hop3Timing < 60:
            self.Hop3Timing += 5
            self.Hop3Entry.setText(str(self.Hop3Timing))

    def DecreaseHop3(self):
        if self.Hop3Timing > 1:
            self.Hop3Timing -= 5
            self.Hop3Entry.setText(str(self.Hop3Timing))

    def IncreaseHop4(self):
        if self.Hop4Timing < 60:
            self.Hop4Timing += 5
            self.Hop4Entry.setText(str(self.Hop4Timing))

    def DecreaseHop4(self):
        if self.Hop4Timing > 1:
            self.Hop4Timing -= 5
            self.Hop4Entry.setText(str(self.Hop4Timing))

    def IncreaseHop5(self):
        if self.Hop5Timing < 60:
            self.Hop5Timing += 5
            self.Hop5Entry.setText(str(self.Hop5Timing))

    def DecreaseHop5(self):
        if self.Hop5Timing > 1:
            self.Hop5Timing -= 5
            self.Hop5Entry.setText(str(self.Hop5Timing))

    def StartBrewing(self):
        ## This function should connect to Husam's brewing program
        print("I don't work yet!")

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

    actualUI = BrewConfig()
    MainWindow.show()
    sys.exit(app.exec_())