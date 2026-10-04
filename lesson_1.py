
def ex_1():
    dev = 'разработка'
    socket = 'сокет'
    wrap = 'декоратор'
    words = [dev, socket, wrap]
    for word in words:
        print(word)
        print(type(word))

    for word in words:
        code_word = word.encode('unicode_escape').decode('utf-8')
        print(code_word)
        print(type(code_word))



ex_1()
print(f'------')
def ex_2():
    cl = 'class'
    df = 'function'
    mt = 'method'
    for word in [cl, df, mt]:
        bytes_word = bytes(word, 'utf-8')
        print(bytes_word)
        print(type(bytes_word))
        print(len(bytes_word))
        print(f'***')


ex_2()
print(bytes('класс', 'utf-8'))

def ex_3():
    ...


def ex_4():
    word = 'разработка'
    word2 = 'soft'
    print(bytes(word, 'utf-8').decode())
    print(bytes(word2, 'utf-8').decode())
ex_4()

print(f'-----')
def ex_5():
    import subprocess
    import chardet
    commands = ['ping', 'ya.ru']

    res = subprocess.Popen(commands, stdout=subprocess.PIPE)
    for line in res.stdout:
        data = chardet.detect(line)

        line = line.decode(data['encoding']).encode('utf-8')
        print(line.decode('utf-8'))

ex_5()
