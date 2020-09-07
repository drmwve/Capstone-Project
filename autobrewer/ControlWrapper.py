import time

from gpiozero import AngularServo, Device, OutputDevice, PWMOutputDevice
from loguru import logger

from .ads1x15 import *
from .BrewState import BrewState
from .exceptions import ComponentControlException
from .osconfig import is_raspberry_pi
from .utils import set_windup_time

if is_raspberry_pi():
    from w1thermsensor import W1ThermSensor, Unit
else:
    from gpiozero.pins.mock import MockFactory, MockPWMPin

# Signals: step completed


class DeviceHandler:
    twoWayBallValveGPIOs = [14, 15, 18, 23, 24]
    pumpGPIOs = [20, 21]
    heatingElementGPIOs = [26, 19, 13, 6]
    threeWayBallValveGPIOs = [25, 8, 7, 12, 16]
    tempSensorGPIO = 9
    ADCGPIO = 11
    hopServoGPIO = 5

    # Only allow one Control Handler
    _instance = None

    def __new__(cls):
        if DeviceHandler._instance is None:
            print("Creating the object")
            DeviceHandler._instance = super(DeviceHandler, DeviceHandler).__new__(
                DeviceHandler
            )
            # Put any initialization here::
            DeviceHandler._instance._connectPins()
            DeviceHandler._instance.brewState = BrewState()
        return DeviceHandler._instance

    def open2WBallValve(self, index):
        # Set the brew state variable to false
        self._set2WayState(index, True)

    def close2WBallValve(self, index):
        self._set2WayState(index, False)

    def open3WBallValve(self, index):
        self._set3WayState(index, True)

    def close3WBallValve(self, index):
        self._set3WayState(index, False)

    def readTemperatureSensor(self, whichSensor):
        logger.debug("Execution read sensor " + str(whichSensor))

    def openPump(self, index):
        self.pumps[index].on()
        self.brewState.pump[index] = True
        logger.debug(f"Excution opened pump {str(index)}")

    def closePump(self, index):
        self.pumps[index].off()
        self.brewState.pump[index] = False
        logger.debug(f"Excution closed pump {str(index)}")

    def enableHeatingElement(self, index):
        self.heatingElements[index].on()
        self.brewState.heatingElement[index] = True
        logger.debug("Excution turned on heating element" + str(index))

    def disableHeatingElement(self, index):
        self.heatingElements[index].off()
        self.brewState.heatingElement[index] = False
        logger.debug("Excution turned off heating element" + str(index))

    def setHeatingElementPWM(self, index):
        self.heatingElements[index].value = index

    def moveHopServo(self, angle):
        if angle in range(0, 360):
            self.hopServo.angle = angle

    def _set2WayState(self, index, state):
        self.twoWayBallValves[index].value = state
        self.brewState.twoWayBallValves[index] = state
        logger.debug(f'Set 2-way ball valve {index} to {"On" if state else "Off"}')

    def _set3WayState(self, index, state):
        self.threeWayBallValves[index].value = state
        self.brewState.threeWayBallValves[index] = state
        logger.debug(
            f'Set 3-way ball valve {index} to {"Direction 1" if state else "Direction 2"}'
        )

    def _releasePins(self):
        for device in self.GPZeroComponents:
            device.close()

    def _connectPins(self):
        # this little bit of weirdness is a consequence of gpiozero's fake pin code being goofy
        self.pwmPinFactory = Device.pin_factory
        if not is_raspberry_pi():
            Device.pin_factory = MockFactory()
            self.pwmPinFactory = MockFactory(pin_class=MockPWMPin)

        self.heatingElements = [
            PWMOutputDevice(n, pin_factory=self.pwmPinFactory)
            for n in DeviceHandler.heatingElementGPIOs
        ]
        self.hopServo = AngularServo(
            DeviceHandler.ADCGPIO, pin_factory=self.pwmPinFactory
        )
        self.twoWayBallValves = [
            OutputDevice(n) for n in DeviceHandler.twoWayBallValveGPIOs
        ]
        self.pumps = [OutputDevice(n) for n in DeviceHandler.pumpGPIOs]
        self.threeWayBallValves = [
            OutputDevice(n) for n in DeviceHandler.threeWayBallValveGPIOs
        ]
        self.GPZeroComponents = (
            self.twoWayBallValves
            + self.threeWayBallValves
            + self.heatingElements
            + [self.hopServo]
            + self.pumps
        )
