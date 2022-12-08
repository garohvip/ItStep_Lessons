import telebot
import re

config = {
    "name": "",
    "token": "5887337428:AAFRKUrVND6fjISP5DHOdzTadUG2SSK-z-8"
}

agent_ghost = telebot.TeleBot(config["token"])


# принимаем текст и делаем вывод
@agent_ghost.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "hi":
        agent_ghost.send_message(message.chat.id, "Hello")
    elif message.text.lower() == "палиндром":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Ну ка давай сюда слово, сейчас я его проверю на палиндром"), palindrom)
    elif message.text.lower() == "парное":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Кидай цифру"), par)
    elif message.text.lower() == "калькулятор":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пиши пример в одну строку"), calculator)
    elif message.text.lower() == "lucky number":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пиши число, сейчас проверю"), lucky_number)
    elif message.text.lower() == "регистрация":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин"), registration_login)
    elif message.text.lower() == "авторизация":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин"), authorization_login)


# функция регистрации с проверкой на наличие логина в БД (текстовом файле)
def registration_login(message):
    def check_login(login_var):
        with open("reg.txt", "r") as file:
            all_info = file.readlines()
        all_info = [line.rstrip() for line in all_info]
        for i in range(0, len(all_info), 4):
            if login_var == all_info[i]:
                return False
        return True

    global login
    login = message.text
    if check_login(login):
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите пароль"), registration_password)
        return login
    else:
        agent_ghost.send_message(message.chat.id, f"Логин \"{login}\" уже зарегистрирован!")


# продолжение регистрации если все True, ввод пароля
def registration_password(message):
    global password
    password = message.text
    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите имя"), registration_name)
    return password


# продолжение регистрации, ввод имени
def registration_name(message):
    name = message.text
    with open("reg.txt", "a") as file:
        file.write(f"""{login.lower()}\n{password}\n{name.title()}\n\n""")
    return agent_ghost.send_message(message.chat.id, "Данные успешно внесены")


# авторизация без проверки на наличие логина в БД (текстовом файле)
def authorization_login(message):
    global login_search
    login_search = message.text
    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите пароль"), authorization_password)


# продолжение авторизации с проверкой на совпадение логин и пароля
def authorization_password(message):
    with open("reg.txt", "r") as file:
        all_info = file.readlines()
    all_info = [line.rstrip() for line in all_info]
    password_search = message.text
    for i in range(0, len(all_info), 4):
        if login_search == all_info[i]:
            if password_search == all_info[i+1]:
                return agent_ghost.send_message(message.chat.id, f"Добро пожаловать, {all_info[i+2]}")
    return agent_ghost.send_message(message.chat.id, "Логин или пароль не верны!")


# проверка на "счастливое" число
def lucky_number(message):
    if message.text.isdigit():
        number_list = list(message.text)
        number = []
        for i in number_list:
            number.append(int(i))
        if sum(number[:int(len(number)/2)]) == sum(number[int(len(number)/2):]):
            return agent_ghost.send_message(message.chat.id, "Счастливое")
        else:
            return agent_ghost.send_message(message.chat.id, "Облом, не счастливое")
    else:
        return agent_ghost.send_message(message.chat.id, "Воспринимаю только цифры")


# функция калькулятор
def calculator(message):
    # основная функция калькулятора
    def calc(message_list):
        result = 0
        count = 1
        while count == 1:
            count = 0
            for i in range(len(message_list)):
                if message_list[i] in ["*", "/"]:
                    if message_list[i] == "*":
                        result = (float(message_list[i - 1]) * float(message_list[i + 1]))
                        message_list[i - 1] = str(result)
                        message_list.pop(i + 1)
                        message_list.pop(i)
                        count += 1
                        break
                    elif message_list[i] == "/":
                        result = (float(message_list[i - 1]) / float(message_list[i + 1]))
                        message_list[i - 1] = str(result)
                        message_list.pop(i + 1)
                        message_list.pop(i)
                        count += 1
                        break
        count = 1
        while count == 1:
            count = 0
            for i in range(len(message_list)):
                if message_list[i] in ["+", "-"]:
                    if message_list[i] == "+":
                        result = (float(message_list[i - 1]) + float(message_list[i + 1]))
                        message_list[i - 1] = str(result)
                        message_list.pop(i + 1)
                        message_list.pop(i)
                        count += 1
                        break
                    elif message_list[i] == "-":
                        result = (float(message_list[i - 1]) - float(message_list[i + 1]))
                        message_list[i - 1] = str(result)
                        message_list.pop(i + 1)
                        message_list.pop(i)
                        count += 1
                        break
        return agent_ghost.send_message(message.chat.id, message_list[0])

    # функция сплита по пробелам
    def space(solve):
        solve_list = solve.split(" ")
        return calc(solve_list)

    # функция сплита, если пользователь вводит пример слитно
    def no_space(solve):
        number = ""
        solve_list = []
        for i in range(len(solve)):
            if solve[i] in ["+", "-", "*", "/"]:
                solve_list.append(number)
                solve_list.append(solve[i])
                number = ""
            else:
                number = number + solve[i]
        solve_list.append(number)
        return calc(solve_list)

# проверка примера на слитность написания
    primer = message.text
    c = 0
    for element in primer:
        if element == " ":
            space(primer)
            c += 1
            break
    if c == 0:
        no_space(primer)


# функция проверки на четность числа
def par(message):
    if message.text.isdigit():
        if int(message.text) % 2 == 0:
            return agent_ghost.send_message(message.chat.id, "Число четное")
        else:
            return agent_ghost.send_message(message.chat.id, "Число не четное!!")
    else:
        return agent_ghost.send_message(message.chat.id, "Воспринимаю только цифры")


# функция проверки на палиндром
def palindrom(message):
    if re.findall(r"\d+", message.text):
        return agent_ghost.send_message(message.chat.id, "Без цифр пожалуйста")
    else:
        if message.text.lower() == message.text.lower()[::-1]:
            return agent_ghost.send_message(message.chat.id, "Это слово - палиндром")
        else:
            return agent_ghost.send_message(message.chat.id, "Не является палиндромом")


# agent_ghost.polling(none_stop=True, interval=0)
agent_ghost.infinity_polling(timeout=10, long_polling_timeout=5)
