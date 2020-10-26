from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .DeviceStatusSensorsGUI import Ui_DeviceStatusSensors
from ..hardware.devicehandler import devicehandler
from functools import partial

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
        self.HeaterPIDDecrease1.clicked.connect(partial(self.decreaseHeater, 0))
        self.HeaterPIDDecrease2.clicked.connect(partial(self.decreaseHeater, 1))
        self.HeaterPIDDecrease3.clicked.connect(partial(self.decreaseHeater, 2))
        self.HeaterPIDDecrease4.clicked.connect(partial(self.decreaseHeater, 3))

        self.HeaterPIDIncrease1.clicked.connect(partial(self.increaseHeater, 0))
        self.HeaterPIDIncrease2.clicked.connect(partial(self.increaseHeater, 1))
        self.HeaterPIDIncrease3.clicked.connect(partial(self.increaseHeater, 2))
        self.HeaterPIDIncrease4.clicked.connect(partial(self.increaseHeater, 3))

        self.IncreaseBK.clicked.connect(partial(self.increaseHeaterTarget, 2))
        self.DecreaseBK.clicked.connect(partial(self.decreaseHeaterTarget, 2))

        self.IncreaseHLT.clicked.connect(partial(self.increaseHeaterTarget, 0))
        self.DecreaseHLT.clicked.connect(partial(self.decreaseHeaterTarget, 0))

        self.IncreaseMT.clicked.connect(partial(self.increaseHeaterTarget, 1))
        self.DecreaseMT.clicked.connect(partial(self.decreaseHeaterTarget, 1))

        
        self.IncreaseServo.clicked.connect(self.increaseServo)
        self.DecreaseServo.clicked.connect(self.decreaseServo)

        self.HomeServo.clicked.connect(partial(self.setServo, -1))
        self.HopServo1.clicked.connect(partial(self.setServo, 0))
        self.HopServo2.clicked.connect(partial(self.setServo, 1))
        self.HopServo3.clicked.connect(partial(self.setServo, 2))
        self.HopServo4.clicked.connect(partial(self.setServo, 3))
        self.HopServo5.clicked.connect(partial(self.setServo, 4))

    def adjustUI(self):
        self.ProcessStatusButton.setHidden(True)

    def updateState(self, hardwarestate):
        self.hardwarestate = hardwarestate
        self.temperatureSensors[0].setText("Temperature (\u00b0F): " + str(self.hardwarestate.temperatures[devicehandler.KETTLE_IDS_GIVEN_NAME["HLT"]]))
        self.temperatureSensors[1].setText("Temperature (\u00b0F): " + str(self.hardwarestate.temperatures[devicehandler.KETTLE_IDS_GIVEN_NAME["MT"]]))
        self.temperatureSensors[2].setText("Temperature (\u00b0F): " + str(self.hardwarestate.temperatures[devicehandler.KETTLE_IDS_GIVEN_NAME["BK"]]))
        self.tankVolumes[0].setText("Volume (gal): " + str(self.hardwarestate.volumes[devicehandler.KETTLE_IDS_GIVEN_NAME["HLT"]]))
        self.tankVolumes[1].setText("Volume (gal): " + str(self.hardwarestate.volumes[devicehandler.KETTLE_IDS_GIVEN_NAME["MT"]]))
        self.tankVolumes[2].setText("Volume (gal): " + str(self.hardwarestate.volumes[devicehandler.KETTLE_IDS_GIVEN_NAME["BK"]]))
        self.CurrentAngleServo.setText("Current Angle (\u00b0): " + str(self.hardwarestate.hopservoangle))
        self.HLTTargetTemp.setText("Target Temperature (\u00b0F): " + str(self.hardwarestate.kettletempsetpoints[0]))
        self.MTTargetTemp.setText("Target Temperature (\u00b0F): " + str(self.hardwarestate.kettletempsetpoints[1]))
        self.BKTargetTemp.setText("Target Temperature (\u00b0F): " + str(self.hardwarestate.kettletempsetpoints[2]))
        self.HeaterPID1.setText("Current PWM: " + str(self.hardwarestate.heatingElements[0]))
        self.HeaterPID2.setText("Current PWM: " + str(self.hardwarestate.heatingElements[1]))
        self.HeaterPID3.setText("Current PWM: " + str(self.hardwarestate.heatingElements[2]))
        self.HeaterPID4.setText("Current PWM: " + str(self.hardwarestate.heatingElements[3]))



    def increaseHeater(self, i):
        ## Increase heater value by 0.1
        if self.hardwarestate.heatingElements[i] < 1:
            logger.info("User requested heating element " + str(i) + " to increase PWM value by 0.1")
            devicehandler.setHeatingElementPWM(i, self.hardwarestate.heatingElements[i]+0.1)

    def decreaseHeater(self, i):
        ## Decrease heater value by 0.1
        if self.hardwarestate.heatingElements[i] > 0:
            logger.info("User requested heating element " + str(i) + " to decrease PWM value by 0.1")
            devicehandler.setHeatingElementPWM(i, self.hardwarestate.heatingElements[i]-0.1)

    def increaseHeaterTarget(self, i):
        ## Increase tank target temp by 1
        if self.hardwarestate.kettletempsetpoints[i] == 0:
            logger.info("User wants to set "+ str(devicehandler.KETTLE_NAMES_GIVEN_ID[i]) + 
            " temperature" + ", setting to 150 for further control.")
            devicehandler.setTargetKettleTemp(i, 150)
        else:
            logger.info("User requested to set " + str(devicehandler.KETTLE_NAMES_GIVEN_ID[i]) + " temperature to: " + str(self.hardwarestate.kettletempsetpoints[i]+1))
            devicehandler.setTargetKettleTemp(i, self.hardwarestate.kettletempsetpoints[i]+1)

    def decreaseHeaterTarget(self, i):
        ## Decrease tank target temp by 1
        if self.hardwarestate.kettletempsetpoints[i] == 0:
            logger.info("User wants to set "+ str(devicehandler.KETTLE_NAMES_GIVEN_ID[i]) + 
            " temperature" + ", setting to 150 for further control.")
            devicehandler.setTargetKettleTemp(i, 150)
        else:
            logger.info("User requested to set " + str(devicehandler.KETTLE_NAMES_GIVEN_ID[i]) + " temperature to: " + str(self.hardwarestate.kettletempsetpoints[i]-1))
            devicehandler.setTargetKettleTemp(i, self.hardwarestate.kettletempsetpoints[i]-1)

    def increaseServo(self):
        ## Increase servo angle by 5
        logger.info("User requested to increase servo angle by 5 degrees")
        devicehandler.setHopServoPosition(self.hardwarestate.hopservoangle+5)

    def decreaseServo(self):
        ## Decrease servo angle by 5
        logger.info("User requested to decrease servo angle by 5 degrees")
        devicehandler.setHopServoPosition(self.hardwarestate.hopservoangle-5)

    def setServo(self, i):
        ## Set servo to predefined position (Home or hop cup)
        logger.info("User requested to set hop servo to position " + str(i))
        devicehandler.goToHopPosition(i)

    def hideMainMenu(self):
        self.ReturnToMenuButton.setHidden(True)
        self.ProcessStatusButton.setHidden(False)

    def hideProcessStatus(self):
        self.ReturnToMenuButton.setHidden(False)
        self.ProcessStatusButton.setHidden(True)