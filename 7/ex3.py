def prime(number):
    if number == 1 and number == 2:
        print(f'{number} - это простое число')

    for i in range(2, number + 1):
        if number % i == 0:
            if number == i:
                print(f'{number} делится только на самого себя и на 1, а значит оно простое')
                return
            else:
                print(f'{number} делится на {i} значит оно составное')
                return


def prime2(number):
    for i in range(2, number + 1):
        if number % i == 0:
            return True


num = int(input('Введите число'))
prime(num)
