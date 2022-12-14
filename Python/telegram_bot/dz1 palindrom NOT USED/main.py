import json
import time
import base64
import telebot
import re

config = {
    "name": "",
    "token": "5887337428:AAFRKUrVND6fjISP5DHOdzTadUG2SSK-z-8"
}

agent_ghost = telebot.TeleBot(config["token"])

keyboard_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_start.add(telebot.types.KeyboardButton("регистрация".title()),
                   telebot.types.KeyboardButton("авторизация".title()),
                   telebot.types.KeyboardButton("остаться гостем".capitalize()))

keyboard_guest = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_guest.add(telebot.types.KeyboardButton("hi"),
                   telebot.types.KeyboardButton("регистрация".title()),
                   telebot.types.KeyboardButton("авторизация".title()),)

keyboard_lvl_1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_lvl_1.add(telebot.types.KeyboardButton("палиндром".title()),
                   telebot.types.KeyboardButton("парное".title()),
                   telebot.types.KeyboardButton("lucky number".capitalize()),
                   telebot.types.KeyboardButton("выйти с аккаунта".capitalize()))

keyboard_lvl_2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_lvl_2.add(telebot.types.KeyboardButton("палиндром".title()),
                   telebot.types.KeyboardButton("парное".title()),
                   telebot.types.KeyboardButton("калькулятор".title()),
                   telebot.types.KeyboardButton("lucky number".capitalize()),
                   telebot.types.KeyboardButton("статистика".title()),
                   telebot.types.KeyboardButton("выйти с аккаунта".capitalize()))


keyboard_all = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_all.add(telebot.types.KeyboardButton("регистрация".title()),
                 telebot.types.KeyboardButton("авторизация".title()),
                 telebot.types.KeyboardButton("палиндром".title()),
                 telebot.types.KeyboardButton("парное".title()),
                 telebot.types.KeyboardButton("калькулятор".title()),
                 telebot.types.KeyboardButton("lucky number".capitalize()),
                 telebot.types.KeyboardButton("статистика".title()),
                 telebot.types.KeyboardButton("кодировать фото".capitalize()),
                 telebot.types.KeyboardButton("выйти с аккаунта".capitalize()))

keyboard_statistic = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_statistic.add(telebot.types.KeyboardButton("всю информацию".capitalize()),
                       telebot.types.KeyboardButton("количество слов".capitalize()),
                       telebot.types.KeyboardButton("количество символов".capitalize()),
                       telebot.types.KeyboardButton("количество гласных букв".capitalize()),
                       telebot.types.KeyboardButton("количество согласных букв".capitalize()),
                       telebot.types.KeyboardButton("количество гласных и согласных букв".capitalize()),
                       telebot.types.KeyboardButton("количество цифр".capitalize()),
                       telebot.types.KeyboardButton("количество спец. символов".capitalize()),
                       telebot.types.KeyboardButton("назад в меню".capitalize()))


@agent_ghost.message_handler(commands=["start", "buttons"])
def start(message):
    if message.text == "/start":
        agent_ghost.send_message(message.chat.id, "Hi, i'm bot. Как насчет чтобы авторизоваться?", reply_markup=keyboard_start)
    elif message.text == "/buttons":
        with open("reg.json", "r") as file:
            all_info = json.load(file)
        for i in all_info.get('musicbot'):
            if i.get('user_id') == message.from_user.id:
                if i.get('lvlrights') == 1:
                    agent_ghost.send_message(message.chat.id, "Выбери действие", reply_markup=keyboard_lvl_1)
                    break
                elif i.get('lvlrights') == 2:
                    agent_ghost.send_message(message.chat.id, "Выбери действие", reply_markup=keyboard_lvl_2)
                    break
                elif i.get('lvlrights') == 10:
                    agent_ghost.send_message(message.chat.id, "Выбери действие", reply_markup=keyboard_all)
                    break


