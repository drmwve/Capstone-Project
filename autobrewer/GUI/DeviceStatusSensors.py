from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .DeviceStatusSensorsGUI import Ui_DeviceStatusSensors


class DeviceStatusSensors(QtWidgets.QWidget, Ui_DeviceStatusSensors):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connections()
        self.adjustUI()

    def connections(self):
        pass

    def adjustUI(self):
        pass