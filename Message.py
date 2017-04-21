from datetime import datetime

class Message:
    author = ""
    channel = ""
    message = ""

    def __init__(self,author,channel,message):
        self.channel = channel
        self.message = message
        self.author = author
        self.date = datetime.now()

    def __str__(self):
        return "(" + str(self .channel) + ") - " + self.date.strftime('%d/%m at %H:%M') + " - " + str(self.author) + " : " + str(self.message)
