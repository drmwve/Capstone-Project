from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from ..BrewRecipe import BrewRecipe, BrewRecipePickler
from .BrewConfigGUI import Ui_BrewConfigWindow
from functools import partial


class BrewConfig(QtWidgets.QWidget, Ui_BrewConfigWindow):
    """The configuration screen from which the user sets the desired brew parameters and starts the brew process. Brew recipes
    can be saved and loaded from the file system. When a brew is started, this screen is replaced by a 'Brew Progress' screen that
    gives feedback to the user on what the brew system is doing."""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.hopEntry = [
            self.Hop1Entry,
            self.Hop2Entry,
            self.Hop3Entry,
            self.Hop4Entry,
            self.Hop5Entry,
        ]
        self.hopIncrease = [
            self.Hop1Increase,
            self.Hop2Increase,
            self.Hop3Increase,
            self.Hop4Increase,
            self.Hop5Increase,
        ]
        self.hopDecrease = [
            self.Hop1Decrease,
            self.Hop2Decrease,
            self.Hop3Decrease,
            self.Hop4Decrease,
            self.Hop5Decrease,
        ]

        self.changeUI()
        self.initializeRecipe()
        self.connections()

    def initializeRecipe(self):
        """Creates the brew recipe pickler, loads the saved recipes, and selects the default brew recipe"""
        self.pickler = BrewRecipePickler()
        self.savedBrewRecipes = self.pickler.loadRecipes()
        logger.debug("Loaded recipes %s" % self.savedBrewRecipes)
        self.QBComboBox.addItems([x.name for x in self.savedBrewRecipes.values()])
        self.changeSelectedRecipe("Default")

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

        self.QBSaveButton.clicked.connect(
            lambda: self.saveRecipe(self.QBComboBox.currentText())
        )
        self.QBDeleteButton.clicked.connect(
            lambda: self.deleteRecipe(self.QBComboBox.currentText())
        )
        self.QBNewButton.clicked.connect(self.enterNewRecipe)
        self.QBComboBox.currentTextChanged.connect(self.changeSelectedRecipe)

    ## Defining button functions
    def IncreaseMashTemp(self):
        self.selectedBrewRecipe.mashTunTemperature += 1
        self.MashTempEntry.setText(str(self.selectedBrewRecipe.mashTunTemperature))

    def DecreaseMashTemp(self):
        self.selectedBrewRecipe.mashTunTemperature -= 1
        self.MashTempEntry.setText(str(self.selectedBrewRecipe.mashTunTemperature))

    def IncreaseCartridgeSelect(self):
        """Increases the number of hop cartridges used in the brew recipe and shows the hop timing UI for the new hop cartridge"""

        if self.selectedBrewRecipe.hopCartridges < 5:
            self.selectedBrewRecipe.hopCartridges += 1
            self.HopCartridgeSelectEntry.setText(
                str(self.selectedBrewRecipe.hopCartridges)
            )
            self.hopEntry[self.selectedBrewRecipe.hopCartridges - 1].setHidden(False)
            self.hopIncrease[self.selectedBrewRecipe.hopCartridges - 1].setHidden(False)
            self.hopDecrease[self.selectedBrewRecipe.hopCartridges - 1].setHidden(False)
            self.selectedBrewRecipe.hopTiming[
                self.selectedBrewRecipe.hopCartridges - 1
            ] = 0
            self.hopEntry[self.selectedBrewRecipe.hopCartridges - 1].setText("0")

    def DecreaseCartridgeSelect(self):
        """Decreases the number of hop cartridges used in the brew recipe and hides the hop timing UI for the unused hop cartridge"""

        if self.selectedBrewRecipe.hopCartridges > 1:
            self.selectedBrewRecipe.hopCartridges -= 1
            self.HopCartridgeSelectEntry.setText(
                str(self.selectedBrewRecipe.hopCartridges)
            )
            self.hopEntry[self.selectedBrewRecipe.hopCartridges].setHidden(True)
            self.hopIncrease[self.selectedBrewRecipe.hopCartridges].setHidden(True)
            self.hopDecrease[self.selectedBrewRecipe.hopCartridges].setHidden(True)
            self.selectedBrewRecipe.hopTiming[
                self.selectedBrewRecipe.hopCartridges
            ] = -1

    def increaseHop(self, index: int):
        """Increases the time to release the relevant hop cartridge

        Args:
            index (int): The hop catridge to adjust the release timing for"""

        if self.selectedBrewRecipe.hopTiming[index] < 60:
            self.selectedBrewRecipe.hopTiming[index] += 5
            self.hopEntry[index].setText(str(self.selectedBrewRecipe.hopTiming[index]))

    def decreaseHop(self, index: int):
        """Decreases the time to release the relevant hop cartridge

        Args:
            index (int): The hop catridge to adjust the release timing for"""

        if self.selectedBrewRecipe.hopTiming[index] > 0:
            self.selectedBrewRecipe.hopTiming[index] -= 5
            self.hopEntry[index].setText(str(self.selectedBrewRecipe.hopTiming[index]))

    def StartBrewing(self):
        ## This function should connect to Husam's brewing program
        self.copyRecipeFromUI(self.selectedBrewRecipe)
        print("I need connected to the brewing program")
        logger.info(f"Starting brew cycle with parameters: {self.selectedBrewRecipe}")

    def saveRecipe(self, recipeName: str):
        """Copies the recipe specified in the UI fields and saves all recipes to disk

        Args:
            recipeName (str): The name of the recipe to be saved. This must exist in the saved recipes dictionary."""

        logger.debug(
            f"Saving recipe, currently selected recipe is: {self.selectedBrewRecipe}"
        )
        logger.info(f"Saving recipe {recipeName}")
        self.copyRecipeFromUI(self.savedBrewRecipes[recipeName])
        self.pickler.saveRecipes(self.savedBrewRecipes)

    def enterNewRecipe(self):
        """Opens a dialog box to enter the name of a new recipe"""

        text, ok = QtWidgets.QInputDialog.getText(
            self, "Enter a new recipe name", "Recipe name:"
        )
        if ok and text:
            self.addNewRecipe(text)

    def addNewRecipe(self, recipeName: str):
        """Adds a blank new recipe with the given name and opens it in the UI

        Args:
            recipeName (str): The name of the recipe to be added to the recipe dictionary"""

        logger.info(f"Adding new recipe: {recipeName}")
        self.savedBrewRecipes[recipeName] = BrewRecipe(recipeName)
        self.selectedBrewRecipe = self.savedBrewRecipes[recipeName]
        self.QBComboBox.addItem(recipeName)
        self.QBComboBox.setCurrentText(recipeName)

    def deleteRecipe(self, recipeName: str):
        """Deletes a recipe from the recipe list and saves the dictionary

        Args:
            recipeName (str): The name of the recipe to be deleted from the dictionary"""

        box = self.QBComboBox
        logger.info(f"Deleting recipe: {recipeName}")
        self.savedBrewRecipes.pop(recipeName, "")
        self.pickler.saveRecipes(self.savedBrewRecipes)

        # change selected recipe is called by this statement because of the signal connection
        box.removeItem(box.currentIndex())

    def changeSelectedRecipe(self, recipeName: str):
        """Switches the UI to a new recipe - this is called when the recipe combo box changes

        Args:
            recipeName (str): The name of the recipe to be switched to in the recipies dictionary"""

        logger.debug(f"Requested change to recipe {recipeName}")
        self.selectedBrewRecipe = self.savedBrewRecipes[recipeName]
        self.loadRecipeToUI(self.selectedBrewRecipe)
        logger.info(f"Changed to recipe: {self.selectedBrewRecipe}")
        if recipeName == "Default":
            self.QBDeleteButton.setEnabled(False)
        else:
            self.QBDeleteButton.setEnabled(True)

    def copyRecipeFromUI(self, recipe: BrewRecipe):
        """Copies the recipe specified in the UI to the given brew recipe object

        Args:
            recipe (BrewRecipe): The recipe object which the UI element values are copied to"""

        recipe.name = self.QBComboBox.currentText()
        recipe.mashTunTemperature = int(self.MashTempEntry.text())
        recipe.hopCartridges = int(self.HopCartridgeSelectEntry.text())
        for i in range(0, 5):
            recipe.hopTiming[i] = int(self.hopEntry[i].text())
        logger.debug(f"Copied recipe from UI: {recipe} ")

    def loadRecipeToUI(self, recipe: BrewRecipe):
        """Loads the given recipe object to the UI

        Args:
            recipe (BrewRecipe): The recipe object to be copied into the UI elements"""

        logger.debug(f"Loading recipe to UI: {recipe}")
        ## Reset text field displays
        for i in range(0, 5):
            self.hopEntry[i].setText(str(recipe.hopTiming[i]))
            if recipe.hopTiming[i] == -1:
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