# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProcessStatus.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ProcessStatus(object):
    def setupUi(self, ProcessStatus):
        if not ProcessStatus.objectName():
            ProcessStatus.setObjectName(u"ProcessStatus")
        ProcessStatus.resize(1024, 600)
        ProcessStatus.setMinimumSize(QSize(1024, 0))
        ProcessStatus.setMaximumSize(QSize(1024, 600))
        self.gridLayout = QGridLayout(ProcessStatus)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LowerLayout = QGridLayout()
        self.LowerLayout.setObjectName(u"LowerLayout")
        self.NextStepButton = QPushButton(ProcessStatus)
        self.NextStepButton.setObjectName(u"NextStepButton")
        self.NextStepButton.setMaximumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(12)
        self.NextStepButton.setFont(font)

        self.LowerLayout.addWidget(self.NextStepButton, 1, 0, 1, 1)

        self.ManualControlButton = QPushButton(ProcessStatus)
        self.ManualControlButton.setObjectName(u"ManualControlButton")
        self.ManualControlButton.setMaximumSize(QSize(200, 60))
        self.ManualControlButton.setFont(font)

        self.LowerLayout.addWidget(self.ManualControlButton, 0, 0, 1, 1)

        self.StopProcessButton = QPushButton(ProcessStatus)
        self.StopProcessButton.setObjectName(u"StopProcessButton")
        self.StopProcessButton.setMaximumSize(QSize(200, 60))
        self.StopProcessButton.setFont(font)

        self.LowerLayout.addWidget(self.StopProcessButton, 0, 1, 1, 1)

        self.ReturnToMenuButton = QPushButton(ProcessStatus)
        self.ReturnToMenuButton.setObjectName(u"ReturnToMenuButton")
        self.ReturnToMenuButton.setMaximumSize(QSize(200, 60))
        self.ReturnToMenuButton.setFont(font)

        self.LowerLayout.addWidget(self.ReturnToMenuButton, 0, 2, 1, 1)


        self.gridLayout.addLayout(self.LowerLayout, 1, 0, 1, 1)

        self.UpperLayout = QGridLayout()
        self.UpperLayout.setObjectName(u"UpperLayout")
        self.CurrentTaskLabel = QLabel(ProcessStatus)
        self.CurrentTaskLabel.setObjectName(u"CurrentTaskLabel")
        self.CurrentTaskLabel.setMaximumSize(QSize(800, 40))
        self.CurrentTaskLabel.setFont(font)
        self.CurrentTaskLabel.setAlignment(Qt.AlignCenter)

        self.UpperLayout.addWidget(self.CurrentTaskLabel, 0, 0, 1, 1)

        self.CurrentTaskProgressBar = QProgressBar(ProcessStatus)
        self.CurrentTaskProgressBar.setObjectName(u"CurrentTaskProgressBar")
        self.CurrentTaskProgressBar.setMaximumSize(QSize(800, 16777215))
        self.CurrentTaskProgressBar.setValue(24)

        self.UpperLayout.addWidget(self.CurrentTaskProgressBar, 1, 0, 1, 1)

        self.ETALabel = QLabel(ProcessStatus)
        self.ETALabel.setObjectName(u"ETALabel")
        self.ETALabel.setMaximumSize(QSize(800, 20))
        self.ETALabel.setFont(font)
        self.ETALabel.setAlignment(Qt.AlignCenter)

        self.UpperLayout.addWidget(self.ETALabel, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.UpperLayout, 0, 0, 1, 1)


        self.retranslateUi(ProcessStatus)

        QMetaObject.connectSlotsByName(ProcessStatus)
    # setupUi

    def retranslateUi(self, ProcessStatus):
        ProcessStatus.setWindowTitle(QCoreApplication.translate("ProcessStatus", u"Form", None))
        self.NextStepButton.setText(QCoreApplication.translate("ProcessStatus", u"Next Step", None))
        self.ManualControlButton.setText(QCoreApplication.translate("ProcessStatus", u"Manual Control", None))
        self.StopProcessButton.setText(QCoreApplication.translate("ProcessStatus", u"Stop Process", None))
        self.ReturnToMenuButton.setText(QCoreApplication.translate("ProcessStatus", u"Main Menu", None))
        self.CurrentTaskLabel.setText(QCoreApplication.translate("ProcessStatus", u"What am I doing?", None))
        self.ETALabel.setText(QCoreApplication.translate("ProcessStatus", u"ETA: 84 Years", None))
    # retranslateUi

