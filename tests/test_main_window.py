import pytest
from PySide2 import QtCore, QtWidgets

from autobrewer.MainWindow import MainWindow
from autobrewer.utils import IS_RASPBERRY_PI

@pytest.fixture
def mainwindow(qtbot, monkeypatch):
    mainwindow = MainWindow()
    monkeypatch.setitem(mainwindow.menus, "test", QtWidgets.QWidget())
    mainwindow.centralWidget().addWidget(mainwindow.menus["test"])
    mainwindow.centralWidget().setCurrentWidget(mainwindow.menus["test"])
    qtbot.addWidget(mainwindow)
    return  mainwindow

def test_connections(mainwindow, qtbot):
    assert mainwindow.centralWidget().currentWidget() == mainwindow.menus["test"]

    qtbot.mouseClick(mainwindow.menus["brewConfig"].BackButton, QtCore.Qt.LeftButton)
    assert mainwindow.centralWidget().currentWidget() == mainwindow.menus["mainMenu"]
    mainwindow.centralWidget().setCurrentWidget(mainwindow.menus["test"])

    qtbot.mouseClick(mainwindow.menus["brewStatus"].ReturnToMenuButton, QtCore.Qt.LeftButton)
    assert mainwindow.centralWidget().currentWidget() == mainwindow.menus["mainMenu"]
    mainwindow.centralWidget().setCurrentWidget(mainwindow.menus["test"])

    qtbot.mouseClick(mainwindow.menus["deviceStatus"].ReturnToMenuButton, QtCore.Qt.LeftButton)
    assert mainwindow.centralWidget().currentWidget() == mainwindow.menus["mainMenu"]
    mainwindow.centralWidget().setCurrentWidget(mainwindow.menus["test"])

    qtbot.mouseClick(mainwindow.menus["cleaningScreen"].ReturnToMenuButton, QtCore.Qt.LeftButton)
    assert mainwindow.centralWidget().currentWidget() == mainwindow.menus["mainMenu"]
    mainwindow.centralWidget().setCurrentWidget(mainwindow.menus["test"])

    qtbot.mouseClick(mainwindow.menus["brewConfig"].StartBrewButton, QtCore.Qt.LeftButton)
    assert mainwindow.centralWidget().currentWidget() == mainwindow.menus["brewConfig"]
    mainwindow.centralWidget().setCurrentWidget(mainwindow.menus["test"])

    qtbot.mouseClick(mainwindow.menus["mainMenu"].EnterBrewConfigButton, QtCore.Qt.LeftButton)
    assert mainwindow.centralWidget().currentWidget() == mainwindow.menus["brewConfig"]
    mainwindow.centralWidget().setCurrentWidget(mainwindow.menus["test"])

    qtbot.mouseClick(mainwindow.menus["mainMenu"].EnterCleanScreenButton, QtCore.Qt.LeftButton)
    assert mainwindow.centralWidget().currentWidget() == mainwindow.menus["cleaningScreen"]
    mainwindow.centralWidget().setCurrentWidget(mainwindow.menus["test"])

    qtbot.mouseClick(mainwindow.menus["mainMenu"].EnterDeviceStatusScreen, QtCore.Qt.LeftButton)
    assert mainwindow.centralWidget().currentWidget() == mainwindow.menus["deviceStatus"]
    mainwindow.centralWidget().setCurrentWidget(mainwindow.menus["test"])
