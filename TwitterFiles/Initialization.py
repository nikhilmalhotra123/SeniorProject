from gensim.models import KeyedVectors
from MailCleanup import MailCleanup as mclean

class Model:
    def __init__(self, path):
        self._model = None
        self._path = path
        self.load_model()

    def load_model(self):
        print("starting")
        mclean.model = KeyedVectors.load_word2vec_format(self._path, binary=True)
        print("done")