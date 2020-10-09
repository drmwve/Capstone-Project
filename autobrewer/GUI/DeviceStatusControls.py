from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .DeviceStatusControlsGUI import Ui_DeviceStatusControls
from ..hardware.devicehandler import DeviceHandler


class DeviceStatusControls(QtWidgets.QWidget, Ui_DeviceStatusControls):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connections()
        self.deviceHandler = DeviceHandler()
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
        self.updateState()
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
        pass

    def updateState(self):
        ## This function checks hardware states, adjusting the UI where needed.
        ## Ball Valves
        for i in range(0, 5):
            if DeviceHandler.hardwareState.ballValves[i] == True:
                ## Set state to open
                self.ballValveButton[i].setText("Close")
                self.ballValveButton[i].setChecked(True)
                self.ballValveState[i].setText("State: Open")
            elif DeviceHandler.hardwareState.ballValves[i] == False:
                ## Set state to closed
                self.ballValveButton[i].setText("Open")
                self.ballValveButton[i].setChecked(False)
                self.ballValveState[i].setText("State: Closed")
        ## Three way valves
        for i in range(5,10):
            if DeviceHandler.hardwareState.ballValves[i] == True:
                ## Set state to direction 2
                self.threeWayValveState[i-5].setText("State: Direction 2")
                self.threeWayValveButton[i-5].setChecked(True)
            elif DeviceHandler.hardwareState.ballValves[i] == False:
                ## Set state to direction 1
                self.threeWayValveState[i-5].setText("State: Direction 1")
                self.threeWayValveButton[i-5].setChecked(False)
        ## Pumps
        for i in range(0,2):
            if DeviceHandler.hardwareState.pumps[i] == True:
                ## Set state to on
                self.pumpButton[i].setText("Turn Off")
                self.pumpState[i].setText("State: On")
                self.pumpButton[i].setChecked(True)
            elif DeviceHandler.hardwareState.pumps[i] == False:
                ## Set state to off
                self.pumpButton[i].setText("Turn On")
                self.pumpState[i].setText("State: Off")
                self.pumpButton[i].setChecked(False)

    ## Defining button functions
    def toggleBallValve(self, index):
        if self.ballValveButton[index].isChecked():
            ## Open ball valve
            logger.info("User requested ball valve " + str(index + 1) + " to open")
            self.deviceHandler.openBallValve(index)
            self.updateState()
        else:
            ## Close ball valve
            logger.info("User requested ball valve " + str(index + 1) + " to close")
            self.deviceHandler.closeBallValve(index)
            self.updateState()

    def toggleThreeWay(self, index):
        if self.threeWayValveButton[index].isChecked():
            ## Change to direction 2
            logger.info(
                "User requested three way valve "
                + str(index + 1)
                + " to change to direction 2"
            )
            self.deviceHandler.openBallValve(index+5)
            self.updateState()
        else:
            ## Change to direction 1
            logger.info(
                "User requested three way valve "
                + str(index + 1)
                + " to change to direction 1"
            )
            self.deviceHandler.closeBallValve(index+5)
            self.updateState()

    def toggleHeater(self, index):
        if self.heaterButton[index].isChecked():
            ## Turn heater on
            logger.info("User requested heater " + str(index + 1) + " to turn on")
            self.heaterButton[index].setText("Turn Off")
            self.heaterState[index].setText("State: On")
        else:
            ##  Turn heater off
            logger.info("User requested heater " + str(index + 1) + " to turn off")
            self.heaterButton[index].setText("Turn On")
            self.heaterState[index].setText("State: Off")

    def togglePump(self, index):
        if self.pumpButton[index].isChecked():
            ## Turn pump on
            logger.info("User requested pump " + str(index + 1) + " to turn on")
            self.deviceHandler.enablePump(index)
            self.updateState()
        else:
            ## Turn pump off
            logger.info("User requested pump " + str(index + 1) + " to turn off")
            self.deviceHandler.disablePump(index)
            self.updateState()
