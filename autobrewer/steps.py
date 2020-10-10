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

    def stop(self):
        self.runtimer.stop()

class HLTtoMT(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "moving 4 gallons to mashing tun"
        self.estimatedtime = 90
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath(HLTtoMT)
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

    def stop(self):
        self.runtimer.stop()

class MTRecirc(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Mashing tun recirculation"
        self.estimatedtime = 90
        self.runtimer = QtCore.QTimer()
        self.index = 0
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath(MTRecirc)
        QtCore.QTimer.singleShot(5000, self.next)      
    
    def next(self):
        self.devicehandler.enablePump(0)
        self.runtimer.start(1000)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running loop (waiting for 60 minutes for recirculation)")
        self.index += 1
        if self.index == 3600:        # will this method cause delays caused by the excution process time? should runtimer be set to 3600,000 instead?
            self.devicehandler.disablePump(0)
            self.stepcomplete.emit()
            self.stop()

    def stop(self):
        self.runtimer.stop()

class MTtoBK(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "moving the liquid from Mashing tun to boiling kettle"
        self.estimatedtime = 130
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath(MTtoBK)
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
        self.hopindex = 0
        self.numHops = numHops #number of hops
        self.timeHops = timeHops  #timing between hops
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.boilComplete)
        self.runtimer2 = QtCore.QTimer()
        self.runtimer2.timeout.connect(self.addHopsChain)

    def run(self):
        logger.debug(f'Running step {self}')
        devicehandler.closeBallValve(3)
        devicehandler.closeBallValve(4)
        self.runtimer.start(3600000)
        self.runtimer2.start(self.timeHops[self.hopindex])
        logger.debug(f'Started timer: {self.runtimer.isActive()}')
        logger.debug(f'Started timer 2: {self.runtimer2.isActive()}')

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
        self.devicehandler.disableAllHeatingElements()


class BKWhirl(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Whirling in the boiling kettle"
        self.estimatedtime = 900
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.stop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath(BKWhirl)
        QtCore.QTimer.singleShot(5000, self.next)      
    
    def next(self):
        self.enablePump(1)
        self.runtimer.start(900000)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')


    def stop(self):
        self.devicehandler.disablePump(1)
        self.stepcomplete.emit()
        self.runtimer.stop()

class Draining(Step):
    def __init__(self):
        super().__init__()
        self.startingmessage = "Draining to fermenter"
        self.estimatedtime = 150
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.stop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.openValvePath(BKDrain)
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
    
    def stop(self):
        self.runtimer.stop()
        self.devicehandler.shutdown()  # Reseting everything to begining state





        

        
        


    

