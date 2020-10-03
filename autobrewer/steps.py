from .hardware.devicehandler import DeviceHandler
from PySide2.QtCore import Signal, QObject
from PySide2 import QtCore
from loguru import logger

class Step(QObject):
    stepcomplete = Signal()
    stepstarted = Signal(str)

    def __init__(self):
        super().__init__()
        self.estimatedtime = 0
        self.startingmessage = "Started base step"
        self.running = False

    def execute(self):
        logger.info(f'Executing step {self}')
        self.stepstarted.emit(self.startingmessage)
        self.running = True
        self.run()

    """Overload and implement in inherited classes"""
    def run(self):
        pass

    """Overload and implement in inherited classes"""
    def stop(self):
        pass

class ExampleStep(Step):

    def __init__(self):
        super(ExampleStep, self).__init__()
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)

    def run(self):
        logger.debug(f'Running step {self}')
        self.index = 0
        self.runtimer.start(1000)
        logger.debug(f'Started timer: {self.runtimer.isActive()}')

    def loop(self):
        logger.debug("Running loop")
        self.index += 1
        if self.index > 6:
            self.stepcomplete.emit()
            self.runtimer.stop()

    def stop(self):
        self.runtimer.stop()
        self.index = 0

class FillHTL():
    def run(self):
        pass
