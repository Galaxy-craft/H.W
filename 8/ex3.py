def check_password(passw):
    # zagl = False
    # nij = False
    # number = False
    # length = False
    password = []
    if len(passw) >= 8:
        if passw.isupper():
            return False
        elif passw.islower():
            return False
        else:
            if passw.isdigit():
                return False
            else:
                return True
    else:
        return False


def main():
    a = str(input('Введите пароль'))
    if check_password(a):
        print('Пароль надёжный')
    else:
        print('Пароль не надёжный')


if __name__ == '__main__':
    main()
