from random import randint
#--------------------------Quest 1, part 1------------------------------

# print("“Don’t compare yourself with anyone in this world…\n\tif you do so, you are insulting yourself.”\n\t\t\t\t\t\t\t\t\t\t\t\tBill Gates")

#--------------------------Quest 2, part 1------------------------------

# def doubleNumbers(first_num, last_num):
#     doubleNum = [i for i in range(first_num, last_num) if i % 2 == 0]
#     return tuple(doubleNum)
#
# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число (должно быть > первого числа): "))
# if number1 < number2:
#     print(doubleNumbers(number1, number2))
# else:
#     print("Второе число должно быть больше первого числа!!!")

#---------------------------Quest 3, part 1------------------------------

# def squareFigure(side, full, symbol=""):
#     if full == "y":
#         for i in range(side):
#             for j in range(side-1):
#                 print(symbol, end="  ")
#             print(symbol)
#         return
#     elif full == "n":
#         for i in range(side+1):
#             if i == 1 or side <= i <= side+1:
#                 for j in range(side-1):
#                     print(symbol, end="  ")
#                 print(symbol)
#             elif 2 <= i < side:
#                 print(symbol, end="  ")
#                 for j in range(side-2):
#                     print(" ", end="  ")
#                 print(symbol)
#         return
#     else:
#         return print("Введите либо \"y\", либо \"n\"")
#
#
# squareFigure(int(input("Введите размер квадрата: ")), (input("Заполненный или нет? y/n: ")), input("Из какого символа будет создан квадрат?: "))

#-----------------------------Quest 4, part 1----------------------------

# def minNumber(setOfNumber):
#     return min(setOfNumber)
#
# numberList = [randint(-1000, 1000) for i in range(int(input("Введите количетсво чисел: ")))]
# print("Минимальное число среди всех чисел", numberList, "=", minNumber(numberList))

#-----------------------------Quest 5, part 1-----------------------------

# def multiplyNumbers(firstRange, lastRange):
#     mp = 1
#     if firstRange > lastRange:
#         firstRange, lastRange = lastRange, firstRange
#     for i in range(firstRange, lastRange):
#         mp *= i
#     return mp
#
#
# print(multiplyNumbers(int(input("Введите первое число диапазона: ")), int(input("Введите второе число диапазона: "))))

#--------------------------Quest 6, part 1-----------------------------

# def countNumbersInNumber(oneNumber):
#     oneNumber = str(oneNumber)
#     countNumber = 0
#     for i in oneNumber:
#         countNumber += 1
#     return countNumber
#
#
# number = int(input("Введите число: "))
# print("В числе", number, "всего", countNumbersInNumber(number), "цифры")

#--------------------------Quest 7, part 1-------------------------------

# def reverseString(any_string):
#     if any_string == "":
#         return any_string
#     else:
#         return reverseString(any_string[1:]) + any_string[:1]
#
# def numberIsPalindrom(numberOne):
#     numberOne = str(numberOne)
#     if len(numberOne) % 2 == 0:
#         onePart = numberOne[:int(len(numberOne)/2)]
#         twoPart = numberOne[int(len(numberOne)/2):]
#         if onePart == reverseString(twoPart):
#             return print("True")
#         else:
#             return print("False")
#     elif len(numberOne) % 2 != 0:
#         onePart = numberOne[:int(len(numberOne) / 2)]
#         twoPart = numberOne[int(len(numberOne) / 2)+1:]
#         if onePart == reverseString(twoPart):
#             return print("True")
#         else:
#             return print("False")
#
# numberIsPalindrom(int(input("Введите число: ")))