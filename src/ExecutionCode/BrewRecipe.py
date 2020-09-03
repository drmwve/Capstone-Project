class BrewRecipe():
    # I'm a messenger class which holds information about the brew recipe such as
    # hop timing, mash temperature, etc. I am created by the BrewConfig UI screen
    # and passed to a Brew Process in the signal that starts the brewing process.
    def __init__(self):
        self.HopCartridges = 5
        self.MashTunTemperature = 160
        self.hopTiming = [0,0,0,0,0]
    pass