my_list = [7, 5, 3, 3, 2]
new_element = int(input('Введите новый элемент - '))
count = 0
for i in my_list:
    if new_element <= i:
        count += 1
my_list.insert(count, new_element)
print(my_list)

