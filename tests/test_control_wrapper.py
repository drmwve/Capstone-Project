import pytest
from autobrewer.hardware.devicehandler import DeviceHandler
from autobrewer.exceptions import ComponentControlError
from autobrewer.hardware.pins import Pins


@pytest.fixture
def devicehandler():
    handler = DeviceHandler()
    handler._refreshPins()
    return DeviceHandler()


class TestControlWrapper():
    @pytest.mark.parametrize("index", [x for x in range(len(Pins.ballValveGPIOs))])
    @pytest.mark.parametrize("state", [True,False])
    def test_set_ball_valve_state(self, index, state, devicehandler):
        assert devicehandler.ballValves[index].value == False
        devicehandler._setBallValveState(index, state)
        assert devicehandler.ballValves[index].value == state

    @pytest.mark.xfail
    @pytest.mark.parametrize("index", [0,1])
    def test_set_pump_open_valves_closed(self, index, devicehandler):
        state = True
        assert devicehandler.pumps[index].value == False
        with pytest.raises(ComponentControlError):
            devicehandler._setPumpState(index, state)
            assert devicehandler.pumps[index].value == False
            assert devicehandler.brewState.pumps[index] == False
