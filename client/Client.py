import socket
from tkinter import *
import pickle
from client.ui.ConnectionFrame import ConnectionFrame
from client.ui.ChatFrame import ChatFrame
from Message import Message

class Client():

    def __init__(self):
        self.view = ConnectionFrame(self)
        self.userNameString = StringVar()
        self.hostname = StringVar(value="127.0.0.1")
        self.port = IntVar(value=8080)
        self.statusString = StringVar(value="Waiting...")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.currentmessage = StringVar()
        self.currentChannel = StringVar(value="general")
        self.messages = []




    def connect(self):
        try :
            if(self.userNameString.get() == ""):
                raise ValueError
            self.statusString.set("Connecting...")
            self.view.refresh()
            self.client.connect((self.hostname.get(),self.port.get()))
            self.statusString.set("Chat connected to  : " + str(self.client.getpeername()[0]) + ":" + str(self.client.getpeername()[1]) )
            self.view.destroy()
            self.view = ChatFrame(self)
            self.currentmessage = StringVar()
            self.currentChannel = StringVar(value="general")
            self.view.init()
            self.mainLoop()
        except IndexError:
            self.statusString.set("Bad hostname/port")
        except ValueError:
            self.statusString.set("Bad Nickname")
        except ConnectionRefusedError:
            self.statusString.set("Connection refused")

    def mainLoop(self):
        shouldRun = True
        while shouldRun:
            response = self.client.recv(4096)
            self.messages += [pickle.loads(response)]

    def sendMessage(self):
        messageToSend = Message(self.userNameString.get(), self.currentChannel.get(), self.currentmessage.get())
        self.client.send(pickle.dumps(messageToSend))
        print(str(messageToSend))
        self.currentmessage.set("")


client = Client()
client.view.init()

