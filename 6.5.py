class Stationary:

    def __init__(self, title="Запуск отрисовки"):
        self.title = title

    def draw(self):
        print(f'{self.title}')

class Pen(Stationary):

    def draw(self):
        print(f'Ручка пишет {self.title}')

class Pencil(Stationary):

    def draw(self):
        print(f'Карандаш рисует {self.title}')

class Marker(Stationary):

    def draw(self):
        print(f'Маркер выделяет {self.title}')

stat = Stationary()
stat.draw()

pen = Pen()
pen.draw()

pen_c = Pencil()
pen_c.draw()

mark = Marker()
mark.draw()

