from gpiozero import Device, OutputDevice, PWMOutputDevice, GPIOPinInUse

from ..utils import IS_RASPBERRY_PI
from .ax import Ax12

if IS_RASPBERRY_PI:
    from ..ads1x15.ads1x15 import ADS1115
    from w1thermsensor import W1ThermSensor, Unit, Sensor
else:
    from gpiozero.pins.mock import MockFactory, MockPWMPin
from loguru import logger
from loguru import logger


class Pins:
    """Low level class which directly interfaces with the Raspberry Pi pins. This gets passed up to the Device Handler which handles higher-level component control logic."""

    ballValveGPIOs = [24,5,6,16,12,26,27,20,13,21]
    pumpGPIOs = [22,23]
    heatingElementGPIOs = [25,17]
    heatingElementSwitchGPIO = 7
    airPumpGPIO = 19
    pins_initialized = False

    TEMP_SENSOR_IDS = ["3c01d607c246",  "3c01d607933f", "3c01d607e8f2"]  # Get actual IDs and add here

    ADC_GAIN = 2 / 3
    ADC_VOLTAGE_SUPPLIED = 5

    SERVO_ID = 1

    def __init__(self):
        super().__init__()
        self._refreshPins()

    @classmethod
    def _connectPins(cls):
        """Creates gpiozero objects for components based on pins specified at class level"""
        if not Pins.pins_initialized:
            logger.debug("Connecting Pins")
            if IS_RASPBERRY_PI:
                cls.adc = ADS1115()
  
                cls.tempsensors = [W1ThermSensor(Sensor.DS18B20, id) for id in Pins.TEMP_SENSOR_IDS]
                for sensor in cls.tempsensors:
                    logger.info(f'Sensor ID: {sensor.id}')
                cls.servo = Ax12()
            else:
                cls.adc = None
                cls.servoconnection = None
                cls.tempsensors = None

            try:
                # this little bit of weirdness is a consequence of gpiozero's fake pin code being goofy

                cls.pwmPinFactory = Device.pin_factory
                if not IS_RASPBERRY_PI:
                    Device.pin_factory = MockFactory()
                    cls.pwmPinFactory = MockFactory(pin_class=MockPWMPin)

                cls.heatingElements = [
                    PWMOutputDevice(n, pin_factory=cls.pwmPinFactory)
                    for n in Pins.heatingElementGPIOs]
                cls.ballValves = [OutputDevice(n) for n in Pins.ballValveGPIOs]
                for index, valve in enumerate(cls.ballValves):
                    if (index >4):
                        valve.close()
                cls.airPump = OutputDevice(Pins.airPumpGPIO)
                cls.airPump.close()
                cls.pumps = [OutputDevice(n, active_high=False)
                    for n in Pins.pumpGPIOs]

                logger.debug(f'Pump states: {[x.value for x in cls.pumps]}')
                cls.heatingElementSwitch = OutputDevice(Pins.heatingElementSwitchGPIO)

                cls.GPZeroComponents = (
                        cls.ballValves + cls.heatingElements + cls.pumps
                )

            except GPIOPinInUse as e:
                print(e)

    @classmethod
    def _releasePins(cls):
        try:
            for device in cls.GPZeroComponents:
                device.close()

            Pins.pins_initialized = False
        except:
            pass

    @classmethod
    def _refreshPins(cls):
        logger.debug("Pins refreshed")
        cls._releasePins()
        cls._connectPins()
