from PySide2 import QtCore, QtGui, QtWidgets
from loguru import logger
from .DeviceStatusControlsGUI import Ui_DeviceStatusControls


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
        pass

    ## Defining button functions
    def toggleBallValve(self, index):
        if self.ballValveButton[index].isChecked():
            ## Open ball valve
            logger.info("User requested ball valve " + str(index + 1) + " to open")
            self.ballValveButton[index].setText("Close")
            self.ballValveState[index].setText("State: Open")
        else:
            ## Close ball valve
            logger.info("User requested ball valve " + str(index + 1) + " to close")
            self.ballValveButton[index].setText("Open")
            self.ballValveState[index].setText("State: Closed")

    def toggleThreeWay(self, index):
        if self.threeWayValveButton[index].isChecked():
            ## Change to direction 2
            logger.info(
                "User requested three way valve "
                + str(index + 1)
                + " to change to direction 2"
            )
            self.threeWayValveState[index].setText("State: Direction 2")
        else:
            ## Change to direction 1
            logger.info(
                "User requested three way valve "
                + str(index + 1)
                + " to change to direction 1"
            )
            self.threeWayValveState[index].setText("State: Direction 1")

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
            self.pumpButton[index].setText("Turn Off")
            self.pumpState[index].setText("State: On")
        else:
            ## Turn pump off
            logger.info("User requested pump " + str(index + 1) + " to turn off")
            self.pumpButton[index].setText("Turn On")
            self.pumpState[index].setText("State: Off")
