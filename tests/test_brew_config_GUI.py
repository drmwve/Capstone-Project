import pytest
from PySide2 import QtCore
from PySide2.QtWidgets import QInputDialog
from loguru import logger

from autobrewer.BrewRecipe import BrewRecipe, BrewRecipePickler
from autobrewer.GUI.BrewConfig import BrewConfig


@pytest.fixture
def defaultbrewconfigscreen(qtbot):
    brewconfig = BrewConfig()
    qtbot.addWidget(brewconfig)
    return brewconfig


recipesdict = {
    "Default": BrewRecipe("Default", 5, 190, [1, 2, 3, 4, 5]),
    "test2": BrewRecipe("test2", 3, 122, [1, 2, 3, -1, -1]),
    "test3": BrewRecipe("test3", 1, 134, [1, -1, -1, -1, -1]),
}


@pytest.fixture
def savedrecipesdict():
    return recipesdict.copy()


@pytest.fixture
def testbrewconfigscreen(qtbot, defaultbrewconfigscreen, savedrecipesdict):
    # clear selection combo box and add dict recipes
    defaultbrewconfigscreen.savedBrewRecipes = savedrecipesdict
    defaultbrewconfigscreen.QBComboBox.blockSignals(True)
    defaultbrewconfigscreen.QBComboBox.clear()
    defaultbrewconfigscreen.QBComboBox.blockSignals(False)
    defaultbrewconfigscreen.QBComboBox.addItems(
        [x.name for x in savedrecipesdict.values()]
    )
    return defaultbrewconfigscreen


