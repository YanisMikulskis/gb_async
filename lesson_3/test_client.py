import json
import unittest

from client_homework import presence, answer
from variables import *

class TestClient(unittest.TestCase):
    """
    Класс с тестами
    """
    def test_presence(self):
        '''Тест корректного запроса'''
        test = presence()
        test['time'] = 1.1
        self.assertEqual(test, {
                            'action': 'presence',
                            'time': 1.1,
                            'account_name':'Guest1'
    })


    def test_answer_200(self):
        test_message = {'response':200}
        test = answer(test_message)
        self.assertEqual(test, 'OK:200')

    def test_answer_300(self):
        test_message = {'response':205, 'error': 'Bad request'}
        test = answer(test_message)
        self.assertEqual(test, '400:Bad request')

    def test_not_requests(self):
        self.assertRaises(ValueError, answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()