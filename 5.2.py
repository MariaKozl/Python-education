file = open('data2.txt', 'r')
count_line = 0
for line in file:
    count_line += 1
    words = line.split()
    print(f'{words} - количество слов в строке равно {len(words)} шт')
print(f'Количество строк равно {count_line} шт')
file.close()
