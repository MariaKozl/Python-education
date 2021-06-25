class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self):
        weight = self._length * self._width * 25 * 5 / 1000
        return f'{self._length} м * {self._width} м * 25 кг * 5 см = {weight} т'

exemp = Road(5000, 20)
print(exemp.asphalt())
    
