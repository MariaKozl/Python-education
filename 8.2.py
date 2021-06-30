class Zerodivision:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def error(a, b):
        try:
            return (a / b)
        except ZeroDivisionError:
            return (f'На ноль делить нельзя!')


print(Zerodivision.error(15, 3))

div = Zerodivision(15, 3)
print(div.error(15, 0))
