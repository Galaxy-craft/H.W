def price(distance, base_price, raz_v_metr, na_skolko_merov):
    distance *= 1000
    price = base_price + (distance / na_skolko_merov) * raz_v_metr
    return price


distance = int(input("Какое расстояние в км?"))
base_price = int(input("Начальная цена?"))
raz_v_metr = int(input("За каждые сколько метров будут платить?"))
na_skolko_merov = int(input("И сколько будут платить?"))
fare = price(distance, base_price, raz_v_metr, na_skolko_merov)
print(f"Итоговая сумма оплаты такси: ${fare:.2f}")

