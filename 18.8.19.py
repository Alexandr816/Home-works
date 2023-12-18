

tickets = int(input("Введите нужное количество билетов: "))
def costa(l):
    free = 0
    cheep = 990
    whole_price = 1390
    cond_free = None
    cond_cheep = None
    cond_whole_price = None
    price = None
    discount = None


    age = list(map(int,input(f"Через пробел введите возраст {l} участников: ").split()))
    if tickets == len(age):
        print(f"Рассчет стоимости {l} билетов")
        for i, j in enumerate(age):
            cond_free = [(j * 0) for j in age if j < 18]
            cond_cheep = [(j / j * 990) for j in age if 18 <= j <= 25]
            cond_whole_price = [(j / j * 1390) for j in age if j > 25]
            price = (free * len(cond_free)) + (cheep * len(cond_cheep)) + (whole_price * len(cond_whole_price))
            if len(age) > 3:
                discount = price / 100 * 10
                price = price - discount
    else:
        print("Проверьте введенные данные")

    print("Цена без скидки: ", discount + price)
    print("Полная цена за билеты составит: ", price)

costa(tickets)










