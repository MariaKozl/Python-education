from functools import reduce

def new_list(el_1, el_2):
    return el_1 * el_2

my_list = [el for el in range(100, 1001, 2)]
print(my_list)
print(reduce(new_list, my_list))
