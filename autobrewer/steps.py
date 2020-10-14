from .hardware.devicehandler import devicehandler
from PySide2.QtCore import Signal, QObject
from PySide2 import QtCore
from loguru import logger


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
        self.execute()



class FillHLT(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Filling Hot Liqure Tank"
        self.estimatedtime = 180     # used seconds instead of millie assuming this will not effect excuting but rather for displaying this number
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath("FillHLT")
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running boilComplete (checking level sensor at HLT)")
        if devicehandler.hardwareState.volume[0] == 8:
            self.devicehandler.closeBallValve(0)
            self.stepcomplete.emit()
            self.stop()
        else if devicehandler.hardwareState.PauseAndResume = True: # this should be stored value by default is False, when pause button press it should change to True
            self.pause()

    def pause(self):
        logger.debug("Filling hot liqure tank step is paused")
            self.runtimer.stop()
            self.devicehandler.closeBallValve(0)
            self.devicehandler.closeBallValve(1)
            while True:
                if devicehandler.hardwareState.PauseAndResume = False:
                    self.resume()
    
    def resume(self):
        logger.debug("Filling hot liqure tank step is resumed")
        self.run()

        

    def stop(self):
        self.runtimer.stop()

class HeatHTL(Step):

    def __init__(self, HLTtemp):
        super().__init__()
        self.startingmessage = "Heating Hot Liquor Tank"
        self.estimatedtime = 2580 #we calculated 43 minutes required time
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)
        self.HLTtemp = HLTtemp  #temperature specified by the user

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.enableHeatingElement(0)
        self.devicehandler.enableHeatingElement(2)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running loop (Checking temperatre sensor in HLT")
        if devicehandler.hardwareState.temperatures[0] == self.HLTtemp:
            self.devicehandler.disableHeatingElement(2)  # i think we should only reset pumps after each step, but not heating elements and valves
            self.stepcomplete.emit()
            self.stop()
        else if devicehandler.hardwareState.PauseAndResume = True:
            self.resume()

    def pause(self):
        logger.debug("Heating hot liqure tank step is paused")
        self.runtimer.stop()
        self.devicehandler.disableHeatingElement(0)
        self.devicehandler.disableHeatingElement(2)
        while True:
            else if devicehandler.hardwareState.PauseAndResume = False:
                self.resume()
    
    def resume(self):
        logger.debug("Heating hot liqure tank step is resumed")
        self.run()

    def stop(self):
        self.devicehandler.disableHeatingElement(0)
        self.devicehandler.disableHeatingElement(2)
        self.runtimer.stop()

class HLTtoMT(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "moving 4 gallons to mashing tun"
        self.estimatedtime = 90
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)
        self.HLTtemp = HLTtemp

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath("HLTtoMT")
        QtCore.QTimer.singleShot(5000, self.next)      
    
    def next(self):
        self.devicehandler.enablePump(0)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running loop (checking level sensor at the mashing tun)")
        if devicehandler.hardwareState.volume[1] == 4:
            self.devicehandler.disablePump(0)
            self.stepcomplete.emit()
            self.stop()
        
        else if devicehandler.hardwareState.PauseAndResume = True:
            self.pause()

        else:
        self.devicehandler.setTargetKettleTemp(0, self.HLTtemp)
    
    def pause(self):
        logger.debug("Hot liqure tank to mashtun step is paused")
        self.runtimer.stop()
        self.devicehandler.disablePump(0)
        while True:
            devicehandler.hardwareState.PauseAndResume = False:
            self.resume()

    def resume(self):
        logger.debug("Hot liqure tank to mashtun step is resumed")
        self.next()

    def stop(self):
        self.runtimer.stop()

class MTRecirc(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Mashing tun recirculation"
        self.estimatedtime = 90
        self.runtimer = QtCore.QTimer()
        self.runtimer2 = QtCore.QTimer()
        self.runtimer2.timeout.connect(self.tempControl)
        self.index = 0
        self.runtimer.timeout.connect(self.loop)
        self.HLTtemp = HLTtemp


    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath(MTRecirc)
        QtCore.QTimer.singleShot(5000, self.next)      
    
    def next(self):
        self.devicehandler.enablePump(0)
        self.runtimer.start(1000)
        self.runtimer2.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')
        logger.debug(f'Started timer 2: {self.runtimer2.isActive()}')

    def loop(self):
        logger.debug("Running loop (waiting for 60 minutes for recirculation)")
        self.index += 1
        if self.index == 3600:
            self.devicehandler.disablePump(0)
            self.stepcomplete.emit()
            self.stop()
        else if devicehandler.hardwareState.PauseAndResume = True:
            self.pause()

    def tempControl(self):
        self.devicehandler.setTargetKettleTemp(1, self.HLTtemp)

    
    def pause(self):
        self.devicehandler.disablePump(0)
        self.runtimer.stop()
        self.runtimer2.stop()
        while True:
            devicehandler.hardwareState.PauseAndResume = False:
                self.resume()

    def resume(self):
        self.next() 

    def stop(self):
        self.runtimer.stop()
        self.runtimer2.stop()

class MTtoBK(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "moving the liquid from Mashing tun to boiling kettle"
        self.estimatedtime = 130
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath("MTtoBK")
        QtCore.QTimer.singleShot(5000, self.next)      
    
    def next(self):
        self.devicehandler.enablePump(0)
        self.devicehandler.enablePump(1)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running loop (checking level sensor at the Boiling kettle)")
        if devicehandler.hardwareState.volume[2] == 6.5:
            self.stepcomplete.emit()
            self.stop()
        else if devicehandler.hardwareState.PauseAndResume = True:
            self.pause()
    
    def pause(self):
        logger.debug("mashtun to boiling kettle step is paused")
        self.runtimer.stop()
        self.devicehandler.disablePump(0)
        self.devicehandler.disablePump(1)
        while True:
            if devicehandler.hardwareState.PauseAndResume = False:
                self.resume()
    
    def resume(self):
        logger.debug("mashtun to boiling kettle step is resumed")
        self.next()


    def stop(self):
        self.runtimer.stop()
        self.devicehandler.disablePump(0)
        self.devicehandler.disablePump(1)
        self.devicehandler.disableHeatingElement(0)
        self.devicehandler.disableHeatingElement(2)


class BKboiling_AddingHops(Step):

    def __init__(self, numHops, timeHops):
        super().__init__()
        self.startingmessage = "Boiling the liquid in the boiling kettle and adding hops"
        self.estimatedtime = 3600 
        self.boilTime = 3600000
        self.hopindex = 0
        self.numHops = numHops #number of hops
        self.timeHops = timeHops  #timing between hops
        self.runtimer0 = QtCore.QTimer()     #temperature control
        self.runtimer0.timeout.connect(self.tempControl)  
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.boilComplete)
        self.runtimer2 = QtCore.QTimer()
        self.runtimer2.timeout.connect(self.addHopsChain)
        self.runtimer3 = QtCore.QTimer()      #check if user paused
        self.runtimer3.timeout.connect(self.checkIfPaused)  

    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.closeBallValve(3)
        devicehandler.closeBallValve(4)
        self.runtimer.start(self.boilTime)
        self.runtimer2.start(self.timeHops[self.hopindex])
        self.runtimer0.start(100)
        self.runetimer3.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')
        logger.debug(f'Started timer 2: {self.runtimer2.isActive()}')
        logger.debug(f'Started timer 0: {self.runtimer0.isActive()}')
    
    def checkIfPaused(self):
        if devicehandler.hardwareState.PauseAndResume = True:
            self.pause()
        
    
    def pause(self):
        logger.debug("boiling and adding hops step is paused")
        self.boilTime = self.runtimer.remainingTime("i dont know how to get the timer id")
        self.timeHops = self.runtimer2.remainingTime("i dont know how to get the timer id")
        self.runtimer.stop()
        self.runtimer2.stop()
        self.runtimer0.stop()
        self.runtimer3.stop()
            while True:
                if devicehandler.hardwareState.PauseAndResume = False:
                    self.resume()
            
    def resume(self):
        logger.debug("boiling and adding hops step is resumed")
        self.run()
    
    def tempControl(self):
        if devicehandler._readTemperature(3) >= 212:
            self.devicehandler.disableHeatingElement(1)
            self.devicehandler._setHeatingElementValue(3, 0.5)
        else:
            self.devicehandler.enableHeatingElement(1)
            self.devicehandler.enableHeatingElement(3)



    def boilComplete(self):
        self.stepcomplete.emit()
        self.stop()

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
        self.stepcomplete.emit()
        self.runtimer.stop()
        self.runtimer2.stop()
        self.runtimer0.stop()
        self.runtimer3.stop()
        self.devicehandler.disableAllHeatingElements()


class BKWhirl(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Whirling in the boiling kettle"
        self.estimatedtime = 900
        self.whirlTime = 900000
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.stop)
        self.runtimer2 = QtCore.QTimer()
        self.runtimer2.timeout.connect(self.checkIfPaused)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath("BKWhirl")
        self.devicehandler.disableAllHeatingElements()
        QtCore.QTimer.singleShot(5000, self.next)      
    
    def next(self):
        self.enablePump(1)
        self.runtimer.start(self.whirlTime)
        self.runtimer2.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def checkIfPaused(self):
        if devicehandler.hardwareState.PauseAndResume = True:
            self.pause()
    
    def pause(self):
        logger.debug("Boiling kettle whirl step is paused")
        self.devicehandler.disablePump(1)
        self.whirlTime = self.runtimer.remainingTime("timer ID")
        self.runtimer.stop()
        self.runtimer2.stop()
            while True:
                if devicehandler.hardwareState.PauseAndResume = False:
                    self.resume()
    
    def resume(self):
        logger.debug("Boiling kettle whirl step is resumed")
        self.next()

    def stop(self):
        self.devicehandler.disablePump(1)
        self.stepcomplete.emit()
        self.runtimer.stop()
        self.runtimer2.stop()

class Draining(Step):
    def __init__(self):
        super().__init__()
        self.startingmessage = "Draining to fermenter"
        self.estimatedtime = 150
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.stop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath("BKDrain")
        QtCore.QTimer.singleShot(5000, self.next)

    def next(self):
        self.enablePump(1)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running loop (Checking Boiling kettle liquid level to completely drain out)")
        if devicehandler.hardwareState.volume[2] == 0:
            self.stepcomplete.emit()
            QtCore.QTimer.singleShot(5000, self.stop)
        
        else if devicehandler.hardwareState.PauseAndResume = True:
            self.pause()
    
    def pause(self):
        logger.debug("Draining step is paused")
        self.devicehandler.disablePump(1)
        self.devicehandler.closeBallValve(4)
        self.runtimer.stop()
            while True:
                if devicehandler.hardwareState.PauseAndResume = False:
                    self.resume()
        
    def resume(self):
        logger.debug("Draining step is resumed")
        self.run()

    def stop(self):
        self.runtimer.stop()
        self.devicehandler.shutdown()  # Reseting everything to begining state







        

        
        


    