# принимаем текст и делаем вывод
@agent_ghost.message_handler(content_types=["text"])
def get_text(message):
    userid = 0
    lvlright = 0
    timein = 0
    username = ""
    with open("reg.json", "r") as file:
        all_users = json.load(file)
    for i in all_users.get('musicbot'):
        if i.get('user_id') == message.from_user.id:
            userid = i.get('user_id')
            lvlright = i.get('lvlrights')
            timein = i.get('timein')
            break
    if message.text == "hi":
        agent_ghost.send_message(message.chat.id, "Hi, " + message.from_user.first_name)
    if time.time() - int(timein) <= 86400 or userid == 0:
        if message.text.lower() == "палиндром":
            if userid == message.from_user.id and lvlright >= 1:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Ну ка давай сюда слово, сейчас я его проверю на палиндром"), palindrome)
            else:
                agent_ghost.send_message(message.chat.id, "Доступа нет!")
        elif message.text.lower() == "парное":
            if userid == message.from_user.id and lvlright >= 1:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Кидай цифру"), par)
            else:
                agent_ghost.send_message(message.chat.id, "Доступа нет!")
        elif message.text.lower() == "калькулятор":
            if userid == message.from_user.id and lvlright >= 2:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пиши пример в одну строку"), calculator)
            else:
                agent_ghost.send_message(message.chat.id, "Доступа нет!")
        elif message.text.lower() == "lucky number":
            if userid == message.from_user.id and lvlright >= 1:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пиши число, сейчас проверю"), lucky_number)
            else:
                agent_ghost.send_message(message.chat.id, "Доступа нет!")
        elif message.text.lower() == "кодировать фото":
            if userid == message.from_user.id and lvlright >= 10:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Кидай фотку"), photo_code)
            else:
                agent_ghost.send_message(message.chat.id, "Доступа нет!")
        elif message.text.lower() == "регистрация":
            if userid == message.from_user.id and lvlright >= 1:
                agent_ghost.send_message(message.chat.id, "Вы уже авторизованы!")
            else:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин"), registration_login)
        elif message.text.lower() == "авторизация":
            if userid == message.from_user.id and lvlright >= 1:
                agent_ghost.send_message(message.chat.id, "Вы уже авторизованы!")
            else:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин"), authorization_login)
        elif message.text.lower() == "статистика":
            if userid == message.from_user.id and lvlright >= 2:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Что конкретно хотите вывести", reply_markup=keyboard_statistic), statistic_check_message)
            else:
                agent_ghost.send_message(message.chat.id, "Доступа нет!")
        elif message.text.lower() == "выйти с аккаунта":
            if userid == message.from_user.id and lvlright >= 1:
                logout_account(message)
                agent_ghost.send_message(message.chat.id, "Вы успешно вышли с аккаунта!", reply_markup=keyboard_start)
            else:
                agent_ghost.send_message(message.chat.id, "Вы не авторизованы!")
        elif message.text.lower() == "остаться гостем":
            agent_ghost.send_message(message.chat.id, "Теперь ты гость.\nФункционал гостя слишком ограничен, по-этому рекомендую зарегистрироваться или же авторизоваться.", reply_markup=keyboard_guest)
    else:
        with open("reg.json", "r") as file:
            all_users = json.load(file)
        for i in all_users.get('musicbot'):
            if i.get('userid') == message.from_user.id:
                all_users['musicbot'][i]['userid'] = 0
                username = i.get('name')
                break
        with open('reg.json', "w") as file:
            json.dump(all_users, file)
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Уважаемый {username}, для безопасности ваших данных требуется повторная авторизация\n\nВведите логин", reply_markup=keyboard_start), authorization_login)


# функция выхода из аккаунта (по факту смена user_id на None)
def logout_account(message):
    with open("reg.json", "r") as file:
        all_info = json.load(file)
    for i in range(len(all_info.get('musicbot'))):
        if all_info['musicbot'][i]['user_id'] == message.from_user.id:
            all_info['musicbot'][i]['user_id'] = 0
            break
    with open("reg.json", "w") as file:
        return json.dump(all_info, file)


# функция регистрации с проверкой на наличие логина в БД (json файле)
def registration_login(message):

    # def check_login(login_var):
    #     with open("reg.json", "r") as file:
    #         all_info = json.load(file)
    #     for i in all_info.get("musicbot"):
    #         if login_var == i.get('login'):
    #             return False
    #     return True
    # login = message.text
    # with open("reg.json", 'r') as file:
    #     all_info = json.load(file)
    #
    # if check_login(login):
    #     agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите пароль"), registration_password)
    #     return login
    # else:
    #     agent_ghost.send_message(message.chat.id, f"Логин \"{login}\" уже зарегистрирован!")


# продолжение регистрации если все True, ввод пароля
def registration_password(message):
    global password
    password = message.text
    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите имя"), registration_name)
    return password


# продолжение регистрации, ввод имени
def registration_name(message):
    name = message.text
    with open("reg.json", "r") as file:
        var_for_edit = json.load(file)
    var_for_edit.get('musicbot').append({"login": login.lower(), "password": password, "name": name.title(), "lvlrights": 1, "user_id": message.from_user.id, "timein": int(time.time())})
    with open("reg.json", "w") as file:
        json.dump(var_for_edit, file)
    return agent_ghost.send_message(message.chat.id, "Успешная регистрация!", reply_markup=keyboard_lvl_1)


# авторизация без проверки на наличие логина в БД (json файле)
def authorization_login(message):
    global login_search
    login_search = message.text
    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите пароль"), authorization_password)


