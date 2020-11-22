from PySide2.QtWidgets import QWidget, QMessageBox
from loguru import logger
from .DeviceStatusGUI import Ui_DeviceStatus
from ..hardware.devicehandler import devicehandler
from ..exceptions import ComponentControlError
from functools import partial

class DeviceStatus(QWidget, Ui_DeviceStatus):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.ballValveButton = [
            self.BallValve1Button,
            self.BallValve2Button,
            self.BallValve3Button,
            self.BallValve4Button,
            self.BallValve5Button,
        ]
        self.ballValveState = [
            self.BallValve1State,
            self.BallValve2State,
            self.BallValve3State,
            self.BallValve4State,
            self.BallValve5State,
        ]
        self.threeWayValveButton = [
            self.ThreeWay1Button,
            self.ThreeWay2Button,
            self.ThreeWay3Button,
            self.ThreeWay4Button,
            self.ThreeWay5Button,
        ]
        self.threeWayValveState = [
            self.ThreeWay1State,
            self.ThreeWay2State,
            self.ThreeWay3State,
            self.ThreeWay4State,
            self.ThreeWay5State,
        ]
        self.heaterButton = [
            self.Heater1Button,
            self.Heater2Button,
            self.Heater3Button,
            self.Heater4Button,
        ]
        self.heaterState = [
            self.Heater1State,
            self.Heater2State,
            self.Heater3State,
            self.Heater4State,
        ]
        self.pumpButton = [self.Pump1Button, self.Pump2Button]
        self.pumpState = [self.Pump1State, self.Pump2State]
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
        self.PIDToggles = [
            self.HLTPIDtoggle,
            self.MTPIDtoggle,
            self.BKPIDtoggle
        ]    

        self.connections()
        self.adjustUI()

    def connections(self):
        self.BallValve1Button.clicked.connect(lambda: self.toggleBallValve(0))
        self.BallValve2Button.clicked.connect(lambda: self.toggleBallValve(1))
        self.BallValve3Button.clicked.connect(lambda: self.toggleBallValve(2))
        self.BallValve4Button.clicked.connect(lambda: self.toggleBallValve(3))
        self.BallValve5Button.clicked.connect(lambda: self.toggleBallValve(4))

        self.ThreeWay1Button.clicked.connect(lambda: self.toggleThreeWay(0))
        self.ThreeWay2Button.clicked.connect(lambda: self.toggleThreeWay(1))
        self.ThreeWay3Button.clicked.connect(lambda: self.toggleThreeWay(2))
        self.ThreeWay4Button.clicked.connect(lambda: self.toggleThreeWay(3))
        self.ThreeWay5Button.clicked.connect(lambda: self.toggleThreeWay(4))

        self.Heater1Button.clicked.connect(lambda: self.toggleHeater(0))
        self.Heater2Button.clicked.connect(lambda: self.toggleHeater(1))
        self.Heater3Button.clicked.connect(lambda: self.toggleHeater(2))
        self.Heater4Button.clicked.connect(lambda: self.toggleHeater(3))

        self.Pump1Button.clicked.connect(lambda: self.togglePump(0))
        self.Pump2Button.clicked.connect(lambda: self.togglePump(1))

        self.HeaterTempToggle.clicked.connect(self.toggleHeaterGroup)
        self.BallValveToggle.clicked.connect(self.toggleBallValveGroup)
        self.PumpVolumeToggle.clicked.connect(self.togglePumpGroup)
        self.ServoMotorToggle.clicked.connect(self.toggleServoGroup)


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

        self.PIDToggles[0].clicked.connect(partial(self.togglePID, 0))
        self.PIDToggles[1].clicked.connect(partial(self.togglePID, 1))
        self.PIDToggles[2].clicked.connect(partial(self.togglePID, 2))

    def adjustUI(self):
        self.ProcessStatusButton.setHidden(True)
        self.hideGroupBoxes()

    ## Hides or shows the main menu when a process is running/completed.
    def hideMainMenu(self):
        self.ReturnToMenuButton.setHidden(True)
        self.ProcessStatusButton.setHidden(False)

    def hideProcessStatus(self):
        self.ReturnToMenuButton.setHidden(False)
        self.ProcessStatusButton.setHidden(True)

    ## Toggle functions control what elements are shown on the screen, based on the four top buttons.
    def hideGroupBoxes(self):
        self.BallValveGroupBox.setHidden(True)
        self.ThreeWayGroupBox.setHidden(True)
        self.HeatersGroupBox.setHidden(True)
        self.HeatersPWMGroupBox.setHidden(True)
        self.TemperatureGroupBox.setHidden(True)
        self.ServoMotorGroupBox.setHidden(True)
        self.PumpsGroupBox.setHidden(True)
        self.TankVolumeGroupBox.setHidden(True)

    def toggleHeaterGroup(self):
        self.hideGroupBoxes()
        self.BallValveToggle.setChecked(False)
        self.PumpVolumeToggle.setChecked(False)
        self.ServoMotorToggle.setChecked(False)
        self.HeatersGroupBox.setHidden(False)
        self.HeatersPWMGroupBox.setHidden(False)
        self.TemperatureGroupBox.setHidden(False)

    def togglePumpGroup(self):
        self.hideGroupBoxes()
        self.BallValveToggle.setChecked(False)
        self.HeaterTempToggle.setChecked(False)
        self.ServoMotorToggle.setChecked(False)
        self.PumpsGroupBox.setHidden(False)
        self.TankVolumeGroupBox.setHidden(False)

    def toggleServoGroup(self):
        self.hideGroupBoxes()
        self.BallValveToggle.setChecked(False)
        self.HeaterTempToggle.setChecked(False)
        self.PumpVolumeToggle.setChecked(False)
        self.ServoMotorGroupBox.setHidden(False)

    def toggleBallValveGroup(self):
        self.hideGroupBoxes()
        self.HeaterTempToggle.setChecked(False)
        self.PumpVolumeToggle.setChecked(False)
        self.ServoMotorToggle.setChecked(False)
        self.BallValveGroupBox.setHidden(False)
        self.ThreeWayGroupBox.setHidden(False)

    ## This function checks hardware states, adjusting the UI where needed.
    def updateState(self, hardwareState):
        self.deviceState = hardwareState

        ## Ball Valves
        for i in range(0, 5):
            if self.deviceState.ballValves[i] == True:
                ## Set state to open
                self.ballValveButton[i].setText("Close")
                self.ballValveState[i].setText("State: Open")
            elif self.deviceState.ballValves[i] == False:
                ## Set state to closed
                self.ballValveButton[i].setText("Open")
                self.ballValveState[i].setText("State: Closed")

        ## Three way valves
        for i in range(5,10):
            if self.deviceState.ballValves[i] == True:
                ## Set state to direction 2
                self.threeWayValveState[i-5].setText("State: Direction 2")
            elif self.deviceState.ballValves[i] == False:
                ## Set state to direction 1
                self.threeWayValveState[i-5].setText("State: Direction 1")

        ## Pumps and tank volume
        self.tankVolumes[0].setText("Volume (gal): " + str(self.deviceState.volumes[0]))
        for i in range(0,2):
            if self.deviceState.pumps[i] == True:
                ## Set state to on
                self.pumpButton[i].setText("Turn Off")
                self.pumpState[i].setText("State: On")
            elif self.deviceState.pumps[i] == False:
                ## Set state to off
                self.pumpButton[i].setText("Turn On")
                self.pumpState[i].setText("State: Off")
        for i in range(0,3):
            self.tankVolumes[i].setText("Volume (gal): " + str(self.deviceState.volumes[i]))
            self.tankVolumes[i].setText("Volume (gal): " + str(self.deviceState.volumes[i]))
            self.tankVolumes[i].setText("Volume (gal): " + str(self.deviceState.volumes[i]))

        ## Heaters and temperatures
        for i in range(0,4):
            if self.deviceState.heatingElements[i] == True:
                ## Set state to on
                self.heaterButton[i].setText("Turn Off")
                self.heaterState[i].setText("State: On")
            elif self.deviceState.heatingElements[i] == False:
                ## Set state to off
                self.heaterButton[i].setText("Turn On")
                self.heaterState[i].setText("State: Off")
        for i in range(len(self.deviceState.kettlepidenabled)):
            if self.deviceState.kettlepidenabled[i] == True:
                self.PIDToggles[i].setText("Disable")
            elif self.deviceState.kettlepidenabled[i] == False:
                self.PIDToggles[i].setText("Enable")
        self.temperatureSensors[0].setText("Temperature (\u00b0F): " + str(self.deviceState.temperatures[devicehandler.KETTLE_IDS_GIVEN_NAME["HLT"]]))
        self.temperatureSensors[1].setText("Temperature (\u00b0F): " + str(self.deviceState.temperatures[devicehandler.KETTLE_IDS_GIVEN_NAME["MT"]]))
        self.temperatureSensors[2].setText("Temperature (\u00b0F): " + str(self.deviceState.temperatures[devicehandler.KETTLE_IDS_GIVEN_NAME["BK"]]))
        self.HeaterPID1.setText("Current PWM: " + str(self.deviceState.heatingElements[0]))
        self.HeaterPID2.setText("Current PWM: " + str(self.deviceState.heatingElements[1]))
        self.HeaterPID3.setText("Current PWM: " + str(self.deviceState.heatingElements[2]))
        self.HeaterPID4.setText("Current PWM: " + str(self.deviceState.heatingElements[3]))
        self.HLTTargetTemp.setText("Target Temperature (\u00b0F): " + str(self.deviceState.kettletempsetpoints[0]))
        self.MTTargetTemp.setText("Target Temperature (\u00b0F): " + str(self.deviceState.kettletempsetpoints[1]))
        self.BKTargetTemp.setText("Target Temperature (\u00b0F): " + str(self.deviceState.kettletempsetpoints[2]))

        ## Servo angle
        self.CurrentAngleServo.setText("Current Angle (\u00b0): " + str(self.deviceState.hopservoangle))

    ## Defining control functions.

    ## BALL VALVE CONTROLS ##
    ## Toggle 2 way ball valves
    def toggleBallValve(self, index):
        if self.deviceState.ballValves[index] == 0:
            ## Open ball valve
            logger.info("User requested ball valve " + str(index + 1) + " to open")
            try:
                devicehandler.openBallValve(index)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))
        elif self.deviceState.ballValves[index] == 1:
            ## Close ball valve
            logger.info("User requested ball valve " + str(index + 1) + " to close")
            try:
                devicehandler.closeBallValve(index)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## Toggle 3 way ball valves
    def toggleThreeWay(self, index):
        if self.deviceState.ballValves[index+5] == 0:
            ## Change to direction 2
            logger.info(
                "User requested three way valve "
                + str(index + 1)
                + " to change to direction 2"
            )
            try:
                devicehandler.openBallValve(index+5)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))
        elif self.deviceState.ballValves[index+5] == 1:
            ## Change to direction 1
            logger.info(
                "User requested three way valve "
                + str(index + 1)
                + " to change to direction 1"
            )
            try:
                devicehandler.closeBallValve(index+5)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## HEATER CONTROLS ##
    ## Simple heater toggle, either on/off.
    def toggleHeater(self, index):
        if self.deviceState.heatingElements[index] == 0:
            ## Turn heater on
            logger.info("User requested heater " + str(index + 1) + " to turn on")
            try:
                devicehandler.enableHeatingElement(index)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))
        elif self.deviceState.heatingElements[index] == 1:
            ##  Turn heater off
            logger.info("User requested heater " + str(index + 1) + " to turn off")
            try:
                devicehandler.disableHeatingElement(index)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## Toggle PID control for setting a target temperature.
    def togglePID(self, i):
        if self.deviceState.kettlepidenabled[i] == True:
            ## Disable control
            logger.info("User requested to disable PID control")
            try:
                devicehandler.setKettlePIDEnabled(i,False)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))
        elif self.deviceState.kettlepidenabled[i] == False:
            ## ENable control
            logger.info("User requested to enable PID control")
            try:
                devicehandler.setKettlePIDEnabled(i,True)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## Increase heater PWM value by 0.1
    def increaseHeater(self, i):
        if self.deviceState.heatingElements[i] < 1:
            logger.info("User requested heating element " + str(i) + " to increase PWM value by 0.1")
            try:
                devicehandler.setHeatingElementPWM(i, self.deviceState.heatingElements[i]+0.1)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## Decrease heater PWM value by 0.1
    def decreaseHeater(self, i):
        if self.deviceState.heatingElements[i] > 0:
            logger.info("User requested heating element " + str(i) + " to decrease PWM value by 0.1")
            try:
                devicehandler.setHeatingElementPWM(i, self.deviceState.heatingElements[i]-0.1)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## Increase tank target temp by 1 degree
    def increaseHeaterTarget(self, i):
        if self.deviceState.kettletempsetpoints[i] == 0:
            logger.info("User wants to set "+ str(devicehandler.KETTLE_NAMES_GIVEN_ID[i]) + 
            " temperature" + ", setting to 150 for further control.")
            try:
                devicehandler.setTargetKettleTemp(i, 150)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))
        else:
            logger.info("User requested to set " + str(devicehandler.KETTLE_NAMES_GIVEN_ID[i]) + " temperature to: " + str(self.hardwarestate.kettletempsetpoints[i]+1))
            try:
                devicehandler.setTargetKettleTemp(i, self.deviceState.kettletempsetpoints[i]+1)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## Decrease tank target temp by 1 degree
    def decreaseHeaterTarget(self, i):
        if self.deviceState.kettletempsetpoints[i] == 0:
            logger.info("User wants to set "+ str(devicehandler.KETTLE_NAMES_GIVEN_ID[i]) + 
            " temperature" + ", setting to 150 for further control.")
            try:
                devicehandler.setTargetKettleTemp(i, 150)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))
        else:
            logger.info("User requested to set " + str(devicehandler.KETTLE_NAMES_GIVEN_ID[i]) + " temperature to: " + str(self.deviceState.kettletempsetpoints[i]-1))
            try:
                devicehandler.setTargetKettleTemp(i, self.deviceState.kettletempsetpoints[i]-1)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## PUMP CONTROLS ##
    ## Toggle pumps
    def togglePump(self, index):
        if self.deviceState.pumps[index] == 0:
            ## Turn pump on
            logger.info("User requested pump " + str(index) + " to turn on")
            try:
                devicehandler.enablePump(index)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))
        elif self.deviceState.pumps[index] == 1:
            ## Turn pump off
            logger.info("User requested pump " + str(index) + " to turn off")
            try:
                devicehandler.disablePump(index)
            except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## SERVO MOTOR CONTROLS ##
    ## Increase servo angle by 5 degrees
    def increaseServo(self):
        logger.info("User requested to increase servo angle by 5 degrees")
        try:
            devicehandler.setHopServoPosition(self.deviceState.hopservoangle+5)
        except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## Decrease servo angle by 5 degrees
    def decreaseServo(self):
        logger.info("User requested to decrease servo angle by 5 degrees")
        try:
            devicehandler.setHopServoPosition(self.deviceState.hopservoangle-5)
        except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))

    ## Set servo to predefined position (Home or hop cup)
    def setServo(self, i):
        logger.info("User requested to set hop servo to position " + str(i))
        try:
            devicehandler.goToHopPosition(i)
        except ComponentControlError as e:
                QMessageBox.information(self, "Component Control Error", str(e))