while True:
    try:
        num = int(input('Введите число:'))
        d = 2
        if num == 1:
            print('1 - это простое число')
        while d <= num:
            print('Пробуем делить на {}'.format(d))
            if num % d == 0:
                if d == num:
                    print(f'{num} - это число делится только на самого себя, значит оно простое')
                    break
                else:
                    print(f"{num} - это число не простое, а составное")
                    break

            else:
                d += 1
    except:
        print('Введите число! НЕ БУКВУ!!!!!!!')