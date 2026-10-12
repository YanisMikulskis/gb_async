# Программа клиента, запрашивающего текущее время
from socket import *
from time import sleep
def client1():
    s = socket(AF_INET, SOCK_STREAM) #создает сокет TCP
    s.connect(('localhost', 8888)) # соединиться с сервером
    tm = s.recv(1024) # принять не более 1024 байтов данных
    s.close()
    print(f'Текущее время {tm.decode('ascii')}')
    print(f'кодировка {tm}')


def client2():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8007))
    msg = f'привет сервер'
    s.send(msg.encode('utf-8'))

    data = s.recv(100000)
    print(f'получен ответ от сервера {data.decode("utf-8")}')
    s.close()

def client3():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    while 1:
        msg = 'запрос'.encode('utf-8')
        s.sendto(msg, ('localhost', 8889))
def client4():
    import hashlib
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 8010))
    username = input('Никнейм: ') + '\n'
    password = input('Пароль: ')
    password = hashlib.sha256(password.encode()).hexdigest()
    s.send(username.encode('utf-8'), )
    s.send(password.encode(), )


if __name__ == '__main__':
    while True:
        sleep(1)
        client4()