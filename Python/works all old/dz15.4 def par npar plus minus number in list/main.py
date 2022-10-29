from time import sleep
def doUndoPlMi(*args):
    doubl = 0
    undoubl = 0
    plus = 0
    minus = 0
    zero = 0
    for i in range(len(args)):
        if args[i] % 2 == 0:
            doubl += 1
        else:
            undoubl += 1
    for i in range(len(args)):
        if args[i] > 0:
            plus += 1
        elif args[i] == 0:
            zero += 1
        else:
            minus += 1

    if doubl == 0:
        print("Парных чисел не найдено")
    elif doubl == 1:
        print("Парных чисел:", doubl, "штука")
    elif doubl >= 2 and doubl <= 4:
        print("Парных чисел:", doubl, "штуки")
    elif doubl >= 5:
        print("Парных чисел:", doubl, "штук")

    if undoubl == 0:
        print("Непарных чисел не найдено")
    elif undoubl == 1:
        print("Непарных чисел:", undoubl, "штука")
    elif undoubl >= 2 and undoubl <= 4:
        print("Непарных чисел:", undoubl, "штуки")
    elif undoubl >= 5:
        print("Непарных чисел:", undoubl, "штук")

    if plus == 0:
        print("Положительных чисел не найдено")
    elif plus == 1:
        print("Положительных чисел:", plus, "штука")
    elif plus >= 2 and plus <= 4:
        print("Положительных чисел:", plus, "штуки")
    elif plus >= 5:
        print("Положительных чисел:", plus, "штук")

    if minus == 0:
        print("Отрицательных чисел не найдено")
    elif minus == 1:
        print("Отрицательных чисел:", minus, "штука")
    elif minus >= 2 and minus <= 4:
        print("Отрицательных чисел:", minus, "штуки")
    elif minus >= 5:
        print("Отрицательных чисел:", minus, "штук")

    if zero > 0:
        if zero == 1:
            print("Так же в вашем списке присутствует", zero, "ноль")
        elif zero >= 2:
            print("Так же в вашем списке присутствуют нули в количестве", zero, "штук")
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
        doUndoPlMi(*box)
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