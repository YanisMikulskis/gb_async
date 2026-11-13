from socket import *
from variables import *


sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', DEFAULT_PORT))
sock.listen(MAX_CONNECTIONS)

try:
    while 1:
        client, addr = sock.accept()
        msg = client.recv(MAX_PACKAGE_LENGTH).decode(DECODING)
        print(f'Сообще юзера: {msg}')


        send_message = f'Привет, клиент!'.encode(ENCODING)

        client.send(send_message)
        client.close()
finally:
    print(F'серв хакрыт')
    sock.close()
