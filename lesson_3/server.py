import sys
from socket import *

import time




class Server:
    def __init__(self, port, connections):
        self.sock_tcp = socket(AF_INET, SOCK_STREAM) #создает сокет TCP
        self.sock_udp = socket(AF_INET, SOCK_DGRAM)
        self.sock_tcp.bind(('', port)) # присваивает порт
        self.sock_tcp.listen(connections) # переходит в режим ожидания запросов
        self.max_size = 1024
        self.port = port
    def send_and_close(self, client, message):
        client.send(message)
        client.close()
    def tcp_1(self):
        while 1:
            client, addr = self.sock_tcp.accept() # принять запрос на соединение
            print(f'получен запрос на соединение от {addr}')
            time_message = time.ctime(time.time()) + '\n'
            self.send_and_close(client, time_message.encode('ascii'))
            # client.send(time_message.encode('ascii'))
            # client.close()
    def tcp_2(self):
        while 1:
            client, addr = self.sock_tcp.accept()
            data = client.recv(self.max_size).decode('utf-8')
            print(F'Юзер {addr} прислал сообщение: {data}')
            send_message = 'привет, клиент!'.encode('utf-8')
            client.send(send_message)
            client.close()

    def udp(self):
        self.sock_udp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # несколько приложений может слушать сокет
        self.sock_udp.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # определяем широковещательные пакеты
        self.sock_udp.bind(('', self.port))
        while 1:
            msg = self.sock_udp.recv(128)
            print(msg.decode('utf-8'))
    def login(self):
        while 1:
            client, addr = self.sock_tcp.accept()
            username = self.sock_tcp.recv(self.max_size)
            password = self.sock_tcp.recv(self.max_size)
            print(f'на сервер зашел {username.decode("utf-8")}')


def main_tcp1():
    server = Server(8888, 5)
    server.tcp_1()

def main_tcp2():
    server = Server(8007, 5)
    server.tcp_2()
def main_udp():
    server = Server(8889, 5)
    server.udp()
def main_login():
    server = Server(8010, 5)
    server.udp()
if __name__ == '__main__':
    main_tcp1()