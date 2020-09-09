from gpiozero import AngularServo, Device, OutputDevice, PWMOutputDevice

from .osconfig import is_raspberry_pi
if is_raspberry_pi():
    from w1thermsensor import W1ThermSensor
else:
    from gpiozero.pins.mock import MockFactory, MockPWMPin


class PinHandler():
    """Low level class which directly interfaces with the Raspberry Pi pins. This gets passed up to the Device Handler which handles higher-level component control logic."""
    twoWayBallValveGPIOs = [25, 8, 7, 12, 16]
    threeWayBallValveGPIOs = [14, 15, 18, 23, 24]
    pumpGPIOs = [20, 21]
    heatingElementGPIOs = [26, 19, 13, 6]
    tempSensorGPIO = 9
    ADCGPIO = 11
    hopServoGPIO = 5

    # Only allow one Pin Handler
    _instance = None
    def __new__(cls):
        if PinHandler._instance is None:
            print("Creating the object")
            PinHandler._instance = super(PinHandler, PinHandler).__new__(
                PinHandler
            )
            # Put any initialization here::
            PinHandler._instance._connectPins()
        return PinHandler._instance

    def _connectPins(self):
        """Creates gpiozero objects for components based on pins specified at class level"""
        # this little bit of weirdness is a consequence of gpiozero's fake pin code being goofy
        self.pwmPinFactory = Device.pin_factory
        if not is_raspberry_pi():
            Device.pin_factory = MockFactory()
            self.pwmPinFactory = MockFactory(pin_class=MockPWMPin)

        self.heatingElements = [
            PWMOutputDevice(n, pin_factory=self.pwmPinFactory)
            for n in PinHandler.heatingElementGPIOs
        ]
        self.hopServo = AngularServo(
            PinHandler.ADCGPIO, pin_factory=self.pwmPinFactory
        )
        self.twoWayBallValves = [
            OutputDevice(n) for n in PinHandler.twoWayBallValveGPIOs
        ]
        self.pumps = [OutputDevice(n) for n in PinHandler.pumpGPIOs]
        self.threeWayBallValves = [
            OutputDevice(n) for n in PinHandler.threeWayBallValveGPIOs
        ]

        self.GPZeroComponents = (
            self.twoWayBallValves
            + self.threeWayBallValves
            + self.heatingElements
            + [self.hopServo]
            + self.pumps
        )

    def _releasePins(self):
        for device in self.GPZeroComponents:
            device.close()
