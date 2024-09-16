import pickle

from _server import Server, TypeServer
from user_thread import ClientThread


class DACServer(Server):

    def __init__(self, _host='127.0.0.1', _port=11000):
        super().__init__(_host, _port)

    def start(self):
        print("Start")

        while True:
            client, address = self.server.accept()

            user_thread = ClientThread(client, address, TypeServer.DAC)

            user_thread.start()


if __name__ == "__main__":
    DACServer(_port=9090).start()
