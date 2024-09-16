import _server
from user_thread import ClientThread


class RBACServer(_server.Server):

    def __init__(self, _host='127.0.0.1', _port=11000):
        super().__init__(_host, _port)

        self.cl = False

    def start(self):
        print("Start")

        while True:

            client, address = self.server.accept()

            user_thread = ClientThread(client, address, _server.TypeServer.RBAC)

            user_thread.start()


    def close(self):
        self.server.close()
        self.cl = True


if __name__ == "__main__":
    RBACServer().start()
