from .hardware.devicehandler import devicehandler
from .hardware import tempState
from . import BrewRecipe
from PySide2.QtCore import Signal, QObject
from PySide2 import QtCore
from loguru import logger
import time


class Step(QObject):
    stepcomplete = Signal()
    stepstarted = Signal(str)

    def __init__(self):
        super().__init__()
        self.estimatedtime = 0
        self.devicehandler = devicehandler
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
        self.startingmessage = "Example step"
        self.estimatedtime = 6
        self.index = 0
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.runtimer.start(1000)

    def loop(self):
        logger.debug(f'Example step running loop index {self.index}')
        self.index += 1
        if self.index > 6:
            self.stepcomplete.emit()
            self.stop()

    def stop(self):
        self.runtimer.stop()
        self.index = 0

    def pause(self):
        self.runtimer.stop()


class FillHTL(Step):
    def __call__(self):
        self.devicehandler.openValvePath("FillHLT")
        #   while true:
        #      if devicehandler.levelsensor(0) == 8 : break             - we still need to work with the level sensor
        self.devicehandler.closeBallValve(0)


class HeatHTL(Step):
    def __call__(self):
        self.devicehandler.enableHeatingElement(0)
        self.devicehandler.enableHeatingElement(2)
        while True:
            if tempState.tempSensor1 == BrewRecipe.mashTunTemperature: break
        self.devicehandler.disableHeatingElement(2)


class HLTtoMT(Step):
    def __call__(self):
        self.devicehandler.openValvePath(HLTtoMT)
        time.sleep(1)
        self.devicehandler.enablePump(0)
        #    while True:
        #       if devicehandler.hardwareState.volume[0] == 4 : break
        self.devicehandler.disablePump(0)


class MTRecirc(Step):
    def __call__(self):
        self.devicehandler.openValvePath(MTRecirc)
        time.sleep(1)  # to make sure the valves are turned before we turn on the pump again
        self.devicehandler.enablePump(0)
        time.sleep(3600)
        self.devicehandler.disablePump(0)


class MTtoBK(Step):
    def __call__(self):
        self.devicehandler.openValvePath(MTtoBK)
        time.sleep(1)
        self.devicehandler.enablePump(1)
        #   while True:
        #       if devicehandler.levelsensor(1) == 6.5 : break
        self.devicehandler.disableHeatingElement(0)
        self.devicehandler.disablePump(1)


class BKWhirl(Step):
    def __call__(self):
        self.devicehandler.openValvePath(BKWhirl)
        time.sleep(1)
        self.devicehandler.enablePump(1)
        self.devicehandler.enableHeatingElement(1)
        self.devicehandler.enableHeatingElement(3)


# Was thinking of adding the 60 minutes wait time here, but fiqured we can put it in the actuall process code


class AddHops(Step):
    def __call__(self):
        R = 0
        Y = BrewRecipe.hopCartridges
        Z = BrewRecipe.hopTiming
        K = 0
        while R < Y:
            self.devicehandler.setHopServoPosition(
                30)  # calling the function in device handler, the angle used is just arbitrary value
            time.sleep(1)  # about the time it take for motor movement
            time.sleep(Z[0])  # timing provided by user
            R = R + 1
            K = K + 1
            self.devicehandler.setHopServoPosition(
                30 * Y - 360)  # this is an idea place holder of what we gonna do for the servo to reset it postion


class BKDrain(Step):
    def __call__(self):
        self.devicehandler.openValvePath(BKDrain)


class Drained(Step):  # wait to drain out, then reset equipments
    # while True:
    #        if devicehandler.levelsensor(2) == 0 : break
    def __call__(self):
        self.devicehandler.resetFlowControl()
        self.devicehandler.disableAllHeatingElements()


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
        logger.debug("Running loop (checking level sensor at HLT)")
        if devicehandler.hardwareState.volume[0] == 8:
            self.devicehandler.closeBallValve(0)
            self.stepcomplete.emit()
            self.stop()

    def stop(self):
        self.runtimer.stop()

class HeatHTL(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Heating Hot Liqure Tank"
        self.estimatedtime = 2580 #we calculated 43 minutes required time
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.enableHeatingElement(0)
        self.devicehandler.enableHeatingElement(2)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running loop (Checking temperatre sensor in HLT")
        if devicehandler.hardwareState.temperatures[0] == BrewRecipe.mashTunTemperature:
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
        time.sleep(1)
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
        self.devicehandler.enablePump(0)
        self.devicehandler.enablePump(1)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running loop (checking level sensor at the Boiling kettle)")
        if devicehandler.hardwareState.volume[2] == 6.5:
            self.devicehandler.disablePump(0)
            self.devicehandler.disablePump(1)
            self.devicehandler.disableHeatingElement(0)
            self.stepcomplete.emit()
            self.stop()

    def stop(self):
        self.runtimer.stop()

class BKWhirl(Step):

    def __init__(self):
        super().__init__()
        self.startingmessage = "Whirl at the black kettle"
        self.estimatedtime = 2580  
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.devicehandler.enableHeatingElement(0)
        self.devicehandler.enableHeatingElement(2)
        self.runtimer.start(100)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running loop (Checking temperatre sensor in HLT")
        if tempState.tempSensor1 == BrewRecipe.mashTunTemperature:
            self.devicehandler.disableHeatingElement(2)  # i think we should only reset pumps after each step, but not heating elements and valves
            self.stepcomplete.emit()
            self.stop()

    def stop(self):
        self.runtimer.stop()