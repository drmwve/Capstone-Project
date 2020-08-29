from PySide2 import QtCore, QtGui, QtWidgets
from GUI.examplePair.example_GUI import Ui_Form

#copy this and adjust 'Ui_Form' to inherit whatever the class Designer created
class example(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connections()
        self.adjustUI()

    def connections(self):
        #add any connections that are internal to the functioning of this widget only
        self.pushButton.clicked.connect(self.buttonPushed)

    def adjustUI(self):
        self.pushButton.setText("Internal Function")
        self.pushButton_2.setText("Brew Config")

    def buttonPushed(self):
        print("I handle something internal to this widget")