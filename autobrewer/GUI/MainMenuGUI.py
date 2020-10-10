# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenu.ui'
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


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(1024, 600)
        MainMenu.setMinimumSize(QSize(1024, 600))
        MainMenu.setMaximumSize(QSize(1024, 600))
        self.MainMenuLayout = QGridLayout(MainMenu)
        self.MainMenuLayout.setObjectName(u"MainMenuLayout")
        self.EnterCleanScreenButton = QPushButton(MainMenu)
        self.EnterCleanScreenButton.setObjectName(u"EnterCleanScreenButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EnterCleanScreenButton.sizePolicy().hasHeightForWidth())
        self.EnterCleanScreenButton.setSizePolicy(sizePolicy)
        self.EnterCleanScreenButton.setMinimumSize(QSize(800, 60))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.EnterCleanScreenButton.setFont(font)

        self.MainMenuLayout.addWidget(self.EnterCleanScreenButton, 1, 0, 1, 1)

        self.EnterBrewConfigButton = QPushButton(MainMenu)
        self.EnterBrewConfigButton.setObjectName(u"EnterBrewConfigButton")
        sizePolicy.setHeightForWidth(self.EnterBrewConfigButton.sizePolicy().hasHeightForWidth())
        self.EnterBrewConfigButton.setSizePolicy(sizePolicy)
        self.EnterBrewConfigButton.setMinimumSize(QSize(800, 60))
        self.EnterBrewConfigButton.setFont(font)

        self.MainMenuLayout.addWidget(self.EnterBrewConfigButton, 0, 0, 1, 1)

        self.EnterDeviceStatusScreen = QPushButton(MainMenu)
        self.EnterDeviceStatusScreen.setObjectName(u"EnterDeviceStatusScreen")
        sizePolicy.setHeightForWidth(self.EnterDeviceStatusScreen.sizePolicy().hasHeightForWidth())
        self.EnterDeviceStatusScreen.setSizePolicy(sizePolicy)
        self.EnterDeviceStatusScreen.setMinimumSize(QSize(800, 60))
        self.EnterDeviceStatusScreen.setFont(font)

        self.MainMenuLayout.addWidget(self.EnterDeviceStatusScreen, 2, 0, 1, 1)


        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"Form", None))
        self.EnterCleanScreenButton.setText(QCoreApplication.translate("MainMenu", u"Maintenance", None))
        self.EnterBrewConfigButton.setText(QCoreApplication.translate("MainMenu", u"Start Brewing", None))
        self.EnterDeviceStatusScreen.setText(QCoreApplication.translate("MainMenu", u"Device Status", None))
    # retranslateUi

