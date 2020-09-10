from .hardware.devicehandler import DeviceHandler

class ExampleStep():
    def __call__(self):
        DeviceHandler.open2WBallValve(3)

class fillHTL():
    def __call__(self):
        pass
