# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CleaningScreen.ui'
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


class Ui_CleaningScreen(object):
    def setupUi(self, CleaningScreen):
        if not CleaningScreen.objectName():
            CleaningScreen.setObjectName(u"CleaningScreen")
        CleaningScreen.resize(1024, 600)
        CleaningScreen.setMinimumSize(QSize(1024, 0))
        CleaningScreen.setMaximumSize(QSize(1024, 600))
        self.CleanScreenLayout = QGridLayout(CleaningScreen)
        self.CleanScreenLayout.setObjectName(u"CleanScreenLayout")
        self.LowerCleaningButtonsLayout = QGridLayout()
        self.LowerCleaningButtonsLayout.setObjectName(u"LowerCleaningButtonsLayout")
        self.FlushSystemButton = QPushButton(CleaningScreen)
        self.FlushSystemButton.setObjectName(u"FlushSystemButton")
        self.FlushSystemButton.setMinimumSize(QSize(200, 60))
        self.FlushSystemButton.setMaximumSize(QSize(800, 60))
        font = QFont()
        font.setPointSize(12)
        self.FlushSystemButton.setFont(font)

        self.LowerCleaningButtonsLayout.addWidget(self.FlushSystemButton, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LowerCleaningButtonsLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.StartCleaningButton = QPushButton(CleaningScreen)
        self.StartCleaningButton.setObjectName(u"StartCleaningButton")
        self.StartCleaningButton.setMinimumSize(QSize(0, 60))
        self.StartCleaningButton.setMaximumSize(QSize(800, 60))
        self.StartCleaningButton.setFont(font)
        self.StartCleaningButton.setAutoFillBackground(False)

        self.LowerCleaningButtonsLayout.addWidget(self.StartCleaningButton, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LowerCleaningButtonsLayout.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LowerCleaningButtonsLayout.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.ReturnToMenuButton = QPushButton(CleaningScreen)
        self.ReturnToMenuButton.setObjectName(u"ReturnToMenuButton")
        self.ReturnToMenuButton.setMinimumSize(QSize(200, 60))
        self.ReturnToMenuButton.setMaximumSize(QSize(800, 60))
        self.ReturnToMenuButton.setFont(font)

        self.LowerCleaningButtonsLayout.addWidget(self.ReturnToMenuButton, 5, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.LowerCleaningButtonsLayout.addItem(self.verticalSpacer_4, 2, 0, 1, 1)


        self.CleanScreenLayout.addLayout(self.LowerCleaningButtonsLayout, 0, 0, 1, 1)


        self.retranslateUi(CleaningScreen)

        QMetaObject.connectSlotsByName(CleaningScreen)
    # setupUi

    def retranslateUi(self, CleaningScreen):
        CleaningScreen.setWindowTitle(QCoreApplication.translate("CleaningScreen", u"Form", None))
        self.FlushSystemButton.setText(QCoreApplication.translate("CleaningScreen", u"Flush System", None))
        self.StartCleaningButton.setText(QCoreApplication.translate("CleaningScreen", u"Start Cleaning Cycle", None))
        self.ReturnToMenuButton.setText(QCoreApplication.translate("CleaningScreen", u"Main Menu", None))
    # retranslateUi

