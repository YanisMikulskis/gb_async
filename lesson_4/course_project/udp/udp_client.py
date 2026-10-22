import json
from socket import *

from lesson_4.course_project.udp.variables import ACTION, TIME, DEFAULT_PORT
import time
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', DEFAULT_PORT))
msg = {
    ACTION: 'msg',
    TIME: time.time(),
    'message': f'привет, сервер'
}
msg = json.dumps(msg).encode('utf-8')
sock.sendall(msg)
