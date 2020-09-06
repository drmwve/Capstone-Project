import sys, platform
from PySide2 import QtCore, QtWidgets
from .MainWindow import MainWindow
from .ExecutionHandler import ExecutionHandler
from loguru import logger
from .GUI.Styler import WindowStyler
from gpiozero import Device
from .ControlWrapper import ControlHandler
import time

def main():
    app = QtWidgets.QApplication(sys.argv)
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG")
    logger.info(platform._syscmd_uname('-a')
)

    executionHandler = ExecutionHandler()
    styler = WindowStyler()
    styler.styleWindows(app)
    handler = ControlHandler()
    mainScreen = MainWindow()
    mainScreen.show()
    logger.info("Opened main screen " + str(mainScreen))
    handler.open2WBallValve(1)
    handler.open2WBallValve(2)
    time.sleep(6)
    handler.open2WBallValve(1)

    sys.exit(app.exec_())