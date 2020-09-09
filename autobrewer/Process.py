from PySide2 import QtCore

class Process(QtCore.QObject):
    # I have an array of steps and an index value. Each step, I emit signals which call process functions like
    # move liquid from tank to tank, heat to certain temperature, drain boil kettle, etc. For now, I receive
    # a "step completed" signal from the brew controller which calls the increment function.
    #
    # I emit a signal for each step in the process, and I emit a signal when I'm finished.
    def __init__(self):
        self.processSteps = []
        self.currentStep = 0

    def addStep(self, step):
        self.processSteps.append(step)

    def start(self):
        # I start the process.
        pass

    def increment(self):
        self.currentStep += self.currentStep
        self.processSteps[self.currentStep]()

        # I move on to the next step.
        pass

    def pause(self):
        #I pause the process in a way that somehow allows it to resume.
        pass

    def stop(self):
        # I stop the process completely and quit executing.
        pass

class BrewProcess(Process):
    def __init__(self, brewRecipe):
        super().__init__()
        self.brewRecipe = brewRecipe
        #emit signal which sets target mash temp
        self.processSteps = ["brewing process step functions"]

class CleaningProcess(Process):
    def __init__(self):
        super().__init__()
        self.processSteps = ["cleaning process step functions"]