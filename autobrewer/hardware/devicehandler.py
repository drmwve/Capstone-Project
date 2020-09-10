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
        set*/open*/close*/enable*/disable*: Individual component control functions"""

    signalState = Signal(HardwareState)

    hardwareState = HardwareState()

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
        cls.disableAllBallValves()
        cls.disableAllHeatingElements()

    @classmethod
    def resetFlowControl(cls):
        cls.disableAllPumps()
        cls.disableAllBallValves()
        logger.info("Shut down all liquid flow")

    @classmethod
    def openValvesHLTtoMT(cls):
        logger.debug("Opening valve path from HLT to Mash Tun")
        cls.open2WBallValve(1)
        cls.close3WBallValve(1)

    @classmethod
    def openValvesMTRecirc(cls):
        logger.debug("Opening valve path for MT recirculation")
        cls.open2WBallValve(2)
        cls.close3WBallValve(2)
        cls.open3WBallValve(1)

    @classmethod
    def openValvesMTtoBK(cls):
        logger.debug("Opening valve path from MT to BK")
        cls.open2WBallValve(2)
        cls.open3WBallValve(2)
        cls.close3WBallValve(3)
        cls.close3WBallValve(4)
        cls.open2WBallValve(3)

    @classmethod
    def openValvesBKWhirl(cls):
        logger.debug("Opening valve path for BK whirl")
        cls.open2WBallValve(4)
        cls.open3WBallValve(3)
        cls.close3WBallValve(4)
        cls.open2WBallValve(3)

    @classmethod
    def openValvesBKDrain(cls):
        logger.debug("Opening valve path for BK drain")
        cls.open2WBallValve(4)
        cls.open3WBallValve(3)
        cls.open3WBallValve(4)

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
    def disableAllBallValves(cls):
        logger.debug("Closing all ball valves")
        for index, _ in enumerate(cls.twoWayBallValves):
            cls.close2WBallValve(index)
        for index, _ in enumerate(cls.threeWayBallValves):
            cls.close3WBallValve(index)

    @classmethod
    def setHopServoPosition(cls, angle: int):
        if angle in range(0, 360):
            cls.hopServo.angle = angle
            cls.hardwareState.hopServo = angle

    @classmethod
    def open2WBallValve(cls, index: int):
        cls._set2WayState(index, True)

    @classmethod
    def close2WBallValve(cls, index: int):
        cls._set2WayState(index, False)

    @classmethod
    def open3WBallValve(cls, index: int):
        cls._set3WayState(index, True)

    @classmethod
    def close3WBallValve(cls, index: int):
        cls._set3WayState(index, False)

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
    def setHeatingElementPWM(cls, index: int, value: int):
        cls._setHeatingElementValue(index, value)

    @classmethod
    def _set2WayState(cls, index: int, state: bool):
        cls.twoWayBallValves[index].value = state
        cls.hardwareState.twoWayBallValves[index] = state
        logger.debug(f'Set 2-way ball valve {index} to {"On" if state else "Off"}')

    @classmethod
    def _set3WayState(cls, index: int, state: bool):
        cls.threeWayBallValves[index].value = state
        cls.hardwareState.threeWayBallValves[index] = state
        logger.debug(
            f'Set 3-way ball valve {index} to {"Direction 1" if state else "Direction 2"}'
        )

    @classmethod
    def _setPumpState(cls, index: int, state: bool):
        # check if a valid path is open for either pump
        pump0ValidPathOpen = (
            cls.hardwareState._pathOpenHLTtoMT() or cls.hardwareState._pathOpenMTRecirc()
        )
        pump1ValidPathOpen = (
            cls.hardwareState._pathOpenMTtoBK()
            or cls.hardwareState._pathOpenBKWhirl()
            or cls.hardwareState._pathOpenBKDrain()
        )
        # disable the pumps if that's requested, or enable the selected pump if there's an open path
        if (
            (not state)
            or (index == 0 and pump0ValidPathOpen)
            or (index == 1 and pump1ValidPathOpen)
        ):
            cls.pumps[index] = state
            cls.hardwareState.pumps[index] = state
            logger.debug(f'Set pump {index} to {"On" if state else "Off"}')
        # raise an error otherwise
        else:
            raise ComponentControlError(
                f"Cannot turn pump {index} on. There is no suitable ball valve path open"
            )

    @classmethod
    def _setHeatingElementValue(cls, index: int, value: int):
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
