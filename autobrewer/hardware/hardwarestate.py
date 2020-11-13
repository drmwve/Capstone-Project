class HardwareState:
    """A messenger class which holds information about what state the brewer
    components are in. This includes the ball valves, heating elements, pumps,
    and sensors. Exists to provide a simple format to send state information
    between the UI and the execution code. Could also be used to save and load
    brew states when a process is paused."""

    def __init__(self):
        self.ballValves = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        self.pumps = [False, False]
        self.heatingElements = [0.0, 0.0, 0.0, 0.0]
        self.kettletempsetpoints = [0, 0, 0]
        self.kettlepidenabled = [False, False, False]
        self.kettleheatingelementsdisabled = [False, False, False]
        self.temperatures = [0.0, 0.0, 0.0]
        self.volumes = [0.0, 0.0, 0.0]
        self.hopservoangle = 0
        self.HLTfilldisabled = False
