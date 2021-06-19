mydict = {}
with open('data6.txt', encoding='utf-8') as f:
    for line in f:
        name, stats = line.split(':')
        elems = [i for i in stats if i == ' ' or (i >= '0' and i <= '9')]
        name_sum = sum(map(int, "".join(elems).split()))
        mydict[name] = name_sum
print(f'{mydict}')
