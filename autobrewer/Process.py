from .steps import *
from loguru import logger

from .utils import IS_RASPBERRY_PI


class Process(QtCore.QObject):
    """This is a string of steps which execute a particular process. This could be brewing beer, cleaning the system,
    or flushing the system of all liquid. This class doesn't actually do anything with the components itself but
    provides the functionality to wrap a related series of component control steps together and start, stop, pause, and
    resume it.
    """
    stepstarted = QtCore.Signal(str)
    processstarted = QtCore.Signal(int)
    processfinished = QtCore.Signal()
    remainingtimesignal = QtCore.Signal(int)

    def __init__(self):
        super(Process, self).__init__()
        self.processSteps = [Step()]
        self.currentindex = 0
        self.totalprocesstime = 0
        self.remainingtime = 0
        self.running = False
        self.currentstep = Step()
        self.processcomplete = False

    def initializeSteps(self):
        logger.debug("Initializing steps")
        self.currentstep = self.processSteps[self.currentindex]
        for step in self.processSteps:
            self.totalprocesstime += step.estimatedtime
        self.remainingtime = self.getRemainingTime()

    def start(self):
        logger.debug(f'Process {self} starting at step {self.currentindex} with completion time {self.totalprocesstime}')
        self.running = True
        self._connectStep(self.currentstep)
        self.currentstep.execute()

    def stop(self):
        logger.debug(f'Process {self} stopping')
        self.running = False
        self._disconnectStep(self.currentstep)
        self.currentstep.stopcommand()

    def pause(self):
        logger.debug(f'Process {self} pausing')
        self.currentstep.pausecommand()

    def resume(self):
        logger.debug(f'Process {self} resuming')
        self.currentstep.execute()

    def executeNextStep(self):
        self.incrementStep()
        logger.debug(f'Executing step {self.currentindex}')
        if not self.processcomplete:
            self.currentstep.execute()

    def incrementStep(self):
        logger.debug("Process moving to next step")
        nextstep = self.currentindex + 1
        if nextstep == len(self.processSteps):
            self._processComplete()
        else:
            self.setStep(nextstep)

    def decrementStep(self):
        logger.debug("Process reverting to previous step")
        self.currentindex -= 1
        self.setStep(self.currentindex)

    def setStep(self, index: int, disconnect=True):
        if disconnect:
            self._disconnectStep(self.currentstep)
        self.currentindex = index
        if self.currentindex in range(len(self.processSteps)):
            self.currentstep = self.processSteps[self.currentindex]
            logger.debug(f'Process set to step {self.currentstep}')
            self._connectStep(self.currentstep)


    def getRemainingTime(self):
        remainingtime = 0
        for i in range(self.currentindex,len(self.processSteps)):
            remainingtime += self.processSteps[i].estimatedtime
        logger.info(f'Remaining time: {remainingtime}')
        self.remainingtimesignal.emit(remainingtime)
        return remainingtime

    def _processComplete(self):
        logger.debug("Process complete")
        self.processcomplete = True
        self._disconnectStep(self.currentstep)
        self.processfinished.emit()

    def _connectStep(self, step: Step):
        try:
            logger.debug(f'Connecting signals for step {self.processSteps.index(step)}')
            step.stepcomplete.connect(self.executeNextStep)
            step.stepstarted.connect(self.stepstarted)
            step.stepstarted.connect(self.getRemainingTime)
        except ValueError:
            logger.error("Step not found")

    def _disconnectStep(self, step: Step):
        try:
            logger.debug(f'Disconnecting signals for step {self.processSteps.index(step)}')
            step.stepcomplete.disconnect(self.executeNextStep)
            step.stepstarted.disconnect(self.stepstarted)
            step.stepstarted.disconnect(self.getRemainingTime)
        except:
            logger.error("Step error")

    def _getStepPersistentData(self):
        return [step.getpersistentdata() for step in self.processSteps]

    def _setStepPersistentData(self, data):
        for index, step in enumerate(self.processSteps):
            step.setpersistentdata(data[index])


class ExampleProcess(Process):
    def __init__(self):
        super(ExampleProcess, self).__init__()
        self.processSteps = [ExampleStep(), ExampleStep()]
        self.initializeSteps()


class BrewProcess(Process):
    def __init__(self, brewrecipe):
        super().__init__()
        self.brewRecipe = brewrecipe
        if IS_RASPBERRY_PI:
            self.processSteps = [FillHLT(),
                                 HeatHTL(brewrecipe.mashTunTemperature),
                                 HLTtoMT(brewrecipe.mashTunTemperature),
                                 MTRecirc(brewrecipe.mashTunTemperature),
                                 MTtoBK(),
                                 BKboiling_AddingHops(brewrecipe.hopCartridges, brewrecipe.hopTiming),
                                 BKWhirl(),
                                 Draining()]
        else:
            self.processSteps = [ExampleStep(), ExampleStep()]
        self.initializeSteps()


class CleaningProcess(Process):
    def __init__(self):
        super().__init__()
        self.processSteps = [ExampleStep(), ExampleStep()]
        self.initializeSteps()


class FlushSystem(Process):
    def __init__(self):
        super(FlushSystem, self).__init__()
        self.processSteps = [Draining(),
                             MTtoBK(-1),
                             Draining(),
                             HLTtoMT(),
                             MTtoBK(),
                             Draining()]
        self.initializeSteps()