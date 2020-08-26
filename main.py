import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI.BrewConfig import BrewConfig
from GUI.examplePair.example import example


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.defineMainScreenUI()
        self.createStackedLayout()
        self.connections()

    def defineMainScreenUI(self):
        self.setObjectName("MainWindow")
        self.resize(1024, 600)
        self.setMinimumSize(QtCore.QSize(1024, 600))
        self.setMaximumSize(QtCore.QSize(1024, 600))
        self.setWindowTitle("Auto Brewser System")

    def createStackedLayout(self):
        self.bigContainerWidget = QtWidgets.QWidget()
        self.screenStack = QtWidgets.QStackedLayout()
        self.bigContainerWidget.setLayout(self.screenStack)
        self.setCentralWidget(self.bigContainerWidget)

        #create instances of the screens and add them to the stacked layout here
        self.mainMenu = example()
        self.screenStack.addWidget(self.mainMenu)

        self.brewConfigScreen = BrewConfig()
        self.screenStack.addWidget(self.brewConfigScreen)

    def connections(self):
        #define button events which move between screens here
        print("global connections made")

        #see "goToMenu" function below. the 'lambda: ' statement is required for arcane reasons when calling a function that takes arguments
        #in a signal-slot connection like this
        self.brewConfigScreen.BackButton.clicked.connect(lambda: self.goToMenu(self.mainMenu))
        self.mainMenu.pushButton_2.clicked.connect(lambda: self.goToMenu(self.brewConfigScreen))

    #this just avoids having a million "switch to menu" functions. the menu passed to this function MUST already be in the stacked layout
    def goToMenu(self, menu):
        self.screenStack.setCurrentWidget(menu)



    def exampleExternalAction(self):
        print("You can tell the stacked layout to switch to another screen here, or perform an action that is external to the signaling widget")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    mainScreen = Main()
    mainScreen.show()

    sys.exit(app.exec_())