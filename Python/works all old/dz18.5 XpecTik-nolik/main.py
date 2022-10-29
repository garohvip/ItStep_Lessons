from random import randint                          #рандом для бота с кем играет игрок
from time import sleep                              #небольшая задержка выбора клетки бота для небольшой реалестичности

def allGame():                                      #Функция вывода игровой сетки (сделал для уменьшения количества строк кода)
    print()
    for j in range(1, 6):
        if j == 1:
            print(a1, "|", a2, "|", a3, end="")
        elif j == 3:
            print(b1, "|", b2, "|", b3, end="")
        elif j == 5:
            print(c1, "|", c2, "|", c3, end="")
        else:
            for k in range(1, 4):
                print("―", end="  ")
        print("")
    return print()

while True:                                         #Сделан для повторного выбора символа чем бессмысленный выход из программы
    vibor = input("Введите символ, которых хотите играть (буква X занята): ")               #ввод символа с которым будете играть

    if vibor.lower() != "x":

        a1 = 1                                      #аннулирование сетки после окончания игры
        a2 = 2                                      #а так же подсказка для выбора клетки
        a3 = 3

        b1 = 4
        b2 = 5
        b3 = 6

        c1 = 7
        c2 = 8
        c3 = 9

        while True:                                 #while для игры до момента заполнения одной из линий или же конца игры

            allGame()
            if a1 != 1 or a2 != 2 or a3 != 3 or b1 != 4 or b2 != 5 or b3 != 6 or c1 != 7 or c1 != 8 or c1 != 9:  # проверка на заполненность клеток
                while True:                             #создан для повторного ввода клетки при неверном вводе
                    variant = int(input(f"Введите клетку, куда хотите записать свой символ {vibor}: "))             #выбор клетки куда будет вводится ваш символ

                    if variant == 1 and a1 == 1:                        #замена символа выбранной клетки на ваш символ
                        a1 = vibor
                        break
                    elif variant == 2 and a2 == 2:
                        a2 = vibor
                        break
                    elif variant == 3 and a3 == 3:
                        a3 = vibor
                        break
                    elif variant == 4 and b1 == 4:
                        b1 = vibor
                        break
                    elif variant == 5 and b2 == 5:
                        b2 = vibor
                        break
                    elif variant == 6 and b3 == 6:
                        b3 = vibor
                        break
                    elif variant == 7 and c1 == 7:
                        c1 = vibor
                        break
                    elif variant == 8 and c2 == 8:
                        c2 = vibor
                        break
                    elif variant == 9 and c3 == 9:
                        c3 = vibor
                        break
                    else:
                        print("Введено неверное число или клетка уже занята. Повторите попытку.")


                if a1 == vibor and a2 == vibor and a3 == vibor:                         #проверка на 3 одинаковые ВАШИХ символа в линии
                    allGame()
                    print("Вы победили. Игра окончена")
                    break
                elif a1 == vibor and b2 == vibor and c3 == vibor:
                    allGame()
                    print("Вы победили. Игра окончена")
                    break
                elif a1 == vibor and b1 == vibor and c1 == vibor:
                    allGame()
                    print("Вы победили. Игра окончена")
                    break

                elif a2 == vibor and b2 == vibor and c2 == vibor:
                    allGame()
                    print("Вы победили. Игра окончена")
                    break

                elif a3 == vibor and b2 == vibor and c1 == vibor:
                    allGame()
                    print("Вы победили. Игра окончена")
                    break
                elif a3 == vibor and b3 == vibor and c3 == vibor:
                    allGame()
                    print("Вы победили. Игра окончена")
                    break

                elif b1 == vibor and b2 == vibor and b3 == vibor:
                    allGame()
                    print("Вы победили. Игра окончена")
                    break

                elif c1 == vibor and c2 == vibor and c3 == vibor:
                    allGame()
                    print("Вы победили. Игра окончена")
                    break
            else:                                                                       # в случае заполненных всех клеток - игра заканчивается в ничью
                print("Все клетки заполнены. У вас ничья. Игра окончена")
                break


            allGame()                               #вывод сетки

            if a1 == 1 or a2 == 2 or a3 == 3 or b1 == 4 or b2 == 5 or b3 == 6 or c1 == 7 or c1 == 8 or c1 == 9:  # проверка на заполненность клеток

                print("Ход бота")                   #сейчас будет ход бота

                sleep(1)

                while True:                         #while создан для повторного ввода символа через рандом для того чтобы при повторном числе он заново его "сгенерировал"
                    variantBot = randint(1, 9)                  #Это же все таки randint

                    if variantBot == 1 and a1 == 1:                 #замена символа сгенерированной рандомом клетки на символ бота
                        a1 = "X"
                        break
                    elif variantBot == 2 and a2 == 2:
                        a2 = "X"
                        break
                    elif variantBot == 3 and a3 == 3:
                        a3 = "X"
                        break
                    elif variantBot == 4 and b1 == 4:
                        b1 = "X"
                        break
                    elif variantBot == 5 and b2 == 5:
                        b2 = "X"
                        break
                    elif variantBot == 6 and b3 == 6:
                        b3 = "X"
                        break
                    elif variantBot == 7 and c1 == 7:
                        c1 = "X"
                        break
                    elif variantBot == 8 and c2 == 8:
                        c2 = "X"
                        break
                    elif variantBot == 9 and c3 == 9:
                        c3 = "X"
                        break


                if a1 == "X" and a2 == "X" and a3 == "X":               #проверка на 3 одинаковые символа БОТА в линии
                    allGame()
                    print("Вы проиграли. Игра окончена")
                    break
                elif a1 == "X" and b2 == "X" and c3 == "X":
                    allGame()
                    print("Вы проиграли. Игра окончена")
                    break
                elif a1 == "X" and b1 == "X" and c1 == "X":
                    allGame()
                    print("Вы проиграли. Игра окончена")
                    break

                elif a2 == "X" and b2 == "X" and c2 == "X":
                    allGame()
                    print("Вы проиграли. Игра окончена")
                    break

                elif a3 == "X" and b2 == "X" and c1 == "X":
                    allGame()
                    print("Вы проиграли. Игра окончена")
                    break
                elif a3 == "X" and b3 == "X" and c3 == "X":
                    allGame()
                    print("Вы проиграли. Игра окончена")
                    break

                elif b1 == "X" and b2 == "X" and b3 == "X":
                    allGame()
                    print("Вы проиграли. Игра окончена")
                    break

                elif c1 == "X" and c2 == "X" and c3 == "X":
                    allGame()
                    print("Вы проиграли. Игра окончена")
                    break
            else:                                                                   #в случае заполненных всех клеток - игра заканчивается в ничью
                print("Все клетки заполнены. У вас ничья. Игра окончена")
                break

        restart = input("Хотите сыграть еще? y/n: ")                        #повторная возможность сыграть в игру
        if restart == "n":
            print("Прощай")
            break

    else:
        print("Выберите другой символ.")