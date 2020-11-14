from PySide2.QtWidgets import QMessageBox
from .Process import *


class ExecutionHandler(QtCore.QObject):
    # I wrap the thread handling up in a neat package. The UI code creates a process and passes it to me with my startProcess(process)
    # function.

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

    def startProcess(self, process):
        if not self.processRunning:
            self.process = process
            logger.info(
                "Started process "
                + str(self.process)
            )
            self.processRunning = True
            self.processstarted.emit(self.process.totalprocesstime)
            self.process.stepstarted.connect(self.stepstarted)
            self.process.processfinished.connect(self.finishedProcess)
            self.process.remainingtimesignal.connect(self.remainingtimesignal)
            self.process.start()
        else:
            error = QMessageBox()
            error.setText("A process is already running.")
            error.exec()

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
            logger.info(f'Paused process {self.process}')

    def resumeProcess(self):
        self.processresumed.emit()
        self.process.resume()
        self.processPaused = False

    def advanceStep(self):
        self.process.incrementStep()

    def reverseStep(self):
        self.process.decrementStep()

    def finishedProcess(self):
        self.processRunning = False
        self.processcomplete.emit()
        logger.debug("Execution handler wrapped up process")


executionhandler = ExecutionHandler()
