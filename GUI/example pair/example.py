from PyQt5 import QtCore, QtGui, QtWidgets
from example_GUI import Ui_Form

class example(QtWidgets.QWidget, Ui_Form):


    def __init__(self):
        super(QtWidgets.Qwidget,self).__init__()
        self.setupUi(self)
        self.connections()
        self.adjustUI()

    def connections(self):
        print("I handle slots and signals which are internal to this widget")

    def adjustUI(self):
        print("I make any small adjustments necessary to the UI code")