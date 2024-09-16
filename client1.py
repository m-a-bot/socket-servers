import pickle
import socket

bufsize = 4096

class Client:

    def __init__(self, _host='127.0.0.1', _port=11000):
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = _host
        self.port = _port

        self.connect()

    def connect(self):

        self.client.connect((self.host, self.port))
        print("user connected")


    def send(self, query):

        self.client.send((query).encode())
        print("send", repr(query))


    def receive(self):

        answer = self.client.recv(bufsize)
        print("receive data")
        
        data = None
        try:
            data = pickle.loads(answer)
        except:
            ...

        return data

    def close(self):
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()


if __name__ == "__main__":

    client1 = Client()
    client1.send("Admin table1 select")
    client1.receive()
    client1.close()

    client2 = Client()
    client2.send("Peter table1 delete 2")
    client2.receive()
    client2.close()

    client2 = Client()
    client2.send("Peter table1 select")
    client2.receive()
    client2.close()

    client3 = Client()
    client3.send("Vova table3 select")
    client3.receive()
    client3.close()