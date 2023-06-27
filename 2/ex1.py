num1 = input('Введите до какого числа надо: ')
num2 = input('Введите на что они должны будут делится: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    for i in range(1, num1):
        if i % num2 == 0:
            print(i)
except:
    print('Введите число!')