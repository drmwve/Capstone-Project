# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeviceStatusControls.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_DeviceStatusControls(object):
    def setupUi(self, DeviceStatusControls):
        DeviceStatusControls.setObjectName("DeviceStatusControls")
        DeviceStatusControls.resize(1024, 600)
        DeviceStatusControls.setMinimumSize(QtCore.QSize(1024, 600))
        DeviceStatusControls.setMaximumSize(QtCore.QSize(1024, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(DeviceStatusControls)
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BallValveGroupBox = QtWidgets.QGroupBox(DeviceStatusControls)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValveGroupBox.setFont(font)
        self.BallValveGroupBox.setStyleSheet("QGroupBox {border: 1px solid black}")
        self.BallValveGroupBox.setObjectName("BallValveGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.BallValveGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BallValveLayout = QtWidgets.QGridLayout()
        self.BallValveLayout.setContentsMargins(-1, 2, -1, 2)
        self.BallValveLayout.setObjectName("BallValveLayout")
        self.BallValve5Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve5Button.setMinimumSize(QtCore.QSize(0, 0))
        self.BallValve5Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve5Button.setFont(font)
        self.BallValve5Button.setCheckable(True)
        self.BallValve5Button.setObjectName("BallValve5Button")
        self.BallValveLayout.addWidget(self.BallValve5Button, 3, 4, 1, 1)
        self.BallValve2State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve2State.setFont(font)
        self.BallValve2State.setObjectName("BallValve2State")
        self.BallValveLayout.addWidget(self.BallValve2State, 2, 1, 1, 1)
        self.BallValve3Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve3Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve3Label.setFont(font)
        self.BallValve3Label.setObjectName("BallValve3Label")
        self.BallValveLayout.addWidget(self.BallValve3Label, 0, 2, 1, 1)
        self.BallValve5Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve5Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve5Label.setFont(font)
        self.BallValve5Label.setObjectName("BallValve5Label")
        self.BallValveLayout.addWidget(self.BallValve5Label, 0, 4, 1, 1)
        self.BallValve1State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve1State.setFont(font)
        self.BallValve1State.setObjectName("BallValve1State")
        self.BallValveLayout.addWidget(self.BallValve1State, 2, 0, 1, 1)
        self.BallValve2Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve2Label.setFont(font)
        self.BallValve2Label.setObjectName("BallValve2Label")
        self.BallValveLayout.addWidget(self.BallValve2Label, 0, 1, 1, 1)
        self.BallValve5State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve5State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve5State.setFont(font)
        self.BallValve5State.setObjectName("BallValve5State")
        self.BallValveLayout.addWidget(self.BallValve5State, 2, 4, 1, 1)
        self.BallValve3Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve3Button.setMinimumSize(QtCore.QSize(0, 0))
        self.BallValve3Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve3Button.setFont(font)
        self.BallValve3Button.setCheckable(True)
        self.BallValve3Button.setObjectName("BallValve3Button")
        self.BallValveLayout.addWidget(self.BallValve3Button, 3, 2, 1, 1)
        self.BallValve1Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve1Label.setFont(font)
        self.BallValve1Label.setObjectName("BallValve1Label")
        self.BallValveLayout.addWidget(self.BallValve1Label, 0, 0, 1, 1)
        self.BallValve4Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve4Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve4Label.setFont(font)
        self.BallValve4Label.setObjectName("BallValve4Label")
        self.BallValveLayout.addWidget(self.BallValve4Label, 0, 3, 1, 1)
        self.BallValve1Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve1Button.setMinimumSize(QtCore.QSize(0, 0))
        self.BallValve1Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve1Button.setFont(font)
        self.BallValve1Button.setAutoFillBackground(False)
        self.BallValve1Button.setCheckable(True)
        self.BallValve1Button.setObjectName("BallValve1Button")
        self.BallValveLayout.addWidget(self.BallValve1Button, 3, 0, 1, 1)
        self.BallValve4Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve4Button.setMinimumSize(QtCore.QSize(0, 0))
        self.BallValve4Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve4Button.setFont(font)
        self.BallValve4Button.setCheckable(True)
        self.BallValve4Button.setObjectName("BallValve4Button")
        self.BallValveLayout.addWidget(self.BallValve4Button, 3, 3, 1, 1)
        self.BallValve4State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve4State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve4State.setFont(font)
        self.BallValve4State.setObjectName("BallValve4State")
        self.BallValveLayout.addWidget(self.BallValve4State, 2, 3, 1, 1)
        self.BallValve2Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve2Button.setMinimumSize(QtCore.QSize(0, 0))
        self.BallValve2Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve2Button.setFont(font)
        self.BallValve2Button.setCheckable(True)
        self.BallValve2Button.setObjectName("BallValve2Button")
        self.BallValveLayout.addWidget(self.BallValve2Button, 3, 1, 1, 1)
        self.BallValve3State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve3State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.BallValve3State.setFont(font)
        self.BallValve3State.setObjectName("BallValve3State")
        self.BallValveLayout.addWidget(self.BallValve3State, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.BallValveLayout)
        self.verticalLayout.addWidget(self.BallValveGroupBox)
        self.ThreeWayGroupBox = QtWidgets.QGroupBox(DeviceStatusControls)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWayGroupBox.setFont(font)
        self.ThreeWayGroupBox.setObjectName("ThreeWayGroupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ThreeWayGroupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ThreeWayLayout = QtWidgets.QGridLayout()
        self.ThreeWayLayout.setContentsMargins(-1, 2, -1, 2)
        self.ThreeWayLayout.setObjectName("ThreeWayLayout")
        self.ThreeWay4Label = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay4Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay4Label.setFont(font)
        self.ThreeWay4Label.setObjectName("ThreeWay4Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay4Label, 0, 3, 1, 1)
        self.ThreeWay2Label = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay2Label.setFont(font)
        self.ThreeWay2Label.setObjectName("ThreeWay2Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay2Label, 0, 1, 1, 1)
        self.ThreeWay5Label = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay5Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay5Label.setFont(font)
        self.ThreeWay5Label.setObjectName("ThreeWay5Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay5Label, 0, 4, 1, 1)
        self.ThreeWay1State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay1State.setFont(font)
        self.ThreeWay1State.setObjectName("ThreeWay1State")
        self.ThreeWayLayout.addWidget(self.ThreeWay1State, 1, 0, 1, 1)
        self.ThreeWay4State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay4State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay4State.setFont(font)
        self.ThreeWay4State.setObjectName("ThreeWay4State")
        self.ThreeWayLayout.addWidget(self.ThreeWay4State, 1, 3, 1, 1)
        self.ThreeWay2State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay2State.setFont(font)
        self.ThreeWay2State.setObjectName("ThreeWay2State")
        self.ThreeWayLayout.addWidget(self.ThreeWay2State, 1, 1, 1, 1)
        self.ThreeWay5State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay5State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay5State.setFont(font)
        self.ThreeWay5State.setObjectName("ThreeWay5State")
        self.ThreeWayLayout.addWidget(self.ThreeWay5State, 1, 4, 1, 1)
        self.ThreeWay1Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay1Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay1Button.setFont(font)
        self.ThreeWay1Button.setCheckable(True)
        self.ThreeWay1Button.setObjectName("ThreeWay1Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay1Button, 2, 0, 1, 1)
        self.ThreeWay4Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay4Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay4Button.setFont(font)
        self.ThreeWay4Button.setCheckable(True)
        self.ThreeWay4Button.setObjectName("ThreeWay4Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay4Button, 2, 3, 1, 1)
        self.ThreeWay5Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay5Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay5Button.setFont(font)
        self.ThreeWay5Button.setCheckable(True)
        self.ThreeWay5Button.setObjectName("ThreeWay5Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay5Button, 2, 4, 1, 1)
        self.ThreeWay3Label = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay3Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay3Label.setFont(font)
        self.ThreeWay3Label.setObjectName("ThreeWay3Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay3Label, 0, 2, 1, 1)
        self.ThreeWay3Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay3Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay3Button.setFont(font)
        self.ThreeWay3Button.setCheckable(True)
        self.ThreeWay3Button.setObjectName("ThreeWay3Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay3Button, 2, 2, 1, 1)
        self.ThreeWay1Label = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay1Label.setFont(font)
        self.ThreeWay1Label.setObjectName("ThreeWay1Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay1Label, 0, 0, 1, 1)
        self.ThreeWay3State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay3State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay3State.setFont(font)
        self.ThreeWay3State.setObjectName("ThreeWay3State")
        self.ThreeWayLayout.addWidget(self.ThreeWay3State, 1, 2, 1, 1)
        self.ThreeWay2Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay2Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ThreeWay2Button.setFont(font)
        self.ThreeWay2Button.setCheckable(True)
        self.ThreeWay2Button.setObjectName("ThreeWay2Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay2Button, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.ThreeWayLayout)
        self.verticalLayout.addWidget(self.ThreeWayGroupBox)
        self.HeatersGroupBox = QtWidgets.QGroupBox(DeviceStatusControls)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.HeatersGroupBox.setFont(font)
        self.HeatersGroupBox.setObjectName("HeatersGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.HeatersGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.HeaterLayout = QtWidgets.QGridLayout()
        self.HeaterLayout.setContentsMargins(-1, 2, -1, 2)
        self.HeaterLayout.setObjectName("HeaterLayout")
        self.Heater3Button = QtWidgets.QPushButton(self.HeatersGroupBox)
        self.Heater3Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater3Button.setFont(font)
        self.Heater3Button.setCheckable(True)
        self.Heater3Button.setObjectName("Heater3Button")
        self.HeaterLayout.addWidget(self.Heater3Button, 2, 2, 1, 1)
        self.Heater1State = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater1State.setFont(font)
        self.Heater1State.setObjectName("Heater1State")
        self.HeaterLayout.addWidget(self.Heater1State, 1, 0, 1, 1)
        self.Heater2Button = QtWidgets.QPushButton(self.HeatersGroupBox)
        self.Heater2Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater2Button.setFont(font)
        self.Heater2Button.setCheckable(True)
        self.Heater2Button.setObjectName("Heater2Button")
        self.HeaterLayout.addWidget(self.Heater2Button, 2, 1, 1, 1)
        self.Heater3State = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater3State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater3State.setFont(font)
        self.Heater3State.setObjectName("Heater3State")
        self.HeaterLayout.addWidget(self.Heater3State, 1, 2, 1, 1)
        self.Heater4Label = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater4Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater4Label.setFont(font)
        self.Heater4Label.setObjectName("Heater4Label")
        self.HeaterLayout.addWidget(self.Heater4Label, 0, 3, 1, 1)
        self.Heater1Button = QtWidgets.QPushButton(self.HeatersGroupBox)
        self.Heater1Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater1Button.setFont(font)
        self.Heater1Button.setCheckable(True)
        self.Heater1Button.setObjectName("Heater1Button")
        self.HeaterLayout.addWidget(self.Heater1Button, 2, 0, 1, 1)
        self.Heater1Label = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater1Label.setFont(font)
        self.Heater1Label.setObjectName("Heater1Label")
        self.HeaterLayout.addWidget(self.Heater1Label, 0, 0, 1, 1)
        self.Heater3Label = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater3Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater3Label.setFont(font)
        self.Heater3Label.setObjectName("Heater3Label")
        self.HeaterLayout.addWidget(self.Heater3Label, 0, 2, 1, 1)
        self.Heater2State = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater2State.setFont(font)
        self.Heater2State.setObjectName("Heater2State")
        self.HeaterLayout.addWidget(self.Heater2State, 1, 1, 1, 1)
        self.Heater2Label = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater2Label.setFont(font)
        self.Heater2Label.setObjectName("Heater2Label")
        self.HeaterLayout.addWidget(self.Heater2Label, 0, 1, 1, 1)
        self.Heater4Button = QtWidgets.QPushButton(self.HeatersGroupBox)
        self.Heater4Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater4Button.setFont(font)
        self.Heater4Button.setCheckable(True)
        self.Heater4Button.setObjectName("Heater4Button")
        self.HeaterLayout.addWidget(self.Heater4Button, 2, 3, 1, 1)
        self.Heater4State = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater4State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Heater4State.setFont(font)
        self.Heater4State.setObjectName("Heater4State")
        self.HeaterLayout.addWidget(self.Heater4State, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.HeaterLayout)
        self.verticalLayout.addWidget(self.HeatersGroupBox)
        self.PumpsGroupBox = QtWidgets.QGroupBox(DeviceStatusControls)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PumpsGroupBox.setFont(font)
        self.PumpsGroupBox.setObjectName("PumpsGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.PumpsGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.PumpLayout = QtWidgets.QGridLayout()
        self.PumpLayout.setContentsMargins(-1, 2, -1, 2)
        self.PumpLayout.setObjectName("PumpLayout")
        self.Pump2State = QtWidgets.QLabel(self.PumpsGroupBox)
        self.Pump2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Pump2State.setFont(font)
        self.Pump2State.setObjectName("Pump2State")
        self.PumpLayout.addWidget(self.Pump2State, 1, 1, 1, 1)
        self.Pump1State = QtWidgets.QLabel(self.PumpsGroupBox)
        self.Pump1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Pump1State.setFont(font)
        self.Pump1State.setObjectName("Pump1State")
        self.PumpLayout.addWidget(self.Pump1State, 1, 0, 1, 1)
        self.Pump2Button = QtWidgets.QPushButton(self.PumpsGroupBox)
        self.Pump2Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Pump2Button.setFont(font)
        self.Pump2Button.setCheckable(True)
        self.Pump2Button.setObjectName("Pump2Button")
        self.PumpLayout.addWidget(self.Pump2Button, 2, 1, 1, 1)
        self.Pump2Label = QtWidgets.QLabel(self.PumpsGroupBox)
        self.Pump2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Pump2Label.setFont(font)
        self.Pump2Label.setObjectName("Pump2Label")
        self.PumpLayout.addWidget(self.Pump2Label, 0, 1, 1, 1)
        self.Pump1Button = QtWidgets.QPushButton(self.PumpsGroupBox)
        self.Pump1Button.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Pump1Button.setFont(font)
        self.Pump1Button.setCheckable(True)
        self.Pump1Button.setObjectName("Pump1Button")
        self.PumpLayout.addWidget(self.Pump1Button, 2, 0, 1, 1)
        self.Pump1Label = QtWidgets.QLabel(self.PumpsGroupBox)
        self.Pump1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Pump1Label.setFont(font)
        self.Pump1Label.setObjectName("Pump1Label")
        self.PumpLayout.addWidget(self.Pump1Label, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.PumpLayout)
        self.verticalLayout.addWidget(self.PumpsGroupBox)
        self.GoToSensorStatusButton = QtWidgets.QPushButton(DeviceStatusControls)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GoToSensorStatusButton.setFont(font)
        self.GoToSensorStatusButton.setObjectName("GoToSensorStatusButton")
        self.verticalLayout.addWidget(self.GoToSensorStatusButton)
        self.ReturnToMenuButton = QtWidgets.QPushButton(DeviceStatusControls)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ReturnToMenuButton.setFont(font)
        self.ReturnToMenuButton.setObjectName("ReturnToMenuButton")
        self.verticalLayout.addWidget(self.ReturnToMenuButton)

        self.retranslateUi(DeviceStatusControls)
        QtCore.QMetaObject.connectSlotsByName(DeviceStatusControls)

    def retranslateUi(self, DeviceStatusControls):
        _translate = QtCore.QCoreApplication.translate
        DeviceStatusControls.setWindowTitle(_translate("DeviceStatusControls", "Form"))
        self.BallValveGroupBox.setTitle(_translate("DeviceStatusControls", "Ball Valves"))
        self.BallValve5Button.setText(_translate("DeviceStatusControls", "Open"))
        self.BallValve2State.setText(_translate("DeviceStatusControls", "State: Closed"))
        self.BallValve3Label.setText(_translate("DeviceStatusControls", "Ball Valve: 3"))
        self.BallValve5Label.setText(_translate("DeviceStatusControls", "Ball Valve: 5"))
        self.BallValve1State.setText(_translate("DeviceStatusControls", "State: Closed"))
        self.BallValve2Label.setText(_translate("DeviceStatusControls", "Ball Valve: 2"))
        self.BallValve5State.setText(_translate("DeviceStatusControls", "State: Closed"))
        self.BallValve3Button.setText(_translate("DeviceStatusControls", "Open"))
        self.BallValve1Label.setText(_translate("DeviceStatusControls", "Ball Valve: 1"))
        self.BallValve4Label.setText(_translate("DeviceStatusControls", "Ball Valve: 4"))
        self.BallValve1Button.setText(_translate("DeviceStatusControls", "Open"))
        self.BallValve4Button.setText(_translate("DeviceStatusControls", "Open"))
        self.BallValve4State.setText(_translate("DeviceStatusControls", "State: Closed"))
        self.BallValve2Button.setText(_translate("DeviceStatusControls", "Open"))
        self.BallValve3State.setText(_translate("DeviceStatusControls", "State: Closed"))
        self.ThreeWayGroupBox.setStyleSheet(_translate("DeviceStatusControls", "QGroupBox {border: 1px solid black}"))
        self.ThreeWayGroupBox.setTitle(_translate("DeviceStatusControls", "Three Way Valves"))
        self.ThreeWay4Label.setText(_translate("DeviceStatusControls", "Three Way Valve: 4"))
        self.ThreeWay2Label.setText(_translate("DeviceStatusControls", "Three Way Valve: 2"))
        self.ThreeWay5Label.setText(_translate("DeviceStatusControls", "Three Way Valve: 5"))
        self.ThreeWay1State.setText(_translate("DeviceStatusControls", "State: Direction 1"))
        self.ThreeWay4State.setText(_translate("DeviceStatusControls", "State: Direction 1"))
        self.ThreeWay2State.setText(_translate("DeviceStatusControls", "State: Direction 1"))
        self.ThreeWay5State.setText(_translate("DeviceStatusControls", "State: Direction 1"))
        self.ThreeWay1Button.setText(_translate("DeviceStatusControls", "Switch Direction"))
        self.ThreeWay4Button.setText(_translate("DeviceStatusControls", "Switch Direction"))
        self.ThreeWay5Button.setText(_translate("DeviceStatusControls", "Switch Direction"))
        self.ThreeWay3Label.setText(_translate("DeviceStatusControls", "Three Way Valve: 3"))
        self.ThreeWay3Button.setText(_translate("DeviceStatusControls", "Switch Direction"))
        self.ThreeWay1Label.setText(_translate("DeviceStatusControls", "Three Way Valve: 1"))
        self.ThreeWay3State.setText(_translate("DeviceStatusControls", "State: Direction 1"))
        self.ThreeWay2Button.setText(_translate("DeviceStatusControls", "Switch Direction"))
        self.HeatersGroupBox.setStyleSheet(_translate("DeviceStatusControls", "QGroupBox {border: 1px solid black}"))
        self.HeatersGroupBox.setTitle(_translate("DeviceStatusControls", "Heaters"))
        self.Heater3Button.setText(_translate("DeviceStatusControls", "Turn On"))
        self.Heater1State.setText(_translate("DeviceStatusControls", "State: Off"))
        self.Heater2Button.setText(_translate("DeviceStatusControls", "Turn On"))
        self.Heater3State.setText(_translate("DeviceStatusControls", "State: Off"))
        self.Heater4Label.setText(_translate("DeviceStatusControls", "Heater: 4"))
        self.Heater1Button.setText(_translate("DeviceStatusControls", "Turn On"))
        self.Heater1Label.setText(_translate("DeviceStatusControls", "Heater: 1"))
        self.Heater3Label.setText(_translate("DeviceStatusControls", "Heater: 3"))
        self.Heater2State.setText(_translate("DeviceStatusControls", "State: Off"))
        self.Heater2Label.setText(_translate("DeviceStatusControls", "Heater: 2"))
        self.Heater4Button.setText(_translate("DeviceStatusControls", "Turn On"))
        self.Heater4State.setText(_translate("DeviceStatusControls", "State: Off"))
        self.PumpsGroupBox.setStyleSheet(_translate("DeviceStatusControls", "QGroupBox {border: 1px solid black}"))
        self.PumpsGroupBox.setTitle(_translate("DeviceStatusControls", "Pumps"))
        self.Pump2State.setText(_translate("DeviceStatusControls", "State: Off"))
        self.Pump1State.setText(_translate("DeviceStatusControls", "State: Off"))
        self.Pump2Button.setText(_translate("DeviceStatusControls", "Turn On"))
        self.Pump2Label.setText(_translate("DeviceStatusControls", "Pump: 2"))
        self.Pump1Button.setText(_translate("DeviceStatusControls", "Turn On"))
        self.Pump1Label.setText(_translate("DeviceStatusControls", "Pump: 1"))
        self.GoToSensorStatusButton.setText(_translate("DeviceStatusControls", "Sensor Status"))
        self.ReturnToMenuButton.setText(_translate("DeviceStatusControls", "Return to Main Menu"))
