try:
    import cPickle as pickle
except:
    import pickle
import hashlib
import hmac
from dataclasses import dataclass, field

from loguru import logger

@dataclass
class BrewRecipe():
    # I'm a messenger class which holds information about the brew recipe such as
    # hop timing, mash temperature, etc. I am created by the BrewConfig UI screen
    # and passed to a Brew Process in the signal that starts the brewing process.
    name: str = "Default"
    hopCartridges: int = 5
    mashTunTemperature: int = 160
    hopTiming: int = field(default_factory=lambda: [0,0,0,0,0])

class BrewRecipePickler(object):
    _instance = None
    _picklefile = "brewrecipes.pkl"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BrewRecipePickler, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance


    def saveRecipes(self, brewRecipes):
        recipePickle = pickle.dumps(brewRecipes)
        pickleDigest = self.make_digest(recipePickle)
        with open(BrewRecipePickler._picklefile, "w") as picklefile:
            picklefile.write(str(pickleDigest) + '\n')
            picklefile.write(str(recipePickle))

    def loadRecipes(self):
        logger.debug("Attempting to load recipes")
        try:
            with open(BrewRecipePickler._picklefile, "r") as picklefile:
                pickleDigest, recipePickle = picklefile.readlines(2)
                checkPD = self.make_digest(pickleDigest)
                if hmac.compare_digest(checkPD, pickleDigest):
                    brewRecipes = pickle.loads(recipePickle)
                logger.debug("Loading " + brewRecipes)
        except:
            brewRecipes = [BrewRecipe()]
            self.saveRecipes(brewRecipes)
            logger.debug("Creating new brew recipes file")
        return brewRecipes

    def make_digest(self, message):
        hash = hmac.new(bytes(192),
                    message,
                    hashlib.sha1)
        return hash.hexdigest()