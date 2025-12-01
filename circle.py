import math

def circle():
    r = float(input('Введите радиус круга в сантиметрах '))
    pi = float (3.14)
    def dlina(r, pi):
        return 2*pi*r
    def square(r, pi):
        return pi*r**2
    print('длина окружности:', dlina(r, pi), 'см')
    print('Площадь окружности:', square(r, pi), 'см^2')

if __name__== '__main__':
    circle()
