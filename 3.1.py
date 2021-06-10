def division():
    div1 = number1 / number2 if number1 != 0 else print('Error!')
    div2 = number2 / number1 if number2 != 0 else print('Error!')
    return(div1, div2)

number1 = int(input('Введите первое число - '))
number2 = int(input('Введите второе число - '))
print(division())
