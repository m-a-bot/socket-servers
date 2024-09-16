import socket
import pickle
import sys

DEBUG = True

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 11000))

print("User connect ...")
bufsize = 4096

if DEBUG:
    parameters = sys.argv

    user = parameters[1]

    table = parameters[2]

    query = parameters[3]

    client.send((" ".join(parameters[1:]).encode()))

    answer = client.recv(bufsize)
    data = None
    try:
        data = pickle.loads(answer)
    except:
        ...

    if data is not None:
        print(data)
    

client.shutdown(socket.SHUT_RDWR)

client.close()

