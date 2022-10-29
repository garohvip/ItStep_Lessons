# ------------------------Quest 1------------------------
# def glasLatin():
#     k = 0
#     str = input("Введите буквы латинского алфавита: ").lower()
#     for i in str:
#         if i.isdigit():
#             print("Введите строку без цифр!!!")
#             break
#         else:
#             if i in "aeiouy":
#                 k+=1
#     if k >= 1:
#         print("В строке \"{}\" всего".format(str), k, "гласных букв.")
#
#
# glasLatin()
# ------------------------Quest 2------------------------

# print("              \"Don't let the noise of others' opinions\n              drown out your own inner voice.\"")
# print("                                        Steve Jobs")

# ------------------------Quest 2------------------------

n = input("Введите шестизначное число: ")

def sixLucky(n):
    test = len(n)
    k = 1
    k1 = 0
    k2 = 0
    if test == 6:
        for j in n:
            if 1 <= k <= 3:
                k1 += int(j)
                k += 1
            elif 4 <= k <= 6:
                k2 += int(j)
    else:
        print("Введите ШЕСТИЗНАЧНОЕ число!!!")
    if k1 == k2:
        print("Число \"{}\" является счастливым.".format(n))
    else:
        print("Число \"{}\" не является счастливым.".format(n))


sixLucky(n)