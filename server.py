# server
import time
import json
import socket


class MySocket:
    """
     coded for clarity, not efficiency
    """

    def __init__(self, sock=None):
        self.MSGLEN = 1024
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < self.MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < self.MSGLEN:
            chunk = self.sock.recv(min(self.MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            while chunk:
                bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)


def receive_mb_data_via_tcp():
    _FRAME_QTY = 3
    _FRAME_LEN = 4
    host = socket.gethostname()
    puerto = 12345

    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    serversocket.bind((host, puerto))
    # become a server socket
    serversocket.listen(5)

    while True:
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        print("aceptada")
        chunks = []
        msg = clientsocket.recv(1024)
        msg = msg.decode()
        print(type(msg))
        #modules = msg.split('}')
        delimiter = "}"
        my_list = [x + delimiter for x in msg.split(delimiter) if x]
        print(my_list)

        # now do something with the clientsocket
        # in this case, we'll pretend this is a threaded server
        #ct = client_thread(clientsocket)
        #ct.run()


if __name__ == "__main__":
    receive_mb_data_via_tcp()
