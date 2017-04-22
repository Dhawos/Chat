import threading

class Channel():

    def __init__(self, name):
        self.name = name
        self.clients = set()
        #self.lock = threading.Lock()


    def __str__(self):
        return self.name