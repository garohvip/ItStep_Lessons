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
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пиши пример в одну строку"), calc)
    elif message.text.lower() == "lucky number":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пиши число, сейчас проверю"), lucky_number)
    elif message.text.lower() == "reg":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин"), registration_login)
    elif message.text.lower() == "author":
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин"), authorization_login)


def registration_login(message):
    global login
    login = message.text
    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите пароль"), registration_password)
    return login

def registration_password(message):
    global password
    password = message.text
    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите имя"), registration_name)
    return password

def registration_name(message):
    name = message.text
    with open("reg.txt", "a") as file:
        file.write(f"""{login.lower()}\n{password}\n{name.title()}\n\n""")
    return agent_ghost.send_message(message.chat.id, "Данные успешно внесены")


def authorization_login(message):
    global login_search
    login_search = message.text
    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите пароль"), authorization_password)


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

#функция калькулятор (вводить действия слитно)
def calc(message):
    if re.findall(r"\d+", message.text) and re.findall(r"[+\-*/]", message.text):
        # agent_ghost.send_message(message.chat.id, eval(message.text))
        all_info = message.text.split()
        value = int(all_info[0])
        for i in range(1, len(all_info)):
            if all_info[i] == '+':
                i += 1
                value += int(all_info[i])
                continue
            elif all_info[i] == '-':
                i += 1
                value -= int(all_info[i])
                continue
            elif all_info[i] == '*':
                i += 1
                value *= int(all_info[i])
                continue
            elif all_info[i] == '/':
                i += 1
                value /= int(all_info[i])
                continue
        return agent_ghost.send_message(message.chat.id, str(value))
    else:
        return agent_ghost.send_message(message.chat.id, "Принимаю только цифры и символы \'+\' \'-\' \'/\' \'*\'")

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