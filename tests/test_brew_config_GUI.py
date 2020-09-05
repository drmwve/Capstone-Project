from autobrewer.GUI.BrewConfig import BrewConfig
from autobrewer.BrewRecipe import BrewRecipe, BrewRecipePickler
import pytest

@pytest.fixture
def brewconfigscreen(qtbot):
    brewConfigWindow = BrewConfig()
    qtbot.addWidget(brewConfigWindow)
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
class TestLoadRecipeToUI:

    def test_hop_cartridges(self, testrecipe, brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        assert (
            int(brewconfigscreen.HopCartridgeSelectEntry.text())
            == testrecipe.hopCartridges
        )

    def test_mash_temp(self,testrecipe,brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        assert (
            int(brewconfigscreen.MashTempEntry.text()) == testrecipe.mashTunTemperature
        )

    def test_hop_entry_value(self,testrecipe,brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        for i in range(0, 5):
            assert int(brewconfigscreen.hopEntry[i].text()) == testrecipe.hopTiming[i]

    def test_hop_entry_hidden(self,testrecipe,brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        for i in range(0, 5):
            if testrecipe.hopTiming[i] == -1:
                assert brewconfigscreen.hopEntry[i].isHidden() == True
            else:
                assert brewconfigscreen.hopEntry[i].isHidden() == False

    def test_hop_increase_hidden(self,testrecipe,brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        for i in range(0, 5):
            if testrecipe.hopTiming[i] == -1:
                assert brewconfigscreen.hopIncrease[i].isHidden() == True
            else:
                assert brewconfigscreen.hopIncrease[i].isHidden() == False

    def test_hop_decrease_hidden(self,testrecipe,brewconfigscreen):
        brewconfigscreen.loadRecipeToUI(testrecipe)
        for i in range(0, 5):
            if testrecipe.hopTiming[i] == -1:
                assert brewconfigscreen.hopDecrease[i].isHidden() == True
            else:
                assert brewconfigscreen.hopDecrease[i].isHidden() == False
