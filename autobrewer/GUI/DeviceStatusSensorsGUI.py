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
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.TempSensGroupBox = QGroupBox(DeviceStatusSensors)
        self.TempSensGroupBox.setObjectName(u"TempSensGroupBox")
        font = QFont()
        font.setPointSize(11)
        self.TempSensGroupBox.setFont(font)
        self.verticalLayout_4 = QVBoxLayout(self.TempSensGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TempSensLayout = QGridLayout()
        self.TempSensLayout.setObjectName(u"TempSensLayout")
        self.TempSensLayout.setContentsMargins(-1, 2, -1, 2)
        self.TempSens1State = QLabel(self.TempSensGroupBox)
        self.TempSens1State.setObjectName(u"TempSens1State")
        self.TempSens1State.setMaximumSize(QSize(16777215, 20))
        self.TempSens1State.setFont(font)

        self.TempSensLayout.addWidget(self.TempSens1State, 1, 0, 1, 1)

        self.TempSens2State = QLabel(self.TempSensGroupBox)
        self.TempSens2State.setObjectName(u"TempSens2State")
        self.TempSens2State.setMaximumSize(QSize(16777215, 20))
        self.TempSens2State.setFont(font)

        self.TempSensLayout.addWidget(self.TempSens2State, 1, 1, 1, 1)

        self.TempSens3Label = QLabel(self.TempSensGroupBox)
        self.TempSens3Label.setObjectName(u"TempSens3Label")
        self.TempSens3Label.setMaximumSize(QSize(16777215, 20))
        self.TempSens3Label.setFont(font)

        self.TempSensLayout.addWidget(self.TempSens3Label, 0, 2, 1, 1)

        self.TempSens1Label = QLabel(self.TempSensGroupBox)
        self.TempSens1Label.setObjectName(u"TempSens1Label")
        self.TempSens1Label.setMaximumSize(QSize(16777215, 20))
        self.TempSens1Label.setFont(font)

        self.TempSensLayout.addWidget(self.TempSens1Label, 0, 0, 1, 1)

        self.TempSens2Label = QLabel(self.TempSensGroupBox)
        self.TempSens2Label.setObjectName(u"TempSens2Label")
        self.TempSens2Label.setMaximumSize(QSize(16777215, 20))
        self.TempSens2Label.setFont(font)

        self.TempSensLayout.addWidget(self.TempSens2Label, 0, 1, 1, 1)

        self.TempSens3State = QLabel(self.TempSensGroupBox)
        self.TempSens3State.setObjectName(u"TempSens3State")
        self.TempSens3State.setMaximumSize(QSize(16777215, 20))
        self.TempSens3State.setFont(font)

        self.TempSensLayout.addWidget(self.TempSens3State, 1, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.TempSensLayout)


        self.verticalLayout.addWidget(self.TempSensGroupBox)

        self.horizontalSpacer = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.TankVolumeGroupBox = QGroupBox(DeviceStatusSensors)
        self.TankVolumeGroupBox.setObjectName(u"TankVolumeGroupBox")
        self.TankVolumeGroupBox.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(self.TankVolumeGroupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.TankVolumeLayout = QGridLayout()
        self.TankVolumeLayout.setObjectName(u"TankVolumeLayout")
        self.TankVolumeLayout.setContentsMargins(-1, 2, -1, 2)
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

        self.TankVolume3Label = QLabel(self.TankVolumeGroupBox)
        self.TankVolume3Label.setObjectName(u"TankVolume3Label")
        self.TankVolume3Label.setMaximumSize(QSize(16777215, 20))
        self.TankVolume3Label.setFont(font)

        self.TankVolumeLayout.addWidget(self.TankVolume3Label, 0, 2, 1, 1)

        self.TankVolume2Label = QLabel(self.TankVolumeGroupBox)
        self.TankVolume2Label.setObjectName(u"TankVolume2Label")
        self.TankVolume2Label.setMaximumSize(QSize(16777215, 20))
        self.TankVolume2Label.setFont(font)

        self.TankVolumeLayout.addWidget(self.TankVolume2Label, 0, 1, 1, 1)

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


        self.verticalLayout_5.addLayout(self.TankVolumeLayout)


        self.verticalLayout.addWidget(self.TankVolumeGroupBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 250, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_3)

        self.GoToControlStatusButton = QPushButton(DeviceStatusSensors)
        self.GoToControlStatusButton.setObjectName(u"GoToControlStatusButton")
        font1 = QFont()
        font1.setPointSize(10)
        self.GoToControlStatusButton.setFont(font1)

        self.verticalLayout.addWidget(self.GoToControlStatusButton)

        self.ReturnToMenuButton = QPushButton(DeviceStatusSensors)
        self.ReturnToMenuButton.setObjectName(u"ReturnToMenuButton")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.ReturnToMenuButton.setFont(font2)

        self.verticalLayout.addWidget(self.ReturnToMenuButton)


        self.retranslateUi(DeviceStatusSensors)

        QMetaObject.connectSlotsByName(DeviceStatusSensors)
    # setupUi

    def retranslateUi(self, DeviceStatusSensors):
        DeviceStatusSensors.setWindowTitle(QCoreApplication.translate("DeviceStatusSensors", u"Form", None))
        self.TempSensGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatusSensors", u"QGroupBox {border: 1px solid black}", None))
        self.TempSensGroupBox.setTitle(QCoreApplication.translate("DeviceStatusSensors", u"Temperature Sensors", None))
        self.TempSens1State.setText(QCoreApplication.translate("DeviceStatusSensors", u"Temperature (\u00b0F): 200", None))
        self.TempSens2State.setText(QCoreApplication.translate("DeviceStatusSensors", u"Temperature (\u00b0F): 200", None))
        self.TempSens3Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Boil Kettle:", None))
        self.TempSens1Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Hot Liquor Tank:", None))
        self.TempSens2Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Mash Tun:", None))
        self.TempSens3State.setText(QCoreApplication.translate("DeviceStatusSensors", u"Temperature (\u00b0F): 200", None))
        self.TankVolumeGroupBox.setStyleSheet(QCoreApplication.translate("DeviceStatusSensors", u"QGroupBox {border: 1px solid black}", None))
        self.TankVolumeGroupBox.setTitle(QCoreApplication.translate("DeviceStatusSensors", u"Tank Volume", None))
        self.TankVolume1State.setText(QCoreApplication.translate("DeviceStatusSensors", u"Volume (gal):", None))
        self.TankVolume2State.setText(QCoreApplication.translate("DeviceStatusSensors", u"Volume (gal):", None))
        self.TankVolume3Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Boil Kettle:", None))
        self.TankVolume2Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Mash Tun:", None))
        self.TankVolume3State.setText(QCoreApplication.translate("DeviceStatusSensors", u"Volume (gal):", None))
        self.TankVolume1Label.setText(QCoreApplication.translate("DeviceStatusSensors", u"Hot Liquor Tank:", None))
        self.GoToControlStatusButton.setText(QCoreApplication.translate("DeviceStatusSensors", u"Device Controls", None))
        self.ReturnToMenuButton.setText(QCoreApplication.translate("DeviceStatusSensors", u"Return to Main Menu", None))
    # retranslateUi

