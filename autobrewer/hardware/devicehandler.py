from simple_pid import PID
from loguru import logger
from PySide2.QtCore import QObject, Signal, QTimer
try:
    import matplotlib.pyplot as plot
except:
    pass
from ..utils import IS_RASPBERRY_PI
if IS_RASPBERRY_PI:
    from w1thermsensor import W1ThermSensor

from .hardwarestate import HardwareState
from ..exceptions import ComponentControlError
from .pins import Pins


# To do: Implement hop servo and sensor code


class DeviceHandler(QObject, Pins):
    """Controls the components and provides checking of invalid states for safety, such as preventing the opening of a pump
    when there is no open ball valve path or running a heating element in an empty kettle.
    This class has many functions for controlling components in logical groups and individually.
    The functions start with the large group controls and break down into low-level private controls.

    NOTE: Because this class controls a single physical hardware system, it is implemented entirely using class methods.

    Attributes:
        emitState: Emits a signal with the current HardwareState
        getState: Returns the current HardwareState
        shutdown: Disables all heating elements and pumps and returns ball valves to de-energized position
        resetFlowControl: Disables all pumps and returns ball valves to de-energized position
        openValves*: Opens particular ball valve paths
        set*/open*/close*/enable*/disable*: Individual component control functions
    """


    HOP_SERVO_HOME = -1
    HOP_SERVO_POSITIONS = {-1: -150, 0: -90, 1: -30, 2: 30, 3: 90, 4: 150}
    KETTLE_NAMES_GIVEN_ID = {0: "HLT", 1: "MT", 2: "BK"}
    KETTLE_IDS_GIVEN_NAME = {"HLT": 0, "MT": 1, "BK": 2}
    HLT_HEATING_ELEMENTS = [0,2]
    BK_HEATING_ELEMENTS = [1,3]
    HEATING_ELEMENT_LEVEL_LIMIT = 1 #gallons

    hltpid = PID(5, 0.01, 0.1, setpoint=155, output_limits=(0, 100), sample_time=None)
    mtpid = PID(5, 0.01, 0.1, setpoint=155, output_limits=(0, 100), sample_time=None)
    bkpid = PID(5, 0.01, 0.1, setpoint=155, output_limits=(0, 100), sample_time=None)
    PIDS = [hltpid, mtpid, bkpid]

    signalState = Signal(HardwareState)
    hardwareState = HardwareState()
    heatingelementdisabled = False

    def __init__(self):
        self._connectPins()
        self._createValvePaths()
        self.signalemit = QTimer()
        self.signalemit.timeout.connect(self._updatestate)
        self.signalemit.start(500)

    def _createValvePaths(self):
        """Defines paths which must be open for a pump to run without forming a vacuum. The valvepaths variable is a
        dictionary of dictionaries, describing the indexes of the valves which must either be opened or closed for
        each path.

        To add paths, add them in the main valvepaths variable (both open and close must be defined, even if they're
        empty) and then add relevant path names to the pumpvalvepathmap tuple in the position of the index of the
        relevant pump
        """
        self.valvepaths = {
            "FillHLT": {"open": [0], "close": [5]},
            "HLTtoMT": {"open": [1], "close": [6]},
            "MTRecirc": {"open": [2, 6], "close": [7]},
            "MTtoBK": {"open": [2, 3, 7], "close": [8, 9]},
            "BKWhirl": {"open": [3, 4, 8], "close": [9]},
            "BKDrain": {"open": [4, 8, 9], "close": []},
        }
        self.pumpvalvepathmap = (
            ("FillHLT", "HLTtoMT", "MTRecirc"),
            ("MTtoBK", "BKWhirl", "BKDrain"),
        )

    def openValvePath(self, pathname: str):
        for valveindex in self.valvepaths[pathname]["open"]:
            self.openBallValve(valveindex)
        for valveindex in self.valvepaths[pathname]["close"]:
            self.closeBallValve(valveindex)

    def getState(self) -> HardwareState:
        return self.hardwareState

    def shutdown(self):
        logger.info("Shutting all system components off")
        self.disableAllPumps()
        self.closeAllBallValves()
        self.disableAllHeatingElements()

    def resetFlowControl(self):
        self.disableAllPumps()
        self.closeAllBallValves()
        logger.info("Shut down all liquid flow")

    def disableAllHeatingElements(self):
        logger.debug("Disabling all heating elements")
        for index, _ in enumerate(self.heatingElements):
            self.disableHeatingElement(index)

    def disableAllPumps(self):
        logger.debug("Disabling all pumps")
        for index, _ in enumerate(self.pumps):
            self.disablePump(index)

    def closeAllBallValves(self):
        logger.debug("Closing all ball valves")
        for index, _ in enumerate(self.ballValves):
            self.closeBallValve(index)

    def goToHopPosition(self, index: int):
        if index in DeviceHandler.HOP_SERVO_POSITIONS.keys():
            self.setHopServoPosition(DeviceHandler.HOP_SERVO_POSITIONS[index])
        else:
            raise ComponentControlError(f'Could not find hop servo position {index}')

    def setHopServoPosition(self, angle: int):
        if angle in range(-150,150):
            if IS_RASPBERRY_PI:
                self.servoconnection.goto(self.SERVO_ID, angle, speed=512, degrees=True)
            self.hardwareState.hopServo = angle
        else:
            raise ComponentControlError("Invalid servo angle selected")

    def openBallValve(self, index: int):
        self._setBallValveState(index, True)

    def closeBallValve(self, index: int):
        self._setBallValveState(index, False)

    def enablePump(self, index: int):
        self._setPumpState(index, True)

    def disablePump(self, index: int):
        self._setPumpState(index, False)

    def setTargetKettleTemp(self, kettleindex: int, target: int, disableothers:bool = True, autoenable:bool = True):
        """Sets the target temperature for a kettle's PID. This automatically enables the PID for that kettle unless
        directed otherwise"""
        if target not in range(100, 211):
            raise ComponentControlError("Cannot set a target temperature below 100 or above 211 degrees Fahrenheit")
            return
        else:
            if kettleindex in DeviceHandler.KETTLE_NAMES_GIVEN_ID.keys():
                kettlename = DeviceHandler.KETTLE_NAMES_GIVEN_ID[kettleindex]
                for index, name in DeviceHandler.KETTLE_NAMES_GIVEN_ID.items():
                    if disableothers and index != kettleindex:
                        self.setKettlePIDEnabled(kettleindex, False)
                logger.info(f'Set kettle {kettlename} target temperature to {target}')
                self.hltpid.setpoint = target
                self.hardwareState.kettletempsetpoints[kettleindex] = target
                if autoenable:
                    self.setKettlePIDEnabled(kettleindex, True)
            else:
                raise ComponentControlError("Could not find given kettle")

    def setKettlePIDEnabled(self, index: int, value: bool):
        """Allows you to enable or disable PID without changing the temperature. Good to use to pause steps"""
        if index not in DeviceHandler.KETTLE_NAMES_GIVEN_ID.keys():
            raise ComponentControlError("Could not find given kettle")
        else:
            self.hardwareState.kettlepidenabled[index] = value

    def enableHeatingElement(self, index: int):
        self._setHeatingElementValue(index, 1)

    def disableHeatingElement(self, index: int):
        self._setHeatingElementValue(index, 0)

    def setHeatingElementPWM(self, index: int, value: float):
        self._setHeatingElementValue(index, value)

    def _setBallValveState(self, index: int, state: bool):
        self.ballValves[index].value = state
        self.hardwareState.ballValves[index] = state
        logger.debug(f'Set ball valve {index} to {"On" if state else "Off"}')

    def _setPumpState(self, pumpindex: int, state: bool):
        # check if a valid path is open for either pump
        if (not state) or (state and self._pumpHasOpenPath(pumpindex)):
            self.pumps[pumpindex].value = state
            self.hardwareState.pumps[pumpindex] = state
            logger.debug(f'Set pump {pumpindex} to {"On" if state else "Off"}')
        # raise an error otherwise
        else:
            raise ComponentControlError(
                f"Cannot turn pump {pumpindex} on. There is no suitable ball valve path open"
            )

    def _pumpHasOpenPath(self, pumpindex: int) -> bool:
        pumphasopenpath = False
        for valvepath in self.pumpvalvepathmap[pumpindex]:
            pathopen = True
            for valveindex in self.valvepaths[valvepath]["open"]:
                if self.ballValves[valveindex].value != 1:
                    pathopen = False
            for valveindex in self.valvepaths[valvepath]["close"]:
                if self.ballValves[valveindex].value != 0:
                    pathopen = False
            if pathopen:
                pumphasopenpath = True
                break
        return pumphasopenpath

    def _updateheatingelementPID(self):
        self._readSensors()
        for kettleindex, kettlename in DeviceHandler.KETTLE_NAMES_GIVEN_ID.items():
            if self.hardwareState.kettlepidenabled[kettleindex] == True:
                if kettlename == "HLT" or kettleindex == "MT":
                    heatingelementindex = 0
                elif kettlename == "BK":
                    heatingelementindex = 1
                self._setHeatingElementValue(heatingelementindex, self.PIDS[kettleindex](self.hardwareState.temperatures[kettleindex]), calledmanually=False)
                lowbound = self.hardwareState.kettletempsetpoints[kettleindex] * 0.8
                if self.hardwareState.temperatures[kettleindex] < lowbound:
                    if kettlename == "HLT":
                        self._setHeatingElementValue(2, 1, True)
                    elif kettlename == "BK":
                        self._setHeatingElementValue(3, 1, True)

    def _setHeatingElementValue(self, index: int, value: float, calledmanually=True):
        disabled = False
        if index in DeviceHandler.HLT_HEATING_ELEMENTS:
            disabled = self.hardwareState.kettleheatingelementsdisabled[DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"]]
        elif index in DeviceHandler.BK_HEATING_ELEMENTS:
            disabled = self.hardwareState.kettleheatingelementsdisabled[DeviceHandler.KETTLE_IDS_GIVEN_NAME["BK"]]
        if not disabled:
            if calledmanually:
                if index in DeviceHandler.HLT_HEATING_ELEMENTS:
                    self.setKettlePIDEnabled(DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"], False)
                elif index in DeviceHandler.BK_HEATING_ELEMENTS:
                    self.setKettlePIDEnabled(DeviceHandler.KETTLE_IDS_GIVEN_NAME["BK"], False)
            self.heatingElements[index].value = value
            self.hardwareState.heatingElements[index] = value
            logger.debug(f"Set heating element {index} to {value}")
        else:
            logger.critical(f'Program is attempting to enable heating element {index} without sufficient liquid level')
            raise ComponentControlError(f'Program is attempting to enable heating element {index} without sufficient liquid level')
            self.shutdown()

    def _readSensors(self):
        # read the sensors and save the values here
        for i, _ in enumerate(self.hardwareState.temperatures):
            self.hardwareState.temperatures[i] = self._readtemperature(i)
            self.hardwareState.volumes[i] = self._readvolume(i)

    def _readTemperature(self, index: int):
        if IS_RASPBERRY_PI:
            temperature = self.tempsensors[index].get_temperature(W1ThermSensor.DEGREES_F)
        else:
            temperature = 70
        return temperature

    def _readvolume(self, index: int) -> float:
        """Reads the ADC for a particular kettle's pressure sensor and converts the pressure value into a volume
        in gallons"""
        if IS_RASPBERRY_PI:
            KETTLE_DIAMETER = 0.320675 # meters
            LIQUID_DENSITY = 997 # kg/m3
            GRAVITY = 9.81 #m/s^2
            PI = 3.142
            # pressure is in kPa
            pressurevoltage = self.adc.read_adc(index, gain=self.ADC_GAIN)
            pressurevalue = (pressurevoltage / self.ADC_VOLTAGE_SUPPLIED - 0.053) / 0.1533
            liquidheight = pressurevalue * 1000 / (LIQUID_DENSITY * GRAVITY)
            volume = PI * (KETTLE_DIAMETER/2)**2 * liquidheight #cubic meters
            volume *= 264.172 # gallons
        else:
            volume = 5
        return volume

    def _updatestate(self):
        self._readSensors()
        self.signalState.emit(self.hardwareState)
        self._updateheatingelementPID()
        for kettleindex, kettlename in DeviceHandler.KETTLE_NAMES_GIVEN_ID.items():
            if self.hardwareState.volumes[kettleindex] < DeviceHandler.HEATING_ELEMENT_LEVEL_LIMIT:
                self.hardwareState.kettleheatingelementsdisabled[kettleindex] = True
            else:
                self.hardwareState.kettleheatingelementsdisabled[kettleindex] = False

devicehandler = DeviceHandler()
