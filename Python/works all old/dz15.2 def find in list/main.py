from time import sleep

def findInList(*args):
    ifka = 1
    kol = 0
    find = int(input("Введите число, которое хотите найти в списке: "))
    for i in range(len(args)):
        if find == args[i]:
            kol += 1
            if kol == 1:
                print("Ваше число", find, "находиться под номером", i+1)
            elif kol >= 2:
                print("О, еще было найдено ваше число", find, "под номером", i+1)
            ifka = 0
    if kol >= 2:
        if kol >= 2 and kol <= 4:
            print("Итого, число", find, "было найдено", kol, "штуки")
        elif kol >= 5:
            print("Итого, число", find, "было найдено", kol, "штук")
    if ifka == 1:
        print("Ваше число", find, "не найдено в списке")

while True:
    nyrepeat = ""
    box = []
    kch = int(input("Введите количество чисел (минимум 3, максимум 10): "))
    if kch <= 2 or kch >= 11:
        print("Введите корректное количество чисел!")
        sleep(0.5)
    else:
        for i in range(kch):
            print("Number ", i + 1, ": ", sep="", end="")
            box.append(int(input()))
        findInList(*box)
        print("Повторить? y/n")
        while True:
            repeat = input()
            if repeat == "y" or repeat == "n":
                if repeat == "n":
                    nyrepeat = "n"
                    break
                if repeat == "y":
                    break
            else:
                print("Введите либо \"y\" либо \"n\"")
        if nyrepeat == "n":
            break