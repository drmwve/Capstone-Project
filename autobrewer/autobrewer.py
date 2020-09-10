import sys
from PySide2 import QtCore, QtWidgets
from .MainWindow import MainWindow
from .ExecutionHandler import ExecutionHandler
from loguru import logger
from .GUI.Styler import WindowStyler

def main():
    app = QtWidgets.QApplication(sys.argv)
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG")

    executionHandler = ExecutionHandler()

    styler = WindowStyler()
    styler.styleWindows(app)

    mainScreen = MainWindow()
    mainScreen.show()
    logger.info("Opened main screen " + str(mainScreen))

    sys.exit(app.exec_())
