class Cell:

    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return f'Сумма равна {self.number + other.number}'

    def __sub__(self, other):
        return f'Разность равна {self.number - other.number}'\
            if (self.number - other.number) > 0 else f'Вычитание невозможно!'

    def __mul__(self, other):
        return f'Произведение равно {self.number * other.number}'

    def __truediv__(self, other):
        return f'Деление равно {self.number // other.number}'

    def make_order(self, other):
        return '\n'.join(['*' * other.number for _ in range(self.number // other.number)]) + '\n' + '*' * (self.number % other.number)


num1 = Cell(12)
num2 = Cell(5)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(Cell.make_order(num1, num2))


