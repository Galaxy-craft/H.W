number = int(input("."))

i = 2
while i < number:
    if number % i == 0:
        print(number, "Это составное")
        break
    elif i == number - 1:
        print('Простое')
    i += 1