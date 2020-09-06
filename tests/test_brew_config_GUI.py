from autobrewer.GUI.BrewConfig import BrewConfig
from autobrewer.BrewRecipe import BrewRecipe, BrewRecipePickler
import pytest
from loguru import logger


@pytest.fixture
def brewconfigscreen(qtbot):
    brewConfigWindow = BrewConfig()
    qtbot.addWidget(brewConfigWindow)
    return brewConfigWindow


@pytest.fixture
def savedrecipesdict():
    data = {
        "Default": BrewRecipe("Default", 5, 190, [1, 2, 3, 4, 5]),
        "test2": BrewRecipe("test2", 3, 122, [1, 2, 3, -1, -1]),
        "test3": BrewRecipe("test3", 1, 134, [1, -1, -1, -1, -1]),
    }
    return data


class TestBrewConfig:
    def test_initialize_recipe(self, brewconfigscreen):
        pickler = BrewRecipePickler()
        loaded_brew_recipes = brewconfigscreen.savedBrewRecipes == pickler.loadRecipes()
        assert loaded_brew_recipes

    @pytest.mark.parametrize(
        "testName", ["Default", "test2", "test3"],
    )
    def test_delete_recipe(self, savedrecipesdict, testName, brewconfigscreen):
        brewconfigscreen.savedBrewRecipes = savedrecipesdict
        brewconfigscreen.deleteRecipe(testName)


    @pytest.mark.parametrize(
        "testName", ["Default", "test2", "test3"],
    )
    def test_change_selected_recipe(self, savedrecipesdict, testName, brewconfigscreen):
        brewconfigscreen.savedBrewRecipes = savedrecipesdict
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
class TestLoadRecipeToUI:
    def test_hop_cartridges(self, testrecipe, brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        assert (
            int(brewconfigscreen.HopCartridgeSelectEntry.text())
            == testrecipe.hopCartridges
        )

    def test_mash_temp(self, testrecipe, brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        assert (
            int(brewconfigscreen.MashTempEntry.text()) == testrecipe.mashTunTemperature
        )

    def test_hop_entry_value(self, testrecipe, brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        for i in range(0, 5):
            assert int(brewconfigscreen.hopEntry[i].text()) == testrecipe.hopTiming[i]

    def test_hop_entry_hidden(self, testrecipe, brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        expected = [
            (testrecipe.hopTiming[i] == -1) for i in range(len(testrecipe.hopTiming))
        ]
        actual = [
            brewconfigscreen.hopEntry[i].isHidden()
            for i in range(len(brewconfigscreen.hopEntry))
        ]
        assert expected == actual

    def test_hop_increase_hidden(self, testrecipe, brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        expected = [
            (testrecipe.hopTiming[i] == -1) for i in range(len(testrecipe.hopTiming))
        ]
        actual = [
            brewconfigscreen.hopIncrease[i].isHidden()
            for i in range(len(brewconfigscreen.hopIncrease))
        ]
        assert expected == actual

    def test_hop_decrease_hidden(self, testrecipe, brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        expected = [
            (testrecipe.hopTiming[i] == -1) for i in range(len(testrecipe.hopTiming))
        ]
        actual = [
            brewconfigscreen.hopDecrease[i].isHidden()
            for i in range(len(brewconfigscreen.hopDecrease))
        ]
        assert expected == actual