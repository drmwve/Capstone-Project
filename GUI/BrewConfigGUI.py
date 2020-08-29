from PySide2 import QtCore, QtGui, QtWidgets





class Ui_BrewConfigWindow(object):
    def setupUi(self, BrewConfigWindow):
        self.centralwidget = QtWidgets.QWidget(BrewConfigWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GUILayout = QtWidgets.QGridLayout(BrewConfigWindow)
        self.GUILayout.setObjectName("GUILayout")

        ## Font Settings
        font = QtGui.QFont()
        font.setPointSize(12)

        ## Mash Tun Temperature ##
        ## Layout
        self.MashTempLayout = QtWidgets.QGridLayout()
        self.MashTempLayout.setContentsMargins(-1, 0, -1, -1)
        self.MashTempLayout.setObjectName("MashTempLayout")
        ## Text label
        self.MashTempLabel = QtWidgets.QLabel(BrewConfigWindow)
        self.MashTempLabel.setFont(font)
        self.MashTempLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.MashTempLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.MashTempLabel.setObjectName("MashTempLabel")
        self.MashTempLayout.addWidget(self.MashTempLabel, 0, 1, 1, 1)
        self.MashTempLabel.setText("Mash Temperature (°F)")
        ## Increase button
        self.MashTempIncrease = QtWidgets.QPushButton(BrewConfigWindow)
        self.MashTempIncrease.setFont(font)
        self.MashTempIncrease.setObjectName("MashTempIncrease")
        self.MashTempLayout.addWidget(self.MashTempIncrease, 1, 2, 1, 1)
        self.MashTempIncrease.setText("+")
        ## Decrease button
        self.MashTempDecrease = QtWidgets.QPushButton(BrewConfigWindow)
        self.MashTempDecrease.setFont(font)
        self.MashTempDecrease.setObjectName("MashTempDecrease")
        self.MashTempLayout.addWidget(self.MashTempDecrease, 1, 0, 1, 1)
        self.MashTempDecrease.setText("-")
        ## Text entry field
        self.MashTempEntry = QtWidgets.QLineEdit(BrewConfigWindow)
        self.MashTempEntry.setFont(font)
        self.MashTempEntry.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.MashTempEntry.setAutoFillBackground(False)
        self.MashTempEntry.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.MashTempEntry.setMaxLength(3)
        self.MashTempEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.MashTempEntry.setReadOnly(True)
        self.MashTempEntry.setClearButtonEnabled(False)
        self.MashTempEntry.setObjectName("MashTempEntry")
        self.MashTempLayout.addWidget(self.MashTempEntry, 1, 1, 1, 1)
        ## Add to main layout
        self.GUILayout.addLayout(self.MashTempLayout, 0, 0, 1, 1)

        ## Hop Cartridge Quantity Selection ##
        ## Layout
        self.HopCartridgeSelectLayout = QtWidgets.QGridLayout()
        self.HopCartridgeSelectLayout.setObjectName("HopCartridgeSelectLayout")
        ## Text entry field
        self.HopCartridgeSelectEntry = QtWidgets.QLineEdit(BrewConfigWindow)
        self.HopCartridgeSelectEntry.setFont(font)
        self.HopCartridgeSelectEntry.setMaxLength(1)
        self.HopCartridgeSelectEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.HopCartridgeSelectEntry.setReadOnly(True)
        self.HopCartridgeSelectEntry.setObjectName("HopCartridgeSelectEntry")
        self.HopCartridgeSelectLayout.addWidget(self.HopCartridgeSelectEntry, 1, 1, 1, 1)
        ## Decrease button
        self.HopCartridgeSelectDecrease = QtWidgets.QPushButton(BrewConfigWindow)
        self.HopCartridgeSelectDecrease.setFont(font)
        self.HopCartridgeSelectDecrease.setObjectName("HopCartridgeSelectDecrease")
        self.HopCartridgeSelectLayout.addWidget(self.HopCartridgeSelectDecrease, 1, 0, 1, 1)
        self.HopCartridgeSelectDecrease.setText("-")
        ## Increase button
        self.HopCartridgeSelectIncrease = QtWidgets.QPushButton(BrewConfigWindow)
        self.HopCartridgeSelectIncrease.setFont(font)
        self.HopCartridgeSelectIncrease.setObjectName("HopCartridgeSelectIncrease")
        self.HopCartridgeSelectLayout.addWidget(self.HopCartridgeSelectIncrease, 1, 2, 1, 1)
        self.HopCartridgeSelectIncrease.setText( "+")
        ## Text label
        self.HopCartridgeSelectLabel = QtWidgets.QLabel(BrewConfigWindow)
        self.HopCartridgeSelectLabel.setFont(font)
        self.HopCartridgeSelectLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.HopCartridgeSelectLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.HopCartridgeSelectLabel.setObjectName("HopCartridgeSelectLabel")
        self.HopCartridgeSelectLayout.addWidget(self.HopCartridgeSelectLabel, 0, 1, 1, 1)
        self.HopCartridgeSelectLabel.setText("Number of hop cartridges")
        ## Add to main layout
        self.GUILayout.addLayout(self.HopCartridgeSelectLayout, 0, 1, 1, 1)

        ## Hop Cartridge Timing ##
        ## Layout
        self.HopTimingLayout = QtWidgets.QGridLayout()
        self.HopTimingLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.HopTimingLayout.setContentsMargins(-1, 40, -1, 0)
        self.HopTimingLayout.setVerticalSpacing(20)
        self.HopTimingLayout.setObjectName("HopTimingLayout")
        ## Text label
        self.HopLabel = QtWidgets.QLabel(BrewConfigWindow)
        self.HopLabel.setFont(font)
        self.HopLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.HopLabel.setObjectName("HopLabel")
        self.HopTimingLayout.addWidget(self.HopLabel, 0, 2, 1, 1)
        self.HopLabel.setText("Hop timing (minutes)")
        ## Add to main layout
        self.GUILayout.addLayout(self.HopTimingLayout, 2, 0, 1, 2)

        ## Hop 1 Settings ##
        ## Text label
        self.Hop1Label = QtWidgets.QLabel(BrewConfigWindow)
        self.Hop1Label.setFont(font)
        self.Hop1Label.setObjectName("Hop1Label")
        self.HopTimingLayout.addWidget(self.Hop1Label, 1, 0, 1, 1)
        self.Hop1Label.setText("Hop #1")
        self.Hop1Label.setMinimumSize(0, 30)
        ## Text entry field
        self.Hop1Entry = QtWidgets.QLineEdit(BrewConfigWindow)
        self.Hop1Entry.setFont(font)
        self.Hop1Entry.setMaxLength(2)
        self.Hop1Entry.setAlignment(QtCore.Qt.AlignCenter)
        self.Hop1Entry.setReadOnly(True)
        self.Hop1Entry.setObjectName("Hop1Entry")
        self.HopTimingLayout.addWidget(self.Hop1Entry, 1, 2, 1, 1)
        self.Hop1Entry.setMinimumSize(0, 30)
        ## Increase button
        self.Hop1Increase = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop1Increase.setFont(font)
        self.Hop1Increase.setObjectName("Hop1Increase")
        self.HopTimingLayout.addWidget(self.Hop1Increase, 1, 3, 1, 1)
        self.Hop1Increase.setText("+")
        self.Hop1Increase.setMinimumSize(0, 30)
        ## Decrease button
        self.Hop1Decrease = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop1Decrease.setFont(font)
        self.Hop1Decrease.setObjectName("Hop1Decrease")
        self.HopTimingLayout.addWidget(self.Hop1Decrease, 1, 1, 1, 1)
        self.Hop1Decrease.setText("-")
        self.Hop1Decrease.setMinimumSize(0, 30)

        ## Hop 2 Settings ##
        ## Text label
        self.Hop2Label = QtWidgets.QLabel(BrewConfigWindow)
        self.Hop2Label.setFont(font)
        self.Hop2Label.setObjectName("Hop2Label")
        self.HopTimingLayout.addWidget(self.Hop2Label, 2, 0, 1, 1)
        self.Hop2Label.setText("Hop #2")
        self.Hop2Label.setMinimumSize(0, 30)
        ## Text entry field
        self.Hop2Entry = QtWidgets.QLineEdit(BrewConfigWindow)
        self.Hop2Entry.setFont(font)
        self.Hop2Entry.setMaxLength(2)
        self.Hop2Entry.setAlignment(QtCore.Qt.AlignCenter)
        self.Hop2Entry.setReadOnly(True)
        self.Hop2Entry.setObjectName("Hop2Entry")
        self.HopTimingLayout.addWidget(self.Hop2Entry, 2, 2, 1, 1)
        self.Hop2Entry.setMinimumSize(0, 30)
        ## Increase button
        self.Hop2Increase = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop2Increase.setFont(font)
        self.Hop2Increase.setObjectName("Hop2Increase")
        self.HopTimingLayout.addWidget(self.Hop2Increase, 2, 3, 1, 1)
        self.Hop2Increase.setText("+")
        self.Hop2Increase.setMinimumSize(0, 30)
        ## Decrease button
        self.Hop2Decrease = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop2Decrease.setFont(font)
        self.Hop2Decrease.setObjectName("Hop2Decrease")
        self.HopTimingLayout.addWidget(self.Hop2Decrease, 2, 1, 1, 1)
        self.Hop2Decrease.setText("-")
        self.Hop2Decrease.setMinimumSize(0, 30)

        ## Hop 3 Settings ##
        ## Text label
        self.Hop3Label = QtWidgets.QLabel(BrewConfigWindow)
        self.Hop3Label.setFont(font)
        self.Hop3Label.setObjectName("Hop3Label")
        self.HopTimingLayout.addWidget(self.Hop3Label, 3, 0, 1, 1)
        self.Hop3Label.setText("Hop #3")
        self.Hop3Label.setMinimumSize(0, 30)
        ## Text entry field
        self.Hop3Entry = QtWidgets.QLineEdit(BrewConfigWindow)
        self.Hop3Entry.setFont(font)
        self.Hop3Entry.setMaxLength(2)
        self.Hop3Entry.setAlignment(QtCore.Qt.AlignCenter)
        self.Hop3Entry.setReadOnly(True)
        self.Hop3Entry.setObjectName("Hop3Entry")
        self.HopTimingLayout.addWidget(self.Hop3Entry, 3, 2, 1, 1)
        self.Hop3Entry.setMinimumSize(0, 30)
        ## Increase button
        self.Hop3Increase = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop3Increase.setFont(font)
        self.Hop3Increase.setObjectName("Hop3Increase")
        self.HopTimingLayout.addWidget(self.Hop3Increase, 3, 3, 1, 1)
        self.Hop3Increase.setText("+")
        self.Hop3Increase.setMinimumSize(0, 30)
        ## Decrease button
        self.Hop3Decrease = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop3Decrease.setFont(font)
        self.Hop3Decrease.setObjectName("Hop3Decrease")
        self.HopTimingLayout.addWidget(self.Hop3Decrease, 3, 1, 1, 1)
        self.Hop3Decrease.setText("-")
        self.Hop3Decrease.setMinimumSize(0, 30)

        ## Hop 4 Settings ##
        ## Text label
        self.Hop4Label = QtWidgets.QLabel(BrewConfigWindow)
        self.Hop4Label.setFont(font)
        self.Hop4Label.setObjectName("Hop4Label")
        self.HopTimingLayout.addWidget(self.Hop4Label, 4, 0, 1, 1)
        self.Hop4Label.setText("Hop #4")
        self.Hop4Label.setMinimumSize(0, 30)
        ## Text entry field
        self.Hop4Entry = QtWidgets.QLineEdit(BrewConfigWindow)
        self.Hop4Entry.setFont(font)
        self.Hop4Entry.setMaxLength(2)
        self.Hop4Entry.setAlignment(QtCore.Qt.AlignCenter)
        self.Hop4Entry.setReadOnly(True)
        self.Hop4Entry.setObjectName("Hop4Entry")
        self.HopTimingLayout.addWidget(self.Hop4Entry, 4, 2, 1, 1)
        self.Hop4Entry.setMinimumSize(0, 30)
        ## Increase button
        self.Hop4Increase = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop4Increase.setFont(font)
        self.Hop4Increase.setObjectName("Hop4Increase")
        self.HopTimingLayout.addWidget(self.Hop4Increase, 4, 3, 1, 1)
        self.Hop4Increase.setText("+")
        self.Hop4Increase.setMinimumSize(0, 30)
        ## Decrease button
        self.Hop4Decrease = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop4Decrease.setFont(font)
        self.Hop4Decrease.setObjectName("Hop4Decrease")
        self.HopTimingLayout.addWidget(self.Hop4Decrease, 4, 1, 1, 1)
        self.Hop4Decrease.setText("-")
        self.Hop4Decrease.setMinimumSize(0, 30)

        ## Hop 5 Settings ##
        ## Text label
        self.Hop5Label = QtWidgets.QLabel(BrewConfigWindow)
        self.Hop5Label.setFont(font)
        self.Hop5Label.setObjectName("Hop5Label")
        self.HopTimingLayout.addWidget(self.Hop5Label, 5, 0, 1, 1)
        self.Hop5Label.setText("Hop #5")
        self.Hop5Label.setMinimumSize(0, 30)
        ## Text entry field
        self.Hop5Entry = QtWidgets.QLineEdit(BrewConfigWindow)
        self.Hop5Entry.setFont(font)
        self.Hop5Entry.setMaxLength(2)
        self.Hop5Entry.setAlignment(QtCore.Qt.AlignCenter)
        self.Hop5Entry.setReadOnly(True)
        self.Hop5Entry.setObjectName("Hop5Entry")
        self.HopTimingLayout.addWidget(self.Hop5Entry, 5, 2, 1, 1)
        self.Hop5Entry.setMinimumSize(0, 30)
        ## Increase button
        self.Hop5Increase = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop5Increase.setFont(font)
        self.Hop5Increase.setObjectName("Hop5Increase")
        self.HopTimingLayout.addWidget(self.Hop5Increase, 5, 3, 1, 1)
        self.Hop5Increase.setText("+")
        self.Hop5Increase.setMinimumSize(0, 30)
        ## Decrease button
        self.Hop5Decrease = QtWidgets.QPushButton(BrewConfigWindow)
        self.Hop5Decrease.setFont(font)
        self.Hop5Decrease.setObjectName("Hop5Decrease")
        self.HopTimingLayout.addWidget(self.Hop5Decrease, 5, 1, 1, 1)
        self.Hop5Decrease.setText("-")
        self.Hop5Decrease.setMinimumSize(0, 30)

        ## Navigation button settings ##
        ## Layout
        self.NavigationButtonLayout = QtWidgets.QGridLayout()
        self.NavigationButtonLayout.setContentsMargins(150, 100, 150, 100)
        self.NavigationButtonLayout.setVerticalSpacing(80)
        self.NavigationButtonLayout.setObjectName("NavigationButtonLayout")
        ## Start Brewing Button
        self.StartBrewButton = QtWidgets.QPushButton(BrewConfigWindow)
        self.StartBrewButton.setMinimumSize(QtCore.QSize(0, 50))
        self.StartBrewButton.setMaximumSize(QtCore.QSize(1000, 50))
        self.StartBrewButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.StartBrewButton.setObjectName("StartBrewButton")
        self.NavigationButtonLayout.addWidget(self.StartBrewButton, 0, 0, 1, 1)
        self.GUILayout.addLayout(self.NavigationButtonLayout, 3, 0, 1, 2)
        self.StartBrewButton.setFont(font)
        self.StartBrewButton.setText("Start brewing!")
        ## Return to main menu button
        self.BackButton = QtWidgets.QPushButton(BrewConfigWindow)
        self.BackButton.setMinimumSize(QtCore.QSize(0, 50))
        self.BackButton.setObjectName("BackButton")
        self.BackButton.setFont(font)
        self.NavigationButtonLayout.addWidget(self.BackButton, 1, 0, 1, 1)
        self.BackButton.setText("Back to Main Menu")
