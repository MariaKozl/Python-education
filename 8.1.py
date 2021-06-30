class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def number_data(cls, data1):
        day, month, year = map(int, data1.split('-'))
        return data1

    @staticmethod
    def valid_data(data1):
        day, month, year = map(int, data1.split('-'))
        return data1 if 1 <= day <= 31 and 1 <= month <= 12 and 1000 <= year <= 9999 \
            else print('Дата введена неверно')

new_data = '29-6-2021'
print(Data.number_data(new_data))
print(Data.valid_data(new_data))
