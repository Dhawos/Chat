import pickle
import socket
import threading

from server.Channel import Channel


class ThreadedServer(object):
    def __init__(self, host, port):
        self.channels = [Channel("channel1"), Channel("channel2")]
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))


    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.send(pickle.dumps(self.channels))
            print("sent channels : " + str(self.channels))
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
                    for clientToSend in messageReceived.channel.clients:
                        clientToSend.send(pickle.dumps(messageReceived))

                else:
                    raise Exception('Client disconnected')
            except:
                client.close()
                return False


if __name__ == "__main__":
    port_num = 8080
    ThreadedServer('',port_num).listen()
