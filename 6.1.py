from time import sleep

class Trafficlight:
    __color = "Черный"

    def running(self):
        while True:
            print('Красный')
            sleep(7)
            print('Желтый')
            sleep(2)
            print('Зеленый')
            sleep(5)

trafficlight = Trafficlight()
trafficlight.running()
