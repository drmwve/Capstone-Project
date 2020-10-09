from PySide2 import QtCore


x = 0
z = 0
class test:


    def __init__(self):
        super().__init__()
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)
        self.X = 0
        self.Z = 0

    def run(self):
        print(" launching sequence started")
        self.runtimer.start(1000)
        

    def loop(self):
        while self.Z < 10:
            print(self.X)
            self.Z = self.Z + 1
            self.X = self.Z + 1

        

    def stop(self):
        self.runtimer.stop()

test.run()