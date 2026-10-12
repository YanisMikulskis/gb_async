from socket import *

import time
def server_tcp_1():
    s = socket(AF_INET, SOCK_STREAM) #создает сокет TCP
    s.bind(('', 8888)) # присваивает порт 8888
    s.listen(5) # переходит в режим ожидания запросов

    while True:
        client, addr = s.accept() # принять запрос на соединение
        print(f'получен запрос на соединение от {addr}')
        timestr = time.ctime(time.time()) + '\n'
        print(f'кодировка {timestr}')
        client.send(timestr.encode('ascii'))
        client.close()
def server_tcp_2():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 8007))
    s.listen(5)
    while 1:
        client, addr = s.accept()
        data = client.recv(1000)
        print(f"сообщение {data.decode('utf-8')} было получено от {addr}")
        msg = 'привет, клиент'
        client.send(msg.encode('utf-8'))
        client.close()

def server3_udp():
    s = socket(AF_INET, SOCK_DGRAM)

    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # несколько приложений может слушать сокет
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) # определяем широковещательные пакеты
    s.bind(('', 8889))
    while 1:
        msg = s.recv(128)
        print(msg.decode('utf-8'))


def server4_login():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 8010))
    s.listen(5)
    while 1:
        client, addr = s.accept()
        username = client.recv(1000)
        password = client.recv(100)
        print(f' на сервер зашел {username.decode('utf-8')}')


if __name__ == '__main__':
    server4_login()