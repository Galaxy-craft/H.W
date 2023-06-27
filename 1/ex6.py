b = 0
# for i in range(1, 101):
while b < 101:
    if b % 3 == 0 and b % 5 == 0:
        print('FizzBuzz')
    elif b % 3 == 0:
        print('Fizz')
    elif b % 5 == 0:
        print('Buzz')
    else:
        print(b)
    b += 1
