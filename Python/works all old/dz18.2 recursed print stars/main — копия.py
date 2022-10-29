def prodNumber(a):
    if a == 0:
        return "*"
    else:
        print("*", end=" ")
        return prodNumber(a-1)


try:
    prodNumber(int(input("Введите количество звездочек: ")))
except ValueError:
    print("Используй только цифры!!!")