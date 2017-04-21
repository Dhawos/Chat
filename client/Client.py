import socket
from tkinter import *
import json
from client.ui.ConnectionFrame import ConnectionFrame
from client.ui.ChatFrame import ChatFrame


class Client():

    def __init__(self):
        self.view = ConnectionFrame(self)
        self.userNameString = StringVar()
        self.hostname = StringVar(value="127.0.0.1")
        self.port = StringVar(value=8080)
        self.statusString = StringVar(value="Waiting...")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.messages = []
        self.currentMessage = StringVar()
        self.currentChannel = StringVar(value="general")



    def connect(self):
        try :
            if(self.userNameString.get() == ""):
                raise ValueError
            self.statusString.set("Connecting...")
            self.view.refresh()
            self.client.connect((self.hostname.get(),int(self.port.get())))
            self.statusString.set("Chat connected to  : " + str(self.client.getpeername()[0]) + ":" + str(self.client.getpeername()[1]) )
            self.view.destroy()
            self.view = ChatFrame(self)
            self.view.init()
            self.mainloop()
        except IndexError:
            self.statusString.set("Bad hostname/port")
        except ValueError:
            self.statusString.set("Bad Nickname")
        except ConnectionRefusedError:
            self.statusString.set("Connection refused")

    def mainLoop(self):
        while True:
            response = self.client.recv(4096)
            self.messages += [json.loads(response)]

    def sendMessage(self,message):
        self.client.send(json.dump(message))
        print(str(message))


client = Client()
client.view.init()

