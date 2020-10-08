import sys
from functools import partial

from loguru import logger
from PySide2.QtWidgets import QApplication

from .ExecutionHandler import executionhandler
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
    mainscreen.menus["brewConfig"].startBrewSignal.connect(executionhandler.startBrewProcess)

    mainscreen.menus["processStatus"].stopProcessRequest.connect(executionhandler.stopProcess)
    mainscreen.menus["processStatus"].nextStepRequest.connect(executionhandler.advanceStep)
    mainscreen.menus["processStatus"].manualOverrideRequest.connect(executionhandler.assumemanualcontrol)

    mainscreen.menus["processStatus"].returnUserToMenu.connect(partial(mainscreen.goToMenu, mainscreen.menus["mainMenu"]))

    executionhandler.stepstarted.connect(mainscreen.menus["processStatus"].updateLabel)
    executionhandler.processstarted.connect(mainscreen.menus["processStatus"].startUpdateTimer)
    executionhandler.processstopped.connect(mainscreen.menus["processStatus"].resetProgressScreen)
    executionhandler.processpaused.connect(mainscreen.menus["processStatus"].updateTimer.stop)
    executionhandler.processresumed.connect(mainscreen.menus["processStatus"].updateTimer.start)
    executionhandler.processcomplete.connect(mainscreen.menus["processStatus"].processComplete)


    mainscreen.menus["cleaningScreen"].startCleaningSignal.connect(executionhandler.startCleaningProcess)
    mainscreen.menus["cleaningScreen"].abortCleaningSignal.connect(executionhandler.stopProcess)
    mainscreen.menus["cleaningScreen"].nextCleaningStepSignal.connect(executionhandler.advanceStep)
    mainscreen.menus["cleaningScreen"].manualOverrideSignal.connect(executionhandler.assumemanualcontrol)


