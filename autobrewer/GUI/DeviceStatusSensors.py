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
            self.HLTCurrentTemp, 
            self.MTCurrentTemp, 
            self.BKCurrentTemp
            ]
        self.tankVolumes = [
            self.TankVolume1State,
            self.TankVolume2State,
            self.TankVolume3State
        ]

    def connections(self):
        self.HeaterPIDDecrease1.clicked.connect(self.decreaseHeater)
        self.HeaterPIDDecrease2.clicked.connect(self.decreaseHeater)
        self.HeaterPIDDecrease3.clicked.connect(self.decreaseHeater)
        self.HeaterPIDDecrease4.clicked.connect(self.decreaseHeater)

        self.HeaterPIDIncrease1.clicked.connect(self.increaseHeater)
        self.HeaterPIDIncrease2.clicked.connect(self.increaseHeater)
        self.HeaterPIDIncrease3.clicked.connect(self.increaseHeater)
        self.HeaterPIDIncrease4.clicked.connect(self.increaseHeater)

        self.IncreaseBK.clicked.connect(self.increaseHeaterTarget)
        self.DecreaseBK.clicked.connect(self.decreaseHeaterTarget)

        self.IncreaseHLT.clicked.connect(self.increaseHeaterTarget)
        self.DecreaseHLT.clicked.connect(self.decreaseHeaterTarget)

        self.IncreaseMT.clicked.connect(self.increaseHeaterTarget)
        self.DecreaseMT.clicked.connect(self.decreaseHeaterTarget)

        self.HomeServo.clicked.connect(self.setServo)
        self.IncreaseServo.clicked.connect(self.increaseServo)
        self.DecreaseServo.clicked.connect(self.decreaseServo)

        self.HopServo1.clicked.connect(self.setServo)
        self.HopServo2.clicked.connect(self.setServo)
        self.HopServo3.clicked.connect(self.setServo)
        self.HopServo4.clicked.connect(self.setServo)
        self.HopServo5.clicked.connect(self.setServo)

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

    def increaseHeater(self):
        ## Increase heater value by 0.1
        pass

    def decreaseHeater(self):
        ## Decrease heater value by 0.1
        pass

    def increaseHeaterTarget(self):
        ## Increase tank target temp by 1
        pass

    def decreaseHeaterTarget(self):
        ## Decrease tank target temp by 1
        pass

    def increaseServo(self):
        ## Increase servo angle by 1
        pass

    def decreaseServo(self):
        ## Decrease servo angle by 1
        pass

    def setServo(self):
        ## Set servo to predefined position (Home or hop cup)
        pass

    def hideMainMenu(self):
        self.ReturnToMenuButton.setHidden(True)
        self.ProcessStatusButton.setHidden(False)

    def hideProcessStatus(self):
        self.ReturnToMenuButton.setHidden(False)
        self.ProcessStatusButton.setHidden(True)