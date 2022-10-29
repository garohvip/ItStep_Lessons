from variant import prand
from time import sleep

player1 = ''  # Игрок 1 под именем Саша
player1_win = 0
players = 0  # количетсво игроков
player = ''  # выбор чем играть
player_win = 0
repeat = True  # повторение игры
reload = ''
while repeat:
    print("С каким количеством людей хотите поиграть? 1-4")
    players = int(input())
    if players == 1:
        print("Вы играете с игроком под именем Саша")
        print("Выберите, чем хотите походить?:")
        print('"rock", "paper", "scissors", "lizard", "spock"')
        player = input()
        if player == "rock" or player == "paper" or player == "scissors" or player == "lizard" or player == "spock":
            if player == "rock":
                player1 = prand("rock", "paper", "scissors", "lizard", "spock")
                if player1 == "rock":
                    print("У Саши", player1)
                    print("У вас ничья")
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "paper":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "scissors":
                    print("У Саши", player1)
                    print("Вы победили")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "lizard":
                    print("У Саши", player1)
                    print("Вы победил")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "spock":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
            elif player == "paper":
                player1 = prand("rock", "paper", "scissors", "lizard", "spock")
                if player1 == "rock":
                    print("У Саши", player1)
                    print("Вы победили")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "paper":
                    print("У Саши", player1)
                    print("У вас ничья")
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "scissors":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "lizard":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "spock":
                    print("У Саши", player1)
                    print("Вы победили")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
            elif player == "scissors":
                player1 = prand("rock", "paper", "scissors", "lizard", "spock")
                if player1 == "rock":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "paper":
                    print("У Саши", player1)
                    print("Вы победили")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "scissors":
                    print("У Саши", player1)
                    print("У вас ничья")
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "lizard":
                    print("У Саши", player1)
                    print("Вы победили")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "spock":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
            elif player == "lizard":
                player1 = prand("rock", "paper", "scissors", "lizard", "spock")
                if player1 == "rock":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "paper":
                    print("У Саши", player1)
                    print("Вы победили")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "scissors":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "lizard":
                    print("У Саши", player1)
                    print("У вас ничья")
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "spock":
                    print("У Саши", player1)
                    print("Вы победили")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
            elif player == "spock":
                player1 = prand("rock", "paper", "scissors", "lizard", "spock")
                if player1 == "rock":
                    print("У Саши", player1)
                    print("Вы победили")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "paper":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "scissors":
                    print("У Саши", player1)
                    print("Вы победили")
                    player_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "lizard":
                    print("У Саши", player1)
                    print("Вы проиграли")
                    player1_win += 1
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
                elif player1 == "spock":
                    print("У Саши", player1)
                    print("У вас ничья")
                    sleep(1)
                    print("-----------------------------------------------------")
                    print("Повторить попытку? yes/no")
                    reload = input()
                    if reload == "no":
                        repeat = False
        else:
            print("Неверный ввод. Повторите снова")
    else:
        print("Некорректный ввод количества игроков (Пока что игроков только 1)")
print("-----------------------------------------------")
print("Общий счет")
print("У Саши -", player1_win, "очков")
print("У Вас -", player_win, "очков")
print("Прощай. Возвращайтесь еще.")