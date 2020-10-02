import sys
from functools import partial

from loguru import logger
from PySide2.QtWidgets import QApplication

from .ExecutionHandler import ExecutionHandler
from .Process import *
from .GUI.Styler import WindowStyler
from .MainWindow import MainWindow
from .utils import IS_RASPBERRY_PI


def main():
    app = QApplication(sys.argv)
    logger.add(
        sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG"
    )
    styler = WindowStyler()
    styler.styleWindows(app)
    mainScreen = MainWindow()
    connections(mainScreen)
    mainScreen.show()
    logger.info("Opened main screen " + str(mainScreen))
    logger.info(f"Is Raspberry Pi: {IS_RASPBERRY_PI}")
    sys.exit(app.exec_())


def connections(mainscreen: MainWindow):
    mainscreen.menus["brewConfig"].startBrewSignal.connect(partial(ExecutionHandler.startBrewProcess, mainscreen.menus["brewConfig"].selectedBrewRecipe))

    mainscreen.menus["brewStatus"].abortBrewSignal.connect(ExecutionHandler.stopProcess)
    mainscreen.menus["brewStatus"].nextBrewStepSignal.connect(ExecutionHandler.advanceStep)
    mainscreen.menus["brewStatus"].manualOverrideSignal.connect(ExecutionHandler.pauseProcess)

    mainscreen.menus["cleaningScreen"].startCleaningSignal.connect(ExecutionHandler.startCleaningProcess)
    mainscreen.menus["cleaningScreen"].abortCleaningSignal.connect(ExecutionHandler.stopProcess)
    mainscreen.menus["cleaningScreen"].nextCleaningStepSignal.connect(ExecutionHandler.advanceStep)



