class Exception:

    def __init__(self):
        self.my_list = []

    def input_numbers(self):
        while True:
            try:
                number = int(input('Введите числа в список, по окончанию нажмите "stop"'))
                new_list = self.my_list.append(number)
            except:
                print('Вы ввели не число!')


list = Exception()
print(list.input_numbers())

