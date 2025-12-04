import math

def even():
    Z = int(input('Введите целое число: '))
    def parity(Z):
        if Z % 2 == 0: print('Число четное')
        elif Z % 2 == 1: print('Число нечетное')
    print(parity(Z))
def main():
    even()
if __name__== '__main__':
    even()
    

