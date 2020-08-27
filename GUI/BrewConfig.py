from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.BrewConfigGUI import Ui_BrewConfigWindow

class BrewConfig(QtWidgets.QWidget,Ui_BrewConfigWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.HopCartridges = 5
        self.MashTunTemperature = 160
        self.hopTiming = [0,0,0,0,0]
        self.hopEntry = [self.Hop1Entry, self.Hop2Entry, self.Hop3Entry, self.Hop4Entry, self.Hop5Entry]
        self.hopIncrease = [self.Hop1Increase, self.Hop2Increase, self.Hop3Increase, self.Hop4Increase, self.Hop5Increase]
        self.hopDecrease = [self.Hop1Decrease, self.Hop2Decrease, self.Hop3Decrease, self.Hop4Decrease, self.Hop5Decrease]
        self.connections()


    def connections(self):
        self.MashTempDecrease.clicked.connect(self.DecreaseMashTemp)
        self.MashTempIncrease.clicked.connect(self.IncreaseMashTemp)
        self.MashTempEntry.setText(str(self.MashTunTemperature))

        self.HopCartridgeSelectEntry.setText(str(self.HopCartridges))
        self.HopCartridgeSelectDecrease.clicked.connect(self.DecreaseCartridgeSelect)
        self.HopCartridgeSelectIncrease.clicked.connect(self.IncreaseCartridgeSelect)
        
        self.Hop1Entry.setText(str(self.hopTiming[0]))
        self.Hop1Decrease.clicked.connect(lambda:self.decreaseHop(0))
        self.Hop1Increase.clicked.connect(lambda:self.increaseHop(0))

        self.Hop2Entry.setText(str(self.hopTiming[1]))
        self.Hop2Increase.clicked.connect(lambda:self.increaseHop(1))
        self.Hop2Decrease.clicked.connect(lambda:self.decreaseHop(1))

        self.Hop3Entry.setText(str(self.hopTiming[2]))
        self.Hop3Increase.clicked.connect(lambda:self.increaseHop(2))
        self.Hop3Decrease.clicked.connect(lambda:self.decreaseHop(2))

        self.Hop4Entry.setText(str(self.hopTiming[3]))
        self.Hop4Increase.clicked.connect(lambda:self.increaseHop(3))
        self.Hop4Decrease.clicked.connect(lambda:self.decreaseHop(3))

        self.Hop5Entry.setText(str(self.hopTiming[4]))
        self.Hop5Increase.clicked.connect(lambda:self.increaseHop(4))
        self.Hop5Decrease.clicked.connect(lambda:self.decreaseHop(4))

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
            self.hopEntry[self.HopCartridges - 1].setHidden(False)
            self.hopIncrease[self.HopCartridges - 1].setHidden(False)
            self.hopDecrease[self.HopCartridges - 1].setHidden(False)
            self.hopTiming[self.HopCartridges - 1] = 0

    def DecreaseCartridgeSelect(self):
        if self.HopCartridges > 1:
            self.HopCartridges -= 1
            self.HopCartridgeSelectEntry.setText(str(self.HopCartridges))
            self.hopEntry[self.HopCartridges].setHidden(True)
            self.hopIncrease[self.HopCartridges].setHidden(True)
            self.hopDecrease[self.HopCartridges].setHidden(True)
            self.hopTiming[self.HopCartridges] = -1

    def increaseHop(self, index):
        if self.hopTiming[index] < 60:
            self.hopTiming[index] +=5
            self.hopEntry[index].setText(str(self.hopTiming[index]))

    def decreaseHop(self, index):
        if self.hopTiming[index] > 0:
            self.hopTiming[index] -=5
            self.hopEntry[index].setText(str(self.hopTiming[index]))

    def StartBrewing(self):
        ## This function should connect to Husam's brewing program
        print("I need connected to the brewing program")

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