number = int(input('Введите целое положительное число '))
n = number % 10 #находим последнюю цифру в числе
number = number // 10 #находим оставшиеся цифры в числе
while number > 0: #пока остаток больше 0, делаем цикл
    n_new = number % 10 #находим следующую цифру в числе
    if n_new > n: #сравниваем 2 найденные цифры (последнюю и предпоследнюю)
        n = n_new #при выполнении условия присваиваем наибольшее значение n
    number = number // 10 #находим следующую цифру числа
print('Наибольшее число ', n)
