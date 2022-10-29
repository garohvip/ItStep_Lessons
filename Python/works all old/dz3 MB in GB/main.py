def convert():
    z=int(input('Введите номер задания '))
    if z == 1:
        m=float(input('Введите количество мегабайт '))
        g=int
        g=m/1024
        print(g)
    elif z==2:
        g=float(input('Введите количество гигабайт '))
        m=int
        m=g*1024
        print(m)


print('Эта программа создана для конвертации мегабайт в гигабайты и обратно')
print('1.-конвертация мегабайт в гигабайты')
print('2.-конвертация гигабайты в мегабайты')

convert()
while True:
    flag = input('Ещё раз? [да/нет]: ')

    if flag == 'да':
        convert()
    else:
        break