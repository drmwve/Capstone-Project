from gpiozero import  Device, OutputDevice, PWMOutputDevice, GPIOPinInUse

from ..utils import IS_RASPBERRY_PI

if IS_RASPBERRY_PI:
    from ..ads1x15.ads1x15 import ADS1115
    from w1thermsensor import *
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

    TEMP_SENSOR_IDS = [0, 1, 2] # Get actual IDs and add here
    if IS_RASPBERRY_PI:
        servoconnection = Connection(port="/dev/ttyAMA0", baudrate=57600)
        adc = ADS1115()
        tempsensors =  [W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, TEMP_SENSOR_IDS[0]),
                        W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, TEMP_SENSOR_IDS[1]),
                        W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, TEMP_SENSOR_IDS[2])]
    else:
        adc = None
        servoconnection = None
        tempsensors = None
    ADC_GAIN = 2/3
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
