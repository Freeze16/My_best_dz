import json
import socket

from hash_table import HashTable

from termcolor import colored

HOST = 'localhost'
PORT = 8080

CONSOLE = {
    'success': colored('[+]', 'green'),
    'warning': colored('[!]', 'light_yellow'),
    'error': colored('[-]', 'red')
}


class ServerSocket:
    DATA_BASE = 'data_base.json'

    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(1)

        with open(ServerSocket.DATA_BASE, 'r') as db:
            self.db = HashTable(json.load(db))

        print('{}The server is waiting for a connection...'.format(CONSOLE['success']))

    def mainloop(self):
        conn, addr = self.server.accept()
        print('{}Connected accepted!'.format(CONSOLE['success']))

        while True:
            request = conn.recv(1024).decode('utf-8').split(' ')
            if not request[0] or request[0] == 'EXIT':
                break

            if len(request) == 1:
                answer = '{}Invalid request'.format(CONSOLE['error'])
            else:
                answer = self.complete_command(request[0], request[1:])
            conn.sendall(answer.encode('utf-8'))

        print('{}Connection interrupted!'.format(CONSOLE['warning']))

    def complete_command(self, command, data):
        match command:
            case 'GET':
                return self.db_get(data[0])
            case 'SET':
                return self.db_set(data[0], *data[1:])
            case 'DEL' | 'DELETE':
                return self.db_del(data[0])
            case _:
                return '{}Command "{}" does not exist'.format(CONSOLE['error'], command)

    def db_get(self, key):
        response = self.db.get_value(key)
        if response:
            return CONSOLE['success'] + response

        return '{}"{}" not found :('.format(CONSOLE['error'], key)

    def db_set(self, key, *args):
        if args:
            response = self.db.set_value(key, ' '.join(args))
            if response:
                self.save_data()
                return '{}Data was added successful under key "{}"!'.format(CONSOLE['success'], key)

            return "{}This entry already exists".format(CONSOLE['warning'])

        return '{}Parameter "value" missing'.format(CONSOLE['error'])

    def db_del(self, key):
        response = self.db.del_value(key)
        if response:
            self.save_data()
            return '{}"{}" was successfully deleted from data base!'.format(CONSOLE['success'], key)

        return '{}Element "{}" does not exist'.format(CONSOLE['error'], key)

    def save_data(self):
        with open(ServerSocket.DATA_BASE, 'w') as db:
            db.write(json.dumps(self.db.in_dict()))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save_data()
        self.server.shutdown(socket.SHUT_RDWR)
        self.server.close()


if __name__ == '__main__':
    with ServerSocket(HOST, PORT) as server:
        try:
            while True:
                server.mainloop()
        except KeyboardInterrupt:
            print('\n{}Server shut down!'.format(CONSOLE['success']))
