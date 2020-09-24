from .hardware.devicehandler import DeviceHandler
from PySide2.QtCore import Signal, QObject
from PySide2 import QtCore
from loguru import logger
from time import sleep

class Step(QObject):
    stepcomplete = Signal()
    stepstarted = Signal(str)
    stepcontinuing = Signal()

    def __init__(self):
        super().__init__()
        self.estimatedtime = 0
        self.startingmessage = "Started base step"
        self.running = False

    def execute(self):
        logger.debug(f'Executing step {self} on thread {self.thread()}')
        self.stepstarted.emit(self.startingmessage)
        self.running = True
        self.run()
        self.stepcomplete.emit()

    """Overload and implement in inherited classes"""
    def run(self):
        pass

    def pause(self):
        self.running = False

    def resume(self):
        self.running = True

class ExampleStep(Step):
    def run(self):
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)
        self.index = 0
        self.runtimer.start(500)

    def loop(self):
        logger.debug(self.index)
        self.index += 1


class FillHTL():
    def run(self):
        pass
