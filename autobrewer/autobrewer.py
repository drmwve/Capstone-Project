import sys

from loguru import logger
from PySide2.QtWidgets import QApplication
from PySide2 import QtCore


from .Process import *
from .GUI.Styler import WindowStyler
from .MainWindow import MainWindow
from .utils import IS_RASPBERRY_PI


def main():
    app = QApplication(sys.argv)
    logger.add(
        sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG"
    )
    logger.debug(f'Qapplication thread is {app.thread()}')
    styler = WindowStyler()
    styler.styleWindows(app)
    mainScreen = MainWindow()
    mainScreen.show()
    logger.debug("Opened main screen " + str(mainScreen))
    logger.info(f"Is Raspberry Pi: {IS_RASPBERRY_PI}")
    sys.exit(app.exec_())

