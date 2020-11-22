from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtGui import QPalette
from loguru import logger


class WindowStyler:
    def styleWindows(self, app):

        ## This defines the style and colors for all windows and widgets.
        #app.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.Window, QtGui.QColor(255, 255, 255))
        palette.setColor(QPalette.WindowText, QtCore.Qt.black)
        palette.setColor(QPalette.Base, QtGui.QColor(255, 255, 255))
        palette.setColor(QPalette.AlternateBase, QtGui.QColor(103, 103, 103))
        palette.setColor(QPalette.ToolTipBase, QtCore.Qt.white)
        palette.setColor(QPalette.ToolTipText, QtCore.Qt.white)
        palette.setColor(QPalette.Text, QtCore.Qt.black)
        palette.setColor(QPalette.Button, QtGui.QColor(179, 229, 252))
        palette.setColor(QPalette.ButtonText, QtCore.Qt.black)
        palette.setColor(QPalette.BrightText, QtCore.Qt.red)
        palette.setColor(QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
        palette.setColor(QPalette.HighlightedText, QtCore.Qt.black)
        palette.setColor(
            QPalette.Disabled, QPalette.Button, QtGui.QColor(88, 88, 88)
        )
        app.setPalette(palette)
        logger.debug("Applied custom window palette")
