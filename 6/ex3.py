def capital(s):
    s = s.lower()
    result = []
    zagl = True
    for check in s:
        if check.isalpha() and zagl:
            check = check.upper()
            zagl = False
                
        elif check == '.' or '!' == check or check == '?':
            zagl = True
        elif check == 'i' and result[-1].isspace() and result[+1].isspace:
            check = 'I'
        result.append(check)
    return ''.join(result)


text = input("Введите строку: ")
a = capital(text)
print(a)
