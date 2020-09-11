from gpiozero import AngularServo, Device, OutputDevice, PWMOutputDevice

from ..osconfig import is_raspberry_pi
if is_raspberry_pi():
    from w1thermsensor import W1ThermSensor
else:
    from gpiozero.pins.mock import MockFactory, MockPWMPin
from loguru import logger

class Pins():
    """Low level class which directly interfaces with the Raspberry Pi pins. This gets passed up to the Device Handler which handles higher-level component control logic."""
    ballValveGPIOs = [25, 8, 7, 12, 16, 14, 15, 18, 23, 24]
    pumpGPIOs = [20, 21]
    heatingElementGPIOs = [26, 19, 13, 6]
    tempSensorGPIO = 9
    ADCGPIO = 11
    hopServoGPIO = 5
    pins_initialized = False

    def __init__(self):
        super().__init__()
        if not Pins.pins_initialized:
            self._connectPins()
            Pins.pins_initialized = True

    @classmethod
    def _connectPins(cls):
        """Creates gpiozero objects for components based on pins specified at class level"""
        # this little bit of weirdness is a consequence of gpiozero's fake pin code being goofy
        logger.debug("Connecting Pins")
        cls.pwmPinFactory = Device.pin_factory
        if not is_raspberry_pi():
            Device.pin_factory = MockFactory()
            cls.pwmPinFactory = MockFactory(pin_class=MockPWMPin)

        cls.heatingElements = [
            PWMOutputDevice(n, pin_factory=cls.pwmPinFactory)
            for n in Pins.heatingElementGPIOs
        ]
        cls.hopServo = AngularServo(
            Pins.ADCGPIO, pin_factory=cls.pwmPinFactory
        )
        cls.ballValves = [
            OutputDevice(n) for n in Pins.ballValveGPIOs
        ]
        cls.pumps = [OutputDevice(n) for n in Pins.pumpGPIOs]

        cls.GPZeroComponents = (
            cls.ballValves
            + cls.heatingElements
            + [cls.hopServo]
            + cls.pumps
        )

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

Pins._connectPins()