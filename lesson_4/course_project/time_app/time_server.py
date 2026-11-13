from socket import *
import json
import time
from variables import (DEFAULT_PORT,
                       MAX_CONNECTIONS,
                       MAX_PACKAGE_LENGTH,
                       DECODING, ENCODING, ACTION)

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', DEFAULT_PORT))
sock.listen(MAX_CONNECTIONS)
try:
    while 1:
        #Получение сообщения от клиента
        client, addr = sock.accept()
        msg = client.recv(MAX_PACKAGE_LENGTH)
        msg = json.loads(msg.decode(DECODING))
        print(f'{addr} прислал сообщение: {msg}')
        # -------------
        #----ответ сервера
        time_now = time.ctime(time.time()) + '\n'
        send_message = {ACTION: 'msg',
                        'message':f'Привет клиент! Время {time_now}'}
        send_message = json.dumps(send_message).encode(ENCODING)
        #--------------------
        client.send(send_message)
        client.close()
finally:
    sock.close()