class TestBrewConfig:
    def test_initialize(self, defaultbrewconfigscreen):
        pickler = BrewRecipePickler()
        loaded_brew_recipes = (
            defaultbrewconfigscreen.savedBrewRecipes == pickler.loadRecipes()
        )
        assert loaded_brew_recipes

    @pytest.mark.parametrize("numclicks", [1, 4, 200])
    def test_increaseMashTemp(self, qtbot, testbrewconfigscreen, numclicks):
        expected = (
            int(testbrewconfigscreen.MashTempEntry.text())
            + BrewConfig.MASH_TEMPERATURE_INCREMENT * numclicks
        )
        if expected > BrewConfig.MASH_TEMPERATURE_MAXIMUM:
            expected = BrewConfig.MASH_TEMPERATURE_MAXIMUM
        for clicks in range(numclicks):
            with qtbot.waitSignal(
                testbrewconfigscreen.MashTempIncrease.clicked, timeout=10
            ):
                qtbot.mouseClick(
                    testbrewconfigscreen.MashTempIncrease, QtCore.Qt.LeftButton
                )
        assert int(testbrewconfigscreen.MashTempEntry.text()) == expected

    @pytest.mark.parametrize("numclicks", [1, 4, 200])
    def test_decreaseMashTemp(self, qtbot, testbrewconfigscreen, numclicks):
        expected = (
            int(testbrewconfigscreen.MashTempEntry.text())
            - BrewConfig.MASH_TEMPERATURE_INCREMENT * numclicks
        )
        if expected < BrewConfig.MASH_TEMPERATURE_MINIMUM:
            expected = BrewConfig.MASH_TEMPERATURE_MINIMUM
        for clicks in range(numclicks):
            with qtbot.waitSignal(
                testbrewconfigscreen.MashTempDecrease.clicked, timeout=10
            ):
                qtbot.mouseClick(
                    testbrewconfigscreen.MashTempDecrease, QtCore.Qt.LeftButton
                )
        assert int(testbrewconfigscreen.MashTempEntry.text()) == expected

    @pytest.mark.parametrize("numclicks", [1, 4, 200])
    def test_increaseCartridgeSelect(self, qtbot, defaultbrewconfigscreen, numclicks):
        expected = (
            int(defaultbrewconfigscreen.HopCartridgeSelectEntry.text()) + numclicks
        )
        if expected > BrewConfig.HOP_CARTRIDGES_MAXIMUM:
            expected = BrewConfig.HOP_CARTRIDGES_MAXIMUM
        for clicks in range(numclicks):
            with qtbot.waitSignal(
                defaultbrewconfigscreen.HopCartridgeSelectIncrease.clicked, timeout=10
            ):
                qtbot.mouseClick(
                    defaultbrewconfigscreen.HopCartridgeSelectIncrease,
                    QtCore.Qt.LeftButton,
                )
        assert int(defaultbrewconfigscreen.HopCartridgeSelectEntry.text()) == expected
        for index in range(BrewConfig.HOP_CARTRIDGES_MAXIMUM):
            if index <= (expected - 1):
                assert defaultbrewconfigscreen.hopEntry[index].isHidden() == False
                assert defaultbrewconfigscreen.hopIncrease[index].isHidden() == False
                assert defaultbrewconfigscreen.hopDecrease[index].isHidden() == False
            else:
                assert defaultbrewconfigscreen.hopEntry[index].isHidden() == True
                assert defaultbrewconfigscreen.hopIncrease[index].isHidden() == True
                assert defaultbrewconfigscreen.hopDecrease[index].isHidden() == True
                assert int(defaultbrewconfigscreen.hopEntry[index].text()) == -1

    @pytest.mark.parametrize("numclicks", [1, 4, 200])
    def test_decreaseCartridgeSelect(self, qtbot, defaultbrewconfigscreen, numclicks):
        expected = (
            int(defaultbrewconfigscreen.HopCartridgeSelectEntry.text()) - numclicks
        )
        if expected < 1:
            expected = 1
        for clicks in range(numclicks):
            with qtbot.waitSignal(
                defaultbrewconfigscreen.HopCartridgeSelectDecrease.clicked, timeout=10
            ):
                qtbot.mouseClick(
                    defaultbrewconfigscreen.HopCartridgeSelectDecrease,
                    QtCore.Qt.LeftButton,
                )
        assert int(defaultbrewconfigscreen.HopCartridgeSelectEntry.text()) == expected
        for index in range(BrewConfig.HOP_CARTRIDGES_MAXIMUM):
            if index <= (expected - 1):
                assert defaultbrewconfigscreen.hopEntry[index].isHidden() == False
                assert defaultbrewconfigscreen.hopIncrease[index].isHidden() == False
                assert defaultbrewconfigscreen.hopDecrease[index].isHidden() == False
            else:
                assert defaultbrewconfigscreen.hopEntry[index].isHidden() == True
                assert defaultbrewconfigscreen.hopIncrease[index].isHidden() == True
                assert defaultbrewconfigscreen.hopDecrease[index].isHidden() == True
                assert int(defaultbrewconfigscreen.hopEntry[index].text()) == -1

    @pytest.mark.parametrize("numclicks", [1, 4, 200])
    @pytest.mark.parametrize("hopindex", [x for x in range(5)])
    def test_increaseHop(self, qtbot, defaultbrewconfigscreen, numclicks, hopindex):
        expected = int(defaultbrewconfigscreen.hopEntry[hopindex].text()) + (
            numclicks * BrewConfig.HOP_TIMING_INCREMENT
        )
        if expected > BrewConfig.HOP_TIMING_MAXIMUM:
            expected = BrewConfig.HOP_TIMING_MAXIMUM
        for clicks in range(numclicks):
            with qtbot.waitSignal(
                defaultbrewconfigscreen.hopIncrease[hopindex].clicked, timeout=10
            ):
                qtbot.mouseClick(
                    defaultbrewconfigscreen.hopIncrease[hopindex], QtCore.Qt.LeftButton
                )
        assert int(defaultbrewconfigscreen.hopEntry[hopindex].text()) == expected

    @pytest.mark.parametrize("numclicks", [0, 1, 4, 200])
    @pytest.mark.parametrize("hopindex", [x for x in range(5)])
    def test_decreaseHop(self, defaultbrewconfigscreen, numclicks, hopindex, qtbot):
        expected = int(defaultbrewconfigscreen.hopEntry[hopindex].text()) - (
            numclicks * BrewConfig.HOP_TIMING_INCREMENT
        )
        if expected < BrewConfig.HOP_TIMING_MINIMUM:
            expected = BrewConfig.HOP_TIMING_MINIMUM
        for clicks in range(numclicks):
            with qtbot.waitSignal(
                defaultbrewconfigscreen.hopDecrease[hopindex].clicked, timeout=10
            ):
                qtbot.mouseClick(
                    defaultbrewconfigscreen.hopDecrease[hopindex], QtCore.Qt.LeftButton
                )
        assert int(defaultbrewconfigscreen.hopEntry[hopindex].text()) == expected

    @pytest.mark.parametrize(
        "testName",
        [x for x in recipesdict],
    )
    def test_AddRecipe(self, testName, testbrewconfigscreen, qtbot, monkeypatch):
        def inputdialog(*args, **kwargs):
            return (testName, True)

        monkeypatch.setattr(QInputDialog, "getText", inputdialog)
        with qtbot.waitSignal(testbrewconfigscreen.QBNewButton.clicked, timeout=1000):
            qtbot.mouseClick(testbrewconfigscreen.QBNewButton, QtCore.Qt.LeftButton)

        assert testName in testbrewconfigscreen.savedBrewRecipes
        assert testbrewconfigscreen.selectedBrewRecipe == BrewRecipe(testName)
        assert testbrewconfigscreen.QBComboBox.findText(testName) >= 0
        assert testbrewconfigscreen.QBComboBox.currentText() == testName

    @pytest.mark.parametrize(
        "testName",
        [x for x in recipesdict],
    )
    def test_deleteRecipe(
        self, monkeypatch, qtbot, testbrewconfigscreen, savedrecipesdict, testName
    ):
        monkeypatch.setattr(
            testbrewconfigscreen.pickler, "saveRecipes", lambda *args: True
        )
        testbrewconfigscreen.QBComboBox.setCurrentText(testName)
        if testName == "Default":
            with qtbot.assert_not_emitted(
                testbrewconfigscreen.QBDeleteButton.clicked, wait=100
            ):
                qtbot.mouseClick(
                    testbrewconfigscreen.QBDeleteButton, QtCore.Qt.LeftButton
                )
        else:
            with qtbot.waitSignal(
                testbrewconfigscreen.QBDeleteButton.clicked, timeout=1000
            ):
                qtbot.mouseClick(
                    testbrewconfigscreen.QBDeleteButton, QtCore.Qt.LeftButton
                )
            assert not testName in testbrewconfigscreen.savedBrewRecipes
            assert testbrewconfigscreen.QBComboBox.findText(testName) == -1

    @pytest.mark.parametrize(
        "testName",
        [x for x in recipesdict],
    )
    def test_changeSelectedRecipe(
        self, testbrewconfigscreen, savedrecipesdict, testName
    ):
        # clear selection combo box and add dict recipes
        logger.debug(savedrecipesdict)
        logger.debug(testName)
        testbrewconfigscreen.QBComboBox.setCurrentText(testName)
        recipe = testbrewconfigscreen.copyRecipeFromUI()
        assert testbrewconfigscreen.selectedBrewRecipe == savedrecipesdict[testName]
        assert recipe.hopTiming == savedrecipesdict[testName].hopTiming
        assert (
            recipe.mashTunTemperature == savedrecipesdict[testName].mashTunTemperature
        )
        if testName == "Default":
            assert not testbrewconfigscreen.QBDeleteButton.isEnabled()
        else:
            assert testbrewconfigscreen.QBDeleteButton.isEnabled()

    @pytest.mark.parametrize("testrecipe", [x for x in recipesdict.values()])
    def test_copyRecipeFromUI(self, testbrewconfigscreen, testrecipe):
        testbrewconfigscreen.QBComboBox.blockSignals(True)
        testbrewconfigscreen.QBComboBox.setItemText(
            testbrewconfigscreen.QBComboBox.currentIndex(), testrecipe.name
        )
        testbrewconfigscreen.MashTempEntry.setText(str(testrecipe.mashTunTemperature))
        testbrewconfigscreen.HopCartridgeSelectEntry.setText(
            str(testrecipe.hopCartridges)
        )
        for i in range(len(testrecipe.hopTiming)):
            testbrewconfigscreen.hopEntry[i].setText(str(testrecipe.hopTiming[i]))
        recipe = testbrewconfigscreen.copyRecipeFromUI()
        assert recipe == testrecipe

    @pytest.mark.parametrize("testrecipe", [x for x in recipesdict.values()])
    def test_loadRecipeToUI(self, testrecipe, testbrewconfigscreen):
        testbrewconfigscreen.loadRecipeToUI(testrecipe)
        assert (
            int(testbrewconfigscreen.HopCartridgeSelectEntry.text())
            == testrecipe.hopCartridges
        )
        assert (
            int(testbrewconfigscreen.MashTempEntry.text())
            == testrecipe.mashTunTemperature
        )

        for i in range(0, 5):
            assert (
                int(testbrewconfigscreen.hopEntry[i].text()) == testrecipe.hopTiming[i]
            )

        expectedHiddenHopRows = [
            (testrecipe.hopTiming[i] == -1) for i in range(len(testrecipe.hopTiming))
        ]
        actualHiddenHopEntries = [
            testbrewconfigscreen.hopEntry[i].isHidden()
            for i in range(len(testbrewconfigscreen.hopEntry))
        ]
        assert expectedHiddenHopRows == actualHiddenHopEntries

        actualHiddenHopIncreases = [
            testbrewconfigscreen.hopIncrease[i].isHidden()
            for i in range(len(testbrewconfigscreen.hopIncrease))
        ]
        assert expectedHiddenHopRows == actualHiddenHopIncreases

        actualHiddenHopDecreases = [
            testbrewconfigscreen.hopDecrease[i].isHidden()
            for i in range(len(testbrewconfigscreen.hopDecrease))
        ]
        assert expectedHiddenHopRows == actualHiddenHopDecreases
