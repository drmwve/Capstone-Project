from PySide2.QtWidgets import QMessageBox
from .Process import *


class ExecutionHandler(QtCore.QObject):
    # I wrap the thread handling up in a neat package. The UI code creates a process and passes it to me with my startProcess(process)
    # function and I create a new thread which this process is executed in.

    stepstarted = Signal(str)
    processRunning = False
    processPaused = False
    process = Process()

    # Starts a new process on a new thread. If a thread is already running, show an error.
    def startProcess(self, process):
        if not self.processRunning:
            self.process = process
            logger.info(
                "Started process "
                + str(self.process)
            )
            self.processRunning = True
            self.process.stepstarted.connect(self.stepstarted)
            self.process.processfinished.connect(self.finishedProcess)
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

    # Stops the process. The process's stop function is called, which is connected to the thread's.
    # This saves the trouble of figuring out what you can do before a thread exits when you call its
    # quit() function.
    def stopProcess(self):
        if self.processRunning:
            self.process.stop()
            self.processRunning = False
            self.process = Process()
            logger.info(f'Stopped process {self.process}')

    def assumemanualcontrol(self):
        logger.debug("Execution handler caught manual control request")
        if self.processPaused:
            self.resumeProcess()
        else:
            self.pauseProcess()

    def pauseProcess(self):
        if self.processRunning:
            self.process.pause()
            self.processPaused = True
            logger.info(f'Paused process {self.process}')

    def resumeProcess(self):
        self.process.resume()
        self.processPaused = False

    def advanceStep(self):
        self.process.incrementStep()

    def reverseStep(self):
        self.process.decrementStep()

    def finishedProcess(self):
        self.processRunning = False
        logger.debug("Execution handler wrapped up process")

executionhandler = ExecutionHandler()
