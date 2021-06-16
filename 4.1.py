from sys import argv

script_name, working, rate, prize = argv
print('Выработка в часах: ', working)
print('Ставка в час: ', rate)
print('Премия: ', prize)

def payment(argv):
    payment_prize = (int(working) * int(rate)) + int(prize)
    return payment_prize

print('Заработная плата: ', payment(argv))

