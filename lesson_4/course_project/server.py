import json
from socket import *
import argparse
from udp.udp_server import *

sock = SOCKET_SERVER
sock.bind(('', 9999))
sock.listen(5)
step = 0
while 1:
    client, addr = sock.accept()
    client_message = client.recv(1000)

    print(f'Сообщение от пользователя {addr}: '
          f'{json.loads(client_message.decode("utf-8"))}')
    response = {
        'response': RESPONSE,
        'message': f'привет клиент {addr}!',
        'alert': ALERT
    }

    send_message = json.dumps(response).encode('utf-8')
    client.sendall(send_message)

