import os

path1 = os.path.join("txtfile1.txt")
path2 = os.path.join("txtfile2.txt")

file1 = open(path1, "r")
file2 = open(path2, "w")

file1_read = file1.readlines()

count_line = 0

for i in file1_read: #проходим по списку строк
    count_line += 1 #считаем строки
    count = 0 # создание или же аннулирование подсчета слов
    p = i.split(" ") # создание списка из списка строк
    for j in p: # проходим по списку из списка строк
        if j.isdigit(): #проверяем слово на цифру (цифра не является словом)
            continue # пропускаем
        else:
            count += 1 #добавляем 1 слово
    if count_line == len(file1_read): # проверка на последнюю строку чтобы не удалить последний символ в последней строке
        file2.write(f"{i} ({count})\n")
    else:
        file2.write(f"{i[:-1]} ({count})\n") #запись без последнего символа \n в строке чтобы количество слов с троке не перешло на некст строку

file1.close()
file2.close()