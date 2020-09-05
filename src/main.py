import sys
from PySide2 import QtCore, QtWidgets
from MainWindow import MainWindow
from ExecutionCode.ExecutionHandler import ExecutionHandler
from loguru import logger

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG")

    executionHandler = ExecutionHandler()
    mainScreen = MainWindow()
    mainScreen.show()
    logger.info("Opened main screen " + str(mainScreen))

    sys.exit(app.exec_())