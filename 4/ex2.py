numbers = [1, 1]
a = 0
while True:
    num = int(input('Введите какое число вас интересует?'))
    try:
        print(numbers[num])
    except:
        while a < num - 2:
            calc = numbers[a] + numbers[a + 1]
            numbers.append(calc)
            print(numbers)
            a += 1
        print(numbers[num - 1])
