import time

from loguru import logger
from PySide2.QtCore import QObject, Signal

from ..ads1x15 import *
from .hardwarestate import HardwareState
from ..exceptions import ComponentControlError
from .pins import Pins


# To do: Implement hop servo and sensor code


class DeviceHandler(QObject, Pins):
    """Controls the components and provides checking of invalid states for safety, such as preventing the opening of a pump
    when there is no open ball valve path or running a heating element in an empty kettle.
    This class has many functions for controlling components in logical groups and individually.
    The functions start with the large group controls and break down into low-level private controls.

    NOTE: Because this class controls a single physical hardware system, it is implemented entirely using class methods.

    Attributes:
        emitState: Emits a signal with the current HardwareState
        getState: Returns the current HardwareState
        shutdown: Disables all heating elements and pumps and returns ball valves to de-energized position
        resetFlowControl: Disables all pumps and returns ball valves to de-energized position
        openValves*: Opens particular ball valve paths
        set*/open*/close*/enable*/disable*: Individual component control functions
    """

    signalState = Signal(HardwareState)
    hardwareState = HardwareState()

    def __init__(self):
        self._connectPins()
        self._createValvePaths()

    def _createValvePaths(self):
        """Defines paths which must be open for a pump to run without forming a vacuum. The valvepaths variable is a
        dictionary of dictionaries, describing the indexes of the valves which must either be opened or closed for
        each path.

        To add paths, add them in the main valvepaths variable (both open and close must be defined, even if they're
        empty) and then add relevant path names to the pumpvalvepathmap tuple in the position of the index of the
        relevant pump
        """
        self.valvepaths = {
            "FillHLT": {"open": [0], "close": [5]},
            "HLTtoMT": {"open": [1], "close": [6]},
            "MTRecirc": {"open": [2, 6], "close": [7]},
            "MTtoBK": {"open": [2, 3, 7], "close": [8, 9]},
            "BKWhirl": {"open": [3, 4, 8], "close": [9]},
            "BKDrain": {"open": [4, 8, 9], "close": []},
        }
        self.pumpvalvepathmap = (
            ("FillHLT", "HLTtoMT", "MTRecirc"),
            ("MTtoBK", "BKWhirl", "BKDrain"),
        )

    def openValvePath(self, pathname: str):
        for valveindex in self.valvepaths[pathname]["open"]:
            self.openBallValve(valveindex)
        for valveindex in self.valvepaths[pathname]["close"]:
            self.closeBallValve(valveindex)

    def emitState(self):
        self.signalState.emit(self.hardwareState)

    def getState(self) -> HardwareState:
        return self.hardwareState

    def shutdown(self):
        logger.info("Shutting all system components off")
        self.disableAllPumps()
        self.closeAllBallValves()
        self.disableAllHeatingElements()

    def resetFlowControl(self):
        self.disableAllPumps()
        self.closeAllBallValves()
        logger.info("Shut down all liquid flow")

    def disableAllHeatingElements(self):
        logger.debug("Disabling all heating elements")
        for index, _ in enumerate(self.heatingElements):
            self.disableHeatingElement(index)

    def disableAllPumps(self):
        logger.debug("Disabling all pumps")
        for index, _ in enumerate(self.pumps):
            self.disablePump(index)

    def closeAllBallValves(self):
        logger.debug("Closing all ball valves")
        for index, _ in enumerate(self.ballValves):
            self.closeBallValve(index)

    def setHopServoPosition(self, angle: int):
        if angle in range(0, 360):
            self.hopServo.angle = angle
            self.hardwareState.hopServo = angle
        else:
            raise ComponentControlError("Invalid servo angle selected")

    def openBallValve(self, index: int):
        self._setBallValveState(index, True)

    def closeBallValve(self, index: int):
        self._setBallValveState(index, False)

    def enablePump(self, index: int):
        self._setPumpState(index, True)

    def disablePump(self, index: int):
        self._setPumpState(index, False)

    def enableHeatingElement(self, index: int):
        self._setHeatingElementValue(index, 1)

    def disableHeatingElement(self, index: int):
        self._setHeatingElementValue(index, 0)

    def setHeatingElementPWM(self, index: int, value: float):
        self._setHeatingElementValue(index, value)

    def _setBallValveState(self, index: int, state: bool):
        self.ballValves[index].value = state
        self.hardwareState.ballValves[index] = state
        logger.debug(f'Set ball valve {index} to {"On" if state else "Off"}')

    def _setPumpState(self, pumpindex: int, state: bool):
        # check if a valid path is open for either pump
        if (not state) or (state and self._pumpHasOpenPath(pumpindex)):
            self.pumps[pumpindex].value = state
            self.hardwareState.pumps[pumpindex] = state
            logger.debug(f'Set pump {pumpindex} to {"On" if state else "Off"}')
        # raise an error otherwise
        else:
            raise ComponentControlError(
                f"Cannot turn pump {pumpindex} on. There is no suitable ball valve path open"
            )

    def _pumpHasOpenPath(self, pumpindex: int) -> bool:
        pumphasopenpath = False
        for valvepath in self.pumpvalvepathmap[pumpindex]:
            pathopen = True
            for valveindex in self.valvepaths[valvepath]["open"]:
                if self.ballValves[valveindex].value != 1:
                    pathopen = False
            for valveindex in self.valvepaths[valvepath]["close"]:
                if self.ballValves[valveindex].value != 0:
                    pathopen = False
            if pathopen:
                pumphasopenpath = True
                break
        return pumphasopenpath

    def _setHeatingElementValue(self, index: int, value: float):
        self.heatingElements[index].value = value
        self.hardwareState.heatingElements[index] = value
        logger.debug(f"Set heating element {index} to {value}")

    def _readSensors(self):
        # read the sensors and save the values here
        for temp in self.hardwareState.temperatures:
            self.hardwareState.temperatures[temp] = 0
        for volume in self.hardwareState.temperatures:
            self.hardwareState.volumes[volume] = 0

