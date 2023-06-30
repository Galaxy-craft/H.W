spisok = []

while True:
    inp = input('Введите число которое вы хотите внести в список:')

    if inp.lower() == 'stop':
        break
    else:
        inp = int(inp)
        spisok.append(inp)

big = spisok[0]
for i in spisok:
    if i > big:
        big = i
print(f"Наибольшее число: {big}")

