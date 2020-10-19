# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeviceStatusSensors.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DeviceStatusSensors(object):
    def setupUi(self, DeviceStatusSensors):
        if not DeviceStatusSensors.objectName():
            DeviceStatusSensors.setObjectName(u"DeviceStatusSensors")
        DeviceStatusSensors.resize(1024, 600)
        DeviceStatusSensors.setMinimumSize(QSize(1024, 600))
        DeviceStatusSensors.setMaximumSize(QSize(1024, 600))
        self.verticalLayout = QVBoxLayout(DeviceStatusSensors)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HeatersGroupBox = QGroupBox(DeviceStatusSensors)
        self.HeatersGroupBox.setObjectName(u"HeatersGroupBox")
        font = QFont()
        font.setPointSize(11)
        self.HeatersGroupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.HeatersGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.HeaterLayout = QGridLayout()
        self.HeaterLayout.setObjectName(u"HeaterLayout")
        self.HeaterLayout.setContentsMargins(-1, 2, -1, 2)
        self.HeaterPID1 = QLabel(self.HeatersGroupBox)
        self.HeaterPID1.setObjectName(u"HeaterPID1")
        self.HeaterPID1.setMaximumSize(QSize(16777215, 20))
        self.HeaterPID1.setFont(font)

        self.HeaterLayout.addWidget(self.HeaterPID1, 1, 0, 1, 1)

        self.HeaterPID4 = QLabel(self.HeatersGroupBox)
        self.HeaterPID4.setObjectName(u"HeaterPID4")
        self.HeaterPID4.setMaximumSize(QSize(16777215, 20))
        self.HeaterPID4.setFont(font)

        self.HeaterLayout.addWidget(self.HeaterPID4, 1, 4, 1, 1)

        self.Heater1Label = QLabel(self.HeatersGroupBox)
        self.Heater1Label.setObjectName(u"Heater1Label")
        self.Heater1Label.setMaximumSize(QSize(16777215, 20))
        self.Heater1Label.setFont(font)

        self.HeaterLayout.addWidget(self.Heater1Label, 0, 0, 1, 1)

        self.Heater3Label = QLabel(self.HeatersGroupBox)
        self.Heater3Label.setObjectName(u"Heater3Label")
        self.Heater3Label.setMaximumSize(QSize(16777215, 20))
        self.Heater3Label.setFont(font)

        self.HeaterLayout.addWidget(self.Heater3Label, 0, 3, 1, 1)

        self.HeaterPID3 = QLabel(self.HeatersGroupBox)
        self.HeaterPID3.setObjectName(u"HeaterPID3")
        self.HeaterPID3.setMaximumSize(QSize(16777215, 20))
        self.HeaterPID3.setFont(font)

        self.HeaterLayout.addWidget(self.HeaterPID3, 1, 3, 1, 1)

        self.Heater4Label = QLabel(self.HeatersGroupBox)
        self.Heater4Label.setObjectName(u"Heater4Label")
        self.Heater4Label.setMaximumSize(QSize(16777215, 20))
        self.Heater4Label.setFont(font)

        self.HeaterLayout.addWidget(self.Heater4Label, 0, 4, 1, 1)

        self.HeaterPID2 = QLabel(self.HeatersGroupBox)
        self.HeaterPID2.setObjectName(u"HeaterPID2")
        self.HeaterPID2.setMaximumSize(QSize(16777215, 20))
        self.HeaterPID2.setFont(font)

        self.HeaterLayout.addWidget(self.HeaterPID2, 1, 2, 1, 1)

        self.Heater2Label = QLabel(self.HeatersGroupBox)
        self.Heater2Label.setObjectName(u"Heater2Label")
        self.Heater2Label.setMaximumSize(QSize(16777215, 20))
        self.Heater2Label.setFont(font)

        self.HeaterLayout.addWidget(self.Heater2Label, 0, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.HeaterPIDDecrease1 = QPushButton(self.HeatersGroupBox)
        self.HeaterPIDDecrease1.setObjectName(u"HeaterPIDDecrease1")
        self.HeaterPIDDecrease1.setMinimumSize(QSize(0, 30))
        self.HeaterPIDDecrease1.setMaximumSize(QSize(16777215, 30))
        self.HeaterPIDDecrease1.setFont(font)
        self.HeaterPIDDecrease1.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.HeaterPIDDecrease1)

        self.HeaterPIDIncrease1 = QPushButton(self.HeatersGroupBox)
        self.HeaterPIDIncrease1.setObjectName(u"HeaterPIDIncrease1")
        self.HeaterPIDIncrease1.setFont(font)

        self.horizontalLayout_4.addWidget(self.HeaterPIDIncrease1)


        self.HeaterLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.HeaterPIDDecrease2 = QPushButton(self.HeatersGroupBox)
        self.HeaterPIDDecrease2.setObjectName(u"HeaterPIDDecrease2")
        self.HeaterPIDDecrease2.setFont(font)

        self.horizontalLayout_5.addWidget(self.HeaterPIDDecrease2)

        self.HeaterPIDIncrease2 = QPushButton(self.HeatersGroupBox)
        self.HeaterPIDIncrease2.setObjectName(u"HeaterPIDIncrease2")
        self.HeaterPIDIncrease2.setFont(font)

        self.horizontalLayout_5.addWidget(self.HeaterPIDIncrease2)


        self.HeaterLayout.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.HeaterPIDDecrease3 = QPushButton(self.HeatersGroupBox)
        self.HeaterPIDDecrease3.setObjectName(u"HeaterPIDDecrease3")
        self.HeaterPIDDecrease3.setFont(font)

        self.horizontalLayout_6.addWidget(self.HeaterPIDDecrease3)

        self.HeaterPIDIncrease3 = QPushButton(self.HeatersGroupBox)
        self.HeaterPIDIncrease3.setObjectName(u"HeaterPIDIncrease3")
        self.HeaterPIDIncrease3.setFont(font)

        self.horizontalLayout_6.addWidget(self.HeaterPIDIncrease3)


        self.HeaterLayout.addLayout(self.horizontalLayout_6, 2, 3, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.HeaterPIDDecrease4 = QPushButton(self.HeatersGroupBox)
        self.HeaterPIDDecrease4.setObjectName(u"HeaterPIDDecrease4")
        self.HeaterPIDDecrease4.setFont(font)

        self.horizontalLayout_7.addWidget(self.HeaterPIDDecrease4)

        self.HeaterPIDIncrease4 = QPushButton(self.HeatersGroupBox)
        self.HeaterPIDIncrease4.setObjectName(u"HeaterPIDIncrease4")
        self.HeaterPIDIncrease4.setFont(font)

        self.horizontalLayout_7.addWidget(self.HeaterPIDIncrease4)


        self.HeaterLayout.addLayout(self.horizontalLayout_7, 2, 4, 1, 1)


        self.verticalLayout_2.addLayout(self.HeaterLayout)


        self.verticalLayout.addWidget(self.HeatersGroupBox)

        self.TemperatureGroupBox = QGroupBox(DeviceStatusSensors)
        self.TemperatureGroupBox.setObjectName(u"TemperatureGroupBox")
        self.TemperatureGroupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.TemperatureGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.HeaterTargetLayout = QGridLayout()
        self.HeaterTargetLayout.setObjectName(u"HeaterTargetLayout")
        self.HeaterTargetLayout.setContentsMargins(-1, 2, -1, 2)
        self.HLTLabel = QLabel(self.TemperatureGroupBox)
        self.HLTLabel.setObjectName(u"HLTLabel")
        self.HLTLabel.setMaximumSize(QSize(16777215, 20))
        self.HLTLabel.setFont(font)

        self.HeaterTargetLayout.addWidget(self.HLTLabel, 0, 0, 1, 1)

        self.MTCurrentTemp = QLabel(self.TemperatureGroupBox)
        self.MTCurrentTemp.setObjectName(u"MTCurrentTemp")
        self.MTCurrentTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.MTCurrentTemp, 1, 2, 1, 1)

        self.HLTTargetTemp = QLabel(self.TemperatureGroupBox)
        self.HLTTargetTemp.setObjectName(u"HLTTargetTemp")
        self.HLTTargetTemp.setMaximumSize(QSize(16777215, 20))
        self.HLTTargetTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.HLTTargetTemp, 2, 0, 1, 1)

        self.MTLabel = QLabel(self.TemperatureGroupBox)
        self.MTLabel.setObjectName(u"MTLabel")
        self.MTLabel.setFont(font)

        self.HeaterTargetLayout.addWidget(self.MTLabel, 0, 2, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.DecreaseMT = QPushButton(self.TemperatureGroupBox)
        self.DecreaseMT.setObjectName(u"DecreaseMT")
        self.DecreaseMT.setMaximumSize(QSize(16777215, 30))
        self.DecreaseMT.setFont(font)

        self.horizontalLayout_8.addWidget(self.DecreaseMT)

        self.IncreaseMT = QPushButton(self.TemperatureGroupBox)
        self.IncreaseMT.setObjectName(u"IncreaseMT")
        self.IncreaseMT.setMaximumSize(QSize(16777215, 30))
        self.IncreaseMT.setFont(font)

        self.horizontalLayout_8.addWidget(self.IncreaseMT)


        self.HeaterTargetLayout.addLayout(self.horizontalLayout_8, 3, 2, 1, 1)

        self.HLTCurrentTemp = QLabel(self.TemperatureGroupBox)
        self.HLTCurrentTemp.setObjectName(u"HLTCurrentTemp")
        self.HLTCurrentTemp.setMaximumSize(QSize(16777215, 20))
        self.HLTCurrentTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.HLTCurrentTemp, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.DecreaseHLT = QPushButton(self.TemperatureGroupBox)
        self.DecreaseHLT.setObjectName(u"DecreaseHLT")
        self.DecreaseHLT.setMinimumSize(QSize(0, 30))
        self.DecreaseHLT.setMaximumSize(QSize(16777215, 30))
        self.DecreaseHLT.setFont(font)

        self.horizontalLayout_10.addWidget(self.DecreaseHLT)

        self.IncreaseHLT = QPushButton(self.TemperatureGroupBox)
        self.IncreaseHLT.setObjectName(u"IncreaseHLT")
        self.IncreaseHLT.setMinimumSize(QSize(0, 30))
        self.IncreaseHLT.setMaximumSize(QSize(16777215, 30))
        self.IncreaseHLT.setFont(font)

        self.horizontalLayout_10.addWidget(self.IncreaseHLT)


        self.HeaterTargetLayout.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)

        self.MTTargetTemp = QLabel(self.TemperatureGroupBox)
        self.MTTargetTemp.setObjectName(u"MTTargetTemp")
        self.MTTargetTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.MTTargetTemp, 2, 2, 1, 1)

        self.BKTargetTemp = QLabel(self.TemperatureGroupBox)
        self.BKTargetTemp.setObjectName(u"BKTargetTemp")
        self.BKTargetTemp.setMaximumSize(QSize(16777215, 20))
        self.BKTargetTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.BKTargetTemp, 2, 3, 1, 1)

        self.BKCurrentTemp = QLabel(self.TemperatureGroupBox)
        self.BKCurrentTemp.setObjectName(u"BKCurrentTemp")
        self.BKCurrentTemp.setMaximumSize(QSize(16777215, 20))
        self.BKCurrentTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.BKCurrentTemp, 1, 3, 1, 1)

        self.BKLabel = QLabel(self.TemperatureGroupBox)
        self.BKLabel.setObjectName(u"BKLabel")
        self.BKLabel.setMaximumSize(QSize(16777215, 20))
        self.BKLabel.setFont(font)

        self.HeaterTargetLayout.addWidget(self.BKLabel, 0, 3, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.DecreaseBK = QPushButton(self.TemperatureGroupBox)
        self.DecreaseBK.setObjectName(u"DecreaseBK")
        self.DecreaseBK.setMinimumSize(QSize(0, 30))
        self.DecreaseBK.setMaximumSize(QSize(16777215, 30))
        self.DecreaseBK.setFont(font)

        self.horizontalLayout_9.addWidget(self.DecreaseBK)

        self.IncreaseBK = QPushButton(self.TemperatureGroupBox)
        self.IncreaseBK.setObjectName(u"IncreaseBK")
        self.IncreaseBK.setMinimumSize(QSize(0, 30))
        self.IncreaseBK.setMaximumSize(QSize(16777215, 30))
        self.IncreaseBK.setFont(font)

        self.horizontalLayout_9.addWidget(self.IncreaseBK)


        self.HeaterTargetLayout.addLayout(self.horizontalLayout_9, 3, 3, 1, 1)


        self.horizontalLayout_2.addLayout(self.HeaterTargetLayout)


        self.verticalLayout.addWidget(self.TemperatureGroupBox)

        self.ServoMotorGroupBox = QGroupBox(DeviceStatusSensors)
        self.ServoMotorGroupBox.setObjectName(u"ServoMotorGroupBox")
        self.ServoMotorGroupBox.setFont(font)
        self.ServoMotorGroupBox.setStyleSheet(u"QGroupBox {border: 1px solid black}")
        self.horizontalLayout_3 = QHBoxLayout(self.ServoMotorGroupBox)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ServoLayout = QGridLayout()
        self.ServoLayout.setObjectName(u"ServoLayout")
        self.ServoLayout.setContentsMargins(-1, 2, -1, 2)
        self.IncreaseServo = QPushButton(self.ServoMotorGroupBox)
        self.IncreaseServo.setObjectName(u"IncreaseServo")
        self.IncreaseServo.setMinimumSize(QSize(0, 30))
        self.IncreaseServo.setMaximumSize(QSize(16777215, 30))
        self.IncreaseServo.setFont(font)

        self.ServoLayout.addWidget(self.IncreaseServo, 0, 4, 1, 1)

        self.HopServo3 = QPushButton(self.ServoMotorGroupBox)
        self.HopServo3.setObjectName(u"HopServo3")
        self.HopServo3.setMinimumSize(QSize(0, 30))
        self.HopServo3.setMaximumSize(QSize(16777215, 30))
        self.HopServo3.setFont(font)
        self.HopServo3.setCheckable(False)

        self.ServoLayout.addWidget(self.HopServo3, 1, 2, 1, 1)

        self.HopServo5 = QPushButton(self.ServoMotorGroupBox)
        self.HopServo5.setObjectName(u"HopServo5")
        self.HopServo5.setMinimumSize(QSize(0, 30))
        self.HopServo5.setMaximumSize(QSize(16777215, 30))
        self.HopServo5.setFont(font)
        self.HopServo5.setCheckable(False)

        self.ServoLayout.addWidget(self.HopServo5, 1, 4, 1, 1)

        self.HopServo1 = QPushButton(self.ServoMotorGroupBox)
        self.HopServo1.setObjectName(u"HopServo1")
        self.HopServo1.setMinimumSize(QSize(0, 30))
        self.HopServo1.setMaximumSize(QSize(16777215, 30))
        self.HopServo1.setFont(font)
        self.HopServo1.setAutoFillBackground(False)
        self.HopServo1.setCheckable(False)

        self.ServoLayout.addWidget(self.HopServo1, 1, 0, 1, 1)

        self.HomeServo = QPushButton(self.ServoMotorGroupBox)
        self.HomeServo.setObjectName(u"HomeServo")
        self.HomeServo.setMinimumSize(QSize(0, 30))
        self.HomeServo.setMaximumSize(QSize(16777215, 30))
        self.HomeServo.setFont(font)

        self.ServoLayout.addWidget(self.HomeServo, 0, 2, 1, 1)

        self.HopServo2 = QPushButton(self.ServoMotorGroupBox)
        self.HopServo2.setObjectName(u"HopServo2")
        self.HopServo2.setMinimumSize(QSize(0, 30))
        self.HopServo2.setMaximumSize(QSize(16777215, 30))
        self.HopServo2.setFont(font)
        self.HopServo2.setCheckable(False)

        self.ServoLayout.addWidget(self.HopServo2, 1, 1, 1, 1)

        self.CurrentAngleServo = QLabel(self.ServoMotorGroupBox)
        self.CurrentAngleServo.setObjectName(u"CurrentAngleServo")
        self.CurrentAngleServo.setMaximumSize(QSize(16777215, 20))
        self.CurrentAngleServo.setFont(font)

        self.ServoLayout.addWidget(self.CurrentAngleServo, 0, 0, 1, 1)

        self.HopServo4 = QPushButton(self.ServoMotorGroupBox)
        self.HopServo4.setObjectName(u"HopServo4")
        self.HopServo4.setMinimumSize(QSize(0, 30))
        self.HopServo4.setMaximumSize(QSize(16777215, 30))
        self.HopServo4.setFont(font)
        self.HopServo4.setCheckable(False)

        self.ServoLayout.addWidget(self.HopServo4, 1, 3, 1, 1)

        self.DecreaseServo = QPushButton(self.ServoMotorGroupBox)
        self.DecreaseServo.setObjectName(u"DecreaseServo")
        self.DecreaseServo.setMinimumSize(QSize(0, 30))
        self.DecreaseServo.setMaximumSize(QSize(16777215, 30))
        self.DecreaseServo.setFont(font)

        self.ServoLayout.addWidget(self.DecreaseServo, 0, 3, 1, 1)


        self.horizontalLayout_3.addLayout(self.ServoLayout)


        self.verticalLayout.addWidget(self.ServoMotorGroupBox)

        self.TankVolumeGroupBox = QGroupBox(DeviceStatusSensors)
        self.TankVolumeGroupBox.setObjectName(u"TankVolumeGroupBox")
        self.TankVolumeGroupBox.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.TankVolumeGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.TankVolumeLayout = QGridLayout()
        self.TankVolumeLayout.setObjectName(u"TankVolumeLayout")
        self.TankVolumeLayout.setContentsMargins(-1, 2, -1, 2)
        self.TankVolume3State = QLabel(self.TankVolumeGroupBox)
        self.TankVolume3State.setObjectName(u"TankVolume3State")
        self.TankVolume3State.setMaximumSize(QSize(16777215, 20))
        self.TankVolume3State.setFont(font)

        self.TankVolumeLayout.addWidget(self.TankVolume3State, 1, 2, 1, 1)

        self.TankVolume1Label = QLabel(self.TankVolumeGroupBox)
        self.TankVolume1Label.setObjectName(u"TankVolume1Label")
        self.TankVolume1Label.setMaximumSize(QSize(16777215, 20))
        self.TankVolume1Label.setFont(font)

        self.TankVolumeLayout.addWidget(self.TankVolume1Label, 0, 0, 1, 1)

        self.TankVolume1State = QLabel(self.TankVolumeGroupBox)
        self.TankVolume1State.setObjectName(u"TankVolume1State")
        self.TankVolume1State.setMaximumSize(QSize(16777215, 20))
        self.TankVolume1State.setFont(font)

        self.TankVolumeLayout.addWidget(self.TankVolume1State, 1, 0, 1, 1)

        self.TankVolume2State = QLabel(self.TankVolumeGroupBox)
        self.TankVolume2State.setObjectName(u"TankVolume2State")
        self.TankVolume2State.setMaximumSize(QSize(16777215, 20))
        self.TankVolume2State.setFont(font)

        self.TankVolumeLayout.addWidget(self.TankVolume2State, 1, 1, 1, 1)

        self.TankVolume2Label = QLabel(self.TankVolumeGroupBox)
        self.TankVolume2Label.setObjectName(u"TankVolume2Label")
        self.TankVolume2Label.setMaximumSize(QSize(16777215, 20))
        self.TankVolume2Label.setFont(font)

        self.TankVolumeLayout.addWidget(self.TankVolume2Label, 0, 1, 1, 1)

        self.TankVolume3Label = QLabel(self.TankVolumeGroupBox)
        self.TankVolume3Label.setObjectName(u"TankVolume3Label")
        self.TankVolume3Label.setMaximumSize(QSize(16777215, 20))
        self.TankVolume3Label.setFont(font)

        self.TankVolumeLayout.addWidget(self.TankVolume3Label, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.TankVolumeLayout)


        self.verticalLayout.addWidget(self.TankVolumeGroupBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.GoToControlStatusButton = QPushButton(DeviceStatusSensors)
        self.GoToControlStatusButton.setObjectName(u"GoToControlStatusButton")
        self.GoToControlStatusButton.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setPointSize(10)
        self.GoToControlStatusButton.setFont(font1)

        self.horizontalLayout.addWidget(self.GoToControlStatusButton)

        self.ReturnToMenuButton = QPushButton(DeviceStatusSensors)
        self.ReturnToMenuButton.setObjectName(u"ReturnToMenuButton")
        self.ReturnToMenuButton.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.ReturnToMenuButton.setFont(font2)

        self.horizontalLayout.addWidget(self.ReturnToMenuButton)

        self.ProcessStatusButton = QPushButton(DeviceStatusSensors)
        self.ProcessStatusButton.setObjectName(u"ProcessStatusButton")
        self.ProcessStatusButton.setMaximumSize(QSize(16777215, 50))
        self.ProcessStatusButton.setFont(font1)

        self.horizontalLayout.addWidget(self.ProcessStatusButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(DeviceStatusSensors)

        QMetaObject.connectSlotsByName(DeviceStatusSensors)
    # setupUi

    def retranslateUi(self, DeviceStatusSensors):
        DeviceStatusSensors.setWindowTitle(QCoreApplication.translate("DeviceStatusSensors", u"Form", None))
        self.HeatersGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatusSensors", u"QGroupBox {border: 1px solid black}", None))
        self.HeatersGroupBox.setTitle(QCoreApplication.translate("DeviceStatusSensors", u"Heaters PID", None))
        self.HeaterPID1.setText(QCoreApplication.translate("DeviceStatusSensors", u"State: Off", None))
        self.HeaterPID4.setText(QCoreApplication.translate("DeviceStatusSensors", u"State: Off", None))
        self.Heater1Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Heater: 1", None))
        self.Heater3Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Heater: 3", None))
        self.HeaterPID3.setText(QCoreApplication.translate("DeviceStatusSensors", u"State: Off", None))
        self.Heater4Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Heater: 4", None))
        self.HeaterPID2.setText(QCoreApplication.translate("DeviceStatusSensors", u"State: Off", None))
        self.Heater2Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Heater: 2", None))
        self.HeaterPIDDecrease1.setText(QCoreApplication.translate("DeviceStatusSensors", u"-", None))
        self.HeaterPIDIncrease1.setText(QCoreApplication.translate("DeviceStatusSensors", u"+", None))
        self.HeaterPIDDecrease2.setText(QCoreApplication.translate("DeviceStatusSensors", u"-", None))
        self.HeaterPIDIncrease2.setText(QCoreApplication.translate("DeviceStatusSensors", u"+", None))
        self.HeaterPIDDecrease3.setText(QCoreApplication.translate("DeviceStatusSensors", u"-", None))
        self.HeaterPIDIncrease3.setText(QCoreApplication.translate("DeviceStatusSensors", u"+", None))
        self.HeaterPIDDecrease4.setText(QCoreApplication.translate("DeviceStatusSensors", u"-", None))
        self.HeaterPIDIncrease4.setText(QCoreApplication.translate("DeviceStatusSensors", u"+", None))
        self.TemperatureGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatusSensors", u"QGroupBox {border: 1px solid black}", None))
        self.TemperatureGroupBox.setTitle(QCoreApplication.translate("DeviceStatusSensors", u"Heater Target Temperature", None))
        self.HLTLabel.setText(QCoreApplication.translate("DeviceStatusSensors", u"Hot Liquor Tank", None))
        self.MTCurrentTemp.setText(QCoreApplication.translate("DeviceStatusSensors", u"Current Temperature (\u00b0F): 20", None))
        self.HLTTargetTemp.setText(QCoreApplication.translate("DeviceStatusSensors", u"Target Temperature (\u00b0F): 20", None))
        self.MTLabel.setText(QCoreApplication.translate("DeviceStatusSensors", u"Mash Tun", None))
        self.DecreaseMT.setText(QCoreApplication.translate("DeviceStatusSensors", u"-", None))
        self.IncreaseMT.setText(QCoreApplication.translate("DeviceStatusSensors", u"+", None))
        self.HLTCurrentTemp.setText(QCoreApplication.translate("DeviceStatusSensors", u"Current Temperature (\u00b0F): 20", None))
        self.DecreaseHLT.setText(QCoreApplication.translate("DeviceStatusSensors", u"-", None))
        self.IncreaseHLT.setText(QCoreApplication.translate("DeviceStatusSensors", u"+", None))
        self.MTTargetTemp.setText(QCoreApplication.translate("DeviceStatusSensors", u"Target Temperature (\u00b0F): 20", None))
        self.BKTargetTemp.setText(QCoreApplication.translate("DeviceStatusSensors", u"Target Temperature (\u00b0F): 20", None))
        self.BKCurrentTemp.setText(QCoreApplication.translate("DeviceStatusSensors", u"Current Temperature (\u00b0F): 20", None))
        self.BKLabel.setText(QCoreApplication.translate("DeviceStatusSensors", u"Boil Kettle", None))
        self.DecreaseBK.setText(QCoreApplication.translate("DeviceStatusSensors", u"-", None))
        self.IncreaseBK.setText(QCoreApplication.translate("DeviceStatusSensors", u"+", None))
        self.ServoMotorGroupBox.setTitle(QCoreApplication.translate("DeviceStatusSensors", u"Servo Motor", None))
        self.IncreaseServo.setText(QCoreApplication.translate("DeviceStatusSensors", u"+", None))
        self.HopServo3.setText(QCoreApplication.translate("DeviceStatusSensors", u"Hop Cup 3", None))
        self.HopServo5.setText(QCoreApplication.translate("DeviceStatusSensors", u"Hop Cup 5", None))
        self.HopServo1.setText(QCoreApplication.translate("DeviceStatusSensors", u"Hop Cup 1", None))
        self.HomeServo.setText(QCoreApplication.translate("DeviceStatusSensors", u"Home", None))
        self.HopServo2.setText(QCoreApplication.translate("DeviceStatusSensors", u"Hop Cup 2", None))
        self.CurrentAngleServo.setText(QCoreApplication.translate("DeviceStatusSensors", u"Current Angle (\u00b0): 270", None))
        self.HopServo4.setText(QCoreApplication.translate("DeviceStatusSensors", u"Hop Cup 4", None))
        self.DecreaseServo.setText(QCoreApplication.translate("DeviceStatusSensors", u"-", None))
        self.TankVolumeGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatusSensors", u"QGroupBox {border: 1px solid black}", None))
        self.TankVolumeGroupBox.setTitle(QCoreApplication.translate("DeviceStatusSensors", u"Tank Volume", None))
        self.TankVolume3State.setText(QCoreApplication.translate("DeviceStatusSensors", u"Volume (gal):", None))
        self.TankVolume1Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Hot Liquor Tank:", None))
        self.TankVolume1State.setText(QCoreApplication.translate("DeviceStatusSensors", u"Volume (gal):", None))
        self.TankVolume2State.setText(QCoreApplication.translate("DeviceStatusSensors", u"Volume (gal):", None))
        self.TankVolume2Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Mash Tun:", None))
        self.TankVolume3Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Boil Kettle:", None))
        self.GoToControlStatusButton.setText(QCoreApplication.translate("DeviceStatusSensors", u"Device Controls", None))
        self.ReturnToMenuButton.setText(QCoreApplication.translate("DeviceStatusSensors", u"Main Menu", None))
        self.ProcessStatusButton.setText(QCoreApplication.translate("DeviceStatusSensors", u"Process Status", None))
    # retranslateUi

