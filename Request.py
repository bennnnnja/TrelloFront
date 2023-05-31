import socket

class Request:
    def init(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def new_user(self, login, password):
        data = f"NewUser?{login}:{password}"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        print(response.decode('utf-8'))
        return str(response.decode('utf-8'))

    def message(self, message):
        data = f"{message}"
        self.sock.send(data.encode('utf-8'))

    def entrance(self, login, password):
        data = f"Entrance?{login}:{password}"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        print(response.decode('utf-8'))
        return str(response.decode('utf-8'))

    def create_desk(self, desk_name, desk_type):
        data = f"NewDesk?{desk_name}:{desk_type}"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        print( response.decode('utf-8'))
        return str(response.decode('utf-8'))


    def UnloadData(self):
        data = f"UnloadData?"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        print(response.decode('utf-8'))







    def close(self):
        self.sock.close()




