from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from GUI.BrewConfigGUI import Ui_BrewConfigWindow
from functools import partial
import linecache

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
        self.QBLoadButton.clicked.connect(self.toggleLoad)
        self.QBSaveButton.clicked.connect(self.toggleSave)

        self.QB1Button.clicked.connect(lambda: self.quickBrew(0))
        self.QB2Button.clicked.connect(lambda: self.quickBrew(1))
        self.QB3Button.clicked.connect(lambda: self.quickBrew(2))
        self.QB4Button.clicked.connect(lambda: self.quickBrew(3))
        self.QB5Button.clicked.connect(lambda: self.quickBrew(4))
        self.QB6Button.clicked.connect(lambda: self.quickBrew(5))

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
        logger.info("Starting brew cycle with parameters: ""MTT:"+str(self.MashTunTemperature)+" HC:"+str(self.HopCartridges)+" HT:"+str(self.hopTiming))


    def toggleLoad(self):
        if self.QBSaveButton.isChecked():
            self.QBSaveButton.toggle()

    def toggleSave(self):
        if self.QBLoadButton.isChecked():
            self.QBLoadButton.toggle()

    def quickBrew(self, index):
        ## Load a brew
        if self.QBLoadButton.isChecked():
            logger.info("Read QuickBrew file "+str(index+1))
            ## Linecache has to be cleared before loading or recently edited files will remain unchanged
            linecache.clearcache()
            ## Retrieve settings from file and store them in the usual variables
            self.MashTunTemperature = int(linecache.getline('src\GUI\QuickBrewSaves\QuickBrew%d.txt'%(index,), 1))
            self.HopCartridges = int(linecache.getline('src\GUI\QuickBrewSaves\QuickBrew%d.txt'%(index,), 2))
            for i in range(0, 5):
                self.hopTiming[i] = int(linecache.getline('src\GUI\QuickBrewSaves\QuickBrew%d.txt'%(index,), 3+i))
            ## Print retrieved settings
            logger.info("Brew parameters set to: ""MTT:"+str(self.MashTunTemperature)+" HC:"+str(self.HopCartridges)+" HT:"+str(self.hopTiming))
            ## Reset text field displays
            for i in range(0,5):
                self.hopEntry[i].setText(str(self.hopTiming[i]))
            self.HopCartridgeSelectEntry.setText(str(self.HopCartridges))
            self.MashTempEntry.setText(str(self.MashTunTemperature))
            ## Show all hop fields
            for i in range(0,5):
                self.hopEntry[i].setHidden(False)
                self.hopIncrease[i].setHidden(False)
                self.hopDecrease[i].setHidden(False)
            ## Hide irrelevant hop fields
            if self.HopCartridges < 5:
                for i in range(self.HopCartridges, 5):
                    self.hopEntry[i].setHidden(True)
                    self.hopIncrease[i].setHidden(True)
                    self.hopDecrease[i].setHidden(True)
        ## Save a brew
        if self.QBSaveButton.isChecked():
            ## Open or create file in writing mode
            self.qbFile = open('src\GUI\QuickBrewSaves\QuickBrew%d.txt'%(index,), 'w')
            ## Logging
            logger.info("Saved QuickBrew file "+str(index+1))
            logger.info("Brew parameters saved: ""MTT:"+str(self.MashTunTemperature)+" HC:"+str(self.HopCartridges)+" HT:"+str(self.hopTiming))
            ## Write Mash temp
            self.qbFile.write(str(self.MashTunTemperature)) 
            ## Write hop cartridges to new line
            self.qbFile.write('\n'+str(self.HopCartridges))
            ## Write hop timings to new individual lines
            for i in range(0,5):
                self.qbFile.write('\n'+str(self.hopTiming[i])) 
            ## Close the file
            self.qbFile.close()
