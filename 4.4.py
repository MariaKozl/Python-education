from random import randint

my_list = [randint(0, 10) for _ in range(10)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_list)
print(new_list)
