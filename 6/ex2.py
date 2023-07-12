s = input('Введите текст ')
w = int(input('Введите ширину'))


def stroka(s, w):
    if len(s) >= w:
        print(s + '1')
    else:
        result = (w - len(s)) // 2
        print('|'+' ' * result + s + ' ' * result + '|')


stroka(s, w)
