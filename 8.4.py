class Storehouse:

    def __init__(self, name, price, numbers, specifications):
        self.name = name
        self.price = price
        self.numbers = numbers
        self.specifications = specifications

class Printer(Storehouse):

    def To_print(self):
        return f'Принтер {self.name} стоит {self.price}'

class Scaner(Storehouse):

    def To_scan(self):
        return f'На складе осталось {self.numbers} сканеров {self.name} '

class Copir(Storehouse):

    def To_copy(self):
        return f'Ксерокс {self.name} имеет характеристики: {self.specifications}'


printer_name = Printer('Samsung', 50000, 10, 'цветная печать')
scan_name = Scaner('Hp', 20000, 5, 'автоматическая подача')
copy_name = Copir('Canon', 40000, 8, 'копирует за 3 секунды')
print(printer_name.To_print())
print(scan_name.To_scan())
print(copy_name.To_copy())
