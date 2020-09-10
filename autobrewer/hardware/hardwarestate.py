class HardwareState():
    """A messenger class which holds information about what state the brewer
    components are in. This includes the ball valves, heating elements, pumps,
    and sensors. Exists to provide a simple format to send state information
    between the UI and the execution code. Could also be used to save and load
    brew states when a process is paused."""

    def __init__(self):
        self.twoWayBallValves = [False, False, False, False, False]
        self.threeWayBallValves = [False, False, False, False, False]
        self.pumps = [False, False]
        self.heatingElements = {"HLT": 0, "BK": 0}
        self.hopservo = 0
        self.temperatures = {"HLT": 0, "MT": 0, "BK": 0}
        self.volumes = {"HLT": 0, "MT": 0, "BK": 0}

    def _pathOpenHLTtoMT(self):
        """Check ball valve path for hot liquor tank to mash tun is open"""
        return (
            self.twoWayBallValves[1] and not self.threeWayBallValves[1]
        )

    def _pathOpenMTRecirc(self):
        """Check ball valve path for mash tun HERMS coil is open"""
        return (
            self.twoWayBallValves[2]
            and not self.threeWayBallValves[2]
            and self.threeWayBallValves[1]
        )

    def _pathOpenMTtoBK(self):
        """Check ball valve path from mash tun to boil kettle is open"""
        return (
            self.twoWayBallValves[2]
            and self.threeWayBallValves[2]
            and not self.threeWayBallValves[3]
            and not self.threeWayBallValves[4]
            and self.twoWayBallValves[3]
        )

    def _pathOpenBKWhirl(self):
        """Check ball valve path to whirlpool boil kettle is open"""
        return (
            self.twoWayBallValves[4]
            and self.threeWayBallValves[3]
            and not self.threeWayBallValves[4]
            and self.twoWayBallValves[3]
        )

    def _pathOpenBKDrain(self):
        """Check ball valve path to drain boil kettle is open"""
        return (
            self.twoWayBallValves[4]
            and self.threeWayBallValves[3]
            and self.threeWayBallValves[3]
        )
