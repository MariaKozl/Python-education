with open ('data3.txt', 'r', encoding='utf-8') as file:
    dict_data = {line.split()[0]: float(line.split()[1]) for line in file}
    print(f'Средний доход равен = {round(sum(dict_data.values()) / len(dict_data), 3)}')
    print(f'Оклад менее 20тыс имеет {[e[0] for e in dict_data.items() if e[1] < 20000]}')

