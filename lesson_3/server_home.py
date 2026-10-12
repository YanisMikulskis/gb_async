import json
from socket import *
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-p', type=int, default=7777)
parser.add_argument('-a', default='')
args = parser.parse_args()


s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8000))
s.listen(5)
while 1:
    client, addr = s.accept()
    msg = client.recv(1000)
    request = json.loads(msg.decode('utf-8'))
    response = {
        'response': 200,
        'alert': 'OK'
    }
    print(request)
    send_message = json.dumps(response).encode('utf-8')
    client.sendall(send_message)
    client.close()




