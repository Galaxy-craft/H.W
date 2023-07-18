def isInteger(s):
    tmp = s.strip()
    tmp = s.strip('+-')
    try:
        tmp = int(s)     
        return f"{s} можно считать численным"
    except:
        return f'{s}, в этой строке обнаружены буквы'


a = input('Ввод: ')
print(isInteger(a))
