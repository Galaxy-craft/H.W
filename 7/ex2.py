def precedence(b):
    if b == '+' or b == '-':
        return 1
    elif b == '*' or b == '/':
        return 2
    elif b == '^':
        return 3
    else:
        return -1


def staart():
    a = input("Введите оператор: ")
    c = precedence(a)
    if c == 1:
        print('Приоритет 1')
    elif c == 2:
        print('Приоритет 2')
    elif c == 3:
        print('Приоритет 3')
    else:
        print('Неккорректный ввод')


staart()
