# def sumNumber(a):
#     if a == int(a):
#         return print(a+a*a+a*a*a)
# a = int(input("Entry number: "))
#
# sumNumber(a)

#----------- Quest 2 (Вариант 1) ---------------
# def evenNumbers(a, b):
#     if a < b:
#         if (a + 2 ) % 2 == 0:
#             while True:
#                 print(a)
#                 a += 2
#                 if a > b:
#                     break
#         else:
#             a += 1
#             while True:
#                 print(a)
#                 a += 2
#                 if a > b:
#                     break
#     else:
#         print("a должно быть меньше b")
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
#
# evenNumbers(a, b)

#----------- Quest 2 (Вариант 2) ---------------
def evenNumbers(a, b):
    if a < b:
        for i in range(a, b+1):
            if i % 2 == 0:
                print(i)
    else:
        print("a должно быть меньше b")
a = int(input("Введите a: "))
b = int(input("Введите b: "))
x = a

evenNumbers(a, b)