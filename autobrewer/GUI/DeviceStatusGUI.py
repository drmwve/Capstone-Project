# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeviceStatus.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_DeviceStatus(object):
    def setupUi(self, DeviceStatus):
        DeviceStatus.setObjectName("DeviceStatus")
        DeviceStatus.resize(1024, 600)
        DeviceStatus.setMinimumSize(QtCore.QSize(1024, 600))
        DeviceStatus.setMaximumSize(QtCore.QSize(1024, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(DeviceStatus)
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BallValveGroupBox = QtWidgets.QGroupBox(DeviceStatus)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.BallValveGroupBox.setFont(font)
        self.BallValveGroupBox.setStyleSheet("QGroupBox {border: 1px solid black}")
        self.BallValveGroupBox.setObjectName("BallValveGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.BallValveGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BallValveLayout = QtWidgets.QGridLayout()
        self.BallValveLayout.setContentsMargins(-1, 2, -1, 2)
        self.BallValveLayout.setObjectName("BallValveLayout")
        self.BallValve5Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve5Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve5Button.setFont(font)
        self.BallValve5Button.setCheckable(True)
        self.BallValve5Button.setObjectName("BallValve5Button")
        self.BallValveLayout.addWidget(self.BallValve5Button, 3, 4, 1, 1)
        self.BallValve2State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve2State.setFont(font)
        self.BallValve2State.setObjectName("BallValve2State")
        self.BallValveLayout.addWidget(self.BallValve2State, 2, 1, 1, 1)
        self.BallValve3Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve3Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve3Label.setFont(font)
        self.BallValve3Label.setObjectName("BallValve3Label")
        self.BallValveLayout.addWidget(self.BallValve3Label, 0, 2, 1, 1)
        self.BallValve5Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve5Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve5Label.setFont(font)
        self.BallValve5Label.setObjectName("BallValve5Label")
        self.BallValveLayout.addWidget(self.BallValve5Label, 0, 4, 1, 1)
        self.BallValve1State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve1State.setFont(font)
        self.BallValve1State.setObjectName("BallValve1State")
        self.BallValveLayout.addWidget(self.BallValve1State, 2, 0, 1, 1)
        self.BallValve2Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve2Label.setFont(font)
        self.BallValve2Label.setObjectName("BallValve2Label")
        self.BallValveLayout.addWidget(self.BallValve2Label, 0, 1, 1, 1)
        self.BallValve5State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve5State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve5State.setFont(font)
        self.BallValve5State.setObjectName("BallValve5State")
        self.BallValveLayout.addWidget(self.BallValve5State, 2, 4, 1, 1)
        self.BallValve3Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve3Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve3Button.setFont(font)
        self.BallValve3Button.setCheckable(True)
        self.BallValve3Button.setObjectName("BallValve3Button")
        self.BallValveLayout.addWidget(self.BallValve3Button, 3, 2, 1, 1)
        self.BallValve1Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve1Label.setFont(font)
        self.BallValve1Label.setObjectName("BallValve1Label")
        self.BallValveLayout.addWidget(self.BallValve1Label, 0, 0, 1, 1)
        self.BallValve4Label = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve4Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve4Label.setFont(font)
        self.BallValve4Label.setObjectName("BallValve4Label")
        self.BallValveLayout.addWidget(self.BallValve4Label, 0, 3, 1, 1)
        self.BallValve1Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve1Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve1Button.setFont(font)
        self.BallValve1Button.setAutoFillBackground(False)
        self.BallValve1Button.setCheckable(True)
        self.BallValve1Button.setObjectName("BallValve1Button")
        self.BallValveLayout.addWidget(self.BallValve1Button, 3, 0, 1, 1)
        self.BallValve4Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve4Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve4Button.setFont(font)
        self.BallValve4Button.setCheckable(True)
        self.BallValve4Button.setObjectName("BallValve4Button")
        self.BallValveLayout.addWidget(self.BallValve4Button, 3, 3, 1, 1)
        self.BallValve4State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve4State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve4State.setFont(font)
        self.BallValve4State.setObjectName("BallValve4State")
        self.BallValveLayout.addWidget(self.BallValve4State, 2, 3, 1, 1)
        self.BallValve2Button = QtWidgets.QPushButton(self.BallValveGroupBox)
        self.BallValve2Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve2Button.setFont(font)
        self.BallValve2Button.setCheckable(True)
        self.BallValve2Button.setObjectName("BallValve2Button")
        self.BallValveLayout.addWidget(self.BallValve2Button, 3, 1, 1, 1)
        self.BallValve3State = QtWidgets.QLabel(self.BallValveGroupBox)
        self.BallValve3State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BallValve3State.setFont(font)
        self.BallValve3State.setObjectName("BallValve3State")
        self.BallValveLayout.addWidget(self.BallValve3State, 2, 2, 1, 1)
        self.horizontalLayout.addLayout(self.BallValveLayout)
        self.verticalLayout.addWidget(self.BallValveGroupBox)
        self.ThreeWayGroupBox = QtWidgets.QGroupBox(DeviceStatus)
        font = QtGui.QFont()
        font.setPointSize(7)
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
        font.setPointSize(10)
        self.ThreeWay4Label.setFont(font)
        self.ThreeWay4Label.setObjectName("ThreeWay4Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay4Label, 0, 3, 1, 1)
        self.ThreeWay2Label = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay2Label.setFont(font)
        self.ThreeWay2Label.setObjectName("ThreeWay2Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay2Label, 0, 1, 1, 1)
        self.ThreeWay5Label = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay5Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay5Label.setFont(font)
        self.ThreeWay5Label.setObjectName("ThreeWay5Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay5Label, 0, 4, 1, 1)
        self.ThreeWay1State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay1State.setFont(font)
        self.ThreeWay1State.setObjectName("ThreeWay1State")
        self.ThreeWayLayout.addWidget(self.ThreeWay1State, 1, 0, 1, 1)
        self.ThreeWay4State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay4State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay4State.setFont(font)
        self.ThreeWay4State.setObjectName("ThreeWay4State")
        self.ThreeWayLayout.addWidget(self.ThreeWay4State, 1, 3, 1, 1)
        self.ThreeWay2State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay2State.setFont(font)
        self.ThreeWay2State.setObjectName("ThreeWay2State")
        self.ThreeWayLayout.addWidget(self.ThreeWay2State, 1, 1, 1, 1)
        self.ThreeWay5State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay5State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay5State.setFont(font)
        self.ThreeWay5State.setObjectName("ThreeWay5State")
        self.ThreeWayLayout.addWidget(self.ThreeWay5State, 1, 4, 1, 1)
        self.ThreeWay1Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay1Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay1Button.setFont(font)
        self.ThreeWay1Button.setCheckable(True)
        self.ThreeWay1Button.setObjectName("ThreeWay1Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay1Button, 2, 0, 1, 1)
        self.ThreeWay4Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay4Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay4Button.setFont(font)
        self.ThreeWay4Button.setCheckable(True)
        self.ThreeWay4Button.setObjectName("ThreeWay4Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay4Button, 2, 3, 1, 1)
        self.ThreeWay5Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay5Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay5Button.setFont(font)
        self.ThreeWay5Button.setCheckable(True)
        self.ThreeWay5Button.setObjectName("ThreeWay5Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay5Button, 2, 4, 1, 1)
        self.ThreeWay3Label = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay3Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay3Label.setFont(font)
        self.ThreeWay3Label.setObjectName("ThreeWay3Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay3Label, 0, 2, 1, 1)
        self.ThreeWay3Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay3Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay3Button.setFont(font)
        self.ThreeWay3Button.setCheckable(True)
        self.ThreeWay3Button.setObjectName("ThreeWay3Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay3Button, 2, 2, 1, 1)
        self.ThreeWay1Label = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay1Label.setFont(font)
        self.ThreeWay1Label.setObjectName("ThreeWay1Label")
        self.ThreeWayLayout.addWidget(self.ThreeWay1Label, 0, 0, 1, 1)
        self.ThreeWay3State = QtWidgets.QLabel(self.ThreeWayGroupBox)
        self.ThreeWay3State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay3State.setFont(font)
        self.ThreeWay3State.setObjectName("ThreeWay3State")
        self.ThreeWayLayout.addWidget(self.ThreeWay3State, 1, 2, 1, 1)
        self.ThreeWay2Button = QtWidgets.QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay2Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ThreeWay2Button.setFont(font)
        self.ThreeWay2Button.setCheckable(True)
        self.ThreeWay2Button.setObjectName("ThreeWay2Button")
        self.ThreeWayLayout.addWidget(self.ThreeWay2Button, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.ThreeWayLayout)
        self.verticalLayout.addWidget(self.ThreeWayGroupBox)
        self.HeatersGroupBox = QtWidgets.QGroupBox(DeviceStatus)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.HeatersGroupBox.setFont(font)
        self.HeatersGroupBox.setObjectName("HeatersGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.HeatersGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.HeaterLayout = QtWidgets.QGridLayout()
        self.HeaterLayout.setContentsMargins(-1, 2, -1, 2)
        self.HeaterLayout.setObjectName("HeaterLayout")
        self.Heater3Button = QtWidgets.QPushButton(self.HeatersGroupBox)
        self.Heater3Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater3Button.setFont(font)
        self.Heater3Button.setCheckable(True)
        self.Heater3Button.setObjectName("Heater3Button")
        self.HeaterLayout.addWidget(self.Heater3Button, 2, 2, 1, 1)
        self.Heater1State = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater1State.setFont(font)
        self.Heater1State.setObjectName("Heater1State")
        self.HeaterLayout.addWidget(self.Heater1State, 1, 0, 1, 1)
        self.Heater2Button = QtWidgets.QPushButton(self.HeatersGroupBox)
        self.Heater2Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater2Button.setFont(font)
        self.Heater2Button.setCheckable(True)
        self.Heater2Button.setObjectName("Heater2Button")
        self.HeaterLayout.addWidget(self.Heater2Button, 2, 1, 1, 1)
        self.Heater3State = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater3State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater3State.setFont(font)
        self.Heater3State.setObjectName("Heater3State")
        self.HeaterLayout.addWidget(self.Heater3State, 1, 2, 1, 1)
        self.Heater4Label = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater4Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater4Label.setFont(font)
        self.Heater4Label.setObjectName("Heater4Label")
        self.HeaterLayout.addWidget(self.Heater4Label, 0, 3, 1, 1)
        self.Heater1Button = QtWidgets.QPushButton(self.HeatersGroupBox)
        self.Heater1Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater1Button.setFont(font)
        self.Heater1Button.setCheckable(True)
        self.Heater1Button.setObjectName("Heater1Button")
        self.HeaterLayout.addWidget(self.Heater1Button, 2, 0, 1, 1)
        self.Heater1Label = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater1Label.setFont(font)
        self.Heater1Label.setObjectName("Heater1Label")
        self.HeaterLayout.addWidget(self.Heater1Label, 0, 0, 1, 1)
        self.Heater3Label = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater3Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater3Label.setFont(font)
        self.Heater3Label.setObjectName("Heater3Label")
        self.HeaterLayout.addWidget(self.Heater3Label, 0, 2, 1, 1)
        self.Heater2State = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater2State.setFont(font)
        self.Heater2State.setObjectName("Heater2State")
        self.HeaterLayout.addWidget(self.Heater2State, 1, 1, 1, 1)
        self.Heater2Label = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater2Label.setFont(font)
        self.Heater2Label.setObjectName("Heater2Label")
        self.HeaterLayout.addWidget(self.Heater2Label, 0, 1, 1, 1)
        self.Heater4Button = QtWidgets.QPushButton(self.HeatersGroupBox)
        self.Heater4Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater4Button.setFont(font)
        self.Heater4Button.setCheckable(True)
        self.Heater4Button.setObjectName("Heater4Button")
        self.HeaterLayout.addWidget(self.Heater4Button, 2, 3, 1, 1)
        self.Heater4State = QtWidgets.QLabel(self.HeatersGroupBox)
        self.Heater4State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Heater4State.setFont(font)
        self.Heater4State.setObjectName("Heater4State")
        self.HeaterLayout.addWidget(self.Heater4State, 1, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.HeaterLayout)
        self.verticalLayout.addWidget(self.HeatersGroupBox)
        self.PumpsGroupBox = QtWidgets.QGroupBox(DeviceStatus)
        font = QtGui.QFont()
        font.setPointSize(7)
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
        font.setPointSize(10)
        self.Pump2State.setFont(font)
        self.Pump2State.setObjectName("Pump2State")
        self.PumpLayout.addWidget(self.Pump2State, 1, 1, 1, 1)
        self.Pump1State = QtWidgets.QLabel(self.PumpsGroupBox)
        self.Pump1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Pump1State.setFont(font)
        self.Pump1State.setObjectName("Pump1State")
        self.PumpLayout.addWidget(self.Pump1State, 1, 0, 1, 1)
        self.Pump2Button = QtWidgets.QPushButton(self.PumpsGroupBox)
        self.Pump2Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Pump2Button.setFont(font)
        self.Pump2Button.setCheckable(True)
        self.Pump2Button.setObjectName("Pump2Button")
        self.PumpLayout.addWidget(self.Pump2Button, 2, 1, 1, 1)
        self.Pump2Label = QtWidgets.QLabel(self.PumpsGroupBox)
        self.Pump2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Pump2Label.setFont(font)
        self.Pump2Label.setObjectName("Pump2Label")
        self.PumpLayout.addWidget(self.Pump2Label, 0, 1, 1, 1)
        self.Pump1Button = QtWidgets.QPushButton(self.PumpsGroupBox)
        self.Pump1Button.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Pump1Button.setFont(font)
        self.Pump1Button.setCheckable(True)
        self.Pump1Button.setObjectName("Pump1Button")
        self.PumpLayout.addWidget(self.Pump1Button, 2, 0, 1, 1)
        self.Pump1Label = QtWidgets.QLabel(self.PumpsGroupBox)
        self.Pump1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Pump1Label.setFont(font)
        self.Pump1Label.setObjectName("Pump1Label")
        self.PumpLayout.addWidget(self.Pump1Label, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.PumpLayout)
        self.verticalLayout.addWidget(self.PumpsGroupBox)
        self.TempSensGroupBox = QtWidgets.QGroupBox(DeviceStatus)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.TempSensGroupBox.setFont(font)
        self.TempSensGroupBox.setObjectName("TempSensGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.TempSensGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.TempSensLayout = QtWidgets.QGridLayout()
        self.TempSensLayout.setContentsMargins(-1, 2, -1, 2)
        self.TempSensLayout.setObjectName("TempSensLayout")
        self.TempSens1State = QtWidgets.QLabel(self.TempSensGroupBox)
        self.TempSens1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempSens1State.setFont(font)
        self.TempSens1State.setObjectName("TempSens1State")
        self.TempSensLayout.addWidget(self.TempSens1State, 1, 0, 1, 1)
        self.TempSens2State = QtWidgets.QLabel(self.TempSensGroupBox)
        self.TempSens2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempSens2State.setFont(font)
        self.TempSens2State.setObjectName("TempSens2State")
        self.TempSensLayout.addWidget(self.TempSens2State, 1, 1, 1, 1)
        self.TempSens3Label = QtWidgets.QLabel(self.TempSensGroupBox)
        self.TempSens3Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempSens3Label.setFont(font)
        self.TempSens3Label.setObjectName("TempSens3Label")
        self.TempSensLayout.addWidget(self.TempSens3Label, 0, 2, 1, 1)
        self.TempSens1Label = QtWidgets.QLabel(self.TempSensGroupBox)
        self.TempSens1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempSens1Label.setFont(font)
        self.TempSens1Label.setObjectName("TempSens1Label")
        self.TempSensLayout.addWidget(self.TempSens1Label, 0, 0, 1, 1)
        self.TempSens2Label = QtWidgets.QLabel(self.TempSensGroupBox)
        self.TempSens2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempSens2Label.setFont(font)
        self.TempSens2Label.setObjectName("TempSens2Label")
        self.TempSensLayout.addWidget(self.TempSens2Label, 0, 1, 1, 1)
        self.TempSens3State = QtWidgets.QLabel(self.TempSensGroupBox)
        self.TempSens3State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TempSens3State.setFont(font)
        self.TempSens3State.setObjectName("TempSens3State")
        self.TempSensLayout.addWidget(self.TempSens3State, 1, 2, 1, 1)
        self.verticalLayout_4.addLayout(self.TempSensLayout)
        self.verticalLayout.addWidget(self.TempSensGroupBox)
        self.FlowSensGroupBox = QtWidgets.QGroupBox(DeviceStatus)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.FlowSensGroupBox.setFont(font)
        self.FlowSensGroupBox.setObjectName("FlowSensGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.FlowSensGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.FlowSensLayout = QtWidgets.QGridLayout()
        self.FlowSensLayout.setContentsMargins(-1, 2, -1, 2)
        self.FlowSensLayout.setObjectName("FlowSensLayout")
        self.FlowSens1State = QtWidgets.QLabel(self.FlowSensGroupBox)
        self.FlowSens1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FlowSens1State.setFont(font)
        self.FlowSens1State.setObjectName("FlowSens1State")
        self.FlowSensLayout.addWidget(self.FlowSens1State, 1, 0, 1, 1)
        self.FlowSens2State = QtWidgets.QLabel(self.FlowSensGroupBox)
        self.FlowSens2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FlowSens2State.setFont(font)
        self.FlowSens2State.setObjectName("FlowSens2State")
        self.FlowSensLayout.addWidget(self.FlowSens2State, 1, 1, 1, 1)
        self.FlowSens3Label = QtWidgets.QLabel(self.FlowSensGroupBox)
        self.FlowSens3Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FlowSens3Label.setFont(font)
        self.FlowSens3Label.setObjectName("FlowSens3Label")
        self.FlowSensLayout.addWidget(self.FlowSens3Label, 0, 2, 1, 1)
        self.FlowSens2Label = QtWidgets.QLabel(self.FlowSensGroupBox)
        self.FlowSens2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FlowSens2Label.setFont(font)
        self.FlowSens2Label.setObjectName("FlowSens2Label")
        self.FlowSensLayout.addWidget(self.FlowSens2Label, 0, 1, 1, 1)
        self.FlowSens3State = QtWidgets.QLabel(self.FlowSensGroupBox)
        self.FlowSens3State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FlowSens3State.setFont(font)
        self.FlowSens3State.setObjectName("FlowSens3State")
        self.FlowSensLayout.addWidget(self.FlowSens3State, 1, 2, 1, 1)
        self.FlowSens1Label = QtWidgets.QLabel(self.FlowSensGroupBox)
        self.FlowSens1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FlowSens1Label.setFont(font)
        self.FlowSens1Label.setObjectName("FlowSens1Label")
        self.FlowSensLayout.addWidget(self.FlowSens1Label, 0, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.FlowSensLayout)
        self.verticalLayout.addWidget(self.FlowSensGroupBox)
        self.LevelSensGroupBox = QtWidgets.QGroupBox(DeviceStatus)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.LevelSensGroupBox.setFont(font)
        self.LevelSensGroupBox.setObjectName("LevelSensGroupBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.LevelSensGroupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.LevelSensLayout = QtWidgets.QGridLayout()
        self.LevelSensLayout.setContentsMargins(-1, 2, -1, 2)
        self.LevelSensLayout.setObjectName("LevelSensLayout")
        self.LevelSens1State = QtWidgets.QLabel(self.LevelSensGroupBox)
        self.LevelSens1State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LevelSens1State.setFont(font)
        self.LevelSens1State.setObjectName("LevelSens1State")
        self.LevelSensLayout.addWidget(self.LevelSens1State, 1, 0, 1, 1)
        self.LevelSens2State = QtWidgets.QLabel(self.LevelSensGroupBox)
        self.LevelSens2State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LevelSens2State.setFont(font)
        self.LevelSens2State.setObjectName("LevelSens2State")
        self.LevelSensLayout.addWidget(self.LevelSens2State, 1, 1, 1, 1)
        self.LevelSens3Label = QtWidgets.QLabel(self.LevelSensGroupBox)
        self.LevelSens3Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LevelSens3Label.setFont(font)
        self.LevelSens3Label.setObjectName("LevelSens3Label")
        self.LevelSensLayout.addWidget(self.LevelSens3Label, 0, 2, 1, 1)
        self.LevelSens1Label = QtWidgets.QLabel(self.LevelSensGroupBox)
        self.LevelSens1Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LevelSens1Label.setFont(font)
        self.LevelSens1Label.setObjectName("LevelSens1Label")
        self.LevelSensLayout.addWidget(self.LevelSens1Label, 0, 0, 1, 1)
        self.LevelSens2Label = QtWidgets.QLabel(self.LevelSensGroupBox)
        self.LevelSens2Label.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LevelSens2Label.setFont(font)
        self.LevelSens2Label.setObjectName("LevelSens2Label")
        self.LevelSensLayout.addWidget(self.LevelSens2Label, 0, 1, 1, 1)
        self.LevelSens3State = QtWidgets.QLabel(self.LevelSensGroupBox)
        self.LevelSens3State.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LevelSens3State.setFont(font)
        self.LevelSens3State.setObjectName("LevelSens3State")
        self.LevelSensLayout.addWidget(self.LevelSens3State, 1, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.LevelSensLayout)
        self.verticalLayout.addWidget(self.LevelSensGroupBox)
        self.ReturnToMenuButton = QtWidgets.QPushButton(DeviceStatus)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ReturnToMenuButton.setFont(font)
        self.ReturnToMenuButton.setObjectName("ReturnToMenuButton")
        self.verticalLayout.addWidget(self.ReturnToMenuButton)

        self.retranslateUi(DeviceStatus)
        QtCore.QMetaObject.connectSlotsByName(DeviceStatus)

    def retranslateUi(self, DeviceStatus):
        _translate = QtCore.QCoreApplication.translate
        DeviceStatus.setWindowTitle(_translate("DeviceStatus", "Form"))
        self.BallValveGroupBox.setTitle(_translate("DeviceStatus", "Ball Valves"))
        self.BallValve5Button.setText(_translate("DeviceStatus", "Open"))
        self.BallValve2State.setText(_translate("DeviceStatus", "State: Closed"))
        self.BallValve3Label.setText(_translate("DeviceStatus", "Ball Valve: 3"))
        self.BallValve5Label.setText(_translate("DeviceStatus", "Ball Valve: 5"))
        self.BallValve1State.setText(_translate("DeviceStatus", "State: Closed"))
        self.BallValve2Label.setText(_translate("DeviceStatus", "Ball Valve: 2"))
        self.BallValve5State.setText(_translate("DeviceStatus", "State: Closed"))
        self.BallValve3Button.setText(_translate("DeviceStatus", "Open"))
        self.BallValve1Label.setText(_translate("DeviceStatus", "Ball Valve: 1"))
        self.BallValve4Label.setText(_translate("DeviceStatus", "Ball Valve: 4"))
        self.BallValve1Button.setText(_translate("DeviceStatus", "Open"))
        self.BallValve4Button.setText(_translate("DeviceStatus", "Open"))
        self.BallValve4State.setText(_translate("DeviceStatus", "State: Closed"))
        self.BallValve2Button.setText(_translate("DeviceStatus", "Open"))
        self.BallValve3State.setText(_translate("DeviceStatus", "State: Closed"))
        self.ThreeWayGroupBox.setStyleSheet(
            _translate("DeviceStatus", "QGroupBox {border: 1px solid black}")
        )
        self.ThreeWayGroupBox.setTitle(_translate("DeviceStatus", "Three Way Valves"))
        self.ThreeWay4Label.setText(_translate("DeviceStatus", "Three Way Valve: 4"))
        self.ThreeWay2Label.setText(_translate("DeviceStatus", "Three Way Valve: 2"))
        self.ThreeWay5Label.setText(_translate("DeviceStatus", "Three Way Valve: 5"))
        self.ThreeWay1State.setText(_translate("DeviceStatus", "State: Direction 1"))
        self.ThreeWay4State.setText(_translate("DeviceStatus", "State: Direction 1"))
        self.ThreeWay2State.setText(_translate("DeviceStatus", "State: Direction 1"))
        self.ThreeWay5State.setText(_translate("DeviceStatus", "State: Direction 1"))
        self.ThreeWay1Button.setText(_translate("DeviceStatus", "Switch Direction"))
        self.ThreeWay4Button.setText(_translate("DeviceStatus", "Switch Direction"))
        self.ThreeWay5Button.setText(_translate("DeviceStatus", "Switch Direction"))
        self.ThreeWay3Label.setText(_translate("DeviceStatus", "Three Way Valve: 3"))
        self.ThreeWay3Button.setText(_translate("DeviceStatus", "Switch Direction"))
        self.ThreeWay1Label.setText(_translate("DeviceStatus", "Three Way Valve: 1"))
        self.ThreeWay3State.setText(_translate("DeviceStatus", "State: Direction 1"))
        self.ThreeWay2Button.setText(_translate("DeviceStatus", "Switch Direction"))
        self.HeatersGroupBox.setStyleSheet(
            _translate("DeviceStatus", "QGroupBox {border: 1px solid black}")
        )
        self.HeatersGroupBox.setTitle(_translate("DeviceStatus", "Heaters"))
        self.Heater3Button.setText(_translate("DeviceStatus", "Turn On"))
        self.Heater1State.setText(_translate("DeviceStatus", "State: Off"))
        self.Heater2Button.setText(_translate("DeviceStatus", "Turn On"))
        self.Heater3State.setText(_translate("DeviceStatus", "State: Off"))
        self.Heater4Label.setText(_translate("DeviceStatus", "Heater: 4"))
        self.Heater1Button.setText(_translate("DeviceStatus", "Turn On"))
        self.Heater1Label.setText(_translate("DeviceStatus", "Heater: 1"))
        self.Heater3Label.setText(_translate("DeviceStatus", "Heater: 3"))
        self.Heater2State.setText(_translate("DeviceStatus", "State: Off"))
        self.Heater2Label.setText(_translate("DeviceStatus", "Heater: 2"))
        self.Heater4Button.setText(_translate("DeviceStatus", "Turn On"))
        self.Heater4State.setText(_translate("DeviceStatus", "State: Off"))
        self.PumpsGroupBox.setStyleSheet(
            _translate("DeviceStatus", "QGroupBox {border: 1px solid black}")
        )
        self.PumpsGroupBox.setTitle(_translate("DeviceStatus", "Pumps"))
        self.Pump2State.setText(_translate("DeviceStatus", "State: Off"))
        self.Pump1State.setText(_translate("DeviceStatus", "State: Off"))
        self.Pump2Button.setText(_translate("DeviceStatus", "Turn On"))
        self.Pump2Label.setText(_translate("DeviceStatus", "Pump: 2"))
        self.Pump1Button.setText(_translate("DeviceStatus", "Turn On"))
        self.Pump1Label.setText(_translate("DeviceStatus", "Pump: 1"))
        self.TempSensGroupBox.setStyleSheet(
            _translate("DeviceStatus", "QGroupBox {border: 1px solid black}")
        )
        self.TempSensGroupBox.setTitle(
            _translate("DeviceStatus", "Temperature Sensors")
        )
        self.TempSens1State.setText(_translate("DeviceStatus", "Temperature: 200"))
        self.TempSens2State.setText(_translate("DeviceStatus", "Temperature: 200"))
        self.TempSens3Label.setText(_translate("DeviceStatus", "Temperature Sensor:3"))
        self.TempSens1Label.setText(_translate("DeviceStatus", "Temperature Sensor: 1"))
        self.TempSens2Label.setText(_translate("DeviceStatus", "Temperature Sensor: 2"))
        self.TempSens3State.setText(_translate("DeviceStatus", "Temperature: 200"))
        self.FlowSensGroupBox.setStyleSheet(
            _translate("DeviceStatus", "QGroupBox {border: 1px solid black}")
        )
        self.FlowSensGroupBox.setTitle(_translate("DeviceStatus", "Flow Sensors"))
        self.FlowSens1State.setText(_translate("DeviceStatus", "Flow: 50"))
        self.FlowSens2State.setText(_translate("DeviceStatus", "Flow: 50"))
        self.FlowSens3Label.setText(_translate("DeviceStatus", "Flow Sensor: 3"))
        self.FlowSens2Label.setText(_translate("DeviceStatus", "Flow Sensor: 2"))
        self.FlowSens3State.setText(_translate("DeviceStatus", "Flow: 50"))
        self.FlowSens1Label.setText(_translate("DeviceStatus", "Flow Sensor: 1"))
        self.LevelSensGroupBox.setStyleSheet(
            _translate("DeviceStatus", "QGroupBox {border: 1px solid black}")
        )
        self.LevelSensGroupBox.setTitle(_translate("DeviceStatus", "Level Sensors"))
        self.LevelSens1State.setText(_translate("DeviceStatus", "Level: 84"))
        self.LevelSens2State.setText(_translate("DeviceStatus", "Level: 84"))
        self.LevelSens3Label.setText(_translate("DeviceStatus", "Level Sensor: 3"))
        self.LevelSens1Label.setText(_translate("DeviceStatus", "Level Sensor: 1"))
        self.LevelSens2Label.setText(_translate("DeviceStatus", "Level Sensor: 2"))
        self.LevelSens3State.setText(_translate("DeviceStatus", "Level: 84"))
        self.ReturnToMenuButton.setText(
            _translate("DeviceStatus", "Return to Main Menu")
        )
