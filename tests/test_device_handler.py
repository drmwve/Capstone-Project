import pytest
from autobrewer.hardware.devicehandler import DeviceHandler
from autobrewer.exceptions import ComponentControlError
from autobrewer.hardware.pins import Pins


@pytest.fixture
def devicehandler():
    yield DeviceHandler()
    DeviceHandler._refreshPins()


# this ugly thing creates a bunch of tests for every path assigned to each pump
# [0,"path1],[0,"path2"],[1,"path3"] etc.
@pytest.fixture(
    params=[
        [x, y]
        for x in range(len(DeviceHandler.pumpvalvepathmap))
        for y in DeviceHandler.valvepaths
        if y in DeviceHandler.pumpvalvepathmap[x]
    ]
)
def indexpathpairs(request):
    return request.param


class TestDeviceHandler:
    @pytest.mark.parametrize("path", [x for x in DeviceHandler.valvepaths.keys()])
    def test_open_valve_path(self, path, devicehandler):
        devicehandler.openValvePath(path)
        for valveindex in devicehandler.valvepaths[path]["open"]:
            assert devicehandler.ballValves[valveindex].value == 1
        for valveindex in devicehandler.valvepaths[path]["close"]:
            assert devicehandler.ballValves[valveindex].value == 0

    @pytest.mark.parametrize("angle", [0, 180, 360])
    def test_set_hop_servo_position_valid(self, angle, devicehandler):
        devicehandler.setHopServoPosition(angle)
        assert devicehandler.hopServo.value == angle
        assert devicehandler.hardwareState.hopservo == angle

    @pytest.mark.parametrize("angle", [-1, 370])
    def test_set_hop_servo_position_valid(self, angle, devicehandler):
        with pytest.raises(ComponentControlError):
            devicehandler.setHopServoPosition(angle)

    @pytest.mark.parametrize("index", [x for x in range(len(Pins.ballValveGPIOs))])
    @pytest.mark.parametrize("state", [True, False])
    def test_set_ball_valve_state(self, index, state, devicehandler):
        assert devicehandler.ballValves[index].value == False
        if state:
            devicehandler.openBallValve(index)
        else:
            devicehandler.closeBallValve(index)
        assert devicehandler.ballValves[index].value == state

    def test_enable_pump_valid(self, indexpathpairs, devicehandler):
        index, pathname = indexpathpairs
        assert devicehandler.pumps[index].value == False
        devicehandler.openValvePath(pathname)
        devicehandler.enablePump(index)
        assert devicehandler.pumps[index].value == True
        assert devicehandler.hardwareState.pumps[index] == True
        devicehandler.closeAllBallValves()

    @pytest.mark.parametrize("index", [x for x in range(len(DeviceHandler.pumpGPIOs))])
    def test_enable_pump_invalid(self, index, devicehandler):
        assert devicehandler.pumps[index].value == False
        with pytest.raises(ComponentControlError):
            devicehandler.enablePump(index)

    def test_disable_pump(self, indexpathpairs, devicehandler):
        index, pathname = indexpathpairs
        devicehandler.openValvePath(pathname)
        devicehandler.enablePump(index)
        assert devicehandler.pumps[index].value == True
        devicehandler.disablePump(index)
        assert devicehandler.pumps[index].value == False
        assert devicehandler.hardwareState.pumps[index] == False

    @pytest.mark.parametrize(
        "pumpindex", [x for x in range(len(DeviceHandler.pumpGPIOs))]
    )
    def test_pump_has_open_path_false(self, pumpindex, devicehandler):
        devicehandler.closeAllBallValves()
        assert not devicehandler._pumpHasOpenPath(pumpindex)

    def test_pump_has_open_path_true(self, indexpathpairs, devicehandler):
        index, pathname = indexpathpairs
        devicehandler.openValvePath(pathname)
        assert devicehandler._pumpHasOpenPath(index)

    @pytest.mark.parametrize("value", [0, 1, 0.2, 0.3, 0.4, 0.5, 0.6])
    @pytest.mark.parametrize(
        "index", [x for x in range(len(DeviceHandler.heatingElementGPIOs))]
    )
    def test_set_heating_element_value(self, index, value, devicehandler):
        assert devicehandler.heatingElements[index].value == 0
        if value == 0:
            devicehandler.disableHeatingElement(index)
        elif value == 1:
            devicehandler.enableHeatingElement(index)
        else:
            devicehandler.setHeatingElementPWM(index, value)
        assert devicehandler.heatingElements[index].value == value
        assert devicehandler.hardwareState.heatingElements[index] == value
