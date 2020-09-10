import platform
import sys
import time

from gpiozero import Device
from loguru import logger
from PySide2 import QtCore, QtWidgets

from .ExecutionHandler import ExecutionHandler
from .GUI.Styler import WindowStyler
from .MainWindow import MainWindow
from .osconfig import is_raspberry_pi


def main():
    app = QtWidgets.QApplication(sys.argv)
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG")
    styler = WindowStyler()
    styler.styleWindows(app)
    mainScreen = MainWindow()
    mainScreen.show()
    logger.debug("Opened main screen " + str(mainScreen))
    logger.info(f'Is Raspberry Pi: {is_raspberry_pi()}')

    sys.exit(app.exec_())
