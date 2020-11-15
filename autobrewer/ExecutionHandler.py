from PySide2.QtWidgets import QMessageBox

from .BrewRecipe import BrewRecipePickler
from .Process import *
import os

class ExecutionHandler(QtCore.QObject):
    # I wrap the thread handling up in a neat package. The UI code creates a process and passes it to me with my startProcess(process)
    # function.

    PROCESS_FILE_SAVE_NAME = "processpickle.pkl"

    stepstarted = Signal(str)
    processstarted = Signal(int)
    processpaused = Signal()
    processstopped = Signal()
    processresumed = Signal()
    processcomplete = Signal()
    remainingtimesignal = Signal(int)
    processRunning = False
    processPaused = False
    process = Process()
    loadedprocess = False

    def __init__(self):
        super().__init__()
        self.processpickler = BrewRecipePickler()
        self.saveprocesstimer = QtCore.QTimer()
        self.saveprocesstimer.timeout.connect(self.saveProcessToDisk)
        ExecutionHandler.process = self.loadProcessFromDisk()

    def startProcess(self, process):
        if not self.processRunning:
            self.process = process
            logger.info(
                "Started process "
                + str(self.process)
            )
            self.processRunning = True
            self.processstarted.emit(self.process.remainingtime)
            self.saveprocesstimer.start(1000)
            self.connectProcessToSignals()
            self.process.start()
        else:
            error = QMessageBox()
            error.setText("A process is already running.")
            error.exec()

    def saveProcessToDisk(self):
        if self.process.__class__ == BrewProcess:
            processdata = [self.process.__class__, self.process.currentindex, self.process.brewRecipe] + self.process._getStepPersistentData()
        else:
            processdata = [self.process.__class__, self.process.currentindex] + self.process._getStepPersistentData()
        logger.debug(f'Saving data {processdata}')
        self.processpickler._savePickleToFile(processdata, ExecutionHandler.PROCESS_FILE_SAVE_NAME)

    def loadProcessFromDisk(self):
        try:
            if os.path.exists(ExecutionHandler.PROCESS_FILE_SAVE_NAME):
                processdata = self.processpickler._readPickleFromFile(ExecutionHandler.PROCESS_FILE_SAVE_NAME)
                logger.debug(f'Loaded process data {processdata}')
                logger.info(processdata)
                logger.info(BrewProcess(None).__class__)
                if processdata[0] == BrewProcess:
                    process = BrewProcess(processdata[2])
                    process._setStepPersistentData(processdata[3:])
                    process.remainingtime = process.getRemainingTime()
                    #process.setStep(processdata[1], disconnect=False)
                    process.currentindex = processdata[1]
                    process.currentstep = process.processSteps[process.currentindex]
                    ExecutionHandler.loadedprocess = True
                    return process
                elif processdata[0] == CleaningProcess:
                    process = CleaningProcess()
                elif processdata[0] == FlushSystem:
                    process = FlushSystem()
                elif processdata[0] == ExampleProcess:
                    process = ExampleProcess()
                else:
                    logger.warning("Could not find class of loaded process object")
                process.remainingtime = process.getRemainingTime()
                #process.setStep(processdata[1], disconnect=False)
                process.currentindex = processdata[1]
                process.currentstep = process.processSteps[process.currentindex]
                process._setStepPersistentData(processdata[2:])
                ExecutionHandler.loadedprocess = True
                return process
            else:
                logger.debug("Could not find existing process")
                return Process()
        except:
            return Process()

    def deleteProcessFromDisk(self):
        if os.path.exists(ExecutionHandler.PROCESS_FILE_SAVE_NAME):
            os.remove(ExecutionHandler.PROCESS_FILE_SAVE_NAME)
        else:
            logger.warning("Could not find process pickle file")

    def connectProcessToSignals(self):
        self.process.stepstarted.connect(self.stepstarted)
        self.process.processfinished.connect(self.finishedProcess)
        self.process.remainingtimesignal.connect(self.remainingtimesignal)

    def startBrewProcess(self, brewRecipe):
        self.startProcess(BrewProcess(brewRecipe))

    def startCleaningProcess(self):
        self.startProcess(CleaningProcess())

    def startFlushProcess(self):
        self.startProcess(FlushSystem())

    def stopProcess(self):
        if self.processRunning:
            self.process.stop()
            self.processstopped.emit()
            self.processRunning = False
            self.deleteProcessFromDisk()
            self.saveprocesstimer.stop()
            logger.info(f'Stopped process {self.process}')

    def assumemanualcontrol(self):
        logger.debug("Execution handler caught manual control request")
        if self.processPaused:
            self.resumeProcess()
        else:
            self.pauseProcess()

    def pauseProcess(self):
        if self.processRunning:
            self.processpaused.emit()
            self.process.pause()
            self.processPaused = True
            self.saveprocesstimer.stop()
            logger.info(f'Paused process {self.process}')

    def resumeProcess(self):
        self.processresumed.emit()
        self.process.resume()
        self.saveprocesstimer.start(1000)
        self.processPaused = False

    def advanceStep(self):
        self.process.incrementStep()

    def reverseStep(self):
        self.process.decrementStep()

    def finishedProcess(self):
        self.processRunning = False
        self.processcomplete.emit()
        self.deleteProcessFromDisk()
        self.saveprocesstimer.stop()
        logger.debug("Execution handler wrapped up process")


executionhandler = ExecutionHandler()
