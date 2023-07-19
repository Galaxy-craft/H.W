from random import randint

new_number = []
d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def number():
    global new_number
    b = 0
    while b < 4:
        a = randint(0, 9)
        a = str(a)
        new_number.append(a)
        b += 1

    c = 0
    while c < 3:
        f = randint(0, 25)
        f = d[f]
        new_number.append(f)
        c += 1
    return ''.join(new_number)


def main():
    print(number())


if __name__ == '__main__':
    main()