profit = int(input('Введите значение выручки - '))
costs = int(input('Введите значение издержек - '))
if profit > costs:
    profitability = (profit - costs) / profit #рентабельность выручки
    print('Фирма работает в прибыль')
    print('Рентабельность выручки составляет -', profitability)
    size = int(input('Введите число сотрудников фирмы '))
    profit_onesize = (profit - costs) / size #прибыль в расчете на 1 сотрудника
    print('Прибыль фирмы в расчете на 1 отрудника составляет -', profit_onesize)
else:
    print('Фирма убыточна')
