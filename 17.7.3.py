per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
a = list(map(float,per_cent.values()))
money = input("Укажите сумму вклада: ")
c = float(money)/100
deposit = [round((i * c),2) for i in a ]
print("накопленные средства за год вклада в каждом из банков: ", deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))













