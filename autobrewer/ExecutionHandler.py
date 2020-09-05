from Process import BrewProcess, CleaningProcess
from PySide2 import QtCore, QtGui
from loguru import logger
#from ExecutionCode.ControlWrapper import ControlHandler

class ExecutionHandler():
    #I wrap the thread handling up in a neat package. The UI code creates a process and passes it to me with my startProcess(process)
    #function and I create a new thread which this process is executed in.
    def __init__(self):
        self.processRunning = False

        #the brew controller lives in its own thread to make constantly updating sensors and changing things easier
        #self.brewControls = ControlHandler()
        #self.controllerThread = QtCore.QThread()
        #self.addProcessToThread(self.brewControls, self.controllerThread)
        #self.controllerThread.start()

    # Starts a new process on a new thread. If a thread is already running, show an error.
    def startProcess(self, process):
        if not self.processRunning:
            self.processRunning = True
            self.processThread = QtCore.QThread()
            self.process = process
            self.addProcessToThread(self.process, self.processThread)
            self.processThread.start()
            logger.info("Started process " + str(self.process) + " on thread " + str(self.processThread))
        else:
            error = QtGui.QMessageBox()
            error.setText("A process is already running.")
            error.exec()

    def startBrewProcess(self, brewRecipe):
        self.startProcess(BrewProcess(brewRecipe))

    def startCleaningProcess(self):
        self.startProcess(CleaningProcess())

    # Stops the process. The process's stop function is called, which is connected to the thread's.
    # This saves the trouble of figuring out what you can do before a thread exits when you call its
    # quit() function.
    def stopProcess(self):
        if self.processRunning:
            self.process.stop()
            self.processRunning = False
            logger.info("Stopped process " + self.process)

    def addProcessToThread(self, process, thread):
        process.moveToThread(thread)
        thread.started.connect(process.start())
        process.finished.connect(thread.quit())

    pass