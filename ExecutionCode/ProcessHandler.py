from Process import Process

class ProcessHandler():
    #I wrap the thread handling up in a neat package. The UI code creates a process and passes it to me with my startProcess(process)
    #function and I create a new thread which this process is executed in.
    def __init__(self):
        self.processRunning = False

    def startProcess(self, process):
        self.processRunning = True
        self.process = process
        self.process.start()

    def stopProcess(self):
        if self.processRunning:
            self.process.stop()
            self.processRunning = False

    pass