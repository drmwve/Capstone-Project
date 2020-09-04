from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from ExecutionCode.BrewRecipe import BrewRecipe, BrewRecipePickler
from GUI.BrewConfigGUI import Ui_BrewConfigWindow
from functools import partial
import linecache

class BrewConfig(QtWidgets.QWidget,Ui_BrewConfigWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pickler = BrewRecipePickler()
        self.savedBrewRecipes = self.pickler.loadRecipes()
        logger.debug("Loaded recipes %s" % self.savedBrewRecipes)
        self.selectedBrewRecipe = self.savedBrewRecipes[0]

        self.hopEntry = [self.Hop1Entry, self.Hop2Entry, self.Hop3Entry, self.Hop4Entry, self.Hop5Entry]
        self.hopIncrease = [self.Hop1Increase, self.Hop2Increase, self.Hop3Increase, self.Hop4Increase, self.Hop5Increase]
        self.hopDecrease = [self.Hop1Decrease, self.Hop2Decrease, self.Hop3Decrease, self.Hop4Decrease, self.Hop5Decrease]
        self.connections()


    def connections(self):
        self.MashTempDecrease.clicked.connect(self.DecreaseMashTemp)
        self.MashTempIncrease.clicked.connect(self.IncreaseMashTemp)
        self.MashTempEntry.setText(str(self.selectedBrewRecipe.mashTunTemperature))

        self.HopCartridgeSelectEntry.setText(str(self.selectedBrewRecipe.hopCartridges))
        self.HopCartridgeSelectDecrease.clicked.connect(self.DecreaseCartridgeSelect)
        self.HopCartridgeSelectIncrease.clicked.connect(self.IncreaseCartridgeSelect)

        for index, hopRow in enumerate(self.hopEntry):
            self.hopEntry[index].setText(str(self.selectedBrewRecipe.hopTiming[index]))
            self.hopIncrease[index].clicked.connect(partial(self.increaseHop, index))
            self.hopDecrease[index].clicked.connect(partial(self.decreaseHop, index))

        self.StartBrewButton.clicked.connect(self.StartBrewing)
        self.QBLoadButton.clicked.connect(self.toggleLoad)
        self.QBSaveButton.clicked.connect(self.toggleSave)

    ## Defining button functions
    def IncreaseMashTemp(self):
        self.selectedBrewRecipe.mashTunTemperature += 1
        self.MashTempEntry.setText(str(self.selectedBrewRecipe.mashTunTemperature))

    def DecreaseMashTemp(self):
        self.selectedBrewRecipe.mashTunTemperature -= 1
        self.MashTempEntry.setText(str(self.selectedBrewRecipe.mashTunTemperature))

    def IncreaseCartridgeSelect(self):
        if self.selectedBrewRecipe.hopCartridges < 5:
            self.selectedBrewRecipe.hopCartridges += 1
            self.HopCartridgeSelectEntry.setText(str(self.selectedBrewRecipe.hopCartridges))
            self.hopEntry[self.selectedBrewRecipe.hopCartridges - 1].setHidden(False)
            self.hopIncrease[self.selectedBrewRecipe.hopCartridges - 1].setHidden(False)
            self.hopDecrease[self.selectedBrewRecipe.hopCartridges - 1].setHidden(False)
            self.selectedBrewRecipe.hopTiming[self.selectedBrewRecipe.hopCartridges - 1] = 0
            self.hopEntry[self.selectedBrewRecipe.hopCartridges - 1].setText("0")

    def DecreaseCartridgeSelect(self):
        if self.selectedBrewRecipe.hopCartridges > 1:
            self.selectedBrewRecipe.hopCartridges -= 1
            self.HopCartridgeSelectEntry.setText(str(self.selectedBrewRecipe.hopCartridges))
            self.hopEntry[self.selectedBrewRecipe.hopCartridges].setHidden(True)
            self.hopIncrease[self.selectedBrewRecipe.hopCartridges].setHidden(True)
            self.hopDecrease[self.selectedBrewRecipe.hopCartridges].setHidden(True)
            self.selectedBrewRecipe.hopTiming[self.selectedBrewRecipe.hopCartridges] = -1

    def increaseHop(self, index):
        if self.selectedBrewRecipe.hopTiming[index] < 60:
            self.selectedBrewRecipe.hopTiming[index] +=5
            self.hopEntry[index].setText(str(self.selectedBrewRecipe.hopTiming[index]))

    def decreaseHop(self, index):
        if self.selectedBrewRecipe.hopTiming[index] > 0:
            self.selectedBrewRecipe.hopTiming[index] -=5
            self.hopEntry[index].setText(str(self.selectedBrewRecipe.hopTiming[index]))

    def StartBrewing(self):
        ## This function should connect to Husam's brewing program
        print("I need connected to the brewing program")
        logger.info("Starting brew cycle with parameters: " + self.selectedBrewRecipe)


    def toggleLoad(self):
        pass

    def toggleSave(self):
        pass

    def quickBrew(self, index):
        ## Load a brew
        if self.QBLoadButton.isChecked():
            self.selectedBrewRecipe = self.savedBrewRecipes[index]
            logger.info("Read QuickBrew file "+str(index+1)+ ": " + self.selectedBrewRecipe)


            ## Reset text field displays
            for i in range(0,5):
                self.hopEntry[i].setText(str(self.selectedBrewRecipe.hopTiming[i]))
            self.HopCartridgeSelectEntry.setText(str(self.selectedBrewRecipe.hopCartridges))
            self.MashTempEntry.setText(str(self.selectedBrewRecipe.mashTunTemperature))
            ## Show all hop fields
            for i in range(0,5):
                self.hopEntry[i].setHidden(False)
                self.hopIncrease[i].setHidden(False)
                self.hopDecrease[i].setHidden(False)
            ## Hide irrelevant hop fields
            if self.selectedBrewRecipe.hopCartridges < 5:
                for i in range(self.selectedBrewRecipe.hopCartridges, 5):
                    self.hopEntry[i].setHidden(True)
                    self.hopIncrease[i].setHidden(True)
                    self.hopDecrease[i].setHidden(True)
        ## Save a brew
        if self.QBSaveButton.isChecked():
            ## Open or create file in writing mode
            #self.qbFile = open('src\GUI\QuickBrewSaves\QuickBrew%d.txt'%(index,), 'w')
            ## Logging
            #logger.info("Saved QuickBrew file "+str(index+1))
            #logger.info("Brew parameters saved: ""MTT:"+str(self.selectedBrewRecipe.mashTunTemperature)+" HC:"+str(self.HopCartridges)+" HT:"+str(self.selectedBrewRecipe.hopTiming))

            self.pickler.saveRecipes(self.savedBrewRecipes)

            ## Close the file
            #self.qbFile.close()
