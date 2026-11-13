import sys
from socket import *
from variables import *
from utils import *


def process_message_client(message):

    if ACTION in message and message[ACTION] == PRESENCE \
        and message[ACCOUNT_NAME] == 'Guest1':
        return {RESPONSE:200}
    return {RESPONSE: 400,
            ERROR: 'Bad Request'}


def main():
    try:
        port = int(sys.argv[2])
        address = sys.argv[1]
        if port < 1024 or port > 65535:
            raise ValueError
    except (IndexError, ValueError):
        port, address = DEFAULT_PORT, DEFAULT_IP_ADDRESS
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((address, port))
    sock.listen(MAX_CONNECTIONS)
    try:
        while 1:
            client, addr = sock.accept()
            try:
                message_from_client = decoding(client)
                response = process_message_client(message_from_client)
                encoding_send(client, response)
                client.close()
            except (ValueError, json.JSONDecodeError):
                print(f'ошибкаааааа')

            client.close()
    finally:
        sock.close()

if __name__ == '__main__':
    main()



