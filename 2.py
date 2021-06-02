time = int(input('Введите время в секундах '))
hours = time // 3600
minuts = (time - hours * 3600) // 60
seconds = (time - hours * 3600) % 60
print (f'{hours}:{minuts}:{seconds}') # вывод в формате чч:мм:сс
