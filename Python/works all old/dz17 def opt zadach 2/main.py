from random import randint
from sympy import isprime
#------------------------------Quest 1, part 2--------------------------------

# def multiplyNumbers(args):
#     mp = 1
#     for i in args:
#         mp *= i
#     return mp
#
# lists = [randint(1, 10) for j in range(int(input("Введите количество чисел которое хотите умножить: ")))]
# print("Произведение чисел из списка", lists, "равно", multiplyNumbers(lists))

#------------------------------Quest 2, part 2--------------------------------

# def minNumberFromList(args):
#     return min(args)
#
# lists = [randint(-1000, 1000) for j in range(int(input("Введите количество чисел: ")))]
# print("Минимальное число из списка", lists, "это:", minNumberFromList(lists))

#------------------------------Quest 3, part 2--------------------------------

# primeLists = []
#
# def primeNumber(args):
#     k = 0
#     global primeLists
#     for i in args:
#         if isprime(i):
#             k += 1
#             primeLists.append(i)
#     return k
#
# lists = [randint(10, 100) for j in range(int(input("Введите количество чисел: ")))]
# print("Ваш список:", lists)
# print("Количество простых чисел из вашего списка: ", primeNumber(lists))
# print("Список простых чисел из вашего списка:", primeLists)

#------------------------------Quest 4, part 2--------------------------------

# def deleteNumber(args, delNumber):
#     k = 0
#     while True:
#         for i in args:
#             if i == delNumber:
#                 args.remove(delNumber)
#                 k += 1
#         break
#     return k
#
# lists = [randint(1, 5) for j in range(int(input("Введите количество чисел: ")))]
# print("Ваш список:", lists)
# print("Количество удаленных чисел из списка:", deleteNumber(lists, int(input("Введите число, которое хотите удалить из списка: "))))
# print("Ваш список теперь:", lists)

#------------------------------Quest 5, part 2--------------------------------

# def joinList(args1, args2):
#     for i in args2:
#         args1.append(i)
#     return args1
#
# list1 = [randint(-1000, 0) for j in range(5)]
# list2 = [randint(0, 1000) for i in range(5)]
#
# print("Ваш первый список:", list1)
# print("Ваш второй список:", list2)
# print("Ваш список теперь:", joinList(list1, list2))

#------------------------------Quest 6, part 2--------------------------------

def degreeNumbers(args, degNum):
    newList = []
    for i in args:
        newList.append(i**degNum)
    return newList

lists = [randint(1, 10) for j in range(int(input("Введите количество чисел: ")))]
print("Ваш список:", lists)
print("Ваш новый список:", degreeNumbers(lists, int(input("Введите число, которое будет степенью: "))))