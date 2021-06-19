f = open('data.txt', 'w')
while True:
    line = input('Введите строку: ')
    if not line:
        break
    f.write(line)
f.close()
