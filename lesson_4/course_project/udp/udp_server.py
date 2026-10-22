import json
from socket import *

from lesson_4.course_project.udp.variables import (DEFAULT_PORT, MAX_CONNECTIONS,
                                                   MAX_PACKAGE_LENGTH, DECODING)

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', DEFAULT_PORT))
sock.listen(MAX_CONNECTIONS)
while 1:
    client, addr = sock.accept()
    message = client.recv(MAX_PACKAGE_LENGTH)
    message_json = json.loads(message.decode(DECODING))
    print(f'Сообщение от клиента на сервере: {message_json}')
