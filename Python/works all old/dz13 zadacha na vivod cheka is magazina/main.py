users = [['Игорь', 600],
         ['Наташа', 140],
         ['Виталий', 50],
         ['Игорь', 300],
         ['Наташа', 400],
         ['Игорь', 1000]]
discont = 3
k = 1

def userClient(*users):
    sum = 0
    global k
    user = input("Кто Вы? (Игорь, Наташа, Виталий): ")
    for i in range(len(users)):
        for j in range(len(users[i])):
            if users[i][j] == user:
                print(users[i][j], ", Ваш чек под номером ", k, " был на сумму: ", users[i][j+1], " грн", sep="")
                sum += users[i][j+1]
                k+=1
    if sum == 0:
        return print("Вас нет в списке покупателей")
    else:
        return print("В общей сумме:", sum, "грн.")

userClient(*users)

if k-1 >= discont:
    print("Следующие покупки в нашем магазине для Вас будут со скидкой 3% на 1 чек.")