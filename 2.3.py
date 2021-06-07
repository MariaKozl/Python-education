#через dict
number_month = int(input('Введите номер месяца - '))
my_dict = {1: 'зима', #создаем словарь
           2: 'зима',
           3: 'весна',
           4: 'весна',
           5: 'весна',
           6: 'лето',
           7: 'лето',
           8: 'лето',
           9: 'осень',
           10: 'осень',
           11: 'осень',
           12: 'зима'}
print(my_dict.get(number_month)) #получаем значение по ключу

#через list
number_month = int(input('Введите номер месяца - '))
my_list = ('зима', 'весна', 'лето', 'осень') #создаем список
if number_month == 1 or number_month == 2 or number_month == 12:
    print(my_list[0])
elif number_month == 3 or number_month == 4 or number_month == 5:
    print(my_list[1])
elif number_month == 6 or number_month == 7 or number_month == 8:
    print(my_list[2])
else:
    print(my_list[3])
