import socket
import pickle
from DatabasePy import Database


class Server:
    def __init__(self, port):
        self.host = socket.gethostname()
        self.port = port  # initiate port no above 1024
        self.server_socket = socket.socket()  # get instance
        self.server_socket.bind((self.host, self.port))  # bind host address and port together
        self.D = Database('SQLite_Python.db', 'Database')

    def Connect(self):
        # configure how many client the server can listen simultaneously
        self.server_socket.listen()
        conn, address = self.server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))

        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        print("from connected user: " + str(data))

        d = self.D.fetch(str(data))
        msg = pickle.dumps(d)
        msg = pickle.loads(msg)

        conn.send(msg.encode())  # send data to the client

        conn.close()  # close the connection


if __name__ == '__main__':
    server = Server(5001)
    server.Connect()

