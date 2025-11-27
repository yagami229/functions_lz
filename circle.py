import math
r = float(input('Введите радиус круга в сантиметрах '))
pi = float (3.14)
def dlina(r, pi):
    return 2*pi*r
print('длина окружности:', dlina(r, pi), 'см')
def square(r, pi):
    return pi*r**2
print('Площадь окружности:', square(r, pi), 'см^2')
