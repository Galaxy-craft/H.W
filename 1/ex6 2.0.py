from random import randint

numhistory = 0
ogr = 0
while ogr <= 100:
    num = input("Введите число:")
    try:
        num = int(num)
        if num == 0 and numhistory == False:
            print('Надо начинать с 1. Переиграем')
            break
        elif num % 3 == 0:
            print('Вы проиграли! Надо было сказать Fizz')
            break
        elif num % 5 == 0:
            print('Вы проиграли! Надо было сказать Buzz')
            break
        elif num % 5 == 0 and num % 3 == 0:
            print('Вы проиграли! Надо было сказать FizzBuzz')
            break
        else:
            c = ["Отлично!", "Молодец!", "Идём дальше", "Ого, верно!"]
            b = randint(0, 3)
            if numhistory == num:
                print("Эту цифру вы уже писали до этого! Так нельзя!")
                break
            else:
                if numhistory == num - 1:
                    numhistory = num
                    ogr += 1
                    print(c[b])
                else:
                    print('Номера должны идти по порядку........')
                    break

    except:
        num = str(num.lower())
        if num == 'fizzbuzz' and numhistory % 3 == 2 and numhistory % 5 == 4:
            print('Верно!')
            numhistory += 1
            ogr += 1
        elif num == 'fizz' and numhistory % 3 == 2:
            if numhistory % 5 == 4:
                print('Надо было ввести FizzBuzz')
            else:
                print('Верно!')
                numhistory += 1
                ogr += 1
        elif num == 'buzz' and numhistory % 5 == 4:
            if numhistory % 3 == 2:
                print('Надо было ввести FizzBuzz')
                break
            else:
                print('Отлично!! Идём дальше')
                numhistory += 1
                ogr += 1
        else:
            print('Неправильно!')
            break
