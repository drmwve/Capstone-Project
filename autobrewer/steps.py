from .hardware.devicehandler import DeviceHandler
from PySide2.QtCore import Signal, QObject

class Step(QObject):
    stepcomplete = Signal()
    stepstarted = Signal(str)

    def __init__(self):
        super().__init__()

class ExampleStep():
    def __call__(self):
        self.stepstarted.emit()
        DeviceHandler.open2WBallValve(3)

class fillHTL():
    def __call__(self):
        pass
