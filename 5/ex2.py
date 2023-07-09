def day(days):
    if days > 365:
        years = int(days)
        years /= 365
        years = int(years)
        print(years)
        days = days - years * 365

        if days >= 30:

            months = int(days / 30)
            print(months)
            print(days)
            days = days - (months * 30)
            print(f'{years} лет/год/года/годов, {months} месяца/месяцев, {days} дней ')

        else:
            print(f'{years} лет/год/года/годов, 0 месяцев, {days} дней ')
    else:
        months = int(days / 30)
        print(months)
        print(days)
        days = days - (months * 30)
        print(f'0 лет, {months} месяца/месяцев, {days} дней ')


a = int(input('Введите сколько дней'))
day(a)
