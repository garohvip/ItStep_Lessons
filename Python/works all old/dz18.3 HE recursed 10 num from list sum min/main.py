from random import randint

def minSumNumbers(listOne):                             #не смог понять как делать через рекурсию по этому просто решение задачи
    sumAll = 100000
    q = 0
    u = 10
    listSaveAll = []
    while True:
        sum1 = 0
        sum2 = 0
        listSave1 = []                                  #созданы два списка для ввода тех цифр, которые были использованы при подсчете
        listSave2 = []

        for i in range(q, u):                           #проверка первых 10 чисел
            sum1 += listOne[i]
            listSave1.append(listOne[i])
        q += 1
        u += 1
        for j in range(q, u):                           #по условию задачи не было сказано - каждые 10 чисел проверять 10 чисел
            sum2 += listOne[j]                          #или каждое 1 число проверять 10 чисел по этому сделал через 1
            listSave2.append(listOne[j])

        if sum1 > sum2:
            if sum2 < sumAll:
                sumAll = sum2
                listSaveAll = listSave2
        elif sum1 < sum2:
            if sum1 < sumAll:
                sumAll = sum1
                listSaveAll = listSave1
        else:
            sumAll = sum1
            listSaveAll = listSave1

        if u == 100:
            break

    return listSaveAll, sumAll

a = [randint(1,10) for i in range(100)]
print(a)
print(minSumNumbers(a))