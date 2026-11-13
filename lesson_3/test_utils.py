import unittest
from unittest import *
import json
from variables import *

from utils import *
class TestSocket:
    def __init__(self, test_dict):
        self.test_dict = test_dict
        self.encoding_mes = None
        self.rec_mes = None

    def send(self, message_to_send):
        '''
        Это фейковая встроенная функция send() в которой мы создаем
        сначала эталон того, что должно быть после работы тестируемой функции,
        а потом передаем в сокет то, что принимает эта функция
        :param message_to_send:
        :return:
        '''
        json_test_dict = json.dumps(self.test_dict)
        self.encoding_mes = json_test_dict.encode(ENCODING)
        self.rec_mes = message_to_send

    def recv(self, max_len):
        '''
        То, что получает сокет
        :return:
        '''
        json_test_dict = json.dumps(self.test_dict)
        return json_test_dict.encode(ENCODING)



class TestUtils(unittest.TestCase):

    test_dict_send = {
        ACTION: PRESENCE,
        TIME: 1.1,
        USER: {
            ACCOUNT_NAME:'test_name'
        }
    }
    test_dict_recv_ok = {
        RESPONSE: 200
    }
    test_dict_recv_error = {
        RESPONSE: 200,
        ERROR: 'Bad request'
    }
    def test_encoding_send(self):
        test_socket = TestSocket(self.test_dict_send)
        encoding_send(test_socket, self.test_dict_send)
        # включается send тестового сокета и в него на вход подается как раз измененная
        # функция из encoding_send и сравнивается с изменением внутри теста в методе send
        self.assertEqual(test_socket.encoding_mes, test_socket.rec_mes)
        with self.assertRaises(Exception):
            encoding_send(test_socket, test_socket)

    def test_decoding(self):
        self.test_socket_ok = TestSocket(self.test_dict_recv_ok)
        self.test_socket_err = TestSocket(self.test_dict_recv_error)
        self.assertEqual(decoding(self.test_socket_ok), self.test_dict_recv_ok)
        self.assertEqual(decoding(self.test_socket_err), self.test_dict_recv_error)
if __name__ == '__main__':
    unittest.main()