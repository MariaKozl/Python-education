def my_func(x, y): #функция с помощью возведения в степень
    if x >= 0 and y < 0:
        return x ** y

print(my_func(2, -5))


def my_func(x, y): #функция с помощью цикла
    degree = 1
    if x >= 0:
        for i in range(abs(y)):
            degree = degree * x
    if y < 0:
        degree = 1 / degree
    return degree

print(my_func(2, -5))
