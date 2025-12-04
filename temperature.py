def temp():
    C = float(input('Введите температуру в градусах Цельсия: '))
    def farengeit(C):
        return C*1.8+32
    print('Температура в градусах по фаренгейту:', farengeit(C))
def main():
    temp()
if __name__== '__main__':
    main()


