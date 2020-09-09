import time

from loguru import logger
from PySide2.QtCore import QObject, Signal

from .ads1x15 import *
from .BrewState import BrewState
from .exceptions import ComponentControlError
from .pinhandler import PinHandler

# To do: Implement hop servo and sensor code
class DeviceHandler(QObject, PinHandler):
    """Controls the components and provides checking of invalid states for safety, such as preventing the opening of a pump
    when there is no open ball valve path or running a heating element in an empty kettle.
    This class has many functions for controlling components in logical groups and individually.
    The functions start with the large group controls and break down into low-level private controls.

    Attributes:
        emitState: Emits a signal with the current BrewState
        getState: Returns the current BrewState
        shutdown: Disables all heating elements and pumps and returns ball valves to de-energized position
        resetFlowControl: Disables all pumps and returns ball valves to de-energized position
        openValves*: Opens particular ball valve paths
        set*/open*/close*/enable*/disable*: Individual component control functions"""

    signalState = Signal(BrewState)

    # Only allow one Control Handler
    _instance = None

    def __new__(cls):
        if DeviceHandler._instance is None:
            logger.warning("Hop servo needs tuning")
            DeviceHandler._instance = super(DeviceHandler, DeviceHandler).__new__(
                DeviceHandler
            )
            # Put any initialization here::
            DeviceHandler._instance.brewState = BrewState()
        return DeviceHandler._instance

    def emitState(self):
        self.signalState.emit(self.brewState)

    def getState(self) -> BrewState:
        return self.brewState

    def shutdown(self):
        logger.info("Shutting all system components off")
        self.disableAllPumps()
        self.disableAllBallValves()
        self.disableAllHeatingElements()

    def resetFlowControl(self):
        self.disableAllPumps()
        self.disableAllBallValves()
        logger.info("Shut down all liquid flow")

    def openValvesHLTtoMT(self):
        logger.debug("Opening valve path from HLT to Mash Tun")
        self.open2WBallValve(1)
        self.close3WBallValve(1)

    def openValvesMTRecirc(self):
        logger.debug("Opening valve path for MT recirculation")
        self.open2WBallValve(2)
        self.close3WBallValve(2)
        self.open3WBallValve(1)

    def openValvesMTtoBK(self):
        logger.debug("Opening valve path from MT to BK")
        self.open2WBallValve(2)
        self.open3WBallValve(2)
        self.close3WBallValve(3)
        self.close3WBallValve(4)
        self.open2WBallValve(3)

    def openValvesBKWhirl(self):
        logger.debug("Opening valve path for BK whirl")
        self.open2WBallValve(4)
        self.open3WBallValve(3)
        self.close3WBallValve(4)
        self.open2WBallValve(3)

    def openValvesBKDrain(self):
        logger.debug("Opening valve path for BK drain")
        self.open2WBallValve(4)
        self.open3WBallValve(3)
        self.open3WBallValve(4)

    def disableAllHeatingElements(self):
        logger.debug("Disabling all heating elements")
        for index, _ in enumerate(self.heatingElements):
            self.disableHeatingElement(index)

    def disableAllPumps(self):
        logger.debug("Disabling all pumps")
        for index, _ in enumerate(self.pumps):
            self.disablePump(index)

    def disableAllBallValves(self):
        logger.debug("Closing all ball valves")
        for index, _ in enumerate(self.twoWayBallValves):
            self.close2WBallValve(index)
        for index, _ in enumerate(self.threeWayBallValves):
            self.close3WBallValve(index)

    def setHopServoPosition(self, angle: int):
        if angle in range(0, 360):
            self.hopServo.angle = angle
            self.brewState.hopServo = angle

    def open2WBallValve(self, index: int):
        self._set2WayState(index, True)

    def close2WBallValve(self, index: int):
        self._set2WayState(index, False)

    def open3WBallValve(self, index: int):
        self._set3WayState(index, True)

    def close3WBallValve(self, index: int):
        self._set3WayState(index, False)

    def enablePump(self, index: int):
        self._setPumpState(index, True)

    def disablePump(self, index: int):
        self._setPumpState(index, False)

    def enableHeatingElement(self, index: int):
        self._setHeatingElementValue(index, 1)

    def disableHeatingElement(self, index: int):
        self._setHeatingElementValue(index, 0)

    def setHeatingElementPWM(self, index: int, value: int):
        self._setHeatingElementValue(index, value)

    def _set2WayState(self, index: int, state: bool):
        self.twoWayBallValves[index].value = state
        self.brewState.twoWayBallValves[index] = state
        logger.debug(f'Set 2-way ball valve {index} to {"On" if state else "Off"}')

    def _set3WayState(self, index: int, state: bool):
        self.threeWayBallValves[index].value = state
        self.brewState.threeWayBallValves[index] = state
        logger.debug(
            f'Set 3-way ball valve {index} to {"Direction 1" if state else "Direction 2"}'
        )

    def _setPumpState(self, index: int, state: bool):
        # check if a valid path is open for either pump
        pump0ValidPathOpen = (
            self.brewState._pathOpenHLTtoMT() or self.brewState._pathOpenMTRecirc()
        )
        pump1ValidPathOpen = (
            self.brewState._pathOpenMTtoBK()
            or self.brewState._pathOpenBKWhirl()
            or self.brewState._pathOpenBKDrain()
        )
        # disable the pumps if that's requested, or enable the selected pump if there's an open path
        if (
            (not state)
            or (index == 0 and pump0ValidPathOpen)
            or (index == 1 and pump1ValidPathOpen)
        ):
            self.pumps[index] = state
            self.brewState.pumps[index] = state
            logger.debug(f'Set pump {index} to {"On" if state else "Off"}')
        # raise an error otherwise
        else:
            raise ComponentControlError(
                f"Cannot turn pump {index} on. There is no suitable ball valve path open"
            )

    def _setHeatingElementValue(self, index: int, value: int):
        self.heatingElements[index].value = value
        self.brewState.heatingElements[index] = value
        logger.debuf(f"Set heating element {index} to {value}")

    def _readSensors(self):
        # read the sensors and save the values here
        for temp in self.brewState.temperatures:
            self.brewState.temperatures[temp] = 0
        for volume in self.brewState.temperatures:
            self.brewState.volumes[volume] = 0