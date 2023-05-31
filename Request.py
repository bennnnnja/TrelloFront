import socket

class Request:
    def __init__(self, host='127.0.0.1', port=65432):
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
        data = "UnloadData?"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        new_data = str(response.decode('utf-8'))
        data_list = new_data.split('\n')
        return data_list

    def SendJson(self, Jsonfile):
        data = "NewJson?"
        with open(f'json/{Jsonfile}.json', 'r') as f:
                for i in f:
                    data+=str(i)
                
        self.sock.send(data.encode('utf-8'))

    def LoadJson(self):
        data = "UnloadJson?"
        self.sock.send(data.encode('utf-8'))
        response = self.sock.recv(1024)
        
        
        with open("json/newjson.json", "a+") as f:
                f.write(str(response))







    def close(self):
        self.sock.close()




