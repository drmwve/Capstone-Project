from .hardware.devicehandler import devicehandler
from PySide2.QtCore import Signal, QObject
from PySide2 import QtCore
from loguru import logger
import random


class Step(QObject):
    stepcomplete = Signal()
    stepstarted = Signal(str)

    def __init__(self):
        super().__init__()
        self.devicehandler = devicehandler
        self.estimatedtime = 0
        self.startingmessage = "Started base step"
        self.running = False

    def execute(self):
        logger.info(f'Executing step {self}')
        self.stepstarted.emit(self.startingmessage)
        self.running = True
        self.run()

    #Overload and implement in inherited classes:

    def run(self):
        pass

    def stop(self):
        pass

    def pause(self):
        self.stop()

    def resume(self):
        self.run()

class ExampleStep(Step):

    def __init__(self):
        super(ExampleStep, self).__init__()
        self.max = random.randint(2,10)
        self.startingmessage = f'Example counting to {self.max}'
        self.estimatedtime = self.max + 1
        self.index = 0
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        logger.debug(self.startingmessage)
        self.runtimer.start(1000)

    def loop(self):
        logger.debug(f'Example step running loop index {self.index}')
        self.index += 1
        if self.index > self.max:
            self.stepcomplete.emit()
            self.stop()

    def stop(self):
        self.runtimer.stop()
        self.index = 0

    def pause(self):
        self.runtimer.stop()


class FillHLT(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Filling Hot Liquor Tank..."
        self.estimatedtime = 180     # used seconds instead of millie assuming this will not effect excuting but rather for displaying this number
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.disableAll()
        devicehandler.openValvePath("FillHLT")
        self.runtimer.start(100)

    def loop(self):
        if devicehandler.hardwareState.volume[0] == devicehandler.KETTLE_MAX_VOLUME:
            self.devicehandler.closeBallValve(0)
            self.stop()
            self.stepcomplete.emit()

    def stop(self):
        devicehandler.disableAll()
        self.runtimer.stop()


class HeatHTL(Step):

    def __init__(self, HLTtemp):
        super().__init__()
        self.startingmessage = "Heating Hot Liquor Tank..."
        self.estimatedtime = 2580 #we calculated 43 minutes required time
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)
        self.HLTtemp = HLTtemp  #temperature specified by the user

    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.disableAll()
        devicehandler.setTargetKettleTemp(devicehandler.KETTLE_IDS_GIVEN_NAME["HLT"], self.HLTtemp)
        self.runtimer.start(100)

    def loop(self):
        if devicehandler.hardwareState.temperatures[0] >= self.HLTtemp:
            self.runtimer.stop()
            self.stepcomplete.emit()

    def stop(self):
        self.disableAll()
        self.runtimer.stop()


class HLTtoMT(Step):

    def __init__(self, HLTtemp):
        super().__init__()
        self.startingmessage = "Adding strike water..."
        self.estimatedtime = 90
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)
        self.HLTtemp = HLTtemp

    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.resetFlowControl()
        for heatingelement in devicehandler.BK_HEATING_ELEMENTS:
            devicehandler.disableHeatingElement(heatingelement)
        devicehandler.openValvePath("HLTtoMT")
        if self.HLTtemp > 0:
            devicehandler.setTargetKettleTemp(devicehandler.KETTLE_IDS_GIVEN_NAME["HLT"], self.HLTtemp)
        QtCore.QTimer.singleShot(5000, self.next)      
    
    def next(self):
        devicehandler.enablePump(0)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        if devicehandler.hardwareState.volume[devicehandler.KETTLE_IDS_GIVEN_NAME["MT"]] >= devicehandler.KETTLE_MAX_VOLUME/2:
            self.stop()
            self.stepcomplete.emit()

    def stop(self):
        self.runtimer.stop()
        devicehandler.disableAll()


class MTRecirc(Step):
# TO-DO: Implement refilling HLT without compromising mash temperature
    def __init__(self, mashtemp):
        super().__init__()
        self.startingmessage = "Recirculating wort..."
        self.estimatedtime = 90
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.mashcomplete)
        self.mashtemp = mashtemp
        self.MTRecirctotaltime = 3600000
        self.MTRecircremainingtime = self.MTRecirctotaltime


    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.resetFlowControl()
        for heatingelement in devicehandler.BK_HEATING_ELEMENTS:
            devicehandler.disableHeatingElement(heatingelement)
        devicehandler.setTargetKettleTemp(devicehandler.KETTLE_IDS_GIVEN_NAME["MT"], self.mashtemp)
        devicehandler.openValvePath("MTRecirc")
        QtCore.QTimer.singleShot(5000, self.next)

    def next(self):
        devicehandler.enablePump(0)
        self.runtimer.start(self.MTRecircremainingtime)
        self.devicehandler.setTargetKettleTemp(1, self.HLTtemp)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def mashcomplete(self):
        self.stop()
        self.stepcomplete.emit()

    def pause(self):
        self.MTRecircremainingtime = self.runtimer.remainingTime()
        devicehandler.disablePump(0)
        self.runtimer.stop()

    def stop(self):
        self.MTRecircremainingtime = self.MTRecirctotaltime
        devicehandler.disableAll()
        self.runtimer.stop()


