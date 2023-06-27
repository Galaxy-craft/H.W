number = int(input('.'))

i = 2
is_prime = True

while i < number:
    if number % i == 0:
        print('Составное')
        is_prime = False
        break
    i += 1
if is_prime:
    print('Простое')