from gpiozero import Device, OutputDevice, PWMOutputDevice, GPIOPinInUse

from ..utils import IS_RASPBERRY_PI

if IS_RASPBERRY_PI:
    from ..ads1x15.ads1x15 import ADS1115
    from w1thermsensor import *
else:
    from gpiozero.pins.mock import MockFactory, MockPWMPin
from loguru import logger
from pyax12.connection import Connection
from loguru import logger


class Pins:
    """Low level class which directly interfaces with the Raspberry Pi pins. This gets passed up to the Device Handler which handles higher-level component control logic."""

    ballValveGPIOs = [5, 27, 22, 19, 26, 23, 24, 25, 20, 21]
    pumpGPIOs = [18, 17]
    heatingElementGPIOs = [12, 13]
    heatingElementSwitchGPIO = 16
    pins_initialized = False

    TEMP_SENSOR_IDS = [0, 1, 2]  # Get actual IDs and add here

    ADC_GAIN = 2 / 3
    ADC_VOLTAGE_SUPPLIED = 5

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
            if IS_RASPBERRY_PI:
                logger.info(W1ThermSensor.get_available_sensors())
                cls.servoconnection = Connection(port="/dev/ttyAMA0", baudrate=57600)
                cls.adc = ADS1115()
                cls.tempsensors = [sensor for sensor in W1ThermSensor.get_available_sensors()]
                for sensor in cls.tempsensors:
                    logger.info(f'Sensor ID: {sensor.id}')
            else:
                cls.adc = None
                cls.servoconnection = None
                cls.tempsensors = None
            cls.pwmPinFactory = Device.pin_factory
            if not IS_RASPBERRY_PI:
                Device.pin_factory = MockFactory()
                cls.pwmPinFactory = MockFactory(pin_class=MockPWMPin)

            cls.heatingElements = [
                PWMOutputDevice(n, pin_factory=cls.pwmPinFactory)
                for n in Pins.heatingElementGPIOs]

            cls.heatingElementSwitch = OutputDevice(Pins.heatingElementSwitchGPIO)
            cls.ballValves = [OutputDevice(n) for n in Pins.ballValveGPIOs]
            cls.pumps = [OutputDevice(n, active_high=False, initial_value=True) for n in Pins.pumpGPIOs]

            cls.GPZeroComponents = (
                    cls.ballValves + cls.heatingElements + cls.pumps
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
