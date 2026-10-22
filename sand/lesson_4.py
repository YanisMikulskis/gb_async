from collections import namedtuple
Salary = namedtuple('Salary', ['first_name', 'last_name', 'work', 'rate'])
salary = Salary('John', 'Smith', 40, 1000)

def get_salary(line):

    line = line.split()
    if line:
        data = Salary(*line)

        fio = ' '.join([data.first_name, data.last_name])
        rate = int(data.work) * int(data.rate)
        res = [fio, rate]
    else:
        return f'no data'
    return res
arr = []
def deco(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    arr.append(wrapper)
    return wrapper

def res_1():
    for result in arr:
        result()

@deco
def test_salary_summ():

    assert get_salary(line='Bob   Anderson  50   1000') == ['Bob Anderson', 50000], 'нет данных'
@deco
def test_salary_fio():
    assert get_salary(line='Bob   Anderson  50   1000')[0] == 'Bob Anderson', 'неверное имя'

# res_1()
# if __name__ == '__main__':
#
#     res_1()
#----------unittests

import unittest
#
# def sum_kv(i,j):
#     return i**2 + j**2
#
#
# class TestSumKv(unittest.TestCase):
#     def test_1(self):
#         self.assertEqual(sum_kv(2,3), 13)


def splitter(line, types=None, delimiter=None):
    fields = line.split(delimiter)
    if types:
        fields = [ty(val) for ty,val in zip(types, fields)]
    return fields



class TestSplitter(unittest.TestCase):
    def test_1(self):
        r = splitter('GOOG   1000   40    50')
        self.assertEqual(r, ['GOOG', '1000', '40', '50'])
    def test_2(self):
        r = splitter('GOOG   1000   40    50', [str, int, float, bool])
        self.assertEqual(r, ['GOOG', 1000, 40.0, True])


print(splitter('GOOG   1000   40    50'))
print(splitter('GOOG   1000   40    50', [str, int, float, bool]))
unittest.main()