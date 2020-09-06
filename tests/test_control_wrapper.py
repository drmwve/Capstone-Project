import pytest
from autobrewer.ControlWrapper import DeviceHandler
from autobrewer.exceptions import ComponentControlException

@pytest.fixture
def controlHandler():
    DeviceHandler._instance = None
    return DeviceHandler()

class TestControlWrapper():
    @pytest.mark.parametrize("index", [0,1,2,3,4])
    @pytest.mark.parametrize("state", [True,False])
    def test_open_2way_ball_valve(self, index, state, controlHandler):
        assert controlHandler.twoWayBallValves[index].value == False
        controlHandler._set2WayState(index, state)
        assert controlHandler.twoWayBallValves[index].value == state

    @pytest.mark.parametrize("index", [0,1,2,3,4])
    @pytest.mark.parametrize("state", [True,False])
    def test_open_3way_ball_valve(self, index, state, controlHandler):
        assert controlHandler.threeWayBallValves[index].value == False
        controlHandler._set3WayState(index, state)
        assert controlHandler.threeWayBallValves[index].value == state
