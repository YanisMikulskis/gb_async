import time
import sys
from utils import *
from socket import *

def presence(account_name = 'Guest1'):
    """
    Проверка сообщения клиента
    :param account_name:
    :return:
    """
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        ACCOUNT_NAME:account_name
    }
    return out


def answer(message):
    """
    Проверка ответа сервера
    :param message:
    :return:
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return f'OK:200'
        return f'400:{message[ERROR]}'
    raise ValueError


def main():
    """Создание клиента"""
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print(f'порт должен быть другого значения')
        sys.exit()
    sock = socket(AF_INET, SOCK_STREAM)

    sock.connect((server_address, server_port))
    message_to_server = presence()
    encoding_send(sock, message_to_server)
    try:
        answer_server = answer(decoding(sock))
        print(f'ОТВЕТ СЕРВАКА {answer_server}')
    except (ValueError, json.JSONDecodeError):
        print(f'декодировать не удалось')

if __name__ == '__main__':
    main()






















# def create_presence(account_name='Guest1'):
#     '''Функция присутствия клиента на сервере'''
#     out = {
#         ACTION:ACTION,
#         TIME: time.time(),
#         USER: {
#             ACCOUNT_NAME:account_name
#         }
#     }
#     return out
#
# def process_ans(message):
#     '''Анализ ответа сервера'''
#     if RESPONSE in message:
#         if message[RESPONSE] == 200:
#             return '200: ok'
#         return f'400: {message[ERROR]}'
#     raise ValueError
#
#
# def main():
#     '''Создание клиента'''
#
#     #Загружаем параметры командной строки
#     try:
#         server_address= sys.argv[1]
#         server_port = int(sys.argv[2])
#         if server_port < 1024 or server_port > 65535:
#             raise ValueError
#     except IndexError:
#         server_address = DEFAULT_IP_ADDRESS
#         server_port = DEFAULT_PORT
#     except ValueError:
#         print(F'не тот диапазон')
#         sys.exit()
#
#     # инициализация сокета и обмен
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind((server_address, server_port))
#     message_to_server = create_presence()
#     encoding_send(sock, message_to_server)
#     try:
#         answer = process_ans(decoding(sock))
#         print(answer)
#     except (ValueError, json.JSONDecodeError):
#         print(f'не удалось декодировать данное сообщение')
