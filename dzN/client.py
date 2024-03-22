import socket

from server import PORT, HOST


class ClientSocket:
    def __init__(self, host, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client.connect((host, port))

    def mainloop(self):
        while True:
            command = input('>> ').encode('utf-8')
            if not command or command == b'EXIT':
                break

            self.client.sendall(command)
            data = self.client.recv(1024).decode('utf-8')
            print(data)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.shutdown(socket.SHUT_RDWR)
        self.client.close()


if __name__ == '__main__':
    with ClientSocket(HOST, PORT) as client:
        try:
            client.mainloop()
        except KeyboardInterrupt:
            print("\nConnection broken!")