class MTtoBK(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Sparging wort..."
        self.estimatedtime = 130
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.disableAll()
        devicehandler.openValvePath("MTtoBK")
        devicehandler.openValvePath("HLTtoMT")
        QtCore.QTimer.singleShot(5000, self.next)

    def next(self):
        devicehandler.enablePump(0)
        devicehandler.enablePump(1)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        if devicehandler.hardwareState.volume[devicehandler.KETTLE_IDS_GIVEN_NAME["BK"]] >= 6.5:
            self.stop()
            self.stepcomplete.emit()

    def stop(self):
        self.runtimer.stop()
        devicehandler.disableAll()


class BKboiling_AddingHops(Step):

    def __init__(self, numHops, timeHops):
        super().__init__()
        self.startingmessage = "Boiling wort and adding hops..."
        self.estimatedtime = 3600 
        self.boilTime = 3600000
        self.hopindex = 0
        self.numHops = numHops #number of hops
        self.timeHops = timeHops  #timing between hops
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.boilComplete)
        self.runtimer2 = QtCore.QTimer()
        self.runtimer2.timeout.connect(self.addHopsChain)
        self.tempcontroltimer = QtCore.QTimer()
        self.tempcontroltimer.timeout.connect(self.tempControl)

    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.disableAll()
        self.runtimer.start(self.boilTime)
        self.runtimer2.start(self.timeHops[self.hopindex])
        self.tempcontroltimer.start(1000)

    def pause(self):
        logger.debug("boiling and adding hops step is paused")
        self.boilTime = self.runtimer.remainingTime()
        self.timeHops = self.runtimer2.remainingTime()
        self.runtimer.stop()
        self.runtimer2.stop()
        self.tempcontroltimer.stop()
        devicehandler.disableAllHeatingElements()

    def tempControl(self):
        if devicehandler.readTemperature(3) >= 212:
            self.devicehandler.disableHeatingElement(3)
            self.devicehandler._setHeatingElementValue(1, 0.5)
        else:
            self.devicehandler.enableHeatingElement(1)
            self.devicehandler.enableHeatingElement(3)

    def boilComplete(self):
        self.stop()
        self.stepcomplete.emit()

    def addHopsChain(self):
        logger.debug("Adding hops")
        devicehandler.goToHopPosition(self.hopindex)
        self.runtimer2.stop()
        self.hopindex += 1
        if self.hopindex < self.numHops:
            self.runtimer2.start(self.timeHops[self.hopindex])
        else:
            QtCore.QTimer.singleShot(5000, self.hopDispenseComplete)

    def hopDispenseComplete(self):
        devicehandler.goToHopPosition(devicehandler.HOP_SERVO_HOME)
        self.runtimer2.stop()

    def stop(self):
        self.hopindex = 0
        self.boilTime = 3600000
        self.runtimer.stop()
        self.runtimer2.stop()
        self.tempcontroltimer.stop()
        self.devicehandler.disableAll()


class BKWhirl(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Whirling in the boiling kettle..."
        self.estimatedtime = 900
        self.whirlTime = 900000
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.stop)

    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.disableAll()
        devicehandler.openValvePath("BKWhirl")
        QtCore.QTimer.singleShot(5000, self.next)
    
    def next(self):
        self.enablePump(1)
        self.runtimer.start(self.whirlTime)

    def whirlcomplete(self):
        self.stop()
        self.stepcomplete.emit()

    def pause(self):
        logger.debug("Boiling kettle whirl step is paused")
        devicehandler.disablePump(1)
        self.whirlTime = self.runtimer.remainingTime()
        self.runtimer.stop()
        self.runtimer2.stop()

    def resume(self):
        logger.debug("Boiling kettle whirl step is resumed")
        self.next()

    def stop(self):
        devicehandler.disableAll()
        self.whirlTime = 900000
        self.runtimer.stop()
        self.runtimer2.stop()


class Draining(Step):
    def __init__(self):
        super().__init__()
        self.startingmessage = "Draining to fermenter..."
        self.estimatedtime = 150
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.stop)

    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.disableAll()
        self.devicehandler.openValvePath("BKDrain")
        QtCore.QTimer.singleShot(5000, self.next)

    def next(self):
        self.enablePump(1)
        devicehandler.openBallValve(5)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        if devicehandler.hardwareState.volume[devicehandler.KETTLE_IDS_GIVEN_NAME["BK"]] == 0:
            self.stop()
            self.stepcomplete.emit()

    def stop(self):
        self.runtimer.stop()
        self.devicehandler.disableAll()  # Resetting everything to beginning state















