import sys
from PySide2 import QtCore, QtWidgets, QtGui
from MainWindow import MainWindow
from ExecutionCode.ExecutionHandler import ExecutionHandler
from GUI.Styler import WindowStyler
from loguru import logger

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG")

    executionHandler = ExecutionHandler()

    styler = WindowStyler()
    styler.styleWindows(app)
    
    mainScreen = MainWindow()
    mainScreen.show()
    logger.info("Created main screen " + str(mainScreen))

    sys.exit(app.exec_())