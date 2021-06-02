number = int(input('Введите целое однозначное число '))
number_2 = number * 10 + number
number_3 = number * 100 + number_2
summ = number + number_2 + number_3
print(f'{number}+{number_2}+{number_3}={summ}')
