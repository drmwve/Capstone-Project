import sys
from loguru import logger
from PySide2.QtWidgets import QApplication

from .ExecutionHandler import executionhandler
from .hardware.devicehandler import devicehandler
from .MainWindow import mainwindow, MainWindow
from .GUI.Styler import WindowStyler
from .utils import IS_RASPBERRY_PI


@logger.catch
def main():
    global mainwindow
    app = QApplication(sys.argv)
    logger.add(
        sys.stderr, format="{time} {level} {message}", filter="my_module", level="DEBUG"
    )
    mainwindow = MainWindow(executionhandler.loadedprocess)
    styler = WindowStyler()
    styler.styleWindows(app)
    devicehandler.signalemit.start(250)
    connections()
    mainwindow.show()
    logger.info("Opened main screen " + str(mainwindow))
    logger.info(f"Is Raspberry Pi: {IS_RASPBERRY_PI}")
    sys.exit(app.exec_())

def resumeprocess(resume: bool):
    if resume:
        executionhandler.startProcess(executionhandler.process)
        mainwindow.goToMenu(mainwindow.menus["processStatus"])
    else:
        executionhandler.deleteProcessFromDisk()

def connections():
    mainwindow.menus["brewConfig"].startBrewSignal.connect(executionhandler.startBrewProcess)
    mainwindow.resumeprocesssignal.connect(resumeprocess)

    mainwindow.menus["processStatus"].stopProcessRequest.connect(executionhandler.stopProcess)
    mainwindow.menus["processStatus"].nextStepRequest.connect(executionhandler.advanceStep)
    mainwindow.menus["processStatus"].manualOverrideRequest.connect(executionhandler.assumemanualcontrol)

    mainwindow.menus["cleaningScreen"].startCleaningSignal.connect(executionhandler.startCleaningProcess)
    mainwindow.menus["cleaningScreen"].flushSystemSignal.connect(executionhandler.startFlushProcess)
    mainwindow.switchedscreensignal.connect(switchedscreen)

    executionhandler.stepstarted.connect(mainwindow.menus["processStatus"].updateLabel)
    executionhandler.processstarted.connect(mainwindow.menus["processStatus"].startUpdateTimer)
    executionhandler.processstopped.connect(mainwindow.menus["processStatus"].resetProgressScreen)
    executionhandler.processpaused.connect(mainwindow.menus["processStatus"].updateTimer.stop)
    executionhandler.processresumed.connect(mainwindow.menus["processStatus"].updateTimer.start)
    executionhandler.processcomplete.connect(mainwindow.menus["processStatus"].processComplete)
    executionhandler.remainingtimesignal.connect(mainwindow.menus["processStatus"].updateremainingtime)

    executionhandler.processstarted.connect(mainwindow.menus["deviceStatus"].hideMainMenu)
    executionhandler.processstopped.connect(mainwindow.menus["deviceStatus"].hideProcessStatus)
    executionhandler.processcomplete.connect(mainwindow.menus["deviceStatus"].hideProcessStatus)

def switchedscreen(menu: str):
    if menu == "deviceStatus":
        logger.debug("Connecting status screen update")
        devicehandler.signalState.connect(mainwindow.menus["deviceStatus"].updateState)
    else:
        try:
            devicehandler.signalState.disconnect(mainwindow.menus["deviceStatus"].updateState)
            logger.debug("Disconnecting status screen update")
        except:
            pass