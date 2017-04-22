import threading

class Channel():

    def __init__(self, name):
        self.name = name
        self.clients = []
        #self.lock = threading.Lock()


    def __getstate__(self):
        """Return state values to be pickled."""
        return (self.name)

    def __setstate__(self, state):
        """Restore state from the unpickled state values."""
        self.name = state

    def __str__(self):
        return self.name