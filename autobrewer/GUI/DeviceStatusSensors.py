from PySide2 import QtWidgets
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

    def connections(self):
        pass

    def adjustUI(self):
        self.ProcessStatusButton.setHidden(True)

    def updateState(self, hardwarestate):
        self.hardwarestate = hardwarestate
        self.temperatureSensors[0].setText("Temperature (\u00b0F): " + str(self.hardwarestate.temperatures[DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"]]))
        self.temperatureSensors[1].setText("Temperature (\u00b0F): " + str(self.hardwarestate.temperatures[DeviceHandler.KETTLE_IDS_GIVEN_NAME["MT"]]))
        self.temperatureSensors[2].setText("Temperature (\u00b0F): " + str(self.hardwarestate.temperatures[DeviceHandler.KETTLE_IDS_GIVEN_NAME["BK"]]))
        self.tankVolumes[0].setText("Volume (gal): " + str(self.hardwarestate.volumes[DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"]]))
        self.tankVolumes[1].setText("Volume (gal): " + str(self.hardwarestate.volumes[DeviceHandler.KETTLE_IDS_GIVEN_NAME["MT"]]))
        self.tankVolumes[2].setText("Volume (gal): " + str(self.hardwarestate.volumes[DeviceHandler.KETTLE_IDS_GIVEN_NAME["BK"]]))

    def hideMainMenu(self):
        self.ReturnToMenuButton.setHidden(True)
        self.ProcessStatusButton.setHidden(False)

    def hideProcessStatus(self):
        self.ReturnToMenuButton.setHidden(False)
        self.ProcessStatusButton.setHidden(True)