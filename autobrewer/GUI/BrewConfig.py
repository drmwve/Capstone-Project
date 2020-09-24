from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from ..BrewRecipe import BrewRecipe, BrewRecipePickler
from .BrewConfigGUI import Ui_BrewConfigWindow
from functools import partial


class BrewConfig(QtWidgets.QWidget, Ui_BrewConfigWindow):
    """The configuration screen from which the user sets the desired brew parameters and starts the brew process. Brew recipes
    can be saved and loaded from the file system. When a brew is started, this screen is replaced by a 'Brew Progress' screen that
    gives feedback to the user on what the brew system is doing."""

    HOP_TIMING_INCREMENT = 5
    HOP_TIMING_MINIMUM = 0
    HOP_TIMING_MAXIMUM = 60
    HOP_CARTRIDGES_MAXIMUM = 5

    MASH_TEMPERATURE_INCREMENT = 1
    MASH_TEMPERATURE_MAXIMUM = 180
    MASH_TEMPERATURE_MINIMUM = 140

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
        newtemp = int(self.MashTempEntry.text()) + 1
        if newtemp > BrewConfig.MASH_TEMPERATURE_MAXIMUM:
            newtemp = BrewConfig.MASH_TEMPERATURE_MAXIMUM
            logger.debug(
                f"Cannot increase mash temperature above maximum {BrewConfig.MASH_TEMPERATURE_MAXIMUM}"
            )
        else:
            logger.debug(
                f"Increased {self.selectedBrewRecipe.name} mash temperature to {newtemp}"
            )
        self.MashTempEntry.setText(str(newtemp))

    def DecreaseMashTemp(self):
        newtemp = int(self.MashTempEntry.text()) - BrewConfig.MASH_TEMPERATURE_INCREMENT
        if newtemp < BrewConfig.MASH_TEMPERATURE_MINIMUM:
            newtemp = BrewConfig.MASH_TEMPERATURE_MINIMUM
            logger.debug(
                f"Cannot decrease mash temperature below maximum {BrewConfig.MASH_TEMPERATURE_MAXIMUM}"
            )
        else:
            logger.debug(
                f"Decreased {self.selectedBrewRecipe.name} mash temperature to {newtemp}"
            )
        self.MashTempEntry.setText(str(newtemp))

    def IncreaseCartridgeSelect(self):
        hopcarts = int(self.HopCartridgeSelectEntry.text())
        if hopcarts < BrewConfig.HOP_CARTRIDGES_MAXIMUM:
            logger.debug(
                f"Increasing {self.selectedBrewRecipe.name} hop cartridges from {hopcarts} to {hopcarts + 1}"
            )
            hopcarts += 1
            self.HopCartridgeSelectEntry.setText(str(hopcarts))
            self.hopEntry[hopcarts - 1].setHidden(False)
            self.hopIncrease[hopcarts - 1].setHidden(False)
            self.hopDecrease[hopcarts - 1].setHidden(False)
            self.hopEntry[hopcarts - 1].setText(
                str(BrewRecipe().hopTiming[hopcarts - 1])
            )
        else:
            logger.debug(
                f"Could not increase {self.selectedBrewRecipe.name} hop cartidges above maximum {BrewConfig.HOP_CARTRIDGES_MAXIMUM}"
            )

    def DecreaseCartridgeSelect(self):
        hopcarts = int(self.HopCartridgeSelectEntry.text())
        if hopcarts > 1:
            logger.debug(
                f"Decreasing {self.selectedBrewRecipe.name} hop cartridges from {hopcarts} to {hopcarts - 1}"
            )
            hopcarts -= 1
            self.HopCartridgeSelectEntry.setText(str(hopcarts))
            self.hopEntry[hopcarts].setHidden(True)
            self.hopIncrease[hopcarts].setHidden(True)
            self.hopDecrease[hopcarts].setHidden(True)
            self.hopEntry[hopcarts].setText("-1")
        else:
            logger.debug(
                f"Could not decrease {self.selectedBrewRecipe.name} hop cartridges below minimum 1"
            )

    def increaseHop(self, index):
        hoptiming = int(self.hopEntry[index].text())
        hoptiming += BrewConfig.HOP_TIMING_INCREMENT
        if hoptiming > BrewConfig.HOP_TIMING_MAXIMUM:
            hoptiming = BrewConfig.HOP_TIMING_MAXIMUM
            logger.debug(
                f"Could not increase {self.selectedBrewRecipe.name} hop timing {index + 1} above maximum {BrewConfig.HOP_TIMING_MAXIMUM}"
            )
        else:
            logger.debug(
                f"Increased {self.selectedBrewRecipe.name} hop timing {index+1} to {hoptiming}"
            )
        self.hopEntry[index].setText(str(hoptiming))

    def decreaseHop(self, index):
        hoptiming = int(self.hopEntry[index].text())
        hoptiming -= BrewConfig.HOP_TIMING_INCREMENT
        if hoptiming < BrewConfig.HOP_TIMING_MINIMUM:
            hoptiming = BrewConfig.HOP_TIMING_MINIMUM
            logger.debug(
                f"Could not decrease {self.selectedBrewRecipe.name} hop timing {index + 1} below minimum {BrewConfig.HOP_TIMING_MINIMUM}"
            )
        else:
            logger.debug(
                f"Decreased {self.selectedBrewRecipe.name} hop timing {index+1} to {hoptiming}"
            )
        self.hopEntry[index].setText(str(hoptiming))

    def StartBrewing(self):
        ## This function should connect to Husam's brewing program
        self.selectedBrewRecipe = self.copyRecipeFromUI()
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
        self.savedBrewRecipes[recipeName] = self.copyRecipeFromUI()
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

        self.selectedBrewRecipe = self.savedBrewRecipes[recipeName]
        self.loadRecipeToUI(self.selectedBrewRecipe)
        logger.info(f"Changed to recipe: {self.selectedBrewRecipe}")
        if recipeName == "Default":
            self.QBDeleteButton.setEnabled(False)
        else:
            self.QBDeleteButton.setEnabled(True)

    def copyRecipeFromUI(self) -> BrewRecipe:
        """Copies the recipe specified in the UI to the given brew recipe object

        Returns:
            recipe (BrewRecipe): The recipe object which the UI element values are copied to"""

        recipe = BrewRecipe()
        recipe.name = self.QBComboBox.currentText()
        recipe.mashTunTemperature = int(self.MashTempEntry.text())
        recipe.hopCartridges = int(self.HopCartridgeSelectEntry.text())
        for i in range(0, 5):
            recipe.hopTiming[i] = int(self.hopEntry[i].text())
        logger.debug(f"Copied recipe from UI: {recipe} ")
        return recipe

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
