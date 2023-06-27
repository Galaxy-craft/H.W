num1 = int(input('Введите первое число'))
num2 = int(input('Введите второе число'))

kr = 2
while True:
    if kr % num1 == 0 and kr % num2 == 0:
        print(kr)
        break
    else:
        kr += 1
