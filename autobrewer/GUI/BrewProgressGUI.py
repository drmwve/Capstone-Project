# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BrewProgress.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_BrewStatus(object):
    def setupUi(self, BrewStatus):
        BrewStatus.setObjectName("BrewStatus")
        BrewStatus.resize(1024, 600)
        BrewStatus.setMinimumSize(QtCore.QSize(1024, 0))
        BrewStatus.setMaximumSize(QtCore.QSize(1024, 600))
        self.gridLayout = QtWidgets.QGridLayout(BrewStatus)
        self.gridLayout.setObjectName("gridLayout")
        self.UpperLayout = QtWidgets.QGridLayout()
        self.UpperLayout.setObjectName("UpperLayout")
        self.CurrentTaskLabel = QtWidgets.QLabel(BrewStatus)
        self.CurrentTaskLabel.setMaximumSize(QtCore.QSize(800, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CurrentTaskLabel.setFont(font)
        self.CurrentTaskLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentTaskLabel.setObjectName("CurrentTaskLabel")
        self.UpperLayout.addWidget(self.CurrentTaskLabel, 0, 0, 1, 1)
        self.CurrentTaskProgressBar = QtWidgets.QProgressBar(BrewStatus)
        self.CurrentTaskProgressBar.setMaximumSize(QtCore.QSize(800, 16777215))
        self.CurrentTaskProgressBar.setProperty("value", 24)
        self.CurrentTaskProgressBar.setObjectName("CurrentTaskProgressBar")
        self.UpperLayout.addWidget(self.CurrentTaskProgressBar, 1, 0, 1, 1)
        self.ETALabel = QtWidgets.QLabel(BrewStatus)
        self.ETALabel.setMaximumSize(QtCore.QSize(800, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ETALabel.setFont(font)
        self.ETALabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ETALabel.setObjectName("ETALabel")
        self.UpperLayout.addWidget(self.ETALabel, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.UpperLayout, 0, 0, 1, 1)
        self.LowerLayout = QtWidgets.QHBoxLayout()
        self.LowerLayout.setObjectName("LowerLayout")
        self.PauseResumeButton = QtWidgets.QPushButton(BrewStatus)
        self.PauseResumeButton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PauseResumeButton.setFont(font)
        self.PauseResumeButton.setObjectName("PauseResumeButton")
        self.LowerLayout.addWidget(self.PauseResumeButton)
        self.AbortBrewButton = QtWidgets.QPushButton(BrewStatus)
        self.AbortBrewButton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AbortBrewButton.setFont(font)
        self.AbortBrewButton.setObjectName("AbortBrewButton")
        self.LowerLayout.addWidget(self.AbortBrewButton)
        self.ReturnToMenuButton = QtWidgets.QPushButton(BrewStatus)
        self.ReturnToMenuButton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ReturnToMenuButton.setFont(font)
        self.ReturnToMenuButton.setObjectName("ReturnToMenuButton")
        self.LowerLayout.addWidget(self.ReturnToMenuButton)
        self.gridLayout.addLayout(self.LowerLayout, 1, 0, 1, 1)

        self.retranslateUi(BrewStatus)
        QtCore.QMetaObject.connectSlotsByName(BrewStatus)

    def retranslateUi(self, BrewStatus):
        _translate = QtCore.QCoreApplication.translate
        BrewStatus.setWindowTitle(_translate("BrewStatus", "Form"))
        self.CurrentTaskLabel.setText(_translate("BrewStatus", "What am I doing?"))
        self.ETALabel.setText(_translate("BrewStatus", "ETA: 84 Years"))
        self.PauseResumeButton.setText(_translate("BrewStatus", "Pause/Resume"))
        self.AbortBrewButton.setText(_translate("BrewStatus", "Abort Brew"))
        self.ReturnToMenuButton.setText(_translate("BrewStatus", "Main Menu"))
