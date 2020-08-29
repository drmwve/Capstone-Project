# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CleaningScreen.ui'
#
# Created by: PySide2 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_CleaningScreen(object):
    def setupUi(self, CleaningScreen):
        CleaningScreen.setObjectName("CleaningScreen")
        CleaningScreen.resize(1024, 600)
        CleaningScreen.setMinimumSize(QtCore.QSize(1024, 0))
        CleaningScreen.setMaximumSize(QtCore.QSize(1024, 600))
        self.CleanScreenLayout = QtWidgets.QGridLayout(CleaningScreen)
        self.CleanScreenLayout.setObjectName("CleanScreenLayout")
        self.LowerCleaningButtonsLayout = QtWidgets.QHBoxLayout()
        self.LowerCleaningButtonsLayout.setObjectName("LowerCleaningButtonsLayout")
        self.PauseResumeCleanButton = QtWidgets.QPushButton(CleaningScreen)
        self.PauseResumeCleanButton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PauseResumeCleanButton.setFont(font)
        self.PauseResumeCleanButton.setObjectName("PauseResumeCleanButton")
        self.LowerCleaningButtonsLayout.addWidget(self.PauseResumeCleanButton)
        self.AbortCleanButton = QtWidgets.QPushButton(CleaningScreen)
        self.AbortCleanButton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AbortCleanButton.setFont(font)
        self.AbortCleanButton.setObjectName("AbortCleanButton")
        self.LowerCleaningButtonsLayout.addWidget(self.AbortCleanButton)
        self.ReturnToMenuButton = QtWidgets.QPushButton(CleaningScreen)
        self.ReturnToMenuButton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ReturnToMenuButton.setFont(font)
        self.ReturnToMenuButton.setObjectName("ReturnToMenuButton")
        self.LowerCleaningButtonsLayout.addWidget(self.ReturnToMenuButton)
        self.CleanScreenLayout.addLayout(self.LowerCleaningButtonsLayout, 3, 0, 1, 1)
        self.CleaningStatusLayout = QtWidgets.QGridLayout()
        self.CleaningStatusLayout.setObjectName("CleaningStatusLayout")
        self.CurrentCleanTaskLabel = QtWidgets.QLabel(CleaningScreen)
        self.CurrentCleanTaskLabel.setMaximumSize(QtCore.QSize(800, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CurrentCleanTaskLabel.setFont(font)
        self.CurrentCleanTaskLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CurrentCleanTaskLabel.setObjectName("CurrentCleanTaskLabel")
        self.CleaningStatusLayout.addWidget(self.CurrentCleanTaskLabel, 0, 0, 1, 1)
        self.CleanETALabel = QtWidgets.QLabel(CleaningScreen)
        self.CleanETALabel.setMaximumSize(QtCore.QSize(800, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CleanETALabel.setFont(font)
        self.CleanETALabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CleanETALabel.setObjectName("CleanETALabel")
        self.CleaningStatusLayout.addWidget(self.CleanETALabel, 2, 0, 1, 1)
        self.CurrentCleanTaskProgressBar = QtWidgets.QProgressBar(CleaningScreen)
        self.CurrentCleanTaskProgressBar.setMaximumSize(QtCore.QSize(800, 16777215))
        self.CurrentCleanTaskProgressBar.setProperty("value", 24)
        self.CurrentCleanTaskProgressBar.setObjectName("CurrentCleanTaskProgressBar")
        self.CleaningStatusLayout.addWidget(self.CurrentCleanTaskProgressBar, 1, 0, 1, 1)
        self.CleanScreenLayout.addLayout(self.CleaningStatusLayout, 0, 0, 1, 1)
        self.StartCleaningButtonLayout = QtWidgets.QHBoxLayout()
        self.StartCleaningButtonLayout.setObjectName("StartCleaningButtonLayout")
        self.StartCleaningButton = QtWidgets.QPushButton(CleaningScreen)
        self.StartCleaningButton.setMaximumSize(QtCore.QSize(250, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.StartCleaningButton.setFont(font)
        self.StartCleaningButton.setAutoFillBackground(False)
        self.StartCleaningButton.setObjectName("pushButton")
        self.StartCleaningButtonLayout.addWidget(self.StartCleaningButton)
        self.CleanScreenLayout.addLayout(self.StartCleaningButtonLayout, 1, 0, 1, 1)

        self.retranslateUi(CleaningScreen)
        QtCore.QMetaObject.connectSlotsByName(CleaningScreen)

    def retranslateUi(self, CleaningScreen):
        _translate = QtCore.QCoreApplication.translate
        CleaningScreen.setWindowTitle(_translate("CleaningScreen", "Form"))
        self.PauseResumeCleanButton.setText(_translate("CleaningScreen", "Pause/Resume"))
        self.AbortCleanButton.setText(_translate("CleaningScreen", "Abort Cleaning"))
        self.ReturnToMenuButton.setText(_translate("CleaningScreen", "Main Menu"))
        self.CurrentCleanTaskLabel.setText(_translate("CleaningScreen", "What am I doing?"))
        self.CleanETALabel.setText(_translate("CleaningScreen", "ETA: 84 Years"))
        self.StartCleaningButton.setText(_translate("CleaningScreen", "Start Cleaning Cycle"))
