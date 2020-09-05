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

# Makes it easy to save and load particular recipes to a file
class BrewRecipePickler(object):
    _instance = None
    _picklefile = "brewrecipes.pkl"

    # All instances of this class point to the same object since you only really need one
    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(BrewRecipePickler, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    def loadRecipes(self):
        logger.debug("Attempting to load recipes")
        try:
            objectToPickle = self._readPickleFromFile(BrewRecipePickler._picklefile)
        except:
            logger.exception("Loading - creating new brew recipes pickle")
            objectToPickle = [BrewRecipe()]
            self._savePickleToFile(objectToPickle, BrewRecipePickler._picklefile)
        logger.debug("Loading " + str(objectToPickle))
        return objectToPickle

    def saveRecipes(self, recipes):
        self._savePickleToFile(recipes)

    #saves a given object to a pickle file with encryption
    def _savePickleToFile(self, objectToPickle, picklefile):
        logger.debug("Pickling object: %s" % objectToPickle)
        pickledObject = pickle.dumps(objectToPickle)
        digest = self._make_digest(pickledObject)
        #hmac code is written as UTF-8 header, pickle is written as bytes
        with open(picklefile, "wb") as picklefile:
            logger.debug("Writing digest to file %s" % digest)
            picklefile.write(("%s\n" % digest).encode('utf-8'))
            logger.debug("Wrote pickle object: %s" % pickledObject)
            picklefile.write(pickledObject)

    #read pickle file and check hmac, raising an exception if there's an issue
    def _readPickleFromFile(self, picklefile):
        with open(picklefile, "rb") as picklefile:
            logger.debug("File %s read successfully" % picklefile.name)
            readDigest = picklefile.readline().decode('utf-8').rstrip()
            readPickle = picklefile.read()
            logger.debug("Read recipePickle: %s" % readPickle)

        actualDigest = self._make_digest(readPickle)
        logger.debug("Doing hmac check: %s  %s" % (actualDigest,readDigest))
        if hmac.compare_digest(actualDigest, readDigest):
            logger.debug("hmac check passed")
            return pickle.loads(readPickle)
        else:
            logger.debug("hmac check failed")
            raise AssertionError

    #creates a string hash (a digest) of a message which can validate data integrity
    def _make_digest(self, message):
        hash = hmac.new(bytes(192),
                    message,
                    hashlib.sha1)
        return hash.hexdigest()