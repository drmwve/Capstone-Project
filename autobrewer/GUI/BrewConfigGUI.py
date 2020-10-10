# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BrewConfig.ui'
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


class Ui_BrewConfigWindow(object):
    def setupUi(self, BrewConfigWindow):
        if not BrewConfigWindow.objectName():
            BrewConfigWindow.setObjectName(u"BrewConfigWindow")
        BrewConfigWindow.resize(1024, 600)
        BrewConfigWindow.setMinimumSize(QSize(1024, 0))
        BrewConfigWindow.setMaximumSize(QSize(1024, 600))
        self.verticalLayout = QVBoxLayout(BrewConfigWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.HopCartridgeSelectLayout = QGridLayout()
        self.HopCartridgeSelectLayout.setObjectName(u"HopCartridgeSelectLayout")
        self.HopCartridgeSelectEntry = QLineEdit(BrewConfigWindow)
        self.HopCartridgeSelectEntry.setObjectName(u"HopCartridgeSelectEntry")
        self.HopCartridgeSelectEntry.setMinimumSize(QSize(0, 30))
        self.HopCartridgeSelectEntry.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.HopCartridgeSelectEntry.setFont(font)
        self.HopCartridgeSelectEntry.setMaxLength(1)
        self.HopCartridgeSelectEntry.setAlignment(Qt.AlignCenter)
        self.HopCartridgeSelectEntry.setReadOnly(True)

        self.HopCartridgeSelectLayout.addWidget(self.HopCartridgeSelectEntry, 1, 1, 1, 1)

        self.HopCartridgeSelectDecrease = QPushButton(BrewConfigWindow)
        self.HopCartridgeSelectDecrease.setObjectName(u"HopCartridgeSelectDecrease")
        self.HopCartridgeSelectDecrease.setMinimumSize(QSize(0, 30))
        self.HopCartridgeSelectDecrease.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.HopCartridgeSelectDecrease.setFont(font1)

        self.HopCartridgeSelectLayout.addWidget(self.HopCartridgeSelectDecrease, 1, 0, 1, 1)

        self.HopCartridgeSelectIncrease = QPushButton(BrewConfigWindow)
        self.HopCartridgeSelectIncrease.setObjectName(u"HopCartridgeSelectIncrease")
        self.HopCartridgeSelectIncrease.setMinimumSize(QSize(0, 30))
        self.HopCartridgeSelectIncrease.setMaximumSize(QSize(16777215, 30))
        self.HopCartridgeSelectIncrease.setFont(font1)

        self.HopCartridgeSelectLayout.addWidget(self.HopCartridgeSelectIncrease, 1, 2, 1, 1)

        self.HopCartridgeSelectLabel = QLabel(BrewConfigWindow)
        self.HopCartridgeSelectLabel.setObjectName(u"HopCartridgeSelectLabel")
        self.HopCartridgeSelectLabel.setMaximumSize(QSize(16777215, 20))
        self.HopCartridgeSelectLabel.setFont(font1)
        self.HopCartridgeSelectLabel.setLayoutDirection(Qt.LeftToRight)
        self.HopCartridgeSelectLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.HopCartridgeSelectLayout.addWidget(self.HopCartridgeSelectLabel, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.HopCartridgeSelectLayout, 0, 1, 1, 1)

        self.MashTempLayout = QGridLayout()
        self.MashTempLayout.setObjectName(u"MashTempLayout")
        self.MashTempLayout.setContentsMargins(-1, 0, -1, -1)
        self.MashTempIncrease = QPushButton(BrewConfigWindow)
        self.MashTempIncrease.setObjectName(u"MashTempIncrease")
        self.MashTempIncrease.setMinimumSize(QSize(0, 30))
        self.MashTempIncrease.setMaximumSize(QSize(16777215, 30))
        self.MashTempIncrease.setFont(font1)

        self.MashTempLayout.addWidget(self.MashTempIncrease, 1, 2, 1, 1)

        self.MashTempLabel = QLabel(BrewConfigWindow)
        self.MashTempLabel.setObjectName(u"MashTempLabel")
        self.MashTempLabel.setMaximumSize(QSize(16777215, 20))
        self.MashTempLabel.setFont(font1)
        self.MashTempLabel.setLayoutDirection(Qt.LeftToRight)
        self.MashTempLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.MashTempLayout.addWidget(self.MashTempLabel, 0, 1, 1, 1)

        self.MashTempDecrease = QPushButton(BrewConfigWindow)
        self.MashTempDecrease.setObjectName(u"MashTempDecrease")
        self.MashTempDecrease.setMinimumSize(QSize(0, 30))
        self.MashTempDecrease.setMaximumSize(QSize(16777215, 30))
        self.MashTempDecrease.setFont(font1)

        self.MashTempLayout.addWidget(self.MashTempDecrease, 1, 0, 1, 1)

        self.MashTempEntry = QLineEdit(BrewConfigWindow)
        self.MashTempEntry.setObjectName(u"MashTempEntry")
        self.MashTempEntry.setMinimumSize(QSize(0, 30))
        self.MashTempEntry.setMaximumSize(QSize(16777215, 30))
        self.MashTempEntry.setFont(font)
        self.MashTempEntry.setCursor(QCursor(Qt.IBeamCursor))
        self.MashTempEntry.setAutoFillBackground(False)
        self.MashTempEntry.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.MashTempEntry.setMaxLength(3)
        self.MashTempEntry.setAlignment(Qt.AlignCenter)
        self.MashTempEntry.setReadOnly(True)
        self.MashTempEntry.setClearButtonEnabled(False)

        self.MashTempLayout.addWidget(self.MashTempEntry, 1, 1, 1, 1)


        self.gridLayout.addLayout(self.MashTempLayout, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.HopTimingLayout = QGridLayout()
        self.HopTimingLayout.setObjectName(u"HopTimingLayout")
        self.HopTimingLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.HopTimingLayout.setVerticalSpacing(10)
        self.HopTimingLayout.setContentsMargins(-1, 0, -1, -1)
        self.Hop4Entry = QLineEdit(BrewConfigWindow)
        self.Hop4Entry.setObjectName(u"Hop4Entry")
        self.Hop4Entry.setMinimumSize(QSize(0, 30))
        self.Hop4Entry.setMaximumSize(QSize(16777215, 30))
        self.Hop4Entry.setFont(font)
        self.Hop4Entry.setMaxLength(2)
        self.Hop4Entry.setAlignment(Qt.AlignCenter)
        self.Hop4Entry.setReadOnly(True)

        self.HopTimingLayout.addWidget(self.Hop4Entry, 4, 2, 1, 1)

        self.Hop1Entry = QLineEdit(BrewConfigWindow)
        self.Hop1Entry.setObjectName(u"Hop1Entry")
        self.Hop1Entry.setMinimumSize(QSize(0, 30))
        self.Hop1Entry.setMaximumSize(QSize(16777215, 30))
        self.Hop1Entry.setFont(font)
        self.Hop1Entry.setMaxLength(2)
        self.Hop1Entry.setAlignment(Qt.AlignCenter)
        self.Hop1Entry.setReadOnly(True)

        self.HopTimingLayout.addWidget(self.Hop1Entry, 1, 2, 1, 1)

        self.Hop5Entry = QLineEdit(BrewConfigWindow)
        self.Hop5Entry.setObjectName(u"Hop5Entry")
        self.Hop5Entry.setMinimumSize(QSize(0, 30))
        self.Hop5Entry.setMaximumSize(QSize(16777215, 30))
        self.Hop5Entry.setFont(font)
        self.Hop5Entry.setMaxLength(2)
        self.Hop5Entry.setAlignment(Qt.AlignCenter)
        self.Hop5Entry.setReadOnly(True)

        self.HopTimingLayout.addWidget(self.Hop5Entry, 5, 2, 1, 1)

        self.Hop3Decrease = QPushButton(BrewConfigWindow)
        self.Hop3Decrease.setObjectName(u"Hop3Decrease")
        self.Hop3Decrease.setMinimumSize(QSize(0, 30))
        self.Hop3Decrease.setMaximumSize(QSize(16777215, 30))
        self.Hop3Decrease.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop3Decrease, 3, 1, 1, 1)

        self.Hop3Increase = QPushButton(BrewConfigWindow)
        self.Hop3Increase.setObjectName(u"Hop3Increase")
        self.Hop3Increase.setMinimumSize(QSize(0, 30))
        self.Hop3Increase.setMaximumSize(QSize(16777215, 30))
        self.Hop3Increase.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop3Increase, 3, 3, 1, 1)

        self.Hop1Label = QLabel(BrewConfigWindow)
        self.Hop1Label.setObjectName(u"Hop1Label")
        self.Hop1Label.setMinimumSize(QSize(80, 30))
        self.Hop1Label.setMaximumSize(QSize(16777215, 30))
        self.Hop1Label.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop1Label, 1, 0, 1, 1)

        self.Hop5Increase = QPushButton(BrewConfigWindow)
        self.Hop5Increase.setObjectName(u"Hop5Increase")
        self.Hop5Increase.setMinimumSize(QSize(0, 30))
        self.Hop5Increase.setMaximumSize(QSize(16777215, 30))
        self.Hop5Increase.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop5Increase, 5, 3, 1, 1)

        self.Hop3Entry = QLineEdit(BrewConfigWindow)
        self.Hop3Entry.setObjectName(u"Hop3Entry")
        self.Hop3Entry.setMinimumSize(QSize(0, 30))
        self.Hop3Entry.setMaximumSize(QSize(16777215, 30))
        self.Hop3Entry.setFont(font)
        self.Hop3Entry.setMaxLength(2)
        self.Hop3Entry.setAlignment(Qt.AlignCenter)
        self.Hop3Entry.setReadOnly(True)

        self.HopTimingLayout.addWidget(self.Hop3Entry, 3, 2, 1, 1)

        self.Hop4Decrease = QPushButton(BrewConfigWindow)
        self.Hop4Decrease.setObjectName(u"Hop4Decrease")
        self.Hop4Decrease.setMinimumSize(QSize(0, 30))
        self.Hop4Decrease.setMaximumSize(QSize(16777215, 30))
        self.Hop4Decrease.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop4Decrease, 4, 1, 1, 1)

        self.Hop2Entry = QLineEdit(BrewConfigWindow)
        self.Hop2Entry.setObjectName(u"Hop2Entry")
        self.Hop2Entry.setMinimumSize(QSize(0, 30))
        self.Hop2Entry.setMaximumSize(QSize(16777215, 30))
        self.Hop2Entry.setFont(font)
        self.Hop2Entry.setMaxLength(2)
        self.Hop2Entry.setAlignment(Qt.AlignCenter)
        self.Hop2Entry.setReadOnly(True)

        self.HopTimingLayout.addWidget(self.Hop2Entry, 2, 2, 1, 1)

        self.Hop4Increase = QPushButton(BrewConfigWindow)
        self.Hop4Increase.setObjectName(u"Hop4Increase")
        self.Hop4Increase.setMinimumSize(QSize(0, 30))
        self.Hop4Increase.setMaximumSize(QSize(16777215, 30))
        self.Hop4Increase.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop4Increase, 4, 3, 1, 1)

        self.Hop2Decrease = QPushButton(BrewConfigWindow)
        self.Hop2Decrease.setObjectName(u"Hop2Decrease")
        self.Hop2Decrease.setMinimumSize(QSize(0, 30))
        self.Hop2Decrease.setMaximumSize(QSize(16777215, 30))
        self.Hop2Decrease.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop2Decrease, 2, 1, 1, 1)

        self.Hop5Decrease = QPushButton(BrewConfigWindow)
        self.Hop5Decrease.setObjectName(u"Hop5Decrease")
        self.Hop5Decrease.setMinimumSize(QSize(0, 30))
        self.Hop5Decrease.setMaximumSize(QSize(16777215, 30))
        self.Hop5Decrease.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop5Decrease, 5, 1, 1, 1)

        self.HopLabel = QLabel(BrewConfigWindow)
        self.HopLabel.setObjectName(u"HopLabel")
        self.HopLabel.setFont(font1)
        self.HopLabel.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.HopLabel.setMargin(0)

        self.HopTimingLayout.addWidget(self.HopLabel, 0, 2, 1, 1)

        self.Hop1Decrease = QPushButton(BrewConfigWindow)
        self.Hop1Decrease.setObjectName(u"Hop1Decrease")
        self.Hop1Decrease.setMinimumSize(QSize(0, 30))
        self.Hop1Decrease.setMaximumSize(QSize(16777215, 30))
        self.Hop1Decrease.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop1Decrease, 1, 1, 1, 1)

        self.Hop2Increase = QPushButton(BrewConfigWindow)
        self.Hop2Increase.setObjectName(u"Hop2Increase")
        self.Hop2Increase.setMinimumSize(QSize(0, 30))
        self.Hop2Increase.setMaximumSize(QSize(16777215, 30))
        self.Hop2Increase.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop2Increase, 2, 3, 1, 1)

        self.Hop1Increase = QPushButton(BrewConfigWindow)
        self.Hop1Increase.setObjectName(u"Hop1Increase")
        self.Hop1Increase.setMinimumSize(QSize(0, 30))
        self.Hop1Increase.setMaximumSize(QSize(16777215, 30))
        self.Hop1Increase.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop1Increase, 1, 3, 1, 1)

        self.Hop2Label = QLabel(BrewConfigWindow)
        self.Hop2Label.setObjectName(u"Hop2Label")
        self.Hop2Label.setMinimumSize(QSize(80, 30))
        self.Hop2Label.setMaximumSize(QSize(16777215, 30))
        self.Hop2Label.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop2Label, 2, 0, 1, 1)

        self.Hop4Label = QLabel(BrewConfigWindow)
        self.Hop4Label.setObjectName(u"Hop4Label")
        self.Hop4Label.setMinimumSize(QSize(80, 30))
        self.Hop4Label.setMaximumSize(QSize(16777215, 30))
        self.Hop4Label.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop4Label, 4, 0, 1, 1)

        self.Hop3Label = QLabel(BrewConfigWindow)
        self.Hop3Label.setObjectName(u"Hop3Label")
        self.Hop3Label.setMinimumSize(QSize(80, 30))
        self.Hop3Label.setMaximumSize(QSize(16777215, 30))
        self.Hop3Label.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop3Label, 3, 0, 1, 1)

        self.Hop5Label = QLabel(BrewConfigWindow)
        self.Hop5Label.setObjectName(u"Hop5Label")
        self.Hop5Label.setMinimumSize(QSize(80, 30))
        self.Hop5Label.setMaximumSize(QSize(16777215, 30))
        self.Hop5Label.setFont(font1)

        self.HopTimingLayout.addWidget(self.Hop5Label, 5, 0, 1, 1)


        self.verticalLayout.addLayout(self.HopTimingLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.BreweButtonLayout = QGridLayout()
        self.BreweButtonLayout.setObjectName(u"BreweButtonLayout")
        self.BreweButtonLayout.setVerticalSpacing(25)
        self.BreweButtonLayout.setContentsMargins(150, 30, 150, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(BrewConfigWindow)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.QBComboBox = QComboBox(BrewConfigWindow)
        self.QBComboBox.setObjectName(u"QBComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QBComboBox.sizePolicy().hasHeightForWidth())
        self.QBComboBox.setSizePolicy(sizePolicy)
        self.QBComboBox.setMinimumSize(QSize(0, 30))
        self.QBComboBox.setMaximumSize(QSize(10000, 16777215))

        self.verticalLayout_3.addWidget(self.QBComboBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.QBLoadButton = QPushButton(BrewConfigWindow)
        self.QBLoadButton.setObjectName(u"QBLoadButton")
        self.QBLoadButton.setFont(font1)
        self.QBLoadButton.setCheckable(False)
        self.QBLoadButton.setChecked(False)

        self.horizontalLayout_2.addWidget(self.QBLoadButton)

        self.QBDeleteButton = QPushButton(BrewConfigWindow)
        self.QBDeleteButton.setObjectName(u"QBDeleteButton")
        self.QBDeleteButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.QBDeleteButton)

        self.QBSaveButton = QPushButton(BrewConfigWindow)
        self.QBSaveButton.setObjectName(u"QBSaveButton")
        self.QBSaveButton.setFont(font1)
        self.QBSaveButton.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.QBSaveButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.BreweButtonLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.BackButton = QPushButton(BrewConfigWindow)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setMinimumSize(QSize(0, 50))
        self.BackButton.setFont(font1)

        self.BreweButtonLayout.addWidget(self.BackButton, 4, 0, 1, 1)

        self.StartBrewButton = QPushButton(BrewConfigWindow)
        self.StartBrewButton.setObjectName(u"StartBrewButton")
        self.StartBrewButton.setMinimumSize(QSize(0, 50))
        self.StartBrewButton.setMaximumSize(QSize(1000, 50))
        self.StartBrewButton.setFont(font1)
        self.StartBrewButton.setLayoutDirection(Qt.LeftToRight)
        self.StartBrewButton.setFlat(False)

        self.BreweButtonLayout.addWidget(self.StartBrewButton, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.BreweButtonLayout)


        self.retranslateUi(BrewConfigWindow)

        self.StartBrewButton.setDefault(False)


        QMetaObject.connectSlotsByName(BrewConfigWindow)
    # setupUi

    def retranslateUi(self, BrewConfigWindow):
        BrewConfigWindow.setWindowTitle(QCoreApplication.translate("BrewConfigWindow", u"Form", None))
        self.HopCartridgeSelectEntry.setText(QCoreApplication.translate("BrewConfigWindow", u"5", None))
        self.HopCartridgeSelectDecrease.setText(QCoreApplication.translate("BrewConfigWindow", u"-", None))
        self.HopCartridgeSelectIncrease.setText(QCoreApplication.translate("BrewConfigWindow", u"+", None))
        self.HopCartridgeSelectLabel.setText(QCoreApplication.translate("BrewConfigWindow", u"Number of hop cartridges", None))
        self.MashTempIncrease.setText(QCoreApplication.translate("BrewConfigWindow", u"+", None))
        self.MashTempLabel.setText(QCoreApplication.translate("BrewConfigWindow", u"Mash Temperature (\u00b0F)", None))
        self.MashTempDecrease.setText(QCoreApplication.translate("BrewConfigWindow", u"-", None))
        self.MashTempEntry.setText(QCoreApplication.translate("BrewConfigWindow", u"170", None))
        self.Hop4Entry.setText(QCoreApplication.translate("BrewConfigWindow", u"15", None))
        self.Hop1Entry.setText(QCoreApplication.translate("BrewConfigWindow", u"5", None))
        self.Hop5Entry.setText(QCoreApplication.translate("BrewConfigWindow", u"30", None))
        self.Hop3Decrease.setText(QCoreApplication.translate("BrewConfigWindow", u"-", None))
        self.Hop3Increase.setText(QCoreApplication.translate("BrewConfigWindow", u"+", None))
        self.Hop1Label.setText(QCoreApplication.translate("BrewConfigWindow", u"Hop #1", None))
        self.Hop5Increase.setText(QCoreApplication.translate("BrewConfigWindow", u"+", None))
        self.Hop3Entry.setText(QCoreApplication.translate("BrewConfigWindow", u"10", None))
        self.Hop4Decrease.setText(QCoreApplication.translate("BrewConfigWindow", u"-", None))
        self.Hop2Entry.setText(QCoreApplication.translate("BrewConfigWindow", u"5", None))
        self.Hop4Increase.setText(QCoreApplication.translate("BrewConfigWindow", u"+", None))
        self.Hop2Decrease.setText(QCoreApplication.translate("BrewConfigWindow", u"-", None))
        self.Hop5Decrease.setText(QCoreApplication.translate("BrewConfigWindow", u"-", None))
        self.HopLabel.setText(QCoreApplication.translate("BrewConfigWindow", u"Hop timing (minutes)", None))
        self.Hop1Decrease.setText(QCoreApplication.translate("BrewConfigWindow", u"-", None))
        self.Hop2Increase.setText(QCoreApplication.translate("BrewConfigWindow", u"+", None))
        self.Hop1Increase.setText(QCoreApplication.translate("BrewConfigWindow", u"+", None))
        self.Hop2Label.setText(QCoreApplication.translate("BrewConfigWindow", u"Hop #2", None))
        self.Hop4Label.setText(QCoreApplication.translate("BrewConfigWindow", u"Hop #4", None))
        self.Hop3Label.setText(QCoreApplication.translate("BrewConfigWindow", u"Hop #3", None))
        self.Hop5Label.setText(QCoreApplication.translate("BrewConfigWindow", u"Hop #5", None))
        self.label.setText(QCoreApplication.translate("BrewConfigWindow", u"Quick Brew", None))
        self.QBLoadButton.setText(QCoreApplication.translate("BrewConfigWindow", u"Load Quick Brew", None))
        self.QBDeleteButton.setText(QCoreApplication.translate("BrewConfigWindow", u"Delete Quick Brew", None))
        self.QBSaveButton.setText(QCoreApplication.translate("BrewConfigWindow", u"Save Quick Brew", None))
        self.BackButton.setText(QCoreApplication.translate("BrewConfigWindow", u"Main Menu", None))
        self.StartBrewButton.setText(QCoreApplication.translate("BrewConfigWindow", u"Start brewing!", None))
    # retranslateUi

