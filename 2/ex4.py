num1 = input('Введите до какого числа надо: ')
num2 = input('Введите первое кратное число: ')
num3 = input('Введите второе кратоное число: ')

spisok = []
try:
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)
    for i in range(1, num1):
        if i % num2 == 0 or i % num3 == 0:
            spisok.append(i)
        else:
            print(i)

except:
    print('Введите число!')
