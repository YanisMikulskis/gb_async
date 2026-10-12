import json
import time
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8000))
msg = {
    'action': 'msg',
    'time':time.time(),
    'message':f'привет, домашний сервер'
}
msg = json.dumps(msg).encode('utf-8')
s.sendall(msg)
answer_server = json.loads(s.recv(1000).decode('utf-8'))
print(f'ответ сервера {answer_server}')
s.close()