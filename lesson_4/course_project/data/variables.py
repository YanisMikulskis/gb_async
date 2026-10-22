import time


# порт по умолчанию для подключения
DEFAULT_PORT = 8888
# ip-адрес для подключения
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная длина подключений
MAX_CONNECTIONS = 5
# Максимальная длина сообщения в байтах
MAX_PACKAGE_LENGTH = 1024
# Кодировка проекта
ENCODING, DECODING = 'utf-8', 'utf-8'


#JIM протокол
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
MESSAGE = 'message'
#прочие ключи
RESPONSE = 'response'
PRESENCE = 'presence'
ERROR = 'error'