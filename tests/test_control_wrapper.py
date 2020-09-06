import pytest
from autobrewer.ControlWrapper import ControlWrapper
from autobrewer.exceptions import ComponentControlException

class TestControlWrapper():

    @pytest.mark.parametrize("index, state", [1,2,3,4,5], [True,False])
    def test_open_2way_ball_valve(self, index, state):
        controller = ControlWrapper()
        controller._set2WayState(index, state)
        assert controller.twoWayBallValves[index] == state
