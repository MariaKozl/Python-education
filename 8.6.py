class Storehouse:

    def __init__(self, name, price, numbers, specifications):
        self.name = name
        self.price = price
        self.numbers = numbers
        self.specifications = specifications
        self.store = []
        self.items = {'Устройство': self.name, 'Цена': self.price, 'Количество': self.numbers, 'Характеристики': self.specifications}

    def To_add_device(self):
        try:
            device_name = input('Введите устройство, которое хотите добавить на склад: ')
            device_price = int(input('Введите цену нового устройства: '))
            device_numbers = int(input('Введите количество новых устройств: '))
            device_specifications = input('Введите характеристики нового устройства: ')
            device = {'Устройство': device_name, 'Цена': device_price, 'Количество': device_numbers, 'Характеристики': device_specifications}
            self.items.update(device)
            self.store.append(self.items)
            print (f'Устройство {device} добавлено на склад {self.store}')
        except:
            return f'Данные введены неверно!'


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
print(printer_name.To_add_device())
print(scan_name.To_add_device())
print(copy_name.To_add_device())
