num2 = 0
while True:
    try:
        num = int(input('Введите число:'))
        if num < 0:
            print(num2)
            break

        else:
            num2 += num
    except:
        print('Число! НЕ БУКВУ!!')
