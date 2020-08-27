import RPi.GPIO as GPIO #to control the input and output

GPIO.setup(1,GPIO.OUT) #2 way valve number 1

class controlHandler():
    def __init__(self):
        self.twoWayBallValveGPIOs = [1, 42, 42,14, 63]



    def openBallValve(self, index):
        GPIO.output(self.twoWayBallValveGPIOs[index-1],True)
        print("open a ball valve")

    def closeBallValve(self, index):
        print("close a ball valve")

    def readTemperatureSensor(self, whichSensor):
        return "sensor reading"


    pass