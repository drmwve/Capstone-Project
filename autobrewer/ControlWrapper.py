import RPi.GPIO as GPIO #to control the input and output
from .BrewState import BrewState
GPIO.setup(1,GPIO.OUT) #2 way valve number 1

# Signals: step completed

class ControlHandler():
    def __init__(self):
        self.twoWayBallValveGPIOs = [14, 15, 18,23, 24]
        self.pumpGPIOs = [20., 21]
        self.heatingElementGPIOs = [6, 13, 19, 26]
        self.threeWayBallValveGPIOs = [25, 8, 7, 12, 16]
        self.liquidSensorGPIOs = [22]
        self.tempSensorGPIOs = [9, 27]
        self.hopServoGPIOs = [10]
        self.flowSensorGPIOs = [11, 5]
        self.brewState = BrewState()


    def openBallValve(self, index):
        # Set the brew state variable to false
        # Print "open ball valve X" if sucessful
        GPIO.output(self.twoWayBallValveGPIOs[index-1],True)
        self.brewState.twoWayBallValves[index-1] = True
        print("Execution opened ball valve " + str(index))

    def closeBallValve(self, index):
        GPIO.output(self.twoWayBallValveGPIOs[index-1],False)
        self.brewState.twoWayBallValves[index-1] = False
        print("Excution closed 2 way ball valve" + str(index))

    def readTemperatureSensor(self, whichSensor):
        print("Execution read sensor " + str(whichSensor))

    def readFlowSensor(self, whichSensor):
        print("Excution read sensor " + str(whichSensor))

    def openPump(self, index):
         GPIO.output(self.pumpGPIOs[index-1],True)
         self.brewState.pump[index-1] = True
         print("Excution opened pump" + str(index))

    def closePump(self, index):
         GPIO.output(self.pumpGPIOs[index-1],False)
         self.brewState.pump[index-1] = False
         print("Excution closed pump" + str(index))

    def openHeatingElement(self, index):
        GPIO.output(self.heatingElementGPIOs[index-1],True)
        self.brewState.heatingElement[index-1] = True
        print("Excution turned on heating element" + str(index))

    def closeHeatingElement(self, index):
        GPIO.output(self.heatingElementGPIOs[index-1],False)
        self.brewState.heatingElement[index-1] = False
        print("Excution turned off heating element" + str(index))



    def openHopServo(self, index):
        GPIO.output(self.hopServoGPIOs[index-1],True)
        self.brewState.hopservo[index-1] = True
        print("Excution turned On the Hop Servo")

    def closeHopServo(self, index):
        GPIO.output(self.hopServoGPIOs[index-1],False)
        self.brewState.hopservo[index-1] = False
        print("Excution turned Off the Hop Servo")



    pass