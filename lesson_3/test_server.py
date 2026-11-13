import unittest

from variables import *
from server_homework import process_message_client


class TestServer(unittest.TestCase):
    def test_process_200(self):
        '''Тест функции, проверящий сообщение от клиента'''
        message = {
            ACTION:PRESENCE,
            ACCOUNT_NAME:'Guest1',
        }
        process = process_message_client(message)
        self.assertEqual(process, {RESPONSE:200})

    def test_process_400(self):
        message = {
            ACTION: PRESENCE,
            ACCOUNT_NAME: 'Guest2',
        }
        process = process_message_client(message)
        self.assertEqual(process, {RESPONSE: 400, ERROR: 'Bad Request'})

    def test_process_presence_bad(self):
        message = {
            ACTION: 'no presence',
            ACCOUNT_NAME: 'Guest1',
        }
        process = process_message_client(message)
        self.assertEqual(process, {RESPONSE: 400, ERROR: 'Bad Request'})
