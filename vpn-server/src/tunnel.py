from socket import socket
from threading import Thread
from time import sleep


class Bridge:
    

    def __init__(self, conn:socket) -> None:
        self.conn = conn
        buffer = bytearray()
        self.send_thread = Thread(target=Bridge.out_stream, args=(conn,buffer))
        self.recv_thread = Thread(target=Bridge.in_stream, args=(conn,buffer))

    def open(self):
        self.send_thread.run()
        self.recv_thread.run()

    @staticmethod
    def in_stream(conn:socket, buffer:bytearray):
        data = b""
        while True:
            data = conn.recv(1024)
            # TODO: repackage payload
            buffer += data
            if not data:
                break

    @staticmethod
    def out_stream(conn:socket, buffer:bytearray):
        while buffer:
            sent = conn.send(buffer[:1024])
            buffer = buffer[sent:]
            sleep(0.005)

    def close(self):
        self.send_thread.join()
        self.recv_thread.join()