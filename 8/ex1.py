from random import randint

random_password = []


def password():
    global random_password
    a = randint(7, 10)
    for i in range(1, a):
        b = randint(33, 126)
        random_password.append(chr(b))
    return ''.join(random_password)


def main():
    print(password())


if __name__ == '__main__':
    main()
