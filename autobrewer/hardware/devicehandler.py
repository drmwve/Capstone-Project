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

    @classmethod
    def _createValvePaths(cls):
        """Defines paths which must be open for a pump to run without forming a vacuum. The valvepaths variable is a
        dictionary of dictionaries, describing the indexes of the valves which must either be opened or closed for
        each path.

        To add paths, add them in the main valvepaths variable (both open and close must be defined, even if they're
        empty) and then add relevant path names to the pumpvalvepathmap tuple in the position of the index of the
        relevant pump
        """
        cls.valvepaths = {
            "HLTtoMT": {"open": [1], "close": [6]},
            "MTRecirc": {"open": [2, 6], "close": [7]},
            "MTtoBK": {"open": [2, 3, 7], "close": [8, 9]},
            "BKWhirl": {"open": [3, 4, 8], "close": [9]},
            "BKDrain": {"open": [4, 8, 9], "close": []},
        }
        cls.pumpvalvepathmap = (
            ("HLTtoMT", "MTRecirc"),
            ("MTtoBK", "BKWhirl", "BKDrain"),
        )

    @classmethod
    def openValvePath(cls, pathname: str):
        for valveindex in cls.valvepaths[pathname]["open"]:
            cls.openBallValve(valveindex)
        for valveindex in cls.valvepaths[pathname]["close"]:
            cls.closeBallValve(valveindex)

    @classmethod
    def emitState(cls):
        cls.signalState.emit(cls.hardwareState)

    @classmethod
    def getState(cls) -> HardwareState:
        return cls.hardwareState

    @classmethod
    def shutdown(cls):
        logger.info("Shutting all system components off")
        cls.disableAllPumps()
        cls.closeAllBallValves()
        cls.disableAllHeatingElements()

    @classmethod
    def resetFlowControl(cls):
        cls.disableAllPumps()
        cls.closeAllBallValves()
        logger.info("Shut down all liquid flow")

    @classmethod
    def disableAllHeatingElements(cls):
        logger.debug("Disabling all heating elements")
        for index, _ in enumerate(cls.heatingElements):
            cls.disableHeatingElement(index)

    @classmethod
    def disableAllPumps(cls):
        logger.debug("Disabling all pumps")
        for index, _ in enumerate(cls.pumps):
            cls.disablePump(index)

    @classmethod
    def closeAllBallValves(cls):
        logger.debug("Closing all ball valves")
        for index, _ in enumerate(cls.ballValves):
            cls.closeBallValve(index)

    @classmethod
    def setHopServoPosition(cls, angle: int):
        if angle in range(0, 360):
            cls.hopServo.angle = angle
            cls.hardwareState.hopServo = angle
        else:
            raise ComponentControlError("Invalid servo angle selected")

    @classmethod
    def openBallValve(cls, index: int):
        cls._setBallValveState(index, True)

    @classmethod
    def closeBallValve(cls, index: int):
        cls._setBallValveState(index, False)

    @classmethod
    def enablePump(cls, index: int):
        cls._setPumpState(index, True)

    @classmethod
    def disablePump(cls, index: int):
        cls._setPumpState(index, False)

    @classmethod
    def enableHeatingElement(cls, index: int):
        cls._setHeatingElementValue(index, 1)

    @classmethod
    def disableHeatingElement(cls, index: int):
        cls._setHeatingElementValue(index, 0)

    @classmethod
    def setHeatingElementPWM(cls, index: int, value: float):
        cls._setHeatingElementValue(index, value)

    @classmethod
    def _setBallValveState(cls, index: int, state: bool):
        cls.ballValves[index].value = state
        cls.hardwareState.ballValves[index] = state
        logger.debug(f'Set ball valve {index} to {"On" if state else "Off"}')

    @classmethod
    def _setPumpState(cls, pumpindex: int, state: bool):
        # check if a valid path is open for either pump
        if (not state) or (state and cls._pumpHasOpenPath(pumpindex)):
            cls.pumps[pumpindex].value = state
            cls.hardwareState.pumps[pumpindex] = state
            logger.debug(f'Set pump {pumpindex} to {"On" if state else "Off"}')
        # raise an error otherwise
        else:
            raise ComponentControlError(
                f"Cannot turn pump {pumpindex} on. There is no suitable ball valve path open"
            )

    @classmethod
    def _pumpHasOpenPath(cls, pumpindex: int) -> bool:
        pumphasopenpath = False
        for valvepath in cls.pumpvalvepathmap[pumpindex]:
            pathopen = True
            for valveindex in cls.valvepaths[valvepath]["open"]:
                if cls.ballValves[valveindex].value != 1:
                    pathopen = False
            for valveindex in cls.valvepaths[valvepath]["close"]:
                if cls.ballValves[valveindex].value != 0:
                    pathopen = False
            if pathopen:
                pumphasopenpath = True
                break
        return pumphasopenpath

    @classmethod
    def _setHeatingElementValue(cls, index: int, value: float):
        cls.heatingElements[index].value = value
        cls.hardwareState.heatingElements[index] = value
        logger.debug(f"Set heating element {index} to {value}")

    @classmethod
    def _readSensors(cls):
        # read the sensors and save the values here
        for temp in cls.hardwareState.temperatures:
            cls.hardwareState.temperatures[temp] = 0
        for volume in cls.hardwareState.temperatures:
            cls.hardwareState.volumes[volume] = 0


DeviceHandler._createValvePaths()
