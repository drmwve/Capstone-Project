import pytest
from autobrewer.hardware.devicehandler import DeviceHandler
from autobrewer.exceptions import ComponentControlError

@pytest.fixture
def devicehandler():
    handler = DeviceHandler()
    handler.refreshPins()
    return DeviceHandler()


class TestControlWrapper():
    @pytest.mark.parametrize("index", [0,1,2,3,4])
    @pytest.mark.parametrize("state", [True,False])
    def test_set_2way_ball_valve_state(self, index, state, devicehandler):
        assert devicehandler.twoWayBallValves[index].value == False
        devicehandler._set2WayState(index, state)
        assert devicehandler.twoWayBallValves[index].value == state

    @pytest.mark.parametrize("index", [0,1,2,3,4])
    @pytest.mark.parametrize("state", [True,False])
    def test_set_3way_ball_valve_state(self, index, state, devicehandler):
        assert devicehandler.threeWayBallValves[index].value == False
        devicehandler._set3WayState(index, state)
        assert devicehandler.threeWayBallValves[index].value == state

    @pytest.mark.parametrize("index", [0,1])
    def test_set_pump_open_valves_closed(self, index, devicehandler):
        state = True
        assert devicehandler.pumps[index].value == False
        with pytest.raises(ComponentControlError):
            devicehandler._setPumpState(index, state)
            assert devicehandler.pumps[index].value == False
            assert devicehandler.brewState.pumps[index] == False
