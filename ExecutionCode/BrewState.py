class BrewState():
    # I'm a messenger class which holds information about what state the brewer
    # components are in. This includes the ball valves, heating elements, pumps,
    # and sensors. I exist to provide a simple format to send state information
    # between the UI and the execution code. I can also be used to save and load
    # brew states when a process is paused.

    def __init__(self):
        self.twoWayBallValves = [False, False, False, False, False]
        self.pump = [False, False]
        self.heatingElement = [False, False]
        self.hopservo = [False]
        self.threeWayBallValve = [False, False, False, False, False, False]
        self.angle = 0


    pass