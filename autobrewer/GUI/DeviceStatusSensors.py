from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .DeviceStatusSensorsGUI import Ui_DeviceStatusSensors
from ..hardware.devicehandler import DeviceHandler

class DeviceStatusSensors(QtWidgets.QWidget, Ui_DeviceStatusSensors):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.adjustUI()
        self.connections()

        self.temperatureSensors = [
            self.TempSens1State, 
            self.TempSens2State, 
            self.TempSens3State
            ]
        self.tankVolumes = [
            self.TankVolume1State,
            self.TankVolume2State,
            self.TankVolume3State
        ]
        self.updateState()

    def connections(self):
        self.updateTimer.timeout.connect(self.updateSensorsTimer)
        self.GoToControlStatusButton.clicked.connect(self.updateTimer.stop)
        self.ReturnToMenuButton.clicked.connect(self.updateTimer.stop)

    def adjustUI(self):
        self.updateTimer=QtCore.QTimer()
        self.disableSensorUpdates = QtCore.Signal()
        self.ProcessStatusButton.setHidden(True)

    def updateState(self):
        self.temperatureSensors[0].setText("Temperature (\u00b0F): "+str(DeviceHandler.hardwareState.temperatures[DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"]]))
        self.temperatureSensors[1].setText("Temperature (\u00b0F): "+str(DeviceHandler.hardwareState.temperatures[DeviceHandler.KETTLE_IDS_GIVEN_NAME["MT"]]))
        self.temperatureSensors[2].setText("Temperature (\u00b0F): "+str(DeviceHandler.hardwareState.temperatures[DeviceHandler.KETTLE_IDS_GIVEN_NAME["BK"]]))
        self.tankVolumes[0].setText("Volume (gal): "+str(DeviceHandler.hardwareState.volumes[DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"]]))
        self.tankVolumes[1].setText("Volume (gal): "+str(DeviceHandler.hardwareState.volumes[DeviceHandler.KETTLE_IDS_GIVEN_NAME["MT"]]))
        self.tankVolumes[2].setText("Volume (gal): "+str(DeviceHandler.hardwareState.volumes[DeviceHandler.KETTLE_IDS_GIVEN_NAME["BK"]]))

    def updateSensorsTimer(self):
        ## This timer runs while the user is on the sensors page and updates the UI every 1 second.
        self.updateState()
        self.updateTimer.start(1000)
        logger.debug("Updated sensors UI")

    def hideMainMenu(self):
        self.ReturnToMenuButton.setHidden(True)
        self.ProcessStatusButton.setHidden(False)

    def hideProcessStatus(self):
        self.ReturnToMenuButton.setHidden(False)
        self.ProcessStatusButton.setHidden(True)