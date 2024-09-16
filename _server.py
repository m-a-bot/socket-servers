import pickle
import socket
import enum


class TypeServer(enum.IntEnum):
    DAC = 1
    MAC = 2
    RBAC = 3


class Server:

    def __init__(self, _host='127.0.0.1', _port=11000):

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = _host
        self.port = _port
        self.__bind()


    def __bind(self):
        self.server.bind((self.host, self.port))
        self.server.listen(100)

    def start(self):
        print("Start")

        while True:
            client, address = self.server.accept()

            print(address, "connected")

            request = self.receive_data(client, 4096)

            dr = request.decode()

            user = "Hello " + dr.split()[0] + " !"

            self.send(client, user.encode())

    def stop(self):
        self.server.close()

    def close(self):
        self.stop()

    def receive_data(self, source, buffer_size):
        request = None
        try:
            request = source.recv(buffer_size)
        except:
            ...
        return request

    def send(self, source, bytes_data):

        try:
            source.send(bytes_data)
        except:
            ...


if __name__ == "__main__":

    ...

