import sys, platform
from PySide2 import QtCore, QtWidgets
from .MainWindow import MainWindow
from .ExecutionHandler import ExecutionHandler
from loguru import logger
from .GUI.Styler import WindowStyler
from gpiozero import Device
from .ControlWrapper import DeviceHandler
from .osconfig import is_raspberry_pi
import time

def main():
    app = QtWidgets.QApplication(sys.argv)
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG")
    executionHandler = ExecutionHandler()
    styler = WindowStyler()
    styler.styleWindows(app)
    mainScreen = MainWindow()
    mainScreen.show()
    logger.info("Opened main screen " + str(mainScreen))
    logger.info(f'Is Raspberry Pi: {is_raspberry_pi()}')

    sys.exit(app.exec_())