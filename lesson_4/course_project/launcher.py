import socket
import subprocess
import time
from pathlib import Path
import time_app
from subprocess import Popen
from socket import *
# импорт констант для модулей

from time_app.variables import DEFAULT_PORT as TIME_PORT
from data.variables import DEFAULT_PORT as DATA_PORT
from udp.variables import DEFAULT_PORT as UDP_PORT
# Папка, в которой находится launcher.py
BASE_DIR = Path(__file__).resolve().parent




#DATA VARS
DATA_DIR = BASE_DIR / 'data'
DATA_SERVER = DATA_DIR / 'data_server.py'
DATA_CLIENT = DATA_DIR / 'data_client.py'


# TIME VARS
TIME_APP_DIR = BASE_DIR / 'time_app'
TIME_SERVER = TIME_APP_DIR / 'time_server.py'
TIME_CLIENT = TIME_APP_DIR / 'time_client.py'


#UDP VARS
UDP_DIR = BASE_DIR / 'udp'
UDP_SERVER = UDP_DIR / 'udp_server.py'
UDP_CLIENT = UDP_DIR / 'udp_client.py'

PROCESS = []


def start_script(dir_server, server) -> str:
    return f'''tell application "Terminal" 
                activate
            if (count of windows) is 0 then 
                do script "cd {dir_server} && python3 {server}" 
            else
                do script "cd {dir_server} && python3 {server}" in front window
            end if
            end tell'''




while True:
    ACTION = input(f'Привет! Выберите, какую пару сервер клиент запусить?\n'
                   f'1 - udp\n'
                   f'2- time_app\n'
                   f'3 - data\n'
                   f'q - выйти')
    if ACTION == 'q':
        break

    elif ACTION == '1':
        subprocess.Popen(['osascript', '-e', start_script(UDP_DIR, UDP_SERVER)])
        time.sleep(2)
        subprocess.run(['python3', UDP_CLIENT])

    elif ACTION == '2':
        subprocess.Popen(['osascript','-e', start_script(TIME_APP_DIR, TIME_SERVER)])
        time.sleep(2)
        subprocess.run(['python3', TIME_CLIENT])

    elif ACTION == '3':
        subprocess.Popen(['osascript','-e', start_script(DATA_DIR, DATA_SERVER)])
        time.sleep(2)
        subprocess.run(['python3', DATA_CLIENT])