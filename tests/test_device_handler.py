import pytest
from autobrewer.hardware.devicehandler import DeviceHandler
from autobrewer.exceptions import ComponentControlError
from autobrewer.hardware.pins import Pins


@pytest.fixture
def devicehandler():
    handler = DeviceHandler()
    handler._refreshPins()
    return DeviceHandler()


@pytest.fixture
def pathnames(index, devicehandler):
    return devicehandler.pumpvalvepathmap[index]


class TestDeviceHandler():
    @pytest.mark.parametrize("index", [x for x in range(len(Pins.ballValveGPIOs))])
    @pytest.mark.parametrize("state", [True, False])
    def test_set_ball_valve_state(self, index, state, devicehandler):
        assert devicehandler.ballValves[index].value == False
        devicehandler._setBallValveState(index, state)
        assert devicehandler.ballValves[index].value == state

    @pytest.mark.parametrize("index", [x for x in range(len(Pins.pumpGPIOs))])
    def test_enable_pump_valves_closed(self, index, devicehandler):
        assert devicehandler.pumps[index].value == False
        with pytest.raises(ComponentControlError):
            devicehandler.enablePump(index)

    @pytest.mark.parametrize("pathnames", [x for x in range(len(Pins.pumpGPIOs))], indirect=True)
    @pytest.mark.parametrize("index", [x for x in range(len(Pins.pumpGPIOs))])
    def test_open_pump_valves_open(self, index, pathnames, devicehandler):
        assert devicehandler.pumps[index].value == False
        for path in pathnames:
            devicehandler.openValvePath(path)
            devicehandler.enablePump(index)
            assert devicehandler.pumps[index].value == True
            devicehandler.disableAllBallValves()
