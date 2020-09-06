from gpiozero import OutputDevice, PWMOutputDevice, AngularServo, Device #to control the input and output
from .BrewState import BrewState
from loguru import logger
from . import osconfig
from . import utils
#from w1thermsensor import W1ThermSensor, Unit

# Signals: step completed

class ControlHandler():
    def __init__(self):

        twoWayBallValveGPIOs = [14, 15, 18,23, 24]
        pumpGPIOs = [20, 21]
        heatingElementGPIOs = [26,19, 13,6]
        threeWayBallValveGPIOs = [25, 8, 7, 12, 16]
        tempSensorGPIO = 9
        ADCGPIO = 11
        hopServoGPIO = 5

        self.twoWayBallValves = [OutputDevice(n) for n in twoWayBallValveGPIOs]
        self.pumps = [OutputDevice(n) for n in pumpGPIOs]
        self.threeWayBallValves = [OutputDevice(n) for n in threeWayBallValveGPIOs]
        #this little bit of weirdness is a consequence of gpiozero's fake pin code being goofy
        if not osconfig.is_raspberry_pi():
            self.heatingElements = [PWMOutputDevice(n, pin_factory=osconfig.pwmPinFactory) for n in heatingElementGPIOs]
            self.hopServo = AngularServo(ADCGPIO,pin_factory=osconfig.pwmPinFactory)
        else:
            self.hopServo = AngularServo(ADCGPIO)
        self.brewState = BrewState()

    @utils.disable_for_a_while_after_called(disable_time=5)
    def open2WBallValve(self, index):
        # Set the brew state variable to false
        # logger.debug "open ball valve X" if sucessful
        self.twoWayBallValves[index].off()
        self.brewState.twoWayBallValves[index] = True
        logger.debug(f'Excution opened 2 way ball valve {index}')

    def close2WBallValve(self, index):
        self.twoWayBallValves[index].on()
        self.brewState.twoWayBallValves[index] = False
        logger.debug(f'Excution closed 2 way ball valve {index}')

    def open3WBallValve(self, index):
        # Set the brew state variable to false
        # logger.debug "open ball valve X" if sucessful
        self.threeWayBallValves[index].off()
        self.brewState.threeWayBallValves[index] = True
        logger.debug("Execution opened ball valve " + str(index))
        logger.debug(f'Excution opened 3 way ball valve {index}')

    def close3WBallValve(self, index):
        self.threeWayBallValves[index].on()
        self.brewState.threeWayBallValves[index] = False
        logger.debug(f'Excution closed 3 way ball valve {index}')

    def readTemperatureSensor(self, whichSensor):
        logger.debug("Execution read sensor " + str(whichSensor))

    def openPump(self, index):
         self.pumps[index].on()
         self.brewState.pump[index] = True
         logger.debug(f'Excution opened pump {str(index)}')

    def closePump(self, index):
         self.pumps[index].off()
         self.brewState.pump[index] = False
         logger.debug(f'Excution closed pump {str(index)}')

    def enableHeatingElement(self, index):
        self.heatingElements[index].on()
        self.brewState.heatingElement[index] = True
        logger.debug("Excution turned on heating element" + str(index))

    def disableHeatingElement(self, index):
        self.heatingElements[index].off()
        self.brewState.heatingElement[index] = False
        logger.debug("Excution turned off heating element" + str(index))

    def moveHopServo(self, angle):
        if angle in range(0,360):
            self.hopServo.angle = angle