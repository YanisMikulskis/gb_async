import json
from socket import *

from variables import (DEFAULT_PORT,
                       ACTION, ENCODING,
                       DECODING, MAX_PACKAGE_LENGTH)

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1', DEFAULT_PORT))
# отправление сообщения серверу
msg = {
    ACTION: 'msg',
    'message': 'Сервер, который час?'
}

msg = json.dumps(msg).encode(ENCODING)
sock.sendall(msg)
#-------------
# получение ответа от сервера
answer_server = json.loads(sock.recv(MAX_PACKAGE_LENGTH).decode(DECODING))
print(f'Ответ сервера {answer_server}')