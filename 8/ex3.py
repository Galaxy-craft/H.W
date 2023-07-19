def check_password(password):
    # zagl = False
    # nij = False
    # number = False
    # length = False
    # password = []
    if len(password) >= 8:
        if password.isupper():
            return False
        elif password.islower():
            return False
        else:
            if password.isdigit():
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
