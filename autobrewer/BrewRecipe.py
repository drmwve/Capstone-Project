from autobrewer.hardware.hardwarestate import HardwareState

try:
    import cPickle as pickle
except:
    import pickle
import hashlib
import hmac
from dataclasses import dataclass, field

from loguru import logger


@dataclass(init=True)
class BrewRecipe:
    """A messenger class which holds information about the brew recipe such as
    hop timing, mash temperature, etc. Created by the BrewConfig UI screen
    and passed to a Brew Process in the signal that starts the brewing process."""

    name: str = "Default"
    hopCartridges: int = 5
    mashTunTemperature: int = 152
    hopTiming: int = field(default_factory=lambda: [0, 15, 30, 45, 60])


class BrewRecipePickler(object):
    """Saves and loads a dictionary of brew recipes to the file system using the 'pickle' module so the user can have a list of saved recipes."""

    _instance = None
    _picklefile = "brewrecipes.pkl"
    _hardwarefile = "hardwarestate.pkl"

    # All instances of this class point to the same object since you only really need one
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BrewRecipePickler, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    def loadRecipes(self) -> dict:
        """Loads the recipes from the file system. Attempts to read pickle object from file, creates a new default one and saves it if this fails or if there's
        not a 'Default' recipe in the brew recipe dictionary for some reason.

        Returns:
            loadedRecipes (dict): A dictionary of brew recipes"""

        logger.debug("Attempting to load recipes")
        try:
            loadedRecipes = self._readPickleFromFile(BrewRecipePickler._picklefile)
            if not "Default" in loadedRecipes:
                raise Exception
        except:
            logger.exception("Loading - creating new brew recipes pickle")
            loadedRecipes = {BrewRecipe().name: BrewRecipe()}
            self._savePickleToFile(loadedRecipes, BrewRecipePickler._picklefile)
        logger.debug("Loading " + str(loadedRecipes))
        return loadedRecipes

    def saveRecipes(self, recipes: dict):
        """Saves the provided recipes to the recipe pickler. Detached from the actual saving function in case
        there's a future need to pickle other files.

        Args:
            recipes (dict): A dictionary of recipes. There must be a 'Default' recipe in the dictionary or it will be
            erased the next time the dictionary is loaded."""

        self._savePickleToFile(recipes, BrewRecipePickler._picklefile)

    def saveHardwareState(self, hardwarestate: dict):
        self._savePickleToFile(hardwarestate, BrewRecipePickler._hardwarefile)

    def loadHardwareState(self) -> dict:
        try:
            loadedstate = self._readPickleFromFile(BrewRecipePickler._hardwarefile)
            logger.debug(f'Loading {loadedstate}')
            return loadedstate
        except:
            logger.warning("Could not load hardware state. A reset hardware state is being loaded")
            return HardwareState()

    def _savePickleToFile(self, objectToPickle: object, picklefile: str):
        """Saves a given object to a file with hmac encryption to validate data integrity and prevent security threats.

        Args:
            objectToPickle (object): The Python object to be pickled
            picklefile (str): The filepath of the file to save the pickle to"""

        logger.debug("Pickling object: %s" % objectToPickle)
        pickledObject = pickle.dumps(objectToPickle)
        digest = self._make_digest(pickledObject)
        # hmac code is written as UTF-8 header, pickle is written as bytes
        with open(picklefile, "wb") as picklefile:
            logger.debug("Writing digest to file %s" % digest)
            picklefile.write(("%s\n" % digest).encode("utf-8"))
            logger.debug("Wrote pickle object: %s" % pickledObject)
            picklefile.write(pickledObject)

    def _readPickleFromFile(self, picklefile: str):
        """Reads the pickled object in the given hmac-validated file. Returns an exception if the validation fails.

        Args:
            picklefile (str): The filepath of the saved pickle object.

        Raises:
            AssertionError: If the hmac validation fails."""

        with open(picklefile, "rb") as picklefile:
            logger.debug("File %s read successfully" % picklefile.name)
            readDigest = picklefile.readline().decode("utf-8").rstrip()
            readPickle = picklefile.read()

        actualDigest = self._make_digest(readPickle)
        if hmac.compare_digest(actualDigest, readDigest):
            logger.debug("hmac check passed")
            return pickle.loads(readPickle)
        else:
            logger.debug("hmac check failed")
            raise AssertionError

    def _make_digest(self, message: str):
        """Creates a string hash (a digest) of a message which can validate data integrity"""

        hash = hmac.new(bytes(192), message, hashlib.sha1)
        return hash.hexdigest()
