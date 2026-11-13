from socket import *
from variables import *


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', DEFAULT_PORT))
msg = 'Привет сервер!'.encode(ENCODING)
sock.sendall(msg)

message_server = sock.recv(MAX_PACKAGE_LENGTH).decode(DECODING)
print(f'Сервер прислал сообщение {message_server}')
