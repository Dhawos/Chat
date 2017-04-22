import socket
from tkinter import *
import pickle
from client.ui.ConnectionFrame import ConnectionFrame
from client.ui.ChatFrame import ChatFrame
from Message import Message
import threading
from time import sleep


class Client():

    def __init__(self):
        self.view = ConnectionFrame(self)
        self.userNameString = StringVar()
        self.hostname = StringVar(value="127.0.0.1")
        self.port = IntVar(value=8080)
        self.statusString = StringVar(value="Waiting...")
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.currentmessage = StringVar()
        self.currentChannel = StringVar(value="general")
        self.messages = []
        self.channels = []
        self.thread = threading.Thread(target = self.run)



    def connect(self):
        try :
            if(self.userNameString.get() == ""):
                raise ValueError
            self.statusString.set("Connecting...")
            self.view.refresh()
            self.client.connect((self.hostname.get(),self.port.get()))

            #Retrieving channels list
            response = self.client.recv(4096)
            self.channels = pickle.loads(response)

            self.statusString.set("Chat connected to  : " + str(self.client.getpeername()[0]) + ":" + str(self.client.getpeername()[1]) )
            self.view.destroy()
            self.view = ChatFrame(self)
            self.currentmessage = StringVar()
            self.currentChannel = StringVar(value=str(self.channels[0]))
            self.view.init()
            self.thread.start()
        except IndexError:
            self.statusString.set("Bad hostname/port")
        except ValueError:
            self.statusString.set("Bad Nickname")
        except ConnectionRefusedError:
            self.statusString.set("Connection refused")

    def run(self):
        self.running = True
        while self.running:
            response = self.client.recv(4096)
            if response:
                self.messages += [pickle.loads(response)]
            else:
                print("Nothing received")
            sleep(10)

    def sendMessage(self):
        messageToSend = Message(self.userNameString.get(), self.currentChannel.get(), self.currentmessage.get())
        self.client.send(pickle.dumps(messageToSend))
        print(str(messageToSend))
        self.currentmessage.set("")

    def exit(self):
        self.running = False
        self.client.close()
        self.view.destroy()
        print("exiting")


client = Client()
client.view.init()