# продолжение авторизации с проверкой на совпадение логин и пароля
def authorization_password(message):
    with open("reg.json", "r") as file:
        all_info = json.load(file)
    password_search = message.text
    for i in range(len(all_info.get('musicbot'))):
        if login_search == all_info.get('musicbot')[i].get("login"):
            if password_search == all_info.get('musicbot')[i].get("password"):
                all_info['musicbot'][i]['user_id'] = message.from_user.id
                all_info['musicbot'][i]['timein'] = int(time.time())
                with open("reg.json", "w") as file:
                    json.dump(all_info, file)
                if all_info.get('musicbot')[i].get('lvlrights') == 1:
                    return agent_ghost.send_message(message.chat.id, f"Добро пожаловать, {all_info.get('musicbot')[i].get('name')}", reply_markup=keyboard_lvl_1)
                elif all_info.get('musicbot')[i].get('lvlrights') == 2:
                    return agent_ghost.send_message(message.chat.id, f"Добро пожаловать, {all_info.get('musicbot')[i].get('name')}", reply_markup=keyboard_lvl_2)
                elif all_info.get('musicbot')[i].get('lvlrights') == 10:
                    return agent_ghost.send_message(message.chat.id, f"Добро пожаловать, {all_info.get('musicbot')[i].get('name')}", reply_markup=keyboard_all)
    return agent_ghost.send_message(message.chat.id, "Логин или пароль введен не верно!")


# запрос конкретного действия с текстом
def statistic_check_message(message):
    if message.text == "Назад в меню":
        with open("reg.json", "r") as file:
            all_info = json.load(file)
        for i in all_info.get('musicbot'):
            if i.get('user_id') == message.from_user.id:
                if i.get('lvlrights') == 1:
                    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Ты в меню", reply_markup=keyboard_lvl_1), get_text)
                    break
                elif i.get('lvlrights') == 2:
                    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Ты в меню", reply_markup=keyboard_lvl_2), get_text)
                    break
                elif i.get('lvlrights') == 10:
                    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Ты в меню", reply_markup=keyboard_all), get_text)
                    break
    else:
        global message_user
        message_user = message.text
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите текст"), statistic_text)


# подсчет информации о тексте
def statistic_text(message):
    stat = [0, 0, 0, 0, 0]
    for i in message.text:
        stat[0] += 1
        if i.lower() in "aeiouy" or i.lower() in "ауоыэяюёие":
            stat[1] += 1
        if i.lower() in "bcdfghjklmnpqrstvwxz" or i.lower() in "бвгджзйклмнпрстфхцчшщ":
            stat[2] += 1
        if i in "1234567890":
            stat[3] += 1
        if i in ".?!,;:-":
            stat[4] += 1
    stat.append(len(message.text.split()))
    if message_user.lower() == "количество слов":
        return agent_ghost.send_message(message.chat.id, f"Количество слов: {stat[5]}")
    elif message_user.lower() == "количество символов":
        return agent_ghost.send_message(message.chat.id, f"Количество символов: {stat[0]}")
    elif message_user.lower() == "количество гласных букв":
        return agent_ghost.send_message(message.chat.id, f"Количество гласных букв: {stat[1]}")
    elif message_user.lower() == "количество согласных букв":
        return agent_ghost.send_message(message.chat.id, f"Количество согласных букв: {stat[2]}")
    elif message_user.lower() == "количество гласных и согласных букв":
        return agent_ghost.send_message(message.chat.id, f"Количество гласных букв: {stat[1]}\nКоличество согласных букв: {stat[2]}")
    elif message_user.lower() == "количество цифр":
        return agent_ghost.send_message(message.chat.id, f"Количество цифр: {stat[3]}")
    elif message_user.lower() == "количество спец. символов":
        return agent_ghost.send_message(message.chat.id, f"Количество спец. символов: {stat[4]}")
    elif message_user.lower() == "всю информацию":
        with open("stat.txt", "w") as file:
            file.write(f"""Количество символов: {stat[0]}\nКоличество слов: {stat[5]}\nКоличество цифр: {stat[3]}\n
            Количество знаков пунктуации: {stat[4]}\nКоличество гласных букв: {stat[1]}\nКоличество согласных букв: {stat[2]}""")
        return agent_ghost.send_document(message.chat.id, open("stat.txt", "r"))


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
def palindrome(message):
    if re.findall(r"\d+", message.text):
        return agent_ghost.send_message(message.chat.id, "Без цифр пожалуйста")
    else:
        if message.text.lower() == message.text.lower()[::-1]:
            return agent_ghost.send_message(message.chat.id, "Это слово - палиндром")
        else:
            return agent_ghost.send_message(message.chat.id, "Не является палиндромом")


# функция кодировки фото
def photo_code(message):
    file_info = agent_ghost.get_file(message.photo[-1].file_id)
    downloaded_file = agent_ghost.download_file(file_info.file_path)
    with open('photo.png', 'wb') as photo:
        photo.write(downloaded_file)
    with open('photo.png', 'rb') as photo:
        photo_coding = base64.b64encode(photo.read()).decode('utf-8')
    with open('photo.txt', "w") as file:
        file.write(photo_coding)
    return agent_ghost.send_document(message.chat.id, open("photo.txt", "r"))


# agent_ghost.polling(none_stop=True, interval=0)
agent_ghost.infinity_polling(timeout=10, long_polling_timeout=5)
