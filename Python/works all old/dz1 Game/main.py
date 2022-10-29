import random
import time
import keyboard


def game():
    player = 0
    spider_hp = 120
    drakon_hp = 300
    player_hp = 100
    player_phys_damage = 5
    wood_sword_damage = 15
    ex_sword_damage = 45
    armor_hp = 50
    elixir = False
    elixir_hp = 50
    player_damage = player_phys_damage + wood_sword_damage
    print('-----=====Приветствую Вас в игре "Пещерный воин"=====-----')
    print("----------------------------------------------------------")
    print("Правила игры очень просты")
    print("1) Выжить и победить.")
    print("2) На начале игры Ваш дамаг будет составлять", player_damage, "единиц.")
    print("3) На начале игры Ваше здоровье будет в количестве", player_hp, "единиц.")
    print("4) Здоровье можно увеличить при помощи \"armor\".")
    print("5) Эликсир восстанавливает здоровье в количестве 50 единиц.")
    print("6) Эликсир восстанавливает максимум до 100 единиц здоровья.")
    print("----------------------------------------------------------")
    print("Управление:")
    print('Использование кодовых слов "вперед", "выйти", "подобрать", "бой", "сдаться"')
    print("У Вас будут подсказки по управлению после каждого вашего действия")
    print("----------------------------------------------------------")
    print("ИГРА НАЧИНАЕТСЯ", end="\n\n")
    print("Воин в темной пещере.")
    print("Ваши действия: \"вперед\", \"выйти\"")

    step = input()
    if step == "вперед" or step == "выйти":
        if step == "вперед":
            player += 1
            print("Вы прошли 10 шагов вперед")
            print("Сейчас Вы на", player, "уровне пещеры")
            print("Вы получили достижение: ПЕРВЫЕ ШАГИ")
            print("Ваши действия: \"вперед\", \"выйти\"")
            step = input()
            if step == "вперед" or step == "выйти":
                if step == "вперед":
                    player += 1
                    print("Вы прошли 10 шагов вперед")
                    print("Сейчас Вы на", player, "уровне пещеры")
                    print("Справа Вы заметили что-то сверкающее в углу темной пещеры")
                    print("Ваши действия: \"вперед\", \"выйти\", \"подобрать\"")
                    step = input()
                    if step == "вперед" or step == "выйти" or step == "подобрать":
                        if step == "вперед":
                            player += 1
                            print("Вы прошли 10 шагов вперед")
                            print("Сейчас Вы на", player, "уровне пещеры")
                            print("Вы встретили громадного паука")
                            print("Урон паука = 9-11 единиц")
                            print("Здоровья паука =", spider_hp, "единиц")
                            print("Ваши действия: \"бой\", \"сдаться\"")
                            step = input()
                            if step == "бой" or step == "сдаться":
                                if step == "бой":
                                    print("Вы приняли БОЙ")
                                    while player_hp > 0 and spider_hp > 0:
                                        print("Вас атакует паук")
                                        time.sleep(1)
                                        player_hp = player_hp - random.randint(9, 11)
                                        print("Ваше здоровье =", player_hp, "единиц")
                                        if player_hp <= 0:
                                            break
                                        print("Нажмите 'SHIFT' чтобы нанести удар пауку")
                                        keyboard.wait('shift')
                                        spider_hp = spider_hp - random.randint(player_damage - 5, player_damage + 5)
                                        print("Здоровье паука =", spider_hp, "единиц")
                                        time.sleep(1)
                                    if spider_hp <= 0:
                                        print("Вы победили паука")
                                        print("Получено достижение: УБИЙЦА МОНСТРОВ")
                                        print("У Вас осталось", player_hp, "здоровья из 100")
                                        print("Ваши действия: \"вперед\", \"выйти\"")
                                        step = input()
                                        if step == "вперед" or step == "выйти":
                                            if step == "вперед":
                                                player += 1
                                                print("Вы прошли 10 шагов вперед")
                                                print("Сейчас Вы на", player, "уровне пещеры")
                                                print("Бродя по пещере, Вы заметили скелет в нагрудной броне и рядом лежит сумка")
                                                print("Ваши действия: \"вперед\", \"выйти\", \"подобрать\"")
                                                step = input()
                                                if step == "вперед" or step == "выйти" or step == "подобрать":
                                                    if step == "вперед":
                                                        player += 1
                                                        print("Вы прошли 10 шагов вперед")
                                                        print("Сейчас Вы на", player, "уровне пещеры")
                                                        print("Вы встретили того самого трехглавого дракона по прозвищу путин")
                                                        print("Урон дракона = 20-40 единиц")
                                                        print("Здоровья дракона =", drakon_hp, "единиц")
                                                        print("Ваши действия: \"бой\", \"сдаться\"")
                                                        step = input()
                                                        if step == "бой" or step == "сдаться":
                                                            if step == "бой":
                                                                print("Вы приняли БОЙ")
                                                                while player_hp > 0 and drakon_hp > 0:
                                                                    print("Вас атакует дракон")
                                                                    time.sleep(1)
                                                                    player_hp = player_hp - random.randint(20, 40)
                                                                    print("Ваше здоровье =", player_hp, "единиц")
                                                                    if player_hp <= 0:
                                                                        break
                                                                    print("Нажмите 'SHIFT' чтобы нанести удар дракону")
                                                                    keyboard.wait('shift')
                                                                    drakon_hp = drakon_hp - random.randint(player_damage - 5, player_damage + 5)
                                                                    print("Здоровье дракона =", drakon_hp, "единиц")
                                                                    time.sleep(1)
                                                                    if player_hp <= 50 and elixir == True:
                                                                        print("У Вас есть возможность выпить эликсир который восстановит 50 единиц здоровья")
                                                                        print("Напишите \"пить\" для того чтобы выпить эликсир или напишите любой текст чтобы продолжить бой")
                                                                        plus_hp = input()
                                                                        if plus_hp == "пить":
                                                                            player_hp = player_hp + elixir_hp
                                                                            print("Теперь у Вас", player_hp, "единиц здоровья")
                                                                            elixir = False
                                                                            time.sleep(1)
                                                                if drakon_hp <= 0:
                                                                    print("Вы победили дракона")
                                                                    print("Получено достижение: УБИЙЦА НЕЧЕСТИ")
                                                                    print("Игра окончена, спасибо за прохождение!")
                                                                    time.sleep(1)
                                                                elif player_hp <= 0:
                                                                    print("Вас убил дракон")
                                                                    print("Вы проиграли")
                                                                    time.sleep(1)
                                                                print("Спасибо, что дошли до конца")
                                                                print("Теперь можете покинуть игру")
                                                            elif step == "сдаться":
                                                                print("Вы были убиты драконом")
                                                                print("Вы проиграли")
                                                        else:
                                                            print("Неправильный ввод. Повторите снова")
                                                    elif step == "выйти":
                                                        print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
                                                    elif step == "подобрать":
                                                        player_hp = player_hp + armor_hp
                                                        print("Вы подобрали и одели нагрудник")
                                                        print("Ваше здоровье состявляет", player_hp, "единиц")
                                                        print("Рядом с Вами лежит сумка")
                                                        print("Ваши действия: \"вперед\", \"выйти\", \"подобрать\"")
                                                        step = input()
                                                        if step == "вперед" or step == "выйти" or step == "подобрать":
                                                            if step == "вперед":
                                                                print(1)
                                                            elif step == "выйти":
                                                                print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
                                                            elif step == "подобрать":
                                                                elixir = True
                                                                print("Вы подобрали эликсир")
                                                                print("Получено достижение: НАХОДЧИВОСТЬ")
                                                                print("Ваши действия: \"вперед\", \"выйти\"")
                                                                step = input()
                                                                if step == "вперед" or step == "выйти":
                                                                    if step == "вперед":
                                                                        player += 1
                                                                        print("Вы прошли 10 шагов вперед")
                                                                        print("Сейчас Вы на", player, "уровне пещеры")
                                                                        print("Вы встретили того самого трехглавого дракона по прозвищу путин")
                                                                        print("Урон дракона = 20-40 единиц")
                                                                        print("Здоровья дракона =", drakon_hp, "единиц")
                                                                        print("Ваши действия: \"бой\", \"сдаться\"")
                                                                        step = input()
                                                                        if step == "бой" or step == "сдаться":
                                                                            if step == "бой":
                                                                                print("Вы приняли БОЙ")
                                                                                while player_hp > 0 and drakon_hp > 0:
                                                                                    print("Вас атакует дракон")
                                                                                    time.sleep(1)
                                                                                    player_hp = player_hp - random.randint(
                                                                                        20, 40)
                                                                                    print("Ваше здоровье =", player_hp,
                                                                                          "единиц")
                                                                                    if player_hp <= 0:
                                                                                        break
                                                                                    print(
                                                                                        "Нажмите 'SHIFT' чтобы нанести удар дракону")
                                                                                    keyboard.wait('shift')
                                                                                    drakon_hp = drakon_hp - random.randint(
                                                                                        player_damage - 5,
                                                                                        player_damage + 5)
                                                                                    print("Здоровье дракона =", drakon_hp,
                                                                                          "единиц")
                                                                                    time.sleep(1)
                                                                                    if player_hp <= 50 and elixir == True:
                                                                                        print(
                                                                                            "У Вас есть возможность выпить эликсир который восстановит 50 единиц здоровья")
                                                                                        print(
                                                                                            "Напишите \"пить\" для того чтобы выпить эликсир или напишите любой текст чтобы продолжить бой")
                                                                                        plus_hp = input()
                                                                                        if plus_hp == "пить":
                                                                                            player_hp = player_hp + elixir_hp
                                                                                            print("Теперь у Вас", player_hp,
                                                                                                  "единиц здоровья")
                                                                                            elixir = False
                                                                                            time.sleep(1)
                                                                                if drakon_hp <= 0:
                                                                                    print("Вы победили дракона")
                                                                                    print(
                                                                                        "Получено достижение: УБИЙЦА НЕЧЕСТИ")
                                                                                    print(
                                                                                        "Игра окончена, спасибо за прохождение!")
                                                                                    time.sleep(1)
                                                                                elif player_hp <= 0:
                                                                                    print("Вас убил дракон")
                                                                                    print("Вы проиграли")
                                                                                    time.sleep(1)
                                                                                print("Спасибо, что дошли до конца")
                                                                                print("Теперь можете покинуть игру")
                                                                            elif step == "сдаться":
                                                                                print("Вы были убиты драконом")
                                                                                print("Вы проиграли")
                                                                        else:
                                                                            print("Неправильный ввод. Повторите снова")
                                                                else:
                                                                    print("Неправильный ввод. Повторите снова")
                                                        else:
                                                            print("Неправильный ввод. Повторите снова")
                                                else:
                                                    print("Неправильный ввод. Повторите снова")
                                            if step == "выйти":
                                                print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
                                        else:
                                            print("Неправильный ввод. Повторите снова")
                                    elif player_hp <= 0:
                                        print("Вас убил паук")
                                        print("Вы проиграли")
                                elif step == "сдаться":
                                    print("Вас убил паук")
                                    print("Вы проиграли")
                            else:
                                print("Неправильный ввод. Повторите снова")
                        elif step == "выйти":
                            print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
                        elif step == "подобрать":
                            player_damage = player_phys_damage + ex_sword_damage
                            print("Поздравляю, Вы подобрали Меч Экскалибур")
                            print("Теперь Ваш дамаг составляет =", player_damage)
                            print("Получено достижение: СВЕРХ ДАМАГ")
                            print("Ваши действия: \"вперед\", \"выйти\"")
                            step = input()
                            if step == "вперед" or step == "выйти":
                                if step == "вперед":
                                    player += 1
                                    print("Вы прошли 10 шагов вперед")
                                    print("Сейчас Вы на", player, "уровне пещеры")
                                    print("Вы встретили громадного паука")
                                    print("Урон паука = 9-11 единиц")
                                    print("Здоровья паука =", spider_hp, "единиц")
                                    print("Ваши действия: \"бой\", \"сдаться\"")
                                    step = input()
                                    if step == "бой" or step == "сдаться":
                                        if step == "бой":
                                            print("Вы приняли БОЙ")
                                            while player_hp > 0 and spider_hp > 0:
                                                print("Вас атакует паук")
                                                time.sleep(1)
                                                player_hp = player_hp - random.randint(9, 11)
                                                print("Ваше здоровье =", player_hp, "единиц")
                                                if player_hp <= 0:
                                                    break
                                                print("Нажмите 'SHIFT' чтобы нанести удар пауку")
                                                keyboard.wait('shift')
                                                spider_hp = spider_hp - random.randint(player_damage - 5, player_damage + 5)
                                                print("Здоровье паука =", spider_hp, "единиц")
                                                time.sleep(1)
                                            if spider_hp <= 0:
                                                print("Вы победили паука")
                                                print("Получено достижение: УБИЙЦА МОНСТРОВ")
                                                print("У Вас осталось", player_hp, "здоровья из 100")
                                                print("Ваши действия: \"вперед\", \"выйти\"")
                                                step = input()
                                                if step == "вперед" or step == "выйти":
                                                    if step == "вперед":
                                                        player += 1
                                                        print("Вы прошли 10 шагов вперед")
                                                        print("Сейчас Вы на", player, "уровне пещеры")
                                                        print("Бродя по пещере Вы заметили скелет в нагрудной броне и рядом с ним лежит сумка")
                                                        print("Ваши действия: \"вперед\", \"выйти\", \"подобрать\"")
                                                        step = input()
                                                        if step == "вперед" or step == "выйти" or step == "подобрать":
                                                            if step == "вперед":
                                                                print(1)
                                                            elif step == "выйти":
                                                                print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
                                                            elif step == "подобрать":
                                                                player_hp = player_hp + armor_hp
                                                                print("Вы подобрали и одели нагрудник")
                                                                print("Ваше здоровье состявляет", player_hp, "единиц")
                                                                print("Рядом с Вами лежит сумка")
                                                                print("Ваши действия: \"вперед\", \"выйти\", \"подобрать\"")
                                                                step = input()
                                                                if step == "вперед" or step == "выйти" or step == "подобрать":
                                                                    if step == "вперед":
                                                                        print(1)
                                                                    elif step == "выйти":
                                                                        print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
                                                                    elif step == "подобрать":
                                                                        elixir = True
                                                                        print("Вы подобрали эликсир")
                                                                        print("Получено достижение: НАХОДЧИВОСТЬ")
                                                                        print("Ваши действия: \"вперед\", \"выйти\"")
                                                                        step = input()
                                                                        if step == "вперед" or step == "выйти":
                                                                            if step == "вперед":
                                                                                player += 1
                                                                                print("Вы прошли 10 шагов вперед")
                                                                                print("Сейчас Вы на", player, "уровне пещеры")
                                                                                print("Вы встретили того самого трехглавого дракона по прозвищу путин")
                                                                                print("Урон дракона = 20-40 единиц")
                                                                                print("Здоровья дракона =", drakon_hp, "единиц")
                                                                                print("Ваши действия: \"бой\", \"сдаться\"")
                                                                                step = input()
                                                                                if step == "бой" or step == "сдаться":
                                                                                    if step == "бой":
                                                                                        print("Вы приняли БОЙ")
                                                                                        while player_hp > 0 and drakon_hp > 0:
                                                                                            print("Вас атакует дракон")
                                                                                            time.sleep(1)
                                                                                            player_hp = player_hp - random.randint(20, 40)
                                                                                            print("Ваше здоровье =", player_hp, "единиц")
                                                                                            if player_hp <= 0:
                                                                                                break
                                                                                            print("Нажмите 'SHIFT' чтобы нанести удар дракону")
                                                                                            keyboard.wait('shift')
                                                                                            drakon_hp = drakon_hp - random.randint(player_damage - 5, player_damage + 5)
                                                                                            print("Здоровье дракона =", drakon_hp, "единиц")
                                                                                            time.sleep(1)
                                                                                            if player_hp <= 50 and elixir == True:
                                                                                                print("У Вас есть возможность выпить эликсир который восстановит 50 единиц здоровья")
                                                                                                print("Напишите \"пить\" для того чтобы выпить эликсир или напишите любой текст чтобы продолжить бой")
                                                                                                plus_hp = input()
                                                                                                if plus_hp == "пить":
                                                                                                    player_hp = player_hp + elixir_hp
                                                                                                    print("Теперь у Вас", player_hp, "единиц здоровья")
                                                                                                    elixir = False
                                                                                                    time.sleep(1)
                                                                                        if drakon_hp <= 0:
                                                                                            print("Вы победили дракона")
                                                                                            print("Получено достижение: УБИЙЦА НЕЧЕСТИ")
                                                                                            print("Игра окончена, спасибо за прохождение!")
                                                                                            time.sleep(1)
                                                                                        elif player_hp <= 0:
                                                                                            print("Вас убил дракон")
                                                                                            print("Вы проиграли")
                                                                                            time.sleep(1)
                                                                                        print("Спасибо, что дошли до конца")
                                                                                        print("Теперь можете покинуть игру")
                                                                                    elif step == "сдаться":
                                                                                        print("Вы были убиты драконом")
                                                                                        print("Вы проиграли")
                                                                                else:
                                                                                    print("Неправильный ввод. Повторите снова")
                                                                        else:
                                                                            print("Неправильный ввод. Повторите снова")
                                                                else:
                                                                    print("Неправильный ввод. Повторите снова")
                                                        else:
                                                            print("Неправильный ввод. Повторите снова")
                                                    if step == "выйти":
                                                        print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
                                                else:
                                                    print("Неправильный ввод. Повторите снова")
                                            elif player_hp <= 0:
                                                print("Вас убил паук")
                                                print("Вы проиграли")
                                                
                                        elif step == "сдаться":
                                            print("Вас убил паук")
                                            print("Вы проиграли")
                                    else:
                                        print("Неправильный ввод. Повторите снова.")
                                elif step == "выйти":
                                    print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
                            else:
                                print("Неправильный ввод. Повторите снова.")
                    else:
                        print("Неправильный ввод. Повторите снова.")
                elif step == "выйти":
                    print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
            else:
                print("Неправильный ввод. Повторите снова.")
        elif step == "выйти":
            print("Вы вышли из пещеры и больше не являетесь \"Сашкой ЗСУ\"")
            
    else:
        print("Неправильный ввод. Повторите снова.")

game()
while True:
    again = input('Хотите начать заново? [да/нет]: ')

    if again == 'да':
        game()
    else:
        break