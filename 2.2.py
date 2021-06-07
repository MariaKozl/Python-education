count = int(input('Введите количество элементов списка - '))
first_list = []
i = 0
while i < count: #цикл на ввод элементов списка
    element = int(input('Введите элемент списка - '))
    first_list.append(element)
    i += 1

for el in range(0, len(first_list)-1, 2): #цикл на перебор длины списка
    first_list[el], first_list[el+1] = first_list[el+1], first_list[el] #обмен значениями
print(first_list)

