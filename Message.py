from datetime import datetime

class Message:
    author = ""
    channel = ""
    message = ""
    date = datetime()
    def __init__(self,author,channel,message):
        self.channel = channel
        self.message = message
        self.author = author

