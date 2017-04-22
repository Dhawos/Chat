class Channel:
    def __init__(self, name):
        self.name = name
        #self.clients = set()

    def __str__(self):
        return self.name