from loguru import logger
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QMessageBox

from .Process import *


class ExecutionHandler:
    # I wrap the thread handling up in a neat package. The UI code creates a process and passes it to me with my startProcess(process)
    # function and I create a new thread which this process is executed in.

    processRunning = False

        # the brew controller lives in its own thread to make constantly updating sensors and changing things easier
        # self.brewControls = ControlHandler()
        # self.controllerThread = QtCore.QThread()
        # self.addProcessToThread(self.brewControls, self.controllerThread)
        # self.controllerThread.start()

    # Starts a new process on a new thread. If a thread is already running, show an error.
    @classmethod
    def startProcess(cls, process):
        if not cls.processRunning:
            cls.process = process
            logger.info(
                "Started process "
                + str(cls.process)
            )
            cls.processRunning = True
            cls.process.processfinished.connect(cls.finishedProcess)
            cls.process.start()
        else:
            error = QMessageBox()
            error.setText("A process is already running.")
            error.exec()

    @classmethod
    def startBrewProcess(cls, brewRecipe):
        cls.startProcess(BrewProcess(brewRecipe))

    @classmethod
    def startCleaningProcess(cls):
        cls.startProcess(CleaningProcess())

    # Stops the process. The process's stop function is called, which is connected to the thread's.
    # This saves the trouble of figuring out what you can do before a thread exits when you call its
    # quit() function.
    @classmethod
    def stopProcess(cls):
        if cls.processRunning:
            cls.process.stop()
            cls.processRunning = False
            cls.process = Process()
            logger.info(f'Stopped process {cls.process}')

    @classmethod
    def pauseProcess(cls):
        if cls.processRunning:
            cls.process.stop()

    @classmethod
    def finishedProcess(cls):
        cls.processRunning = False
        logger.debug("Execution handler wrapped up progress")
