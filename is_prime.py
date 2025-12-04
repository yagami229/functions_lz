def prime():
    p = int(input('Введите число: '))
    def simple(p):
        d = 2
        while p % d != 0:
            d +=  1 
        return d == p
    print(simple(p))
def main():
    prime()
if __name__== '__main__':
    main()


