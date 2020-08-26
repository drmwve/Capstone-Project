import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.bigContainerWidget = QtWidgets.QWidget()
        self.screenStack = QtWidgets.QStackedLayout()
        self.addstacks(self.screenStack)
        self.connections()

        self.bigContainerWidget.setLayout(self.screenStack)
        self.setCentralWidget(self.bigContainerWidget)

    def addStacks(self, layout):
        #layout.addWidget(a screen to be added)
        print("nothing yet")

    def connections(self):
        #define button events which move between screens here
        print("nothing yet")


if __name__ == "__main__":
    app = QtCore.QApplication(sys.argv)

    mainScreen = Main()
    mainScreen.show()

    sys.exit(app.exec_())