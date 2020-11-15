# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeviceStatus.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DeviceStatus(object):
    def setupUi(self, DeviceStatus):
        if not DeviceStatus.objectName():
            DeviceStatus.setObjectName(u"DeviceStatus")
        DeviceStatus.resize(1024, 600)
        DeviceStatus.setMinimumSize(QSize(1024, 600))
        DeviceStatus.setMaximumSize(QSize(1024, 600))
        self.verticalLayout_10 = QVBoxLayout(DeviceStatus)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BallValveToggle = QPushButton(DeviceStatus)
        self.BallValveToggle.setObjectName(u"BallValveToggle")
        self.BallValveToggle.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(11)
        self.BallValveToggle.setFont(font)
        self.BallValveToggle.setCheckable(True)

        self.horizontalLayout.addWidget(self.BallValveToggle)

        self.HeaterTempToggle = QPushButton(DeviceStatus)
        self.HeaterTempToggle.setObjectName(u"HeaterTempToggle")
        self.HeaterTempToggle.setMinimumSize(QSize(0, 40))
        self.HeaterTempToggle.setFont(font)
        self.HeaterTempToggle.setCheckable(True)

        self.horizontalLayout.addWidget(self.HeaterTempToggle)

        self.PumpVolumeToggle = QPushButton(DeviceStatus)
        self.PumpVolumeToggle.setObjectName(u"PumpVolumeToggle")
        self.PumpVolumeToggle.setMinimumSize(QSize(0, 40))
        self.PumpVolumeToggle.setFont(font)
        self.PumpVolumeToggle.setCheckable(True)

        self.horizontalLayout.addWidget(self.PumpVolumeToggle)

        self.ServoMotorToggle = QPushButton(DeviceStatus)
        self.ServoMotorToggle.setObjectName(u"ServoMotorToggle")
        self.ServoMotorToggle.setMinimumSize(QSize(0, 40))
        self.ServoMotorToggle.setFont(font)
        self.ServoMotorToggle.setCheckable(True)

        self.horizontalLayout.addWidget(self.ServoMotorToggle)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.HeatersPWMGroupBox = QGroupBox(DeviceStatus)
        self.HeatersPWMGroupBox.setObjectName(u"HeatersPWMGroupBox")
        self.HeatersPWMGroupBox.setMaximumSize(QSize(16777215, 140))
        self.HeatersPWMGroupBox.setFont(font)
        self.verticalLayout_6 = QVBoxLayout(self.HeatersPWMGroupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_9)

        self.HeaterLayout_2 = QGridLayout()
        self.HeaterLayout_2.setObjectName(u"HeaterLayout_2")
        self.HeaterLayout_2.setContentsMargins(-1, 2, -1, 2)
        self.HeaterPID1 = QLabel(self.HeatersPWMGroupBox)
        self.HeaterPID1.setObjectName(u"HeaterPID1")
        self.HeaterPID1.setMaximumSize(QSize(16777215, 20))
        self.HeaterPID1.setFont(font)

        self.HeaterLayout_2.addWidget(self.HeaterPID1, 1, 0, 1, 1)

        self.HeaterPID4 = QLabel(self.HeatersPWMGroupBox)
        self.HeaterPID4.setObjectName(u"HeaterPID4")
        self.HeaterPID4.setMaximumSize(QSize(16777215, 20))
        self.HeaterPID4.setFont(font)

        self.HeaterLayout_2.addWidget(self.HeaterPID4, 1, 4, 1, 1)

        self.Heater1Label_2 = QLabel(self.HeatersPWMGroupBox)
        self.Heater1Label_2.setObjectName(u"Heater1Label_2")
        self.Heater1Label_2.setMaximumSize(QSize(16777215, 20))
        self.Heater1Label_2.setFont(font)

        self.HeaterLayout_2.addWidget(self.Heater1Label_2, 0, 0, 1, 1)

        self.Heater3Label_2 = QLabel(self.HeatersPWMGroupBox)
        self.Heater3Label_2.setObjectName(u"Heater3Label_2")
        self.Heater3Label_2.setMaximumSize(QSize(16777215, 20))
        self.Heater3Label_2.setFont(font)

        self.HeaterLayout_2.addWidget(self.Heater3Label_2, 0, 3, 1, 1)

        self.HeaterPID3 = QLabel(self.HeatersPWMGroupBox)
        self.HeaterPID3.setObjectName(u"HeaterPID3")
        self.HeaterPID3.setMaximumSize(QSize(16777215, 20))
        self.HeaterPID3.setFont(font)

        self.HeaterLayout_2.addWidget(self.HeaterPID3, 1, 3, 1, 1)

        self.Heater4Label_2 = QLabel(self.HeatersPWMGroupBox)
        self.Heater4Label_2.setObjectName(u"Heater4Label_2")
        self.Heater4Label_2.setMaximumSize(QSize(16777215, 20))
        self.Heater4Label_2.setFont(font)

        self.HeaterLayout_2.addWidget(self.Heater4Label_2, 0, 4, 1, 1)

        self.HeaterPID2 = QLabel(self.HeatersPWMGroupBox)
        self.HeaterPID2.setObjectName(u"HeaterPID2")
        self.HeaterPID2.setMaximumSize(QSize(16777215, 20))
        self.HeaterPID2.setFont(font)

        self.HeaterLayout_2.addWidget(self.HeaterPID2, 1, 2, 1, 1)

        self.Heater2Label_2 = QLabel(self.HeatersPWMGroupBox)
        self.Heater2Label_2.setObjectName(u"Heater2Label_2")
        self.Heater2Label_2.setMaximumSize(QSize(16777215, 20))
        self.Heater2Label_2.setFont(font)

        self.HeaterLayout_2.addWidget(self.Heater2Label_2, 0, 2, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.HeaterPIDDecrease1 = QPushButton(self.HeatersPWMGroupBox)
        self.HeaterPIDDecrease1.setObjectName(u"HeaterPIDDecrease1")
        self.HeaterPIDDecrease1.setMinimumSize(QSize(0, 30))
        self.HeaterPIDDecrease1.setMaximumSize(QSize(16777215, 30))
        self.HeaterPIDDecrease1.setFont(font)
        self.HeaterPIDDecrease1.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.HeaterPIDDecrease1)

        self.HeaterPIDIncrease1 = QPushButton(self.HeatersPWMGroupBox)
        self.HeaterPIDIncrease1.setObjectName(u"HeaterPIDIncrease1")
        self.HeaterPIDIncrease1.setMinimumSize(QSize(0, 30))
        self.HeaterPIDIncrease1.setMaximumSize(QSize(16777215, 30))
        self.HeaterPIDIncrease1.setFont(font)

        self.horizontalLayout_4.addWidget(self.HeaterPIDIncrease1)


        self.HeaterLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.HeaterPIDDecrease2 = QPushButton(self.HeatersPWMGroupBox)
        self.HeaterPIDDecrease2.setObjectName(u"HeaterPIDDecrease2")
        self.HeaterPIDDecrease2.setMinimumSize(QSize(0, 30))
        self.HeaterPIDDecrease2.setMaximumSize(QSize(16777215, 30))
        self.HeaterPIDDecrease2.setFont(font)

        self.horizontalLayout_5.addWidget(self.HeaterPIDDecrease2)

        self.HeaterPIDIncrease2 = QPushButton(self.HeatersPWMGroupBox)
        self.HeaterPIDIncrease2.setObjectName(u"HeaterPIDIncrease2")
        self.HeaterPIDIncrease2.setMinimumSize(QSize(0, 30))
        self.HeaterPIDIncrease2.setMaximumSize(QSize(16777215, 30))
        self.HeaterPIDIncrease2.setFont(font)

        self.horizontalLayout_5.addWidget(self.HeaterPIDIncrease2)


        self.HeaterLayout_2.addLayout(self.horizontalLayout_5, 2, 2, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.HeaterPIDDecrease3 = QPushButton(self.HeatersPWMGroupBox)
        self.HeaterPIDDecrease3.setObjectName(u"HeaterPIDDecrease3")
        self.HeaterPIDDecrease3.setMinimumSize(QSize(0, 30))
        self.HeaterPIDDecrease3.setMaximumSize(QSize(16777215, 30))
        self.HeaterPIDDecrease3.setFont(font)

        self.horizontalLayout_6.addWidget(self.HeaterPIDDecrease3)

        self.HeaterPIDIncrease3 = QPushButton(self.HeatersPWMGroupBox)
        self.HeaterPIDIncrease3.setObjectName(u"HeaterPIDIncrease3")
        self.HeaterPIDIncrease3.setMinimumSize(QSize(0, 30))
        self.HeaterPIDIncrease3.setMaximumSize(QSize(16777215, 30))
        self.HeaterPIDIncrease3.setFont(font)

        self.horizontalLayout_6.addWidget(self.HeaterPIDIncrease3)


        self.HeaterLayout_2.addLayout(self.horizontalLayout_6, 2, 3, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.HeaterPIDDecrease4 = QPushButton(self.HeatersPWMGroupBox)
        self.HeaterPIDDecrease4.setObjectName(u"HeaterPIDDecrease4")
        self.HeaterPIDDecrease4.setMinimumSize(QSize(0, 30))
        self.HeaterPIDDecrease4.setMaximumSize(QSize(16777215, 30))
        self.HeaterPIDDecrease4.setFont(font)

        self.horizontalLayout_7.addWidget(self.HeaterPIDDecrease4)

        self.HeaterPIDIncrease4 = QPushButton(self.HeatersPWMGroupBox)
        self.HeaterPIDIncrease4.setObjectName(u"HeaterPIDIncrease4")
        self.HeaterPIDIncrease4.setMinimumSize(QSize(0, 30))
        self.HeaterPIDIncrease4.setMaximumSize(QSize(16777215, 30))
        self.HeaterPIDIncrease4.setFont(font)

        self.horizontalLayout_7.addWidget(self.HeaterPIDIncrease4)


        self.HeaterLayout_2.addLayout(self.horizontalLayout_7, 2, 4, 1, 1)


        self.verticalLayout_6.addLayout(self.HeaterLayout_2)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_10)


        self.verticalLayout_10.addWidget(self.HeatersPWMGroupBox)

        self.TemperatureGroupBox = QGroupBox(DeviceStatus)
        self.TemperatureGroupBox.setObjectName(u"TemperatureGroupBox")
        self.TemperatureGroupBox.setMaximumSize(QSize(16777215, 160))
        self.TemperatureGroupBox.setFont(font)
        self.verticalLayout_9 = QVBoxLayout(self.TemperatureGroupBox)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_15)

        self.HeaterTargetLayout = QGridLayout()
        self.HeaterTargetLayout.setObjectName(u"HeaterTargetLayout")
        self.HeaterTargetLayout.setContentsMargins(-1, 2, -1, 2)
        self.BKTargetTemp = QLabel(self.TemperatureGroupBox)
        self.BKTargetTemp.setObjectName(u"BKTargetTemp")
        self.BKTargetTemp.setMaximumSize(QSize(16777215, 20))
        self.BKTargetTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.BKTargetTemp, 2, 3, 1, 1)

        self.HLTCurrentTemp = QLabel(self.TemperatureGroupBox)
        self.HLTCurrentTemp.setObjectName(u"HLTCurrentTemp")
        self.HLTCurrentTemp.setMaximumSize(QSize(16777215, 20))
        self.HLTCurrentTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.HLTCurrentTemp, 1, 0, 1, 1)

        self.BKCurrentTemp = QLabel(self.TemperatureGroupBox)
        self.BKCurrentTemp.setObjectName(u"BKCurrentTemp")
        self.BKCurrentTemp.setMaximumSize(QSize(16777215, 20))
        self.BKCurrentTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.BKCurrentTemp, 1, 3, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.DecreaseBK = QPushButton(self.TemperatureGroupBox)
        self.DecreaseBK.setObjectName(u"DecreaseBK")
        self.DecreaseBK.setMinimumSize(QSize(0, 30))
        self.DecreaseBK.setMaximumSize(QSize(16777215, 30))
        self.DecreaseBK.setFont(font)

        self.horizontalLayout_9.addWidget(self.DecreaseBK)

        self.BKPIDtoggle = QPushButton(self.TemperatureGroupBox)
        self.BKPIDtoggle.setObjectName(u"BKPIDtoggle")
        self.BKPIDtoggle.setMaximumSize(QSize(16777215, 30))
        self.BKPIDtoggle.setFont(font)

        self.horizontalLayout_9.addWidget(self.BKPIDtoggle)

        self.IncreaseBK = QPushButton(self.TemperatureGroupBox)
        self.IncreaseBK.setObjectName(u"IncreaseBK")
        self.IncreaseBK.setMinimumSize(QSize(0, 30))
        self.IncreaseBK.setMaximumSize(QSize(16777215, 30))
        self.IncreaseBK.setFont(font)

        self.horizontalLayout_9.addWidget(self.IncreaseBK)


        self.HeaterTargetLayout.addLayout(self.horizontalLayout_9, 3, 3, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.DecreaseHLT = QPushButton(self.TemperatureGroupBox)
        self.DecreaseHLT.setObjectName(u"DecreaseHLT")
        self.DecreaseHLT.setMinimumSize(QSize(0, 30))
        self.DecreaseHLT.setMaximumSize(QSize(16777215, 30))
        self.DecreaseHLT.setFont(font)

        self.horizontalLayout_10.addWidget(self.DecreaseHLT)

        self.HLTPIDtoggle = QPushButton(self.TemperatureGroupBox)
        self.HLTPIDtoggle.setObjectName(u"HLTPIDtoggle")
        self.HLTPIDtoggle.setMaximumSize(QSize(16777215, 30))
        self.HLTPIDtoggle.setFont(font)

        self.horizontalLayout_10.addWidget(self.HLTPIDtoggle)

        self.IncreaseHLT = QPushButton(self.TemperatureGroupBox)
        self.IncreaseHLT.setObjectName(u"IncreaseHLT")
        self.IncreaseHLT.setMinimumSize(QSize(0, 30))
        self.IncreaseHLT.setMaximumSize(QSize(16777215, 30))
        self.IncreaseHLT.setFont(font)

        self.horizontalLayout_10.addWidget(self.IncreaseHLT)


        self.HeaterTargetLayout.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)

        self.HLTTargetTemp = QLabel(self.TemperatureGroupBox)
        self.HLTTargetTemp.setObjectName(u"HLTTargetTemp")
        self.HLTTargetTemp.setMaximumSize(QSize(16777215, 20))
        self.HLTTargetTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.HLTTargetTemp, 2, 0, 1, 1)

        self.MTCurrentTemp = QLabel(self.TemperatureGroupBox)
        self.MTCurrentTemp.setObjectName(u"MTCurrentTemp")
        self.MTCurrentTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.MTCurrentTemp, 1, 2, 1, 1)

        self.MTTargetTemp = QLabel(self.TemperatureGroupBox)
        self.MTTargetTemp.setObjectName(u"MTTargetTemp")
        self.MTTargetTemp.setFont(font)

        self.HeaterTargetLayout.addWidget(self.MTTargetTemp, 2, 2, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.DecreaseMT = QPushButton(self.TemperatureGroupBox)
        self.DecreaseMT.setObjectName(u"DecreaseMT")
        self.DecreaseMT.setMaximumSize(QSize(16777215, 30))
        self.DecreaseMT.setFont(font)

        self.horizontalLayout_8.addWidget(self.DecreaseMT)

        self.MTPIDtoggle = QPushButton(self.TemperatureGroupBox)
        self.MTPIDtoggle.setObjectName(u"MTPIDtoggle")
        self.MTPIDtoggle.setMaximumSize(QSize(16777215, 30))
        self.MTPIDtoggle.setFont(font)

        self.horizontalLayout_8.addWidget(self.MTPIDtoggle)

        self.IncreaseMT = QPushButton(self.TemperatureGroupBox)
        self.IncreaseMT.setObjectName(u"IncreaseMT")
        self.IncreaseMT.setMaximumSize(QSize(16777215, 30))
        self.IncreaseMT.setFont(font)

        self.horizontalLayout_8.addWidget(self.IncreaseMT)


        self.HeaterTargetLayout.addLayout(self.horizontalLayout_8, 3, 2, 1, 1)

        self.BKLabel = QLabel(self.TemperatureGroupBox)
        self.BKLabel.setObjectName(u"BKLabel")
        self.BKLabel.setMaximumSize(QSize(16777215, 20))
        self.BKLabel.setFont(font)

        self.HeaterTargetLayout.addWidget(self.BKLabel, 0, 3, 1, 1)

        self.HLTLabel = QLabel(self.TemperatureGroupBox)
        self.HLTLabel.setObjectName(u"HLTLabel")
        self.HLTLabel.setMaximumSize(QSize(16777215, 20))
        self.HLTLabel.setFont(font)

        self.HeaterTargetLayout.addWidget(self.HLTLabel, 0, 0, 1, 1)

        self.MTLabel = QLabel(self.TemperatureGroupBox)
        self.MTLabel.setObjectName(u"MTLabel")
        self.MTLabel.setFont(font)

        self.HeaterTargetLayout.addWidget(self.MTLabel, 0, 2, 1, 1)


        self.verticalLayout_9.addLayout(self.HeaterTargetLayout)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_16)


        self.verticalLayout_10.addWidget(self.TemperatureGroupBox)

        self.ServoMotorGroupBox = QGroupBox(DeviceStatus)
        self.ServoMotorGroupBox.setObjectName(u"ServoMotorGroupBox")
        self.ServoMotorGroupBox.setMaximumSize(QSize(16777215, 140))
        self.ServoMotorGroupBox.setFont(font)
        self.ServoMotorGroupBox.setStyleSheet(u"QGroupBox {border: 1px solid black}")
        self.verticalLayout_8 = QVBoxLayout(self.ServoMotorGroupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_13)

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


        self.verticalLayout_8.addLayout(self.ServoLayout)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_14)


        self.verticalLayout_10.addWidget(self.ServoMotorGroupBox)

        self.TankVolumeGroupBox = QGroupBox(DeviceStatus)
        self.TankVolumeGroupBox.setObjectName(u"TankVolumeGroupBox")
        self.TankVolumeGroupBox.setMaximumSize(QSize(16777215, 140))
        self.TankVolumeGroupBox.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.TankVolumeGroupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_11)

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


        self.verticalLayout_7.addLayout(self.TankVolumeLayout)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_12)


        self.verticalLayout_10.addWidget(self.TankVolumeGroupBox)

        self.BallValveGroupBox = QGroupBox(DeviceStatus)
        self.BallValveGroupBox.setObjectName(u"BallValveGroupBox")
        self.BallValveGroupBox.setMaximumSize(QSize(16777215, 140))
        self.BallValveGroupBox.setFont(font)
        self.BallValveGroupBox.setStyleSheet(u"QGroupBox {border: 1px solid black}")
        self.verticalLayout_5 = QVBoxLayout(self.BallValveGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.BallValveLayout = QGridLayout()
        self.BallValveLayout.setObjectName(u"BallValveLayout")
        self.BallValveLayout.setContentsMargins(-1, 2, -1, 2)
        self.BallValve2Button = QPushButton(self.BallValveGroupBox)
        self.BallValve2Button.setObjectName(u"BallValve2Button")
        self.BallValve2Button.setMinimumSize(QSize(0, 30))
        self.BallValve2Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve2Button.setFont(font)
        self.BallValve2Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve2Button, 3, 1, 1, 1)

        self.BallValve2Label = QLabel(self.BallValveGroupBox)
        self.BallValve2Label.setObjectName(u"BallValve2Label")
        self.BallValve2Label.setMaximumSize(QSize(16777215, 20))
        self.BallValve2Label.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve2Label, 0, 1, 1, 1)

        self.BallValve4State = QLabel(self.BallValveGroupBox)
        self.BallValve4State.setObjectName(u"BallValve4State")
        self.BallValve4State.setMaximumSize(QSize(16777215, 20))
        self.BallValve4State.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve4State, 2, 3, 1, 1)

        self.BallValve3Button = QPushButton(self.BallValveGroupBox)
        self.BallValve3Button.setObjectName(u"BallValve3Button")
        self.BallValve3Button.setMinimumSize(QSize(0, 30))
        self.BallValve3Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve3Button.setFont(font)
        self.BallValve3Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve3Button, 3, 2, 1, 1)

        self.BallValve1State = QLabel(self.BallValveGroupBox)
        self.BallValve1State.setObjectName(u"BallValve1State")
        self.BallValve1State.setMaximumSize(QSize(16777215, 20))
        self.BallValve1State.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve1State, 2, 0, 1, 1)

        self.BallValve4Label = QLabel(self.BallValveGroupBox)
        self.BallValve4Label.setObjectName(u"BallValve4Label")
        self.BallValve4Label.setMaximumSize(QSize(16777215, 20))
        self.BallValve4Label.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve4Label, 0, 3, 1, 1)

        self.BallValve1Label = QLabel(self.BallValveGroupBox)
        self.BallValve1Label.setObjectName(u"BallValve1Label")
        self.BallValve1Label.setMaximumSize(QSize(16777215, 20))
        self.BallValve1Label.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve1Label, 0, 0, 1, 1)

        self.BallValve5Button = QPushButton(self.BallValveGroupBox)
        self.BallValve5Button.setObjectName(u"BallValve5Button")
        self.BallValve5Button.setMinimumSize(QSize(0, 30))
        self.BallValve5Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve5Button.setFont(font)
        self.BallValve5Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve5Button, 3, 4, 1, 1)

        self.BallValve1Button = QPushButton(self.BallValveGroupBox)
        self.BallValve1Button.setObjectName(u"BallValve1Button")
        self.BallValve1Button.setMinimumSize(QSize(0, 30))
        self.BallValve1Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve1Button.setFont(font)
        self.BallValve1Button.setAutoFillBackground(False)
        self.BallValve1Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve1Button, 3, 0, 1, 1)

        self.BallValve5State = QLabel(self.BallValveGroupBox)
        self.BallValve5State.setObjectName(u"BallValve5State")
        self.BallValve5State.setMaximumSize(QSize(16777215, 20))
        self.BallValve5State.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve5State, 2, 4, 1, 1)

        self.BallValve3State = QLabel(self.BallValveGroupBox)
        self.BallValve3State.setObjectName(u"BallValve3State")
        self.BallValve3State.setMaximumSize(QSize(16777215, 20))
        self.BallValve3State.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve3State, 2, 2, 1, 1)

        self.BallValve2State = QLabel(self.BallValveGroupBox)
        self.BallValve2State.setObjectName(u"BallValve2State")
        self.BallValve2State.setMaximumSize(QSize(16777215, 20))
        self.BallValve2State.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve2State, 2, 1, 1, 1)

        self.BallValve3Label = QLabel(self.BallValveGroupBox)
        self.BallValve3Label.setObjectName(u"BallValve3Label")
        self.BallValve3Label.setMaximumSize(QSize(16777215, 20))
        self.BallValve3Label.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve3Label, 0, 2, 1, 1)

        self.BallValve5Label = QLabel(self.BallValveGroupBox)
        self.BallValve5Label.setObjectName(u"BallValve5Label")
        self.BallValve5Label.setMaximumSize(QSize(16777215, 20))
        self.BallValve5Label.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve5Label, 0, 4, 1, 1)

        self.BallValve4Button = QPushButton(self.BallValveGroupBox)
        self.BallValve4Button.setObjectName(u"BallValve4Button")
        self.BallValve4Button.setMinimumSize(QSize(0, 30))
        self.BallValve4Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve4Button.setFont(font)
        self.BallValve4Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve4Button, 3, 3, 1, 1)


        self.verticalLayout_5.addLayout(self.BallValveLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_10.addWidget(self.BallValveGroupBox)

        self.ThreeWayGroupBox = QGroupBox(DeviceStatus)
        self.ThreeWayGroupBox.setObjectName(u"ThreeWayGroupBox")
        self.ThreeWayGroupBox.setMaximumSize(QSize(16777215, 140))
        self.ThreeWayGroupBox.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.ThreeWayGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.ThreeWayLayout = QGridLayout()
        self.ThreeWayLayout.setObjectName(u"ThreeWayLayout")
        self.ThreeWayLayout.setContentsMargins(-1, 2, -1, 2)
        self.ThreeWay4Label = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay4Label.setObjectName(u"ThreeWay4Label")
        self.ThreeWay4Label.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay4Label.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay4Label, 0, 3, 1, 1)

        self.ThreeWay2Label = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay2Label.setObjectName(u"ThreeWay2Label")
        self.ThreeWay2Label.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay2Label.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay2Label, 0, 1, 1, 1)

        self.ThreeWay5Label = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay5Label.setObjectName(u"ThreeWay5Label")
        self.ThreeWay5Label.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay5Label.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay5Label, 0, 4, 1, 1)

        self.ThreeWay1State = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay1State.setObjectName(u"ThreeWay1State")
        self.ThreeWay1State.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay1State.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay1State, 1, 0, 1, 1)

        self.ThreeWay4State = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay4State.setObjectName(u"ThreeWay4State")
        self.ThreeWay4State.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay4State.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay4State, 1, 3, 1, 1)

        self.ThreeWay2State = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay2State.setObjectName(u"ThreeWay2State")
        self.ThreeWay2State.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay2State.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay2State, 1, 1, 1, 1)

        self.ThreeWay5State = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay5State.setObjectName(u"ThreeWay5State")
        self.ThreeWay5State.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay5State.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay5State, 1, 4, 1, 1)

        self.ThreeWay1Button = QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay1Button.setObjectName(u"ThreeWay1Button")
        self.ThreeWay1Button.setMinimumSize(QSize(0, 30))
        self.ThreeWay1Button.setMaximumSize(QSize(16777215, 30))
        self.ThreeWay1Button.setFont(font)
        self.ThreeWay1Button.setCheckable(False)

        self.ThreeWayLayout.addWidget(self.ThreeWay1Button, 2, 0, 1, 1)

        self.ThreeWay4Button = QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay4Button.setObjectName(u"ThreeWay4Button")
        self.ThreeWay4Button.setMinimumSize(QSize(0, 30))
        self.ThreeWay4Button.setMaximumSize(QSize(16777215, 30))
        self.ThreeWay4Button.setFont(font)
        self.ThreeWay4Button.setCheckable(False)

        self.ThreeWayLayout.addWidget(self.ThreeWay4Button, 2, 3, 1, 1)

        self.ThreeWay5Button = QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay5Button.setObjectName(u"ThreeWay5Button")
        self.ThreeWay5Button.setMinimumSize(QSize(0, 30))
        self.ThreeWay5Button.setMaximumSize(QSize(16777215, 30))
        self.ThreeWay5Button.setFont(font)
        self.ThreeWay5Button.setCheckable(False)

        self.ThreeWayLayout.addWidget(self.ThreeWay5Button, 2, 4, 1, 1)

        self.ThreeWay3Label = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay3Label.setObjectName(u"ThreeWay3Label")
        self.ThreeWay3Label.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay3Label.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay3Label, 0, 2, 1, 1)

        self.ThreeWay3Button = QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay3Button.setObjectName(u"ThreeWay3Button")
        self.ThreeWay3Button.setMinimumSize(QSize(0, 30))
        self.ThreeWay3Button.setMaximumSize(QSize(16777215, 30))
        self.ThreeWay3Button.setFont(font)
        self.ThreeWay3Button.setCheckable(False)

        self.ThreeWayLayout.addWidget(self.ThreeWay3Button, 2, 2, 1, 1)

        self.ThreeWay1Label = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay1Label.setObjectName(u"ThreeWay1Label")
        self.ThreeWay1Label.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay1Label.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay1Label, 0, 0, 1, 1)

        self.ThreeWay3State = QLabel(self.ThreeWayGroupBox)
        self.ThreeWay3State.setObjectName(u"ThreeWay3State")
        self.ThreeWay3State.setMaximumSize(QSize(16777215, 20))
        self.ThreeWay3State.setFont(font)

        self.ThreeWayLayout.addWidget(self.ThreeWay3State, 1, 2, 1, 1)

        self.ThreeWay2Button = QPushButton(self.ThreeWayGroupBox)
        self.ThreeWay2Button.setObjectName(u"ThreeWay2Button")
        self.ThreeWay2Button.setMinimumSize(QSize(0, 30))
        self.ThreeWay2Button.setMaximumSize(QSize(16777215, 30))
        self.ThreeWay2Button.setFont(font)
        self.ThreeWay2Button.setCheckable(False)

        self.ThreeWayLayout.addWidget(self.ThreeWay2Button, 2, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.ThreeWayLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.verticalLayout_10.addWidget(self.ThreeWayGroupBox)

        self.HeatersGroupBox = QGroupBox(DeviceStatus)
        self.HeatersGroupBox.setObjectName(u"HeatersGroupBox")
        self.HeatersGroupBox.setMaximumSize(QSize(16777215, 140))
        self.HeatersGroupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.HeatersGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.HeaterLayout = QGridLayout()
        self.HeaterLayout.setObjectName(u"HeaterLayout")
        self.HeaterLayout.setContentsMargins(-1, 2, -1, 2)
        self.Heater3Button = QPushButton(self.HeatersGroupBox)
        self.Heater3Button.setObjectName(u"Heater3Button")
        self.Heater3Button.setMinimumSize(QSize(0, 30))
        self.Heater3Button.setMaximumSize(QSize(16777215, 30))
        self.Heater3Button.setFont(font)
        self.Heater3Button.setCheckable(False)

        self.HeaterLayout.addWidget(self.Heater3Button, 2, 2, 1, 1)

        self.Heater1State = QLabel(self.HeatersGroupBox)
        self.Heater1State.setObjectName(u"Heater1State")
        self.Heater1State.setMaximumSize(QSize(16777215, 20))
        self.Heater1State.setFont(font)

        self.HeaterLayout.addWidget(self.Heater1State, 1, 0, 1, 1)

        self.Heater2Button = QPushButton(self.HeatersGroupBox)
        self.Heater2Button.setObjectName(u"Heater2Button")
        self.Heater2Button.setMinimumSize(QSize(0, 30))
        self.Heater2Button.setMaximumSize(QSize(16777215, 30))
        self.Heater2Button.setFont(font)
        self.Heater2Button.setCheckable(False)

        self.HeaterLayout.addWidget(self.Heater2Button, 2, 1, 1, 1)

        self.Heater3State = QLabel(self.HeatersGroupBox)
        self.Heater3State.setObjectName(u"Heater3State")
        self.Heater3State.setMaximumSize(QSize(16777215, 20))
        self.Heater3State.setFont(font)

        self.HeaterLayout.addWidget(self.Heater3State, 1, 2, 1, 1)

        self.Heater4Label = QLabel(self.HeatersGroupBox)
        self.Heater4Label.setObjectName(u"Heater4Label")
        self.Heater4Label.setMaximumSize(QSize(16777215, 20))
        self.Heater4Label.setFont(font)

        self.HeaterLayout.addWidget(self.Heater4Label, 0, 3, 1, 1)

        self.Heater1Button = QPushButton(self.HeatersGroupBox)
        self.Heater1Button.setObjectName(u"Heater1Button")
        self.Heater1Button.setMinimumSize(QSize(0, 30))
        self.Heater1Button.setMaximumSize(QSize(16777215, 30))
        self.Heater1Button.setFont(font)
        self.Heater1Button.setCheckable(False)

        self.HeaterLayout.addWidget(self.Heater1Button, 2, 0, 1, 1)

        self.Heater1Label = QLabel(self.HeatersGroupBox)
        self.Heater1Label.setObjectName(u"Heater1Label")
        self.Heater1Label.setMaximumSize(QSize(16777215, 20))
        self.Heater1Label.setFont(font)

        self.HeaterLayout.addWidget(self.Heater1Label, 0, 0, 1, 1)

        self.Heater3Label = QLabel(self.HeatersGroupBox)
        self.Heater3Label.setObjectName(u"Heater3Label")
        self.Heater3Label.setMaximumSize(QSize(16777215, 20))
        self.Heater3Label.setFont(font)

        self.HeaterLayout.addWidget(self.Heater3Label, 0, 2, 1, 1)

        self.Heater2State = QLabel(self.HeatersGroupBox)
        self.Heater2State.setObjectName(u"Heater2State")
        self.Heater2State.setMaximumSize(QSize(16777215, 20))
        self.Heater2State.setFont(font)

        self.HeaterLayout.addWidget(self.Heater2State, 1, 1, 1, 1)

        self.Heater2Label = QLabel(self.HeatersGroupBox)
        self.Heater2Label.setObjectName(u"Heater2Label")
        self.Heater2Label.setMaximumSize(QSize(16777215, 20))
        self.Heater2Label.setFont(font)

        self.HeaterLayout.addWidget(self.Heater2Label, 0, 1, 1, 1)

        self.Heater4Button = QPushButton(self.HeatersGroupBox)
        self.Heater4Button.setObjectName(u"Heater4Button")
        self.Heater4Button.setMinimumSize(QSize(0, 30))
        self.Heater4Button.setMaximumSize(QSize(16777215, 30))
        self.Heater4Button.setFont(font)
        self.Heater4Button.setCheckable(False)

        self.HeaterLayout.addWidget(self.Heater4Button, 2, 3, 1, 1)

        self.Heater4State = QLabel(self.HeatersGroupBox)
        self.Heater4State.setObjectName(u"Heater4State")
        self.Heater4State.setMaximumSize(QSize(16777215, 20))
        self.Heater4State.setFont(font)

        self.HeaterLayout.addWidget(self.Heater4State, 1, 3, 1, 1)


        self.verticalLayout_2.addLayout(self.HeaterLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)


        self.verticalLayout_10.addWidget(self.HeatersGroupBox)

        self.PumpsGroupBox = QGroupBox(DeviceStatus)
        self.PumpsGroupBox.setObjectName(u"PumpsGroupBox")
        self.PumpsGroupBox.setMaximumSize(QSize(16777215, 140))
        self.PumpsGroupBox.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.PumpsGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_7)

        self.PumpLayout = QGridLayout()
        self.PumpLayout.setObjectName(u"PumpLayout")
        self.PumpLayout.setContentsMargins(-1, 2, -1, 2)
        self.Pump2State = QLabel(self.PumpsGroupBox)
        self.Pump2State.setObjectName(u"Pump2State")
        self.Pump2State.setMaximumSize(QSize(16777215, 20))
        self.Pump2State.setFont(font)

        self.PumpLayout.addWidget(self.Pump2State, 1, 1, 1, 1)

        self.Pump1State = QLabel(self.PumpsGroupBox)
        self.Pump1State.setObjectName(u"Pump1State")
        self.Pump1State.setMaximumSize(QSize(16777215, 20))
        self.Pump1State.setFont(font)

        self.PumpLayout.addWidget(self.Pump1State, 1, 0, 1, 1)

        self.Pump2Button = QPushButton(self.PumpsGroupBox)
        self.Pump2Button.setObjectName(u"Pump2Button")
        self.Pump2Button.setMinimumSize(QSize(0, 30))
        self.Pump2Button.setMaximumSize(QSize(16777215, 30))
        self.Pump2Button.setFont(font)
        self.Pump2Button.setCheckable(False)

        self.PumpLayout.addWidget(self.Pump2Button, 2, 1, 1, 1)

        self.Pump2Label = QLabel(self.PumpsGroupBox)
        self.Pump2Label.setObjectName(u"Pump2Label")
        self.Pump2Label.setMaximumSize(QSize(16777215, 20))
        self.Pump2Label.setFont(font)

        self.PumpLayout.addWidget(self.Pump2Label, 0, 1, 1, 1)

        self.Pump1Button = QPushButton(self.PumpsGroupBox)
        self.Pump1Button.setObjectName(u"Pump1Button")
        self.Pump1Button.setMinimumSize(QSize(0, 30))
        self.Pump1Button.setMaximumSize(QSize(16777215, 30))
        self.Pump1Button.setFont(font)
        self.Pump1Button.setCheckable(False)

        self.PumpLayout.addWidget(self.Pump1Button, 2, 0, 1, 1)

        self.Pump1Label = QLabel(self.PumpsGroupBox)
        self.Pump1Label.setObjectName(u"Pump1Label")
        self.Pump1Label.setMaximumSize(QSize(16777215, 20))
        self.Pump1Label.setFont(font)

        self.PumpLayout.addWidget(self.Pump1Label, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.PumpLayout)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)


        self.verticalLayout_10.addWidget(self.PumpsGroupBox)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_17)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ReturnToMenuButton = QPushButton(DeviceStatus)
        self.ReturnToMenuButton.setObjectName(u"ReturnToMenuButton")
        self.ReturnToMenuButton.setMinimumSize(QSize(0, 30))
        self.ReturnToMenuButton.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.ReturnToMenuButton.setFont(font1)

        self.horizontalLayout_3.addWidget(self.ReturnToMenuButton)

        self.ProcessStatusButton = QPushButton(DeviceStatus)
        self.ProcessStatusButton.setObjectName(u"ProcessStatusButton")
        self.ProcessStatusButton.setMinimumSize(QSize(0, 30))
        self.ProcessStatusButton.setMaximumSize(QSize(16777215, 30))
        self.ProcessStatusButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.ProcessStatusButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)


        self.retranslateUi(DeviceStatus)

        QMetaObject.connectSlotsByName(DeviceStatus)
    # setupUi

    def retranslateUi(self, DeviceStatus):
        DeviceStatus.setWindowTitle(QCoreApplication.translate("DeviceStatus", u"Form", None))
        self.BallValveToggle.setText(QCoreApplication.translate("DeviceStatus", u"Ball Valves", None))
        self.HeaterTempToggle.setText(QCoreApplication.translate("DeviceStatus", u"Heaters and Temperature", None))
        self.PumpVolumeToggle.setText(QCoreApplication.translate("DeviceStatus", u"Pumps and Tank Volume", None))
        self.ServoMotorToggle.setText(QCoreApplication.translate("DeviceStatus", u"Servo Motor", None))
        self.HeatersPWMGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatus", u"QGroupBox {border: 1px solid black}", None))
        self.HeatersPWMGroupBox.setTitle(QCoreApplication.translate("DeviceStatus", u"Heaters PWM", None))
        self.HeaterPID1.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.HeaterPID4.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.Heater1Label_2.setText(QCoreApplication.translate("DeviceStatus", u"Heater: 1", None))
        self.Heater3Label_2.setText(QCoreApplication.translate("DeviceStatus", u"Heater: 3", None))
        self.HeaterPID3.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.Heater4Label_2.setText(QCoreApplication.translate("DeviceStatus", u"Heater: 4", None))
        self.HeaterPID2.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.Heater2Label_2.setText(QCoreApplication.translate("DeviceStatus", u"Heater: 2", None))
        self.HeaterPIDDecrease1.setText(QCoreApplication.translate("DeviceStatus", u"-", None))
        self.HeaterPIDIncrease1.setText(QCoreApplication.translate("DeviceStatus", u"+", None))
        self.HeaterPIDDecrease2.setText(QCoreApplication.translate("DeviceStatus", u"-", None))
        self.HeaterPIDIncrease2.setText(QCoreApplication.translate("DeviceStatus", u"+", None))
        self.HeaterPIDDecrease3.setText(QCoreApplication.translate("DeviceStatus", u"-", None))
        self.HeaterPIDIncrease3.setText(QCoreApplication.translate("DeviceStatus", u"+", None))
        self.HeaterPIDDecrease4.setText(QCoreApplication.translate("DeviceStatus", u"-", None))
        self.HeaterPIDIncrease4.setText(QCoreApplication.translate("DeviceStatus", u"+", None))
        self.TemperatureGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatus", u"QGroupBox {border: 1px solid black}", None))
        self.TemperatureGroupBox.setTitle(QCoreApplication.translate("DeviceStatus", u"Heater Target Temperature", None))
        self.BKTargetTemp.setText(QCoreApplication.translate("DeviceStatus", u"Target Temperature (\u00b0F): 20", None))
        self.HLTCurrentTemp.setText(QCoreApplication.translate("DeviceStatus", u"Current Temperature (\u00b0F): 20", None))
        self.BKCurrentTemp.setText(QCoreApplication.translate("DeviceStatus", u"Current Temperature (\u00b0F): 20", None))
        self.DecreaseBK.setText(QCoreApplication.translate("DeviceStatus", u"-", None))
        self.BKPIDtoggle.setText(QCoreApplication.translate("DeviceStatus", u"Enable", None))
        self.IncreaseBK.setText(QCoreApplication.translate("DeviceStatus", u"+", None))
        self.DecreaseHLT.setText(QCoreApplication.translate("DeviceStatus", u"-", None))
        self.HLTPIDtoggle.setText(QCoreApplication.translate("DeviceStatus", u"Enable", None))
        self.IncreaseHLT.setText(QCoreApplication.translate("DeviceStatus", u"+", None))
        self.HLTTargetTemp.setText(QCoreApplication.translate("DeviceStatus", u"Target Temperature (\u00b0F): 20", None))
        self.MTCurrentTemp.setText(QCoreApplication.translate("DeviceStatus", u"Current Temperature (\u00b0F): 20", None))
        self.MTTargetTemp.setText(QCoreApplication.translate("DeviceStatus", u"Target Temperature (\u00b0F): 20", None))
        self.DecreaseMT.setText(QCoreApplication.translate("DeviceStatus", u"-", None))
        self.MTPIDtoggle.setText(QCoreApplication.translate("DeviceStatus", u"Enable", None))
        self.IncreaseMT.setText(QCoreApplication.translate("DeviceStatus", u"+", None))
        self.BKLabel.setText(QCoreApplication.translate("DeviceStatus", u"Boil Kettle", None))
        self.HLTLabel.setText(QCoreApplication.translate("DeviceStatus", u"Hot Liquor Tank", None))
        self.MTLabel.setText(QCoreApplication.translate("DeviceStatus", u"Mash Tun", None))
        self.ServoMotorGroupBox.setTitle(QCoreApplication.translate("DeviceStatus", u"Servo Motor", None))
        self.IncreaseServo.setText(QCoreApplication.translate("DeviceStatus", u"+", None))
        self.HopServo3.setText(QCoreApplication.translate("DeviceStatus", u"Hop Cup 3", None))
        self.HopServo5.setText(QCoreApplication.translate("DeviceStatus", u"Hop Cup 5", None))
        self.HopServo1.setText(QCoreApplication.translate("DeviceStatus", u"Hop Cup 1", None))
        self.HomeServo.setText(QCoreApplication.translate("DeviceStatus", u"Home", None))
        self.HopServo2.setText(QCoreApplication.translate("DeviceStatus", u"Hop Cup 2", None))
        self.CurrentAngleServo.setText(QCoreApplication.translate("DeviceStatus", u"Current Angle (\u00b0): 270", None))
        self.HopServo4.setText(QCoreApplication.translate("DeviceStatus", u"Hop Cup 4", None))
        self.DecreaseServo.setText(QCoreApplication.translate("DeviceStatus", u"-", None))
        self.TankVolumeGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatus", u"QGroupBox {border: 1px solid black}", None))
        self.TankVolumeGroupBox.setTitle(QCoreApplication.translate("DeviceStatus", u"Tank Volume", None))
        self.TankVolume3State.setText(QCoreApplication.translate("DeviceStatus", u"Volume (gal):", None))
        self.TankVolume1Label.setText(QCoreApplication.translate("DeviceStatus", u"Hot Liquor Tank:", None))
        self.TankVolume1State.setText(QCoreApplication.translate("DeviceStatus", u"Volume (gal):", None))
        self.TankVolume2State.setText(QCoreApplication.translate("DeviceStatus", u"Volume (gal):", None))
        self.TankVolume2Label.setText(QCoreApplication.translate("DeviceStatus", u"Mash Tun:", None))
        self.TankVolume3Label.setText(QCoreApplication.translate("DeviceStatus", u"Boil Kettle:", None))
        self.BallValveGroupBox.setTitle(QCoreApplication.translate("DeviceStatus", u"Ball Valves", None))
        self.BallValve2Button.setText(QCoreApplication.translate("DeviceStatus", u"Open", None))
        self.BallValve2Label.setText(QCoreApplication.translate("DeviceStatus", u"Ball Valve: 2", None))
        self.BallValve4State.setText(QCoreApplication.translate("DeviceStatus", u"State: Closed", None))
        self.BallValve3Button.setText(QCoreApplication.translate("DeviceStatus", u"Open", None))
        self.BallValve1State.setText(QCoreApplication.translate("DeviceStatus", u"State: Closed", None))
        self.BallValve4Label.setText(QCoreApplication.translate("DeviceStatus", u"Ball Valve: 4", None))
        self.BallValve1Label.setText(QCoreApplication.translate("DeviceStatus", u"Ball Valve: 1", None))
        self.BallValve5Button.setText(QCoreApplication.translate("DeviceStatus", u"Open", None))
        self.BallValve1Button.setText(QCoreApplication.translate("DeviceStatus", u"Open", None))
        self.BallValve5State.setText(QCoreApplication.translate("DeviceStatus", u"State: Closed", None))
        self.BallValve3State.setText(QCoreApplication.translate("DeviceStatus", u"State: Closed", None))
        self.BallValve2State.setText(QCoreApplication.translate("DeviceStatus", u"State: Closed", None))
        self.BallValve3Label.setText(QCoreApplication.translate("DeviceStatus", u"Ball Valve: 3", None))
        self.BallValve5Label.setText(QCoreApplication.translate("DeviceStatus", u"Ball Valve: 5", None))
        self.BallValve4Button.setText(QCoreApplication.translate("DeviceStatus", u"Open", None))
        self.ThreeWayGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatus", u"QGroupBox {border: 1px solid black}", None))
        self.ThreeWayGroupBox.setTitle(QCoreApplication.translate("DeviceStatus", u"Three Way Valves", None))
        self.ThreeWay4Label.setText(QCoreApplication.translate("DeviceStatus", u"Three Way Valve: 4", None))
        self.ThreeWay2Label.setText(QCoreApplication.translate("DeviceStatus", u"Three Way Valve: 2", None))
        self.ThreeWay5Label.setText(QCoreApplication.translate("DeviceStatus", u"Three Way Valve: 5", None))
        self.ThreeWay1State.setText(QCoreApplication.translate("DeviceStatus", u"State: Direction 1", None))
        self.ThreeWay4State.setText(QCoreApplication.translate("DeviceStatus", u"State: Direction 1", None))
        self.ThreeWay2State.setText(QCoreApplication.translate("DeviceStatus", u"State: Direction 1", None))
        self.ThreeWay5State.setText(QCoreApplication.translate("DeviceStatus", u"State: Direction 1", None))
        self.ThreeWay1Button.setText(QCoreApplication.translate("DeviceStatus", u"Switch Direction", None))
        self.ThreeWay4Button.setText(QCoreApplication.translate("DeviceStatus", u"Switch Direction", None))
        self.ThreeWay5Button.setText(QCoreApplication.translate("DeviceStatus", u"Switch Direction", None))
        self.ThreeWay3Label.setText(QCoreApplication.translate("DeviceStatus", u"Three Way Valve: 3", None))
        self.ThreeWay3Button.setText(QCoreApplication.translate("DeviceStatus", u"Switch Direction", None))
        self.ThreeWay1Label.setText(QCoreApplication.translate("DeviceStatus", u"Three Way Valve: 1", None))
        self.ThreeWay3State.setText(QCoreApplication.translate("DeviceStatus", u"State: Direction 1", None))
        self.ThreeWay2Button.setText(QCoreApplication.translate("DeviceStatus", u"Switch Direction", None))
        self.HeatersGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatus", u"QGroupBox {border: 1px solid black}", None))
        self.HeatersGroupBox.setTitle(QCoreApplication.translate("DeviceStatus", u"Heaters", None))
        self.Heater3Button.setText(QCoreApplication.translate("DeviceStatus", u"Turn On", None))
        self.Heater1State.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.Heater2Button.setText(QCoreApplication.translate("DeviceStatus", u"Turn On", None))
        self.Heater3State.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.Heater4Label.setText(QCoreApplication.translate("DeviceStatus", u"Heater: 4", None))
        self.Heater1Button.setText(QCoreApplication.translate("DeviceStatus", u"Turn On", None))
        self.Heater1Label.setText(QCoreApplication.translate("DeviceStatus", u"Heater: 1", None))
        self.Heater3Label.setText(QCoreApplication.translate("DeviceStatus", u"Heater: 3", None))
        self.Heater2State.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.Heater2Label.setText(QCoreApplication.translate("DeviceStatus", u"Heater: 2", None))
        self.Heater4Button.setText(QCoreApplication.translate("DeviceStatus", u"Turn On", None))
        self.Heater4State.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.PumpsGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatus", u"QGroupBox {border: 1px solid black}", None))
        self.PumpsGroupBox.setTitle(QCoreApplication.translate("DeviceStatus", u"Pumps", None))
        self.Pump2State.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.Pump1State.setText(QCoreApplication.translate("DeviceStatus", u"State: Off", None))
        self.Pump2Button.setText(QCoreApplication.translate("DeviceStatus", u"Turn On", None))
        self.Pump2Label.setText(QCoreApplication.translate("DeviceStatus", u"Pump: 2", None))
        self.Pump1Button.setText(QCoreApplication.translate("DeviceStatus", u"Turn On", None))
        self.Pump1Label.setText(QCoreApplication.translate("DeviceStatus", u"Pump: 1", None))
        self.ReturnToMenuButton.setText(QCoreApplication.translate("DeviceStatus", u"Main Menu", None))
        self.ProcessStatusButton.setText(QCoreApplication.translate("DeviceStatus", u"Process Status", None))
    # retranslateUi

