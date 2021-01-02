from gpiozero import OutputDevice, GPIOPinInUse
from simple_pid import PID
from loguru import logger
from PySide2.QtCore import QObject, Signal, QTimer
from w1thermsensor import Unit
from ..utils import truncate
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
        disableAll: Disables all heating elements and pumps and returns ball valves to de-energized position
        resetFlowControl: Disables all pumps and returns ball valves to de-energized position
        openValves*: Opens particular ball valve paths
        set*/open*/close*/enable*/disable*: Individual component control functions
    """


    HOP_SERVO_HOME = -1
    HOP_SERVO_POSITIONS = {-1: -150, 0: -78, 1: -8, 2: 52, 3: 112, 4: 150}
    KETTLE_NAMES_GIVEN_ID = {0: "HLT", 1: "MT", 2: "BK"}
    KETTLE_IDS_GIVEN_NAME = {"HLT": 0, "MT": 1, "BK": 2}
    HLT_HEATING_ELEMENTS = [0,2]
    BK_HEATING_ELEMENTS = [1,3]
    HEATING_ELEMENTS = [HLT_HEATING_ELEMENTS,[None], BK_HEATING_ELEMENTS]
    KETTLE_MAX_VOLUME = 7.5 #gallons
    HEATING_ELEMENT_MIN_VOLUME = 1 #gallons
    INPUT_WATER_VALVE = 5
    PUMP_PWM_VALUE = 1

    hltpid = PID(40/100, 1/100, 3/100, setpoint=200, output_limits=(0, 1), sample_time=None)
    mtpid = PID(40/100, 1/100, 3/100, setpoint=155, output_limits=(0, 1), sample_time=None)
    bkpid = PID(40/100, 1/100, 3/100, setpoint=155, output_limits=(0, 1), sample_time=None)
    PIDS = [hltpid, mtpid, bkpid]

    signalState = Signal(HardwareState)
    hardwareState = HardwareState()

    def __init__(self):
        super().__init__()  # this calls all constructors up to Foo
        super(QObject, self).__init__()
        self._createValvePaths()
        self.signalemit = QTimer()
        self.signalemit.timeout.connect(self._updatestate)
        self.signalemit.start(500)
        self.temptimer = QTimer()
        self.temptimer.timeout.connect(self._readAllTemps)
        self.PIDtimer = QTimer()
        self.PIDtimer.timeout.connect(self._updateheatingelementPID)
        self.airPump = OutputDevice(Pins.airPumpGPIO)
        self.sensorindex = 0
        self._readAllTemps()
        self.volumeaverages = [[],[],[]]

    def _createValvePaths(self):
        """Defines paths which must be open for a pump to run without forming a vacuum. The valvepaths variable is a
        dictionary of dictionaries, describing the indexes of the valves which must either be opened or closed for
        each path.

        To add paths, add them in the main valvepaths variable and then add relevant path names to the pumpvalvepathmap
        tuple in the position of the index of the relevant pump
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

    ## MASTER CONTROLS ##

    def openValvePath(self, pathname: str):
        if "open" in self.valvepaths[pathname].keys():
            for valveindex in self.valvepaths[pathname]["open"]:
                self.openBallValve(valveindex)
        if "close" in self.valvepaths[pathname].keys():
            for valveindex in self.valvepaths[pathname]["close"]:
                self.closeBallValve(valveindex)

    def getState(self) -> HardwareState:
        return self.hardwareState

    def disableAll(self):
        logger.info("Setting all major components to disabled state")
        self.resetFlowControl()
        self.disableAllHeatingElements()

    def resetFlowControl(self):
        self.disableAllPumps()
        self.closeAllTwoWayValves()
        self.closeBallValve(self.INPUT_WATER_VALVE)
        logger.info("Shut down all liquid flow")

    ## BALL VALVE CONTROLS ##

    def openBallValve(self, index: int):
        self._setBallValveState(index, True)

    def closeBallValve(self, index: int):
        self._setBallValveState(index, False)

    def openBallValves(self, valves):
        for valve in valves:
            self.openBallValves(valve)

    def closeBallValves(self, valves):
        for valve in valves:
            self.closeBallValve(valve)

    def closeAllTwoWayValves(self):
        logger.debug("Closing all two way valves")
        for index in range (0,5):
            self.closeBallValve(index)

    def closeAllBallValves(self):
        logger.debug("Closing all ball valves")
        for index, _ in enumerate(self.hardwareState.ballValves):
            self.closeBallValve(index)

    ## PUMP CONTROLS ##

    def enablePump(self, index: int):
        self._setPumpState(index, True)

    def disablePump(self, index: int):
        self._setPumpState(index, False)

    def disableAllPumps(self):
        logger.debug("Disabling all pumps")
        for index, _ in enumerate(self.pumps):
            self.disablePump(index)

    ## HEATING ELEMENT CONTROLS ##

    def enableHeatingElement(self, index: int):
        self._setHeatingElementValue(index, 1)

    def disableHeatingElement(self, index: int):
        self._setHeatingElementValue(index, 0)

    def disableAllHeatingElements(self):
        logger.debug("Disabling all heating elements")
        for index, _ in enumerate(self.heatingElements):
            self.disableHeatingElement(index)

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
        if index in DeviceHandler.KETTLE_NAMES_GIVEN_ID.keys():
            self.hardwareState.kettlepidenabled[index] = value
            if not value:
                self.PIDtimer.stop()
                self._setHeatingElementValue(index, 0)
              
            else:
                self.PIDtimer.start(30)

        else:
            raise ComponentControlError("Could not find given kettle")

    def setHeatingElementPWM(self, index: int, value: float):
        self._setHeatingElementValue(index, value)

    ## HOP SERVO CONTROLS ##

    def goToHopPosition(self, index: int):
        if index in DeviceHandler.HOP_SERVO_POSITIONS.keys():
            self.setHopServoPosition(DeviceHandler.HOP_SERVO_POSITIONS[index])
        else:
            raise ComponentControlError(f'Could not find hop servo position {index}')

    def setHopServoPosition(self, angle: int):
        if angle in range(-150,151):
            if IS_RASPBERRY_PI:
                logger.debug("Setting servo angle")
                self.servo.moveSpeed(1, angle,64)
            logger.debug("Set servo angle")
            self.hardwareState.hopservoangle = angle
        else:
            raise ComponentControlError("Invalid servo angle selected")

    ## SENSOR CONTROLS ##

    def readTemperature(self, index: int):
        if IS_RASPBERRY_PI:
            temperature = self.tempsensors[index].get_temperature(Unit.DEGREES_F)
 
        else:
            temperature = 70
        return temperature

    def readvolume(self, index: int) -> float:
        """Reads the ADC for a particular kettle's pressure sensor and converts the pressure value into a volume
        in gallons"""
        if IS_RASPBERRY_PI:
            if DeviceHandler.KETTLE_NAMES_GIVEN_ID[index] == "MT":
                offset = .3
            elif DeviceHandler.KETTLE_NAMES_GIVEN_ID[index] == "HLT":
                offset = .3
            elif DeviceHandler.KETTLE_NAMES_GIVEN_ID[index] == "BK":
                offset = .3
            scale = 15/5
            # pressure is in kPa
            try:
                pressurevoltage = self.adc.raw_to_v(self.adc.read(channel1=index))
            except:
                pressurevoltage = 0
            #return pressurevoltage

            volume = (pressurevoltage - offset) * scale
            self.volumeaverages[index].append(volume)
            self.volumeaverages[index][-0:]
            return volume
            #return sum(self.volumeaverages[index])/len(self.volumeaverages[index])

        else:
            volume = 5
        return volume

    ## Under the hood controls

    def _setBallValveState(self, index: int, state: bool):
        if index == 0 and self.hardwareState.HLTfilldisabled and state == True:
            logger.critical("HLT is full, cannot add any more water")
            raise ComponentControlError("HLT is full, cannot add any more water")
        else:
            try:
                tempstate = self.hardwareState.ballValves[index]
                self.hardwareState.ballValves[index] = state
                for i in range(len(self.hardwareState.pumps)):
                    if self.hardwareState.pumps[i] == 1 and not self._pumpHasOpenPath(i):
                        self.hardwareState.ballValves[index] = tempstate
                        raise ComponentControlError(f'Cannot close valve path while pump {index} is running')
                ## the relay board the ball valves are connected to will only turn a relay off if the ouput pin is disabled entirely
                ## and will always stay on if an output pin is enabled regardless of its state (on or off)
                if state == True:
                    if (index >= 5):
                        try:
                            self.ballValves[index] = OutputDevice(self.ballValveGPIOs[index])
                        except GPIOPinInUse:
                            pass
                    else:
                        self.ballValves[index].on()
                else:
                    if (index>=5):
                        self.ballValves[index].close()
                    else:
                        self.ballValves[index].off()
                logger.debug(f'Set ball valve {index} to {"On" if state else "Off"}')
            except ComponentControlError as e:
                logger.critical(e)

    def _setPumpState(self, pumpindex: int, state: bool):
        # check if a valid path is open for either pump
        if (state == False) or (state and self._pumpHasOpenPath(pumpindex)):
            if state == True:
                self.pumps[pumpindex].on()
            else:
                self.pumps[pumpindex].off()
            self.hardwareState.pumps[pumpindex] = state
            logger.debug(f'Set pump {pumpindex} to {"On" if state else "Off"}')
            # raise an error otherwise
        else:
            error = ComponentControlError(
                f"Cannot turn pump {pumpindex} on. There is no suitable ball valve path open"
            )
            logger.exception(error)
            raise error

    def _pumpHasOpenPath(self, pumpindex: int) -> bool:
        pumphasopenpath = False
        for valvepath in self.pumpvalvepathmap[pumpindex]:
            pathopen = True
            for valveindex in self.valvepaths[valvepath]["open"]:
                if DeviceHandler.hardwareState.ballValves[valveindex] != 1:
                    pathopen = False
            for valveindex in self.valvepaths[valvepath]["close"]:
                if DeviceHandler.hardwareState.ballValves[valveindex] != 0:
                    pathopen = False
            if pathopen:
                pumphasopenpath = True
                break
        return pumphasopenpath

    def _setHeatingElementValue(self, index: int, value: float, calledmanually=True):
        kettleheatingdisabled = False
        if index in DeviceHandler.HLT_HEATING_ELEMENTS:
            kettleheatingdisabled = self.hardwareState.kettleheatingelementsdisabled[DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"]]
        elif index in DeviceHandler.BK_HEATING_ELEMENTS:
            kettleheatingdisabled = self.hardwareState.kettleheatingelementsdisabled[DeviceHandler.KETTLE_IDS_GIVEN_NAME["BK"]]

        if not kettleheatingdisabled or value == 0:
            if calledmanually:
                if index in DeviceHandler.HLT_HEATING_ELEMENTS:
                    self.hardwareState.kettlepidenabled[DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"]] = False
                    self.hardwareState.kettlepidenabled[DeviceHandler.KETTLE_IDS_GIVEN_NAME["MT"]] = False
                elif index in DeviceHandler.BK_HEATING_ELEMENTS:
                    self.hardwareState.kettlepidenabled[DeviceHandler.KETTLE_IDS_GIVEN_NAME["BK"]] = False
            for kettleindex, elementpair in enumerate(DeviceHandler.HEATING_ELEMENTS):
                if index in elementpair:
                    otherkettleon = False
                    if kettleindex == DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"]:
                        otherheatingelements = DeviceHandler.BK_HEATING_ELEMENTS
                    else:
                        otherheatingelements = DeviceHandler.HLT_HEATING_ELEMENTS
                    if value != 0:
                        for he in otherheatingelements:
                            if self.hardwareState.heatingElements[he] != 0:
                                otherkettleon = True
                                break
                    if not otherkettleon:
                        self.heatingElementSwitch.value = index in DeviceHandler.BK_HEATING_ELEMENTS
                        self.heatingElements[elementpair.index(index)].value = value
                        self.hardwareState.heatingElements[index] = value
                        if calledmanually:
                            logger.debug(f"Set heating element {index} to {value}, switch {self.heatingElementSwitch.value}")
                    else:
                        error = ComponentControlError(f'Attempted to turn on {DeviceHandler.KETTLE_NAMES_GIVEN_ID[kettleindex]} heating elements while other kettle heating elements are on')
                        logger.critical(error)
                        raise error
                    break
        else:
            logger.critical(f'Program is attempting to enable heating element {index} without sufficient liquid level')
            raise ComponentControlError(f'Program is attempting to enable heating element {index} without sufficient liquid level')

    def _readAllVolumes(self):
        # read the sensors and save the values here
        for i, _ in enumerate(self.hardwareState.volumes):
            self.hardwareState.volumes[i] = self.readvolume(i)

    def _readAllTemps(self):
        for i, _ in enumerate(self.hardwareState.temperatures):
            self.hardwareState.temperatures[i] = self.readTemperature(i)

    def _updateheatingelementPID(self):
        for kettleindex, kettlename in DeviceHandler.KETTLE_NAMES_GIVEN_ID.items():
            if self.hardwareState.kettlepidenabled[kettleindex] == True:
                logger.debug(f'Kettle name: {kettlename}')
                if kettlename == "HLT" or kettleindex == "MT":
                    heatingelementindex = 0
                    self.readTemperature(DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"])
                elif kettlename == "BK":
                    heatingelementindex = 1
                
                self.readTemperature(kettleindex)
                self._setHeatingElementValue(heatingelementindex, self.PIDS[kettleindex](self.hardwareState.temperatures[kettleindex]), calledmanually=False)
                lowbound = self.hardwareState.kettletempsetpoints[kettleindex] * 0.8
                if self.hardwareState.temperatures[kettleindex] < lowbound:
                    if kettlename == "HLT":
                        self._setHeatingElementValue(2, 1, True)
                    elif kettlename == "BK":
                        self._setHeatingElementValue(3, 1, True)

    def _updatestate(self):
        self._readAllVolumes()
        self.signalState.emit(DeviceHandler.hardwareState)

        #check that kettle volume is high enough to cover heating elements, otherwise disable them
     #   for kettleindex, kettlename in DeviceHandler.KETTLE_NAMES_GIVEN_ID.items():
       #     if kettlename in ("HLT", "BK"):
        #        if self.hardwareState.volumes[kettleindex] < DeviceHandler.HEATING_ELEMENT_MIN_VOLUME:
        #            if not self.hardwareState.kettleheatingelementsdisabled[kettleindex]:
         #               logger.critical(f'Kettle {kettlename} heating elements disabled due to insufficient liquid volume')
         #           self.hardwareState.kettleheatingelementsdisabled[kettleindex] = True
       #         else:
       #             self.hardwareState.kettleheatingelementsdisabled[kettleindex] = False

        #check that HLT isn't about to flood, otherwise disable valve that adds water
        if self.hardwareState.volumes[DeviceHandler.KETTLE_IDS_GIVEN_NAME["HLT"]] > DeviceHandler.KETTLE_MAX_VOLUME:
            if self.hardwareState.ballValves[0] == True:
                self.closeBallValve(0)
            if not self.hardwareState.HLTfilldisabled:
                logger.critical("Fresh water flow to HLT disabled due to excess volume")
            self.hardwareState.HLTfilldisabled = True
        else:
            self.hardwareState.HLTfilldisabled = False

        #check that pumps still have valid valve paths open
        for index, pump in enumerate(self.hardwareState.pumps):
            if pump == 1 and not self._pumpHasOpenPath(index):
                self._setPumpState(index, False)
                logger.critical(f'Pump {index} caught running without valid ball valve path, pump disabled')

devicehandler = DeviceHandler()
