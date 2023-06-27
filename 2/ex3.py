while True:
    num = str(input('Введите число'))
    if len(num) == 1:
        print('Введите двух знгачное число')
    else:
        if num == num[:: -1]:
            print('Это палиндромом')
        else:
            print("Это не палиндромом")
    # num_string = str(num)

    # if num == num[:: -1]:
    #     print('Это палиндромом')
    # else:
    #     print("Это не палиндромом")