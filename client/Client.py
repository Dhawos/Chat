from tkinter import *
from tkinter import ttk
from client.ConnectionFrame import ConnectionFrame
import socket

class Client():

    def __init__(self):
        self.view = ConnectionFrame(self)
        self.userNameString = StringVar()
        self.hostname = StringVar(value="127.0.0.1")
        self.port = StringVar(value=8080)
        self.statusString = StringVar(value="Waiting...")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self):
        try :
            if(self.userNameString.get() == ""):
                raise ValueError
            self.statusString.set("Connecting...")
            self.view.refresh()
            self.client.connect((self.hostname.get(),int(self.port.get())))
        except IndexError:
            self.statusString.set("Bad hostname/port")
        except ValueError:
            self.statusString.set("Bad Nickname")
        except ConnectionRefusedError:
            self.statusString.set("Connection refused")


client = Client()
client.view.initConnectionFrame()

