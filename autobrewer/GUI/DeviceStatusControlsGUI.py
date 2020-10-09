# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeviceStatusControls.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_DeviceStatusControls(object):
    def setupUi(self, DeviceStatusControls):
        if not DeviceStatusControls.objectName():
            DeviceStatusControls.setObjectName(u"DeviceStatusControls")
        DeviceStatusControls.resize(1024, 600)
        DeviceStatusControls.setMinimumSize(QSize(1024, 600))
        DeviceStatusControls.setMaximumSize(QSize(1024, 600))
        self.verticalLayout = QVBoxLayout(DeviceStatusControls)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.BallValveGroupBox = QGroupBox(DeviceStatusControls)
        self.BallValveGroupBox.setObjectName(u"BallValveGroupBox")
        font = QFont()
        font.setPointSize(11)
        self.BallValveGroupBox.setFont(font)
        self.BallValveGroupBox.setStyleSheet(u"QGroupBox {border: 1px solid black}")
        self.horizontalLayout = QHBoxLayout(self.BallValveGroupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BallValveLayout = QGridLayout()
        self.BallValveLayout.setObjectName(u"BallValveLayout")
        self.BallValveLayout.setContentsMargins(-1, 2, -1, 2)
        self.BallValve5Button = QPushButton(self.BallValveGroupBox)
        self.BallValve5Button.setObjectName(u"BallValve5Button")
        self.BallValve5Button.setMinimumSize(QSize(0, 30))
        self.BallValve5Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve5Button.setFont(font)
        self.BallValve5Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve5Button, 3, 4, 1, 1)

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

        self.BallValve1State = QLabel(self.BallValveGroupBox)
        self.BallValve1State.setObjectName(u"BallValve1State")
        self.BallValve1State.setMaximumSize(QSize(16777215, 20))
        self.BallValve1State.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve1State, 2, 0, 1, 1)

        self.BallValve2Label = QLabel(self.BallValveGroupBox)
        self.BallValve2Label.setObjectName(u"BallValve2Label")
        self.BallValve2Label.setMaximumSize(QSize(16777215, 20))
        self.BallValve2Label.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve2Label, 0, 1, 1, 1)

        self.BallValve5State = QLabel(self.BallValveGroupBox)
        self.BallValve5State.setObjectName(u"BallValve5State")
        self.BallValve5State.setMaximumSize(QSize(16777215, 20))
        self.BallValve5State.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve5State, 2, 4, 1, 1)

        self.BallValve3Button = QPushButton(self.BallValveGroupBox)
        self.BallValve3Button.setObjectName(u"BallValve3Button")
        self.BallValve3Button.setMinimumSize(QSize(0, 30))
        self.BallValve3Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve3Button.setFont(font)
        self.BallValve3Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve3Button, 3, 2, 1, 1)

        self.BallValve1Label = QLabel(self.BallValveGroupBox)
        self.BallValve1Label.setObjectName(u"BallValve1Label")
        self.BallValve1Label.setMaximumSize(QSize(16777215, 20))
        self.BallValve1Label.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve1Label, 0, 0, 1, 1)

        self.BallValve4Label = QLabel(self.BallValveGroupBox)
        self.BallValve4Label.setObjectName(u"BallValve4Label")
        self.BallValve4Label.setMaximumSize(QSize(16777215, 20))
        self.BallValve4Label.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve4Label, 0, 3, 1, 1)

        self.BallValve1Button = QPushButton(self.BallValveGroupBox)
        self.BallValve1Button.setObjectName(u"BallValve1Button")
        self.BallValve1Button.setMinimumSize(QSize(0, 30))
        self.BallValve1Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve1Button.setFont(font)
        self.BallValve1Button.setAutoFillBackground(False)
        self.BallValve1Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve1Button, 3, 0, 1, 1)

        self.BallValve4Button = QPushButton(self.BallValveGroupBox)
        self.BallValve4Button.setObjectName(u"BallValve4Button")
        self.BallValve4Button.setMinimumSize(QSize(0, 30))
        self.BallValve4Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve4Button.setFont(font)
        self.BallValve4Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve4Button, 3, 3, 1, 1)

        self.BallValve4State = QLabel(self.BallValveGroupBox)
        self.BallValve4State.setObjectName(u"BallValve4State")
        self.BallValve4State.setMaximumSize(QSize(16777215, 20))
        self.BallValve4State.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve4State, 2, 3, 1, 1)

        self.BallValve2Button = QPushButton(self.BallValveGroupBox)
        self.BallValve2Button.setObjectName(u"BallValve2Button")
        self.BallValve2Button.setMinimumSize(QSize(0, 30))
        self.BallValve2Button.setMaximumSize(QSize(16777215, 30))
        self.BallValve2Button.setFont(font)
        self.BallValve2Button.setCheckable(False)

        self.BallValveLayout.addWidget(self.BallValve2Button, 3, 1, 1, 1)

        self.BallValve3State = QLabel(self.BallValveGroupBox)
        self.BallValve3State.setObjectName(u"BallValve3State")
        self.BallValve3State.setMaximumSize(QSize(16777215, 20))
        self.BallValve3State.setFont(font)

        self.BallValveLayout.addWidget(self.BallValve3State, 2, 2, 1, 1)


        self.horizontalLayout.addLayout(self.BallValveLayout)


        self.verticalLayout.addWidget(self.BallValveGroupBox)

        self.horizontalSpacer = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.ThreeWayGroupBox = QGroupBox(DeviceStatusControls)
        self.ThreeWayGroupBox.setObjectName(u"ThreeWayGroupBox")
        self.ThreeWayGroupBox.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.ThreeWayGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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


        self.horizontalLayout_2.addLayout(self.ThreeWayLayout)


        self.verticalLayout.addWidget(self.ThreeWayGroupBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_2)

        self.HeatersGroupBox = QGroupBox(DeviceStatusControls)
        self.HeatersGroupBox.setObjectName(u"HeatersGroupBox")
        self.HeatersGroupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.HeatersGroupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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


        self.verticalLayout.addWidget(self.HeatersGroupBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.PumpsGroupBox = QGroupBox(DeviceStatusControls)
        self.PumpsGroupBox.setObjectName(u"PumpsGroupBox")
        self.PumpsGroupBox.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.PumpsGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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


        self.verticalLayout.addWidget(self.PumpsGroupBox)

        self.GoToSensorStatusButton = QPushButton(DeviceStatusControls)
        self.GoToSensorStatusButton.setObjectName(u"GoToSensorStatusButton")
        font1 = QFont()
        font1.setPointSize(10)
        self.GoToSensorStatusButton.setFont(font1)

        self.verticalLayout.addWidget(self.GoToSensorStatusButton)

        self.ReturnToMenuButton = QPushButton(DeviceStatusControls)
        self.ReturnToMenuButton.setObjectName(u"ReturnToMenuButton")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.ReturnToMenuButton.setFont(font2)

        self.verticalLayout.addWidget(self.ReturnToMenuButton)


        self.retranslateUi(DeviceStatusControls)

        QMetaObject.connectSlotsByName(DeviceStatusControls)
    # setupUi

    def retranslateUi(self, DeviceStatusControls):
        DeviceStatusControls.setWindowTitle(QCoreApplication.translate("DeviceStatusControls", u"Form", None))
        self.BallValveGroupBox.setTitle(QCoreApplication.translate("DeviceStatusControls", u"Ball Valves", None))
        self.BallValve5Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Open", None))
        self.BallValve2State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Closed", None))
        self.BallValve3Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Ball Valve: 3", None))
        self.BallValve5Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Ball Valve: 5", None))
        self.BallValve1State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Closed", None))
        self.BallValve2Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Ball Valve: 2", None))
        self.BallValve5State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Closed", None))
        self.BallValve3Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Open", None))
        self.BallValve1Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Ball Valve: 1", None))
        self.BallValve4Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Ball Valve: 4", None))
        self.BallValve1Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Open", None))
        self.BallValve4Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Open", None))
        self.BallValve4State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Closed", None))
        self.BallValve2Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Open", None))
        self.BallValve3State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Closed", None))
        self.ThreeWayGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatusControls", u"QGroupBox {border: 1px solid black}", None))
        self.ThreeWayGroupBox.setTitle(QCoreApplication.translate("DeviceStatusControls", u"Three Way Valves", None))
        self.ThreeWay4Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Three Way Valve: 4", None))
        self.ThreeWay2Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Three Way Valve: 2", None))
        self.ThreeWay5Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Three Way Valve: 5", None))
        self.ThreeWay1State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Direction 1", None))
        self.ThreeWay4State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Direction 1", None))
        self.ThreeWay2State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Direction 1", None))
        self.ThreeWay5State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Direction 1", None))
        self.ThreeWay1Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Switch Direction", None))
        self.ThreeWay4Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Switch Direction", None))
        self.ThreeWay5Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Switch Direction", None))
        self.ThreeWay3Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Three Way Valve: 3", None))
        self.ThreeWay3Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Switch Direction", None))
        self.ThreeWay1Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Three Way Valve: 1", None))
        self.ThreeWay3State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Direction 1", None))
        self.ThreeWay2Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Switch Direction", None))
        self.HeatersGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatusControls", u"QGroupBox {border: 1px solid black}", None))
        self.HeatersGroupBox.setTitle(QCoreApplication.translate("DeviceStatusControls", u"Heaters", None))
        self.Heater3Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Turn On", None))
        self.Heater1State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Off", None))
        self.Heater2Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Turn On", None))
        self.Heater3State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Off", None))
        self.Heater4Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Heater: 4", None))
        self.Heater1Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Turn On", None))
        self.Heater1Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Heater: 1", None))
        self.Heater3Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Heater: 3", None))
        self.Heater2State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Off", None))
        self.Heater2Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Heater: 2", None))
        self.Heater4Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Turn On", None))
        self.Heater4State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Off", None))
        self.PumpsGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatusControls", u"QGroupBox {border: 1px solid black}", None))
        self.PumpsGroupBox.setTitle(QCoreApplication.translate("DeviceStatusControls", u"Pumps", None))
        self.Pump2State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Off", None))
        self.Pump1State.setText(QCoreApplication.translate("DeviceStatusControls", u"State: Off", None))
        self.Pump2Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Turn On", None))
        self.Pump2Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Pump: 2", None))
        self.Pump1Button.setText(QCoreApplication.translate("DeviceStatusControls", u"Turn On", None))
        self.Pump1Label.setText(QCoreApplication.translate("DeviceStatusControls", u"Pump: 1", None))
        self.GoToSensorStatusButton.setText(QCoreApplication.translate("DeviceStatusControls", u"Sensor Status", None))
        self.ReturnToMenuButton.setText(QCoreApplication.translate("DeviceStatusControls", u"Return to Main Menu", None))
    # retranslateUi

