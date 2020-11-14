from PySide2 import QtWidgets
from loguru import logger
from .DeviceStatusControlsGUI import Ui_DeviceStatusControls
from ..hardware.devicehandler import devicehandler
from ..exceptions import ComponentControlError

class DeviceStatusControls(QtWidgets.QWidget, Ui_DeviceStatusControls):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connections()
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

        self.adjustUI()

    def connections(self):
        # add any connections that are internal to the functioning of this widget only
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

    def adjustUI(self):
        self.ProcessStatusButton.setHidden(True)

    def updateState(self, hardwareState):
        ## This function checks hardware states, adjusting the UI where needed.
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
        ## Pumps
        for i in range(0,2):
            if self.deviceState.pumps[i] == True:
                ## Set state to on
                self.pumpButton[i].setText("Turn Off")
                self.pumpState[i].setText("State: On")
            elif self.deviceState.pumps[i] == False:
                ## Set state to off
                self.pumpButton[i].setText("Turn On")
                self.pumpState[i].setText("State: Off")
        ## Heaters
        for i in range(0,4):
            if self.deviceState.heatingElements[i] == True:
                ## Set state to on
                self.heaterButton[i].setText("Turn Off")
                self.heaterState[i].setText("State: On")
            elif self.deviceState.heatingElements[i] == False:
                ## Set state to off
                self.heaterButton[i].setText("Turn On")
                self.heaterState[i].setText("State: Off")

    ## Defining button functions
    def toggleBallValve(self, index):
        if self.deviceState.ballValves[index] == 0:
            ## Open ball valve
            logger.info("User requested ball valve " + str(index + 1) + " to open")
            try:
                devicehandler.openBallValve(index)
            except ComponentControlError as e:
                QtWidgets.QMessageBox.information(self, "Component Control Error", str(e))
        elif self.deviceState.ballValves[index] == 1:
            ## Close ball valve
            logger.info("User requested ball valve " + str(index + 1) + " to close")
            try:
                devicehandler.closeBallValve(index)
            except ComponentControlError as e:
                QtWidgets.QMessageBox.information(self, "Component Control Error", str(e))

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
                QtWidgets.QMessageBox.information(self, "Component Control Error", str(e))
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
                QtWidgets.QMessageBox.information(self, "Component Control Error", str(e))

    def toggleHeater(self, index):
        if self.deviceState.heatingElements[index] == 0:
            ## Turn heater on
            logger.info("User requested heater " + str(index + 1) + " to turn on")
            try:
                devicehandler.enableHeatingElement(index)
            except ComponentControlError as e:
                QtWidgets.QMessageBox.information(self, "Component Control Error", str(e))
        elif self.deviceState.heatingElements[index] == 1:
            ##  Turn heater off
            logger.info("User requested heater " + str(index + 1) + " to turn off")
            try:
                devicehandler.disableHeatingElement(index)
            except ComponentControlError as e:
                QtWidgets.QMessageBox.information(self, "Component Control Error", str(e))

    def togglePump(self, index):
        if self.deviceState.pumps[index] == 0:
            ## Turn pump on
            logger.info("User requested pump " + str(index + 1) + " to turn on")
            try:
                devicehandler.enablePump(index)
            except ComponentControlError as e:
                QtWidgets.QMessageBox.information(self, "Component Control Error", str(e))
        elif self.deviceState.pumps[index] == 1:
            ## Turn pump off
            logger.info("User requested pump " + str(index + 1) + " to turn off")
            try:
                devicehandler.disablePump(index)
            except ComponentControlError as e:
                QtWidgets.QMessageBox.information(self, "Component Control Error", str(e))

    def hideMainMenu(self):
        self.ReturnToMenuButton.setHidden(True)
        self.ProcessStatusButton.setHidden(False)

    def hideProcessStatus(self):
        self.ReturnToMenuButton.setHidden(False)
        self.ProcessStatusButton.setHidden(True)