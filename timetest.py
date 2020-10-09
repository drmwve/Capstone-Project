from PySide2 import QtCore

timing: int = [3,6,10]
x = 0
z = 0
class test:


    def __init__(self):
        super().__init__()
        self.runtimer = QtCore.QTimer()
        self.runtimer.timeout.connect(self.loop)
        self.Z = timing
        self.X: int = 0

    def run(self):
        print(" launching sequence started")
        self.runtimer.start(self.Z[self.X])

    def loop(self):
        print("waited for %s seconds" % self.Z[self.X])
        self.X += 1
        

    def stop(self):
        self.runtimer.stop()

while z < 3:
    print(timing[x])
    x = x + 1
    z = z + 1



