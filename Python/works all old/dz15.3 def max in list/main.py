from time import sleep

def maxInList(*args):
    return print(max(args))

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
        maxInList(*box)
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