import pytest
from autobrewer.ControlWrapper import ControlHandler
from autobrewer.exceptions import ComponentControlException

@pytest.fixture
def controlHandler():
    return ControlHandler()

class TestControlWrapper():
    @pytest.mark.parametrize("index", [0,1,2,3,4])
    @pytest.mark.parametrize("state", [True,False])
    def test_open_2way_ball_valve(self, index, state, controlHandler):
        controlHandler._set2WayState(index, state)
        assert controlHandler.twoWayBallValves[index].value == state

    @pytest.mark.parametrize("index", [0,1,2,3,4])
    @pytest.mark.parametrize("state", [True,False])
    def test_open_3way_ball_valve(self, index, state, controlHandler):
        controlHandler._set3WayState(index, state)
        assert controlHandler.threeWayBallValves[index].value == state
