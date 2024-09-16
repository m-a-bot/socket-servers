from _server import Server, TypeServer
from user_thread import ClientThread


class MACServer(Server):

    def __init__(self, _host='127.0.0.1', _port=11000):
        super().__init__(_host, _port)

    def start(self):
        print("Start")

        while True:
            client, address = self.server.accept()

            user_thread = ClientThread(client, address, TypeServer.MAC)

            user_thread.start()


if __name__ == "__main__":
    MACServer(_port=8080).start()