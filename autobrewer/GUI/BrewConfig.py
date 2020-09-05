from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from BrewRecipe import BrewRecipe, BrewRecipePickler
from GUI.BrewConfigGUI import Ui_BrewConfigWindow
from functools import partial

class BrewConfig(QtWidgets.QWidget, Ui_BrewConfigWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hopEntry = [self.Hop1Entry, self.Hop2Entry, self.Hop3Entry, self.Hop4Entry, self.Hop5Entry]
        self.hopIncrease = [self.Hop1Increase, self.Hop2Increase, self.Hop3Increase, self.Hop4Increase, self.Hop5Increase]
        self.hopDecrease = [self.Hop1Decrease, self.Hop2Decrease, self.Hop3Decrease, self.Hop4Decrease, self.Hop5Decrease]

        self.changeUI()
        self.initializeRecipe()
        self.connections()

    def initializeRecipe(self):
        self.pickler = BrewRecipePickler()
        self.savedBrewRecipes = self.pickler.loadRecipes()
        logger.debug("Loaded recipes %s" % self.savedBrewRecipes)
        self.selectedBrewRecipe = self.savedBrewRecipes["Default"]
        self.QBDeleteButton.setEnabled(False)
        self.QBComboBox.addItems([x.name for x in self.savedBrewRecipes.values()])
        self.loadRecipeToUI(self.selectedBrewRecipe)

    def changeUI(self):
        self.QBNewButton = self.QBLoadButton
        self.QBNewButton.setText("New Quick Brew")

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

        self.QBSaveButton.clicked.connect(lambda: self.saveRecipe(self.selectedBrewRecipe))
        self.QBDeleteButton.clicked.connect(lambda: self.deleteRecipe(self.selectedBrewRecipe))
        self.QBNewButton.clicked.connect(self.addNewRecipe)
        self.QBComboBox.currentTextChanged.connect(self.changeSelectedRecipe)

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
        self.saveRecipeFromUI(self.selectedBrewRecipe)
        print("I need connected to the brewing program")
        logger.info(f'Starting brew cycle with parameters: {self.selectedBrewRecipe}')

    def saveRecipe(self, recipe):
        logger.debug(f'Saving recipe, currently selected recipe is: {self.selectedBrewRecipe}')
        logger.info(f'Saving recipe {recipe}')
        self.saveRecipeFromUI(recipe)
        self.pickler.saveRecipes(self.savedBrewRecipes)

    def addNewRecipe(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "Enter a new recipe name","Recipe name:")
        if ok and text:
            logger.info(f'Adding new recipe: {text}')
            self.savedBrewRecipes[text] = BrewRecipe(text)
            self.selectedBrewRecipe = self.savedBrewRecipes[text]
            self.QBComboBox.addItem(text)
            self.QBComboBox.setCurrentText(text)
            self.loadRecipeToUI(self.selectedBrewRecipe)

    def deleteRecipe(self, recipe):
        box = self.QBComboBox
        logger.info(f'Deleting recipe: {recipe}')
        self.savedBrewRecipes.pop(recipe.name,"")
        self.pickler.saveRecipes(self.savedBrewRecipes)
        box.removeItem(box.currentIndex())
        self.selectedBrewRecipe = self.savedBrewRecipes[box.currentText()]
        self.loadRecipeToUI(self.selectedBrewRecipe)

    def changeSelectedRecipe(self, newRecipeName):
        logger.debug(f'Requested change to recipe {newRecipeName}')
        self.selectedBrewRecipe = self.savedBrewRecipes[newRecipeName]
        self.loadRecipeToUI(self.selectedBrewRecipe)
        logger.info(f'Changed to recipe: {self.selectedBrewRecipe}')
        if (newRecipeName == "Default"):
            self.QBDeleteButton.setEnabled(False)
        else:
            self.QBDeleteButton.setEnabled(True)

    def saveRecipeFromUI(self, recipe):
        recipe.name = self.QBComboBox.currentText()
        recipe.mashTunTemperature = int(self.MashTempEntry.text())
        recipe.hopCartridges = int(self.HopCartridgeSelectEntry.text())
        for i in range(0, 5):
            recipe.hopTiming[i] = int(self.hopEntry[i].text())
        logger.debug(f'Loaded recipe from UI: {recipe} ')

    def loadRecipeToUI(self, recipe):
        logger.debug(f'Loading recipe to UI: {recipe}')
        ## Reset text field displays
        for i in range(0,5):
            self.hopEntry[i].setText(str(recipe.hopTiming[i]))
            if (self.selectedBrewRecipe.hopTiming[i] == -1):
                self.hopEntry[i].setHidden(True)
                self.hopIncrease[i].setHidden(True)
                self.hopDecrease[i].setHidden(True)
                self.hopEntry[i].setText("-1")
            else:
                self.hopEntry[i].setHidden(False)
                self.hopIncrease[i].setHidden(False)
                self.hopDecrease[i].setHidden(False)

        self.HopCartridgeSelectEntry.setText(str(recipe.hopCartridges))
        self.MashTempEntry.setText(str(recipe.mashTunTemperature))