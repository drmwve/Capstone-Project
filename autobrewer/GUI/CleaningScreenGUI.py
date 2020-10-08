# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CleaningScreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CleaningScreen(object):
    def setupUi(self, CleaningScreen):
        if not CleaningScreen.objectName():
            CleaningScreen.setObjectName(u"CleaningScreen")
        CleaningScreen.resize(1024, 600)
        CleaningScreen.setMinimumSize(QSize(1024, 0))
        CleaningScreen.setMaximumSize(QSize(1024, 600))
        self.CleanScreenLayout = QGridLayout(CleaningScreen)
        self.CleanScreenLayout.setObjectName(u"CleanScreenLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.FlushSystemButton = QPushButton(CleaningScreen)
        self.FlushSystemButton.setObjectName(u"FlushSystemButton")
        self.FlushSystemButton.setMinimumSize(QSize(200, 0))
        self.FlushSystemButton.setMaximumSize(QSize(200, 60))
        font = QFont()
        font.setPointSize(12)
        self.FlushSystemButton.setFont(font)

        self.horizontalLayout.addWidget(self.FlushSystemButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.ReturnToMenuButton = QPushButton(CleaningScreen)
        self.ReturnToMenuButton.setObjectName(u"ReturnToMenuButton")
        self.ReturnToMenuButton.setMinimumSize(QSize(200, 0))
        self.ReturnToMenuButton.setMaximumSize(QSize(200, 60))
        self.ReturnToMenuButton.setFont(font)

        self.horizontalLayout.addWidget(self.ReturnToMenuButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.CleanScreenLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.LowerCleaningButtonsLayout = QGridLayout()
        self.LowerCleaningButtonsLayout.setObjectName(u"LowerCleaningButtonsLayout")
        self.StartCleaningButton = QPushButton(CleaningScreen)
        self.StartCleaningButton.setObjectName(u"StartCleaningButton")
        self.StartCleaningButton.setMaximumSize(QSize(250, 60))
        self.StartCleaningButton.setFont(font)
        self.StartCleaningButton.setAutoFillBackground(False)

        self.LowerCleaningButtonsLayout.addWidget(self.StartCleaningButton, 1, 0, 1, 1)


        self.CleanScreenLayout.addLayout(self.LowerCleaningButtonsLayout, 0, 0, 1, 1)


        self.retranslateUi(CleaningScreen)

        QMetaObject.connectSlotsByName(CleaningScreen)
    # setupUi

    def retranslateUi(self, CleaningScreen):
        CleaningScreen.setWindowTitle(QCoreApplication.translate("CleaningScreen", u"Form", None))
        self.FlushSystemButton.setText(QCoreApplication.translate("CleaningScreen", u"Flush System", None))
        self.ReturnToMenuButton.setText(QCoreApplication.translate("CleaningScreen", u"Main Menu", None))
        self.StartCleaningButton.setText(QCoreApplication.translate("CleaningScreen", u"Start Cleaning Cycle", None))
    # retranslateUi

