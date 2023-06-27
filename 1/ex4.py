num2 = 0
while True:
    try:
        num = int(input('Введите число:'))
        if num < 0:
            num2 += num
        else:
            print(num2)
            break
    except:
        print('Число! НЕ БУКВУ!!')
