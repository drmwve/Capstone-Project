from PySide2 import QtCore, QtGui, QtWidgets
from GUI.BrewConfigGUI import Ui_BrewConfigWindow
from functools import partial

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

        for index, hopRow in enumerate(self.hopEntry):
            print(index)
            self.hopEntry[index].setText(str(self.hopTiming[index]))
            self.hopIncrease[index].clicked.connect(partial(self.increaseHop, index))
            self.hopDecrease[index].clicked.connect(partial(self.decreaseHop, index))

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
            self.hopEntry[self.HopCartridges - 1].setText("0")

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