class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма чисел равна: {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'Произведение чисел равно: {(self.a * other.a) - (self.b * other.b)} + {self.b * other.a}i'

num_1 = ComplexNumber(5, 4)
num_2 = ComplexNumber(3, 7)
print(num_1 + num_2)
print(num_1 * num_2)
