from PySide2.QtWidgets import QWidget
from .MainMenuGUI import Ui_MainMenu

# copy this and adjust 'Ui_Form' to inherit whatever the class Designer created
class MainMenu(QWidget, Ui_MainMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connections()
        self.adjustUI()

    def connections(self):
        pass

    def adjustUI(self):
        pass
