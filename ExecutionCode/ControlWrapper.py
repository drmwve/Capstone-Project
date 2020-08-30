import RPi.GPIO as GPIO #to control the input and output
from ExecutionCode.BrewState import BrewState
GPIO.setup(1,GPIO.OUT) #2 way valve number 1

# Signals: step completed

class ControlHandler():
    def __init__(self):
        self.twoWayBallValveGPIOs = [1, 42, 42,14, 63]
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
        print("close a ball valve")

    def readTemperatureSensor(self, whichSensor):
        print("Execution read sensor " + str(whichSensor))


    pass