from threading import Thread
import socket
import struct
from src.tunnel import Bridge

HOST = "127.0.0.1"
PORT = 65432


def handle_connection(conn : socket.socket):
    # TODO establish shared key

    bridge = Bridge(conn)
    bridge.open()
    # Main Thread can do something here
    conn.close()


if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        # Listen for connections
        conn, addr = s.accept()
        # If connection is found start thread to handle connection
        Thread(target=handle_connection, args=(conn ), daemon=True)
        