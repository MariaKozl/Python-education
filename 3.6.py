def int_func(word):
    return word.title()

print(int_func('text'))


many_words = input('Введите предложение - ').split()
for i in many_words:
    print(int_func(i))


