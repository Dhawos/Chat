import pickle
import socket
import threading
from Message import Message
from server.Channel import Channel
from server.Command import *

class ThreadedServer(object):
    def __init__(self, host, port):
        self.channels = [Channel("general"), Channel("shitpost")]
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))


    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            username = pickle.dumps(client.recv(4096))
            client.send(pickle.dumps(self.channels))
            welcomeMessage = Message("SERVER",self.channels[0],"Bienvenue sur le serveur de chat !!")
            client.send(pickle.dumps(welcomeMessage))
            for channel in self.channels:
                channel.clients += [client]

            #client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        print("[+] listening to " + str(address))
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    messageReceived = pickle.loads(data)
                    if messageReceived.isCommand:
                        self.processCommand(messageReceived)
                    else:
                        print(messageReceived)
                        channel = next(filter(lambda x: x.name == messageReceived.channel, self.channels))
                        for clientToSend in channel.clients:
                            clientToSend.send(pickle.dumps(messageReceived))

                else:
                    raise Exception('Client disconnected')
            except Exception as ex:
                print(type(ex))
                print(ex)
                for channel in self.channels:
                    channel.clients.remove(client)
                client.close()
                return False

    @check_channel("general")
    def date(self,**kwargs):
        date = datetime.now()
        message = Message("SERVER",kwargs.get("channel"),date.strftime("Today is : %d/%m"))
        self.postMessage(message)

    def postMessage(self,message):
        channel = next(filter(lambda x: x.name == message.channel, self.channels))
        for clientToSend in channel.clients:
            clientToSend.send(pickle.dumps(message))

    def processCommand(self,commande):
        splittedCommande = commande.message.split(" ")
        method_to_call = getattr(self, splittedCommande[0])
        if(len(splittedCommande) > 1):
            arguments = splittedCommande[1].split(",")
            dict = {}
            for argument in arguments :
                splitted_argument = argument.split(":")
                key = splitted_argument[0]
                value = splitted_argument[1]
                dict[key] = value
        dict["author"] = commande.author
        dict["channel"] = commande.channel
        return method_to_call(**dict)

if __name__ == "__main__":
    port_num = 8080
    ThreadedServer('',port_num).listen()
