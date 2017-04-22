import socket
from tkinter import *
import pickle
from client.ui.ConnectionFrame import ConnectionFrame
from client.ui.ChatFrame import ChatFrame
from Message import Message
import threading
from time import sleep
from client.NewMessageEvent import NewMessageEvent

class Client():
    command_prefix = "!"
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
        self.channels = []
        self.thread = threading.Thread(target = self.run)
        self.listeners = []



    def connect(self):
        try :
            if(self.userNameString.get() == ""):
                raise ValueError
            self.statusString.set("Connecting...")
            self.view.refresh()
            self.client.connect((self.hostname.get(),self.port.get()))
            self.client.settimeout(1)
            #Retrieving channels list
            response = self.client.recv(4096)
            self.channels = pickle.loads(response)

            self.statusString.set("Chat connected to  : " + str(self.client.getpeername()[0]) + ":" + str(self.client.getpeername()[1]))

            self.view.destroy()
            self.view = ChatFrame(self)


            self.currentmessage = StringVar()
            self.currentChannel = StringVar(value=str(self.channels[0]))

            self.view.init()

        except IndexError:
            self.statusString.set("Bad hostname/port")
        except ValueError:
            self.statusString.set("Bad Nickname")
        except ConnectionRefusedError:
            self.statusString.set("Connection refused")
        except ConnectionResetError:
            self.statusString.set("Connection reset")

    def run(self):
        self.running = True
        while self.running:
            try:
                response = self.client.recv(4096)
                self.messages += [pickle.loads(response)]
                self.fireEvent(NewMessageEvent())
            except socket.timeout:
                if not self.running:
                    self.client.close()
            except EOFError:
                exit()
                print("Server unexpectedly closed the connection")


    def sendMessage(self):
        string = self.currentmessage.get()
        isCommand = False
        if string.startswith(self.command_prefix):
            isCommand = True
            string = string.strip(self.command_prefix)
        messageToSend = Message(self.userNameString.get(), self.currentChannel.get(), string,isCommand)
        self.client.send(pickle.dumps(messageToSend))
        print(str(messageToSend))
        self.currentmessage.set("")

    def exit(self):
        self.running = False
        self.view.destroy()

    def fireEvent(self,Event):
        for listener in self.listeners:
            listener.notify()

    def registerListener(self,listener):
        self.listeners += [listener]

client = Client()
client.view.init()

