def ordinalDate(day, month, year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        days_in_month[1] = 29
    elif days_in_month[month - 1] < day:
        print('Ошибка')
        return

    for i in range(1, month):
        day += days_in_month[i - 1]

    print(day)


while True:
    day = int(input("Введите день:"))
    month = int(input("Введите месяц"))
    year = int(input("Введите год"))


    ordinalDate(day, month, year)
