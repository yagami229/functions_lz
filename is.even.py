import math
Z = int(input('Введите целое число: '))
def parity(Z):
    if Z % 2 == 0: print('Число четное')
    elif Z % 2 == 1: print('Число нечетное')
parity(Z)