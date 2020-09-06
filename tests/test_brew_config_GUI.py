from autobrewer.GUI.BrewConfig import BrewConfig
from autobrewer.BrewRecipe import BrewRecipe, BrewRecipePickler
import pytest
from loguru import logger

@pytest.fixture
def savedrecipesdict():
    data = {
        "Default": BrewRecipe("Default", 5, 190, [1, 2, 3, 4, 5]),
        "test2": BrewRecipe("test2", 3, 122, [1, 2, 3, -1, -1]),
        "test3": BrewRecipe("test3", 1, 134, [1, -1, -1, -1, -1]),
    }
    return data

@pytest.fixture
def brewconfigscreen(qtbot,savedrecipesdict):
    brewConfigWindow = BrewConfig()
    qtbot.addWidget(brewConfigWindow)
    #clear selection combo box and add dict recipes
    brewConfigWindow.QBComboBox.blockSignals(True)
    brewConfigWindow.QBComboBox.clear()
    brewConfigWindow.QBComboBox.addItems([x.name for x in savedrecipesdict.values()])
    brewConfigWindow.QBComboBox.blockSignals(False)
    return brewConfigWindow

class TestBrewConfig:
    def test_initialize_recipe(self, brewconfigscreen):
        pickler = BrewRecipePickler()
        loaded_brew_recipes = brewconfigscreen.savedBrewRecipes == pickler.loadRecipes()
        assert loaded_brew_recipes

    @pytest.mark.parametrize(
        "testrecipe",
        [
            BrewRecipe("test", 5, 190, [1, 2, 3, 4, 5]),
            BrewRecipe("test", 3, 122, [1, 2, 3, -1, -1]),
            BrewRecipe("test", 1, 134, [1, -1, -1, -1, -1]),
        ],
    )
    def test_add_new_recipe(self, testName, brewconfigscreen):
        brewconfigscreen.addNewRecipe(testName)
        assert testName in brewconfigscreen.savedBrewRecipes
        assert brewconfigscreen.selectedBrewRecipe == BrewRecipe(testName)
        assert brewconfigscreen.QBComboBox.findText(testName) >= 0
        assert brewconfigscreen.QBComboBox.currentText() == testName

    @pytest.mark.parametrize(
        "testName", ["test2", "test3"],
    )
    def test_delete_recipe(self, savedrecipesdict, testName, brewconfigscreen, monkeypatch):
        monkeypatch.setattr(brewconfigscreen.pickler, "saveRecipes", lambda *args: True)

        brewconfigscreen.QBComboBox.blockSignals(True)
        brewconfigscreen.QBComboBox.setCurrentText(testName)
        brewconfigscreen.QBComboBox.blockSignals(False)
        brewconfigscreen.savedBrewRecipes = savedrecipesdict

        brewconfigscreen.deleteRecipe(testName)
        assert not testName in brewconfigscreen.savedBrewRecipes
        assert brewconfigscreen.QBComboBox.findText(testName) == -1

    @pytest.mark.parametrize(
        "testName", ["Default", "test2", "test3"],
    )
    def test_change_selected_recipe(self, savedrecipesdict, testName, brewconfigscreen):
        brewconfigscreen.savedBrewRecipes = savedrecipesdict
        #clear selection combo box and add dict recipes
        brewconfigscreen.QBComboBox.blockSignals(True)
        brewconfigscreen.QBComboBox.setCurrentText(testName)
        brewconfigscreen.QBComboBox.blockSignals(False)

        brewconfigscreen.changeSelectedRecipe(testName)
        recipe = BrewRecipe()
        brewconfigscreen.saveRecipeFromUI(recipe)
        assert brewconfigscreen.selectedBrewRecipe == savedrecipesdict[testName]
        assert recipe.hopTiming == savedrecipesdict[testName].hopTiming
        assert recipe.mashTunTemperature == savedrecipesdict[testName].mashTunTemperature
        if (testName == "Default"):
            assert not brewconfigscreen.QBDeleteButton.isEnabled()
        else:
            assert brewconfigscreen.QBDeleteButton.isEnabled()

    @pytest.mark.parametrize(
        "testrecipe",
        [
            BrewRecipe("test", 5, 190, [1, 2, 3, 4, 5]),
            BrewRecipe("test", 3, 122, [1, 2, 3, -1, -1]),
            BrewRecipe("test", 1, 134, [1, -1, -1, -1, -1]),
        ],
    )
    def test_save_recipe_from_ui(self, testrecipe, brewconfigscreen):
        brewconfigscreen.QBComboBox.blockSignals(True)
        brewconfigscreen.QBComboBox.setItemText(
            brewconfigscreen.QBComboBox.currentIndex(), testrecipe.name
        )
        brewconfigscreen.MashTempEntry.setText(str(testrecipe.mashTunTemperature))
        brewconfigscreen.HopCartridgeSelectEntry.setText(str(testrecipe.hopCartridges))
        for i in range(len(testrecipe.hopTiming)):
            brewconfigscreen.hopEntry[i].setText(str(testrecipe.hopTiming[i]))
        recipe = BrewRecipe()
        brewconfigscreen.saveRecipeFromUI(recipe)
        assert recipe == testrecipe


    @pytest.mark.parametrize(
        "testrecipe",
        [
            BrewRecipe("test", 5, 190, [1, 2, 3, 4, 5]),
            BrewRecipe("test", 3, 122, [1, 2, 3, -1, -1]),
            BrewRecipe("test", 1, 134, [1, -1, -1, -1, -1]),
        ],
    )
    def test_load_recipe_to_ui(self, testrecipe, brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        assert (
            int(brewconfigscreen.HopCartridgeSelectEntry.text())
            == testrecipe.hopCartridges
        )
        assert (
            int(brewconfigscreen.MashTempEntry.text()) == testrecipe.mashTunTemperature
        )

        for i in range(0, 5):
            assert int(brewconfigscreen.hopEntry[i].text()) == testrecipe.hopTiming[i]

        expectedHiddenHopRows = [
            (testrecipe.hopTiming[i] == -1) for i in range(len(testrecipe.hopTiming))
        ]
        actualHiddenHopEntries = [
            brewconfigscreen.hopEntry[i].isHidden()
            for i in range(len(brewconfigscreen.hopEntry))
        ]
        assert expectedHiddenHopRows == actualHiddenHopEntries

        actualHiddenHopIncreases = [
            brewconfigscreen.hopIncrease[i].isHidden()
            for i in range(len(brewconfigscreen.hopIncrease))
        ]
        assert expectedHiddenHopRows == actualHiddenHopIncreases

        actualHiddenHopDecreases = [
            brewconfigscreen.hopDecrease[i].isHidden()
            for i in range(len(brewconfigscreen.hopDecrease))
        ]
        assert expectedHiddenHopRows == actualHiddenHopDecreases