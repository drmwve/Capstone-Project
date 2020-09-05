from autobrewer.BrewRecipe import BrewRecipe, BrewRecipePickler
try:
    import cPickle as pickle
except:
    import pickle
import pytest
from loguru import logger
import hmac

#basic test data:
#object being pickled, pickle, pickle digest, formatted file data, file
@pytest.fixture
def pickle_file_data(tmpdir):
    tempfile = tmpdir.join("test.pkl")
    pickler = BrewRecipePickler()
    brewRecipe = [BrewRecipe()]
    pickledobject = pickle.dumps(brewRecipe)
    digest = pickler._make_digest(pickledobject)
    expectedFileData = ("%s\n" % digest).encode('utf-8') + pickledobject
    return {
        "object": brewRecipe,
        "pickledobject": pickledobject,
        "digest": digest,
        "expectedFileData": expectedFileData,
        "file": tempfile
    }

class TestRecipePickler():

    def test_load_recipes_file_exists(self, pickle_file_data):
        data = pickle_file_data
        pickler = BrewRecipePickler()
        BrewRecipePickler._picklefile = data["file"]
        with open(data["file"], "wb") as tempfile:
            tempfile.write(data["expectedFileData"])
        assert pickler.loadRecipes() == data["object"]

    def test_load_recipes_file_does_not_exist(self, pickle_file_data):
        data = pickle_file_data
        pickler = BrewRecipePickler()
        BrewRecipePickler._picklefile = data["file"]
        assert pickler.loadRecipes() == data["object"]

    def test_save_file(self, pickle_file_data):
        data = pickle_file_data
        pickler = BrewRecipePickler()
        pickler._savePickleToFile(data["object"],data["file"])

        with open(data["file"], "rb") as tempfile:
            assert tempfile.read() == data["expectedFileData"]

    #write expected data to file and check it's valid
    def test_read_file(self, pickle_file_data):
        data = pickle_file_data
        pickler = BrewRecipePickler()
        with open(data["file"], "wb") as tempfile:
            tempfile.write(data["expectedFileData"])
        assert pickler._readPickleFromFile(data["file"]) == data["object"]

    #write wrong data to file and check it's correctly rejected
    def test_read_file_corrupted(self, pickle_file_data):
        data = pickle_file_data
        pickler = BrewRecipePickler()
        with open(data["file"], "wb") as tempfile:
            tempfile.write("corrupt data".encode('utf-8'))
        with pytest.raises(AssertionError):
            pickledobject = pickler._readPickleFromFile(data["file"])
            assert pickledobject == data["object"]
