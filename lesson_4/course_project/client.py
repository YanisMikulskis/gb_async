import json
import time_app
from socket import *
from lesson_4.course_project.udp.variables import (DEFAULT_PORT,
                                                   ACTION, TIME, MESSAGE)
step = 1

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', DEFAULT_PORT))
msg = {
    ACTION: 'msg',
    TIME: time_app.time(),
    MESSAGE: f'привет, сервер {step}'
}
msg = json.dumps(msg).encode('utf-8')
sock.sendall(msg)
answer_server = json.loads(sock.recv(1000).decode('utf-8'))
print(f'ответ сервера {answer_server}')

step += 1
time_app.sleep(1)
