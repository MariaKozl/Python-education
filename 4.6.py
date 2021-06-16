from itertools import count, cycle

for i in count(int(input('Введите начальное число от 1 до 5: '))):#программа начнет цикл от 1 до 5
    print(i)
    if i == 10: #программа остановит цикл на числе 10
        break

my_list = input('Введите список, разделяя элементы пробелом, для выхода из программы нажмите q: ').split()
iter = cycle(my_list)
exit = None

while exit != 'q':
    print(next(iter), end='')
    exit = input()


