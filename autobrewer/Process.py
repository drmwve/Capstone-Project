from PySide2 import QtCore
from .steps import *
from loguru import logger

class Process(QtCore.QObject):
    # I have an array of steps and an index value. Each step, I emit signals which call process functions like
    # move liquid from tank to tank, heat to certain temperature, drain boil kettle, etc. For now, I receive
    # a "step completed" signal from the brew controller which calls the increment function.
    #
    # I emit a signal for each step in the process, and I emit a signal when I'm finished.

    stepstarted = QtCore.Signal(str)
    finished = QtCore.Signal()

    def __init__(self):
        super(Process, self).__init__()
        logger.debug(f'Process created on thread {self.thread}')
        self.processSteps = [Step()]
        self.currentindex = 0
        self.running = False
        self.stepthread = QtCore.QThread()

    def initializeSteps(self):
        self.currentstep = self.processSteps[self.currentindex]
        self.connectStep(self.currentstep)
        self.addsteptothread(self.currentstep, self.stepthread)

    def start(self):
        logger.debug(f'Process {self} starting')
        self.running = True
        self.executeStep()

    def pause(self):
        logger.debug(f'Process {self} pausing')
        self.disconnectStep(self.currentstep)
        self.running = False
        pass

    def resume(self):
        logger.debug(f'Process {self} resuming')
        pass

    def stop(self):
        logger.debug(f'Process {self} exiting')
        self.stepthread.finished.connect(self.test)
        self.stepthread.quit()
        logger.debug(f'Thread running: {self.stepthread.isRunning()}')

    def test(self):
        logger.debug("Thread quit")

    @QtCore.Slot()
    def incrementStep(self, execute=True):
        logger.debug("Process moving to next step")
        self.currentindex += 1
        self.setStep(self.currentindex, execute)

    def decrementStep(self, execute=True):
        logger.debug("Process reverting to previous step")
        self.currentindex -= 1
        self.setStep(self.currentindex, execute)

    def setStep(self, index: int, execute: bool = True):
        self.disconnectStep(self.currentstep)
        self.currentindex = index
        self.currentstep = self.processSteps[self.currentindex]
        logger.debug(f'Process set to step {self.currentstep}')
        self.connectStep(self.currentstep)
        self.addsteptothread(self.currentstep, self.stepthread)
        if execute:
            self.executeStep(self.currentstep)

    def executeStep(self):
        if not self.stepthread.isRunning():
            logger.debug(f'Executing step {self.currentstep}')
            self.stepthread.start()
            logger.debug(f'Thread running: {self.stepthread.isRunning()}')
        else:
            logger.debug("Step already running")

    def connectStep(self, step: Step):
        logger.debug(f'Connecting signals for step {step}')
        step.stepcomplete.connect(self.incrementStep)
        step.stepstarted.connect(self.stepstarted)

    def disconnectStep(self, step: Step):
        logger.debug(f'Disconnecting signals for step {step}')
        step.stepcomplete.disconnect(self.incrementStep)
        step.stepstarted.disconnect(self.stepstarted)

    def addsteptothread(self, step, thread):
        logger.debug(f'Adding step {step} to thread {thread}')
        step.moveToThread(thread)
        step.stepcomplete.connect(thread.quit)
        thread.started.connect(step.execute)
        thread.finished.connect(step.pause)


class ExampleProcess(Process):
    def __init__(self):
        super(ExampleProcess, self).__init__()
        self.processSteps = [ExampleStep()]
        self.initializeSteps()


class BrewProcess(Process):
    def __init__(self, brewRecipe):
        super().__init__()
        self.brewRecipe = brewRecipe
        # emit signal which sets target mash temp
        self.processSteps = ["brewing process step functions"]


class CleaningProcess(Process):
    def __init__(self):
        super().__init__()
        self.processSteps = ["cleaning process step functions"]


class FlushSystem(Process):
    def __init__(self):
        super(FlushSystem, self).__init__()
        self.processSteps = ["steps to flush system"]