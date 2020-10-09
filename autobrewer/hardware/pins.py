from gpiozero import AngularServo, Device, OutputDevice, PWMOutputDevice, GPIOPinInUse

from ..Adafruit_ADS1x15 import ADS1115
from ..utils import IS_RASPBERRY_PI

if IS_RASPBERRY_PI:
    from w1thermsensor import W1ThermSensor
else:
    from gpiozero.pins.mock import MockFactory, MockPWMPin
from loguru import logger
from pyax12.connection import Connection


class Pins:
    """Low level class which directly interfaces with the Raspberry Pi pins. This gets passed up to the Device Handler which handles higher-level component control logic."""

    ballValveGPIOs = [25, 8, 7, 12, 16, 17, 27, 22, 23, 24]
    pumpGPIOs = [20, 21]
    heatingElementGPIOs = [26, 19, 13, 6]
    tempSensorGPIO = 9
    pins_initialized = False

    adc = ADS1115()
    ADC_GAIN = 2/3
    ADC_VOLTAGE_SUPPLIED = 5

    servoconnection = Connection(port="/dev/ttyAMA0", baudrate=57600)
    SERVO_ID = 1

    def __init__(self):
        super().__init__()
        if not Pins.pins_initialized:
            self._connectPins()
            Pins.pins_initialized = True

    @classmethod
    def _connectPins(cls):
        """Creates gpiozero objects for components based on pins specified at class level"""
        try:
            # this little bit of weirdness is a consequence of gpiozero's fake pin code being goofy
            logger.debug("Connecting Pins")
            cls.pwmPinFactory = Device.pin_factory
            if not IS_RASPBERRY_PI:
                Device.pin_factory = MockFactory()
                cls.pwmPinFactory = MockFactory(pin_class=MockPWMPin)

            cls.heatingElements = [
                PWMOutputDevice(n, pin_factory=cls.pwmPinFactory)
                for n in Pins.heatingElementGPIOs
            ]
            cls.ballValves = [OutputDevice(n) for n in Pins.ballValveGPIOs]
            cls.pumps = [OutputDevice(n) for n in Pins.pumpGPIOs]

            cls.GPZeroComponents = (
                cls.ballValves + cls.heatingElements + [cls.hopServo] + cls.pumps
            )
        except GPIOPinInUse:
            pass

    @classmethod
    def _releasePins(cls):
        try:
            for device in cls.GPZeroComponents:
                device.close()
        except:
            pass

    @classmethod
    def _refreshPins(cls):
        logger.debug("Pins refreshed")
        cls._releasePins()
        cls._connectPins()
