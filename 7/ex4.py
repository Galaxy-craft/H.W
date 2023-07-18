def prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def nextPrime(n):
    num = n + 1
    while True:
        if prime(num):
            return num
        num += 1


number = int(input("Введите число: "))
result = nextPrime(number)
print(result)
