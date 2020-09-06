from gpiozero import OutputDevice, PWMOutputDevice, AngularServo, Device #to control the input and output
from .BrewState import BrewState
from loguru import logger
from . import osconfig
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
        self.pumpGPIOs = [OutputDevice(n) for n in pumpGPIOs]
        self.heatingElements = [OutputDevice(n) for n in heatingElementGPIOs]
        self.threeWayBallValves = [OutputDevice(n) for n in threeWayBallValveGPIOs]
        if not osconfig.is_raspberry_pi():
            self.hopServo = AngularServo(ADCGPIO,pin_factory=osconfig.pwmPinFactory)
        else:
            self.hopServo = AngularServo(ADCGPIO)
        logger.debug(self.twoWayBallValves[0].pin_factory)
        self.brewState = BrewState()

    def openBallValve(self, index):
        # Set the brew state variable to false
        # logger.debug "open ball valve X" if sucessful
        GPIO.output(self.twoWayBallValveGPIOs[index-1],True)
        self.brewState.twoWayBallValves[index-1] = True
        logger.debug("Execution opened ball valve " + str(index))

    def closeBallValve(self, index):
        GPIO.output(self.twoWayBallValveGPIOs[index-1],False)
        self.brewState.twoWayBallValves[index-1] = False
        logger.debug("Excution closed 2 way ball valve" + str(index))

    def readTemperatureSensor(self, whichSensor):
        logger.debug("Execution read sensor " + str(whichSensor))

    def readFlowSensor(self, whichSensor):
        logger.debug("Excution read sensor " + str(whichSensor))

    def openPump(self, index):
         GPIO.output(self.pumpGPIOs[index-1],True)
         self.brewState.pump[index-1] = True
         logger.debug("Excution opened pump" + str(index))

    def closePump(self, index):
         GPIO.output(self.pumpGPIOs[index-1],False)
         self.brewState.pump[index-1] = False
         logger.debug("Excution closed pump" + str(index))

    def openHeatingElement(self, index):
        GPIO.output(self.heatingElementGPIOs[index-1],True)
        self.brewState.heatingElement[index-1] = True
        logger.debug("Excution turned on heating element" + str(index))

    def closeHeatingElement(self, index):
        GPIO.output(self.heatingElementGPIOs[index-1],False)
        self.brewState.heatingElement[index-1] = False
        logger.debug("Excution turned off heating element" + str(index))



    def openHopServo(self, index):
        GPIO.output(self.hopServoGPIOs[index-1],True)
        self.brewState.hopservo[index-1] = True
        logger.debug("Excution turned On the Hop Servo")

    def closeHopServo(self, index):
        GPIO.output(self.hopServoGPIOs[index-1],False)
        self.brewState.hopservo[index-1] = False
        logger.debug("Excution turned Off the Hop Servo")
