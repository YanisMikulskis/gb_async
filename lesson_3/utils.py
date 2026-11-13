import json

from variables import *


def decoding(message_sender):
    '''Функция декодирования сообщения'''
    message = message_sender.recv(MAX_PACKAGE_LENGTH)
    if isinstance(message, bytes):
        decode_message = message.decode(DECODING)
        response = json.loads(decode_message)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def encoding_send(message_recipient, message):
    '''Функция кодирования и отправки сообщения'''
    js_message = json.dumps(message)
    encode_message = js_message.encode(ENCODING)
    message_recipient.send(encode_message)
