from .steps import *
from loguru import logger


class Process(QtCore.QObject):
    """This is a string of steps which execute a particular process. This could be brewing beer, cleaning the system,
    or flushing the system of all liquid. This class doesn't actually do anything with the components itself but
    provides the functionality to wrap a related series of component control steps together and start, stop, pause, and
    resume it.
    """
    stepstarted = QtCore.Signal(str)
    processstarted = QtCore.Signal(int)
    processfinished = QtCore.Signal()

    def __init__(self):
        super(Process, self).__init__()
        self.processSteps = [Step()]
        self.currentindex = 0
        self.totalprocesstime = 0
        self.running = False
        self.currentstep = Step()

    def initializeSteps(self):
        self.currentstep = self.processSteps[self.currentindex]
        for step in self.processSteps:
            self.totalprocesstime += step.estimatedtime

    def start(self):
        logger.debug(f'Process {self} starting with completion time {self.totalprocesstime}')
        self.running = True
        self._connectStep(self.currentstep)
        self.executeCurrentStep()

    def stop(self):
        logger.debug(f'Process {self} stopping')
        self.running = False
        self._disconnectStep(self.currentstep)
        self.currentstep.stop()

    def pause(self):
        logger.debug(f'Process {self} pausing')
        self.currentstep.pause()

    def resume(self):
        logger.debug(f'Process {self} resuming')
        self.currentstep.resume()

    def executeCurrentStep(self):
        self.currentstep.execute()

    def executeNextStep(self):
        self.incrementStep()
        self.executeCurrentStep()

    def incrementStep(self):
        logger.debug("Process moving to next step")
        self.currentindex += 1
        self.setStep(self.currentindex)

    def decrementStep(self):
        logger.debug("Process reverting to previous step")
        self.currentindex -= 1
        self.setStep(self.currentindex)

    def setStep(self, index: int):
        self._disconnectStep(self.currentstep)
        self.currentindex = index
        try:
            self.currentstep = self.processSteps[self.currentindex]
            logger.debug(f'Process set to step {self.currentstep}')
            self._connectStep(self.currentstep)

        except IndexError:
            logger.debug("Process complete")
            self.processfinished.emit()

    def _connectStep(self, step: Step):
        try:
            logger.debug(f'Connecting signals for step {self.processSteps.index(step)}')
            step.stepcomplete.connect(self.executeNextStep)
            step.stepstarted.connect(self.stepstarted)
        except ValueError:
            logger.error("Step not found")

    def _disconnectStep(self, step: Step):
        try:
            logger.debug(f'Disconnecting signals for step {self.processSteps.index(step)}')
            step.stepcomplete.disconnect(self.executeNextStep)
            step.stepstarted.disconnect(self.stepstarted)
        except ValueError:
            logger.error("Step not found")


class ExampleProcess(Process):
    def __init__(self):
        super(ExampleProcess, self).__init__()
        self.processSteps = [ExampleStep(), ExampleStep()]
        self.initializeSteps()


class BrewProcess(Process):
    def __init__(self, brewrecipe):
        super().__init__()
        self.brewRecipe = brewrecipe
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
        self.processSteps = [ExampleStep(), ExampleStep()]
        self.initializeSteps()