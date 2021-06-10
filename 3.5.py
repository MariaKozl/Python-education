count = 0
try:
    while True:
        for i in map(int, input('Введите числа через пробел - ').split()):
            count += i
        print(count)
except ValueError:
        print(count)

