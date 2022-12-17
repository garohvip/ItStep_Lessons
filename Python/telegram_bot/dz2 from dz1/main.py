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

# Старт
keyboard_start = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_start.add(telebot.types.KeyboardButton("Регистрация"),
                   telebot.types.KeyboardButton("Авторизация"),
                   telebot.types.KeyboardButton("Остаться гостем"),
                   telebot.types.KeyboardButton("Забыли пароль?"))

# восстановление логина или пароля
keyboard_restore = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_restore.add(telebot.types.KeyboardButton("Логин"),
                     telebot.types.KeyboardButton("Пароль"),
                     telebot.types.KeyboardButton("Отмена"))

# отмена
keyboard_cancel = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_cancel.add(telebot.types.KeyboardButton("Отмена"))

# да, нет
keyboard_yes_or_no = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_yes_or_no.add(telebot.types.KeyboardButton("Да"),
                       telebot.types.KeyboardButton("Нет"))

# Для гостей
keyboard_guest = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_guest.add(telebot.types.KeyboardButton("hi"),
                   telebot.types.KeyboardButton("Регистрация"),
                   telebot.types.KeyboardButton("Авторизация"),
                   telebot.types.KeyboardButton("Забыли пароль?"))

# Для пользователей 1 уровня
keyboard_lvl_1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_lvl_1.add(telebot.types.KeyboardButton("Палиндром"),
                   telebot.types.KeyboardButton("Парное"),
                   telebot.types.KeyboardButton("Lucky number"),
                   telebot.types.KeyboardButton("Выйти с аккаунта"))

# Для пользователей 2 уровня
keyboard_lvl_2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_lvl_2.add(telebot.types.KeyboardButton("Палиндром"),
                   telebot.types.KeyboardButton("Парное"),
                   telebot.types.KeyboardButton("Калькулятор"),
                   telebot.types.KeyboardButton("Lucky number"),
                   telebot.types.KeyboardButton("Статистика"),
                   telebot.types.KeyboardButton("Выйти с аккаунта"))

# Для пользователей 10 уровня
keyboard_all = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_all.add(telebot.types.KeyboardButton("Палиндром"),
                 telebot.types.KeyboardButton("Парное"),
                 telebot.types.KeyboardButton("Калькулятор"),
                 telebot.types.KeyboardButton("Lucky number"),
                 telebot.types.KeyboardButton("Статистика"),
                 telebot.types.KeyboardButton("Кодировать фото"),
                 telebot.types.KeyboardButton("Выйти с аккаунта"))

# Кнопки для функции статистики
keyboard_statistic = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_statistic.add(telebot.types.KeyboardButton("Всю информацию"),
                       telebot.types.KeyboardButton("Количество слов"),
                       telebot.types.KeyboardButton("Количество символов"),
                       telebot.types.KeyboardButton("Количество гласных букв"),
                       telebot.types.KeyboardButton("Количество согласных букв"),
                       telebot.types.KeyboardButton("Количество гласных и согласных букв"),
                       telebot.types.KeyboardButton("Количество цифр"),
                       telebot.types.KeyboardButton("Количество спец. символов"),
                       telebot.types.KeyboardButton("Отмена"))


@agent_ghost.message_handler(commands=["start", "buttons"])
def start(message):
    if message.text == "/start":
        agent_ghost.send_message(message.chat.id, "Привет. Для работы бота нужно быть зарегистрированным.\n\nВыберите ниже действие:", reply_markup=keyboard_start)
    elif message.text == "/buttons":
        with open("reg.json", "r") as file:
            all_info = json.load(file)
        for i in all_info.get('musicbot'):
            if i.get('user_id') == message.from_user.id:
                if i.get('lvl_right') == 1:
                    agent_ghost.send_message(message.chat.id, "Выбери действие", reply_markup=keyboard_lvl_1)
                    break
                elif i.get('lvl_right') == 2:
                    agent_ghost.send_message(message.chat.id, "Выбери действие", reply_markup=keyboard_lvl_2)
                    break
                elif i.get('lvl_right') == 10:
                    agent_ghost.send_message(message.chat.id, "Выбери действие", reply_markup=keyboard_all)
                    break


# принимаем текст и делаем вывод
@agent_ghost.message_handler(content_types=["text"])
def get_text(message):
    all_commands_for_quest_and_lvl_10 = ["палиндром", "парное", "калькулятор", "lucky number", "статистика", "кодировать фото", "выйти с аккаунта"]
    text = message.text.lower()
    lvl_right = 0
    time_in = 0
    in_online = False
    username = ""
    with open('reg.json', "r") as reg:
        all_users = json.load(reg)
    for i in all_users.get('musicbot'):
        if i.get('user_id') == message.from_user.id:
            lvl_right = i.get('lvl_right')
            time_in = i.get('time_in')
            in_online = i.get('in_online')
            username = i.get('name')
            break
    if lvl_right == 0 and in_online is False and time_in == 0:
        if text == "остаться гостем":
            agent_ghost.send_message(message.chat.id, "Теперь Вы гость.\nФункционал гостя слишком ограничен, по-этому рекомендую зарегистрироваться или же авторизоваться", reply_markup=keyboard_guest)
        elif text == "hi":
            agent_ghost.send_message(message.chat.id, "Hi, " + message.from_user.first_name)
        elif text == "авторизация":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин", reply_markup=keyboard_cancel), authorization_login)
        elif text == "регистрация":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин", reply_markup=keyboard_cancel), registration_login)
        elif text == "забыли пароль?":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите id своего телеграм-аккаунта", reply_markup=keyboard_cancel), restore_user_data_check)
        elif text in all_commands_for_quest_and_lvl_10:
            agent_ghost.send_message(message.chat.id, "Команда для Вас не доступна. Зарегистрируйтесь или авторизуйтесь для ее использования", reply_markup=keyboard_start)
        else:
            agent_ghost.send_message(message.chat.id, "Команда не найдена")
    elif lvl_right >= 1 and in_online is True:
        if time.time() - int(time_in) <= 86400:
            if text == "палиндром":
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Напишите слово", reply_markup=keyboard_cancel), palindrome)
            elif text == "парное":
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Кидай цифру", reply_markup=keyboard_cancel), par)
            elif text == "калькулятор":
                if lvl_right >= 2:
                    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пиши пример в одну строку", reply_markup=keyboard_cancel), calculator)
                else:
                    agent_ghost.send_message(message.chat.id, "Доступа нет!")
            elif text == "lucky number":
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пиши число, сейчас проверю", reply_markup=keyboard_cancel), lucky_number)
            elif text == "кодировать фото":
                if lvl_right >= 10:
                    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Кидай фотку", reply_markup=keyboard_cancel), photo_code)
                else:
                    agent_ghost.send_message(message.chat.id, "Доступа нет!")
            elif text == "статистика":
                if lvl_right >= 2:
                    agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Что конкретно хотите вывести", reply_markup=keyboard_statistic), statistic_check_message)
                else:
                    agent_ghost.send_message(message.chat.id, "Доступа нет!")
            elif text == "регистрация":
                agent_ghost.send_message(message.chat.id, "Вы уже авторизованы!")
            elif text == "авторизация":
                agent_ghost.send_message(message.chat.id, "Вы уже авторизованы!")
            elif text == "забыли пароль?":
                agent_ghost.send_message(message.chat.id, "Вы уже авторизованы!")
            elif text == "выйти с аккаунта":
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Вы действительно хотите выйти с аккаунта?", reply_markup=keyboard_yes_or_no), logout_account)
            else:
                agent_ghost.send_message(message.chat.id, "Команда не найдена!")
        else:
            auto_logout_account(message)
            agent_ghost.send_message(message.chat.id, f"Уважаемый {username}, для безопасности ваших данных требуется повторная авторизация", reply_markup=keyboard_start)
    else:
        if text == "остаться гостем":
            agent_ghost.send_message(message.chat.id, "Теперь Вы гость.\nФункционал гостя слишком ограничен, по-этому рекомендую зарегистрироваться или же авторизоваться", reply_markup=keyboard_guest)
        elif text == "hi":
            agent_ghost.send_message(message.chat.id, "Hi, " + message.from_user.first_name)
        elif text == "авторизация":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин", reply_markup=keyboard_cancel), authorization_login)
        elif text == "регистрация":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите логин", reply_markup=keyboard_cancel), registration_login)
        elif text == "забыли пароль?":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите id своего телеграм-аккаунта", reply_markup=keyboard_cancel), restore_user_data_check)
        elif text in all_commands_for_quest_and_lvl_10:
            agent_ghost.send_message(message.chat.id, "Команда для Вас не доступна. Зарегистрируйтесь или авторизуйтесь для ее использования", reply_markup=keyboard_start)
        else:
            agent_ghost.send_message(message.chat.id, "Команда не найдена")


# функция проверки на права аккаунта (вообще тут должна быть отправка по типу кода на e-mail но пока, что только проверка на знание id телеграм-аккаунта пользователя)
def restore_user_data_check(message):
    if message.text.lower() == "отмена":
        return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_start)
    elif int(message.text) == message.from_user.id:
        return agent_ghost.register_next_step_handler(
            agent_ghost.send_message(message.chat.id, "Что именно хотите восстановить?", reply_markup=keyboard_restore),
            restore_user_data_what)
    else:
        return agent_ghost.register_next_step_handler(
            agent_ghost.send_message(message.chat.id, "Неверный ввод.\n\nПовторите попытку",
                                     reply_markup=keyboard_cancel), restore_user_data_check)


# функция выбора какие данные нужно восстановить
def restore_user_data_what(message):
    if message.text.lower() == "отмена":
        return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_start)
    elif message.text.lower() == "логин":
        with open("reg.json", "r") as reg:
            all_info = json.load(reg)
        for i in all_info.get("musicbot"):
            if i.get('user_id') == message.from_user.id:
                return agent_ghost.send_message(message.chat.id, f"Ваш логин:\n\n{i.get('login')}", reply_markup=keyboard_start)
    elif message.text.lower() == "пароль":
        return agent_ghost.register_next_step_handler(
            agent_ghost.send_message(message.chat.id, "Введите новый пароль",
                                     reply_markup=keyboard_cancel), restore_user_data_password)
    else:
        return agent_ghost.register_next_step_handler(
            agent_ghost.send_message(message.chat.id, "Неверный ввод!\n\nПовторите попытку",
                                     reply_markup=keyboard_restore), restore_user_data_check)


# функция ввода нового пароля
def restore_user_data_password(message):
    if message.text.lower() == "отмена":
        return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_start)
    else:
        check = 0
        with open("reg.json", "r") as reg:
            all_info = json.load(reg)
        for i in all_info.get('musicbot'):
            if i.get('user_id') == message.from_user.id:
                check += 1
                break
        if check == 1:
            for i in range(len(all_info.get('musicbot'))):
                if all_info['musicbot'][i]['user_id'] == message.from_user.id:
                    all_info['musicbot'][i]['password'] = message.text
                    break
            with open("reg.json", "w") as reg:
                json.dump(all_info, reg)
            return agent_ghost.send_message(message.chat.id, "Пароль успешно изменен!\n\nТеперь можете авторизоваться",
                                            reply_markup=keyboard_start)
        elif check == 0:
            return agent_ghost.send_message(message.chat.id,
                                            "На данном телеграм-аккаунте не зарегистрировано еще пользователей!",
                                            reply_markup=keyboard_start)


# функция выхода с аккаунта после суток inactive
def auto_logout_account(message):
    with open("reg.json", "r") as reg:
        all_info = json.load(reg)
    for i in range(len(all_info.get('musicbot'))):
        if all_info['musicbot'][i]['user_id'] == message.from_user.id:
            all_info["musicbot"][i]['in_online'] = False
            break
    with open("reg.json", "w") as reg:
        json.dump(all_info, reg)


# функция выхода из аккаунта
def logout_account(message):
    lvl_right = 0
    with open("reg.json", "r") as reg:
        all_info = json.load(reg)
    for i in all_info.get('musicbot'):
        if i.get('user_id') == message.from_user.id:
            lvl_right = i.get('lvl_right')
            break
    if message.text.lower() == "нет":
        if lvl_right == 1:
            return agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_lvl_1)
        elif lvl_right == 2:
            return agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_lvl_2)
        elif lvl_right == 10:
            return agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    elif message.text.lower() == "да":
        for i in range(len(all_info.get('musicbot'))):
            if all_info['musicbot'][i]['user_id'] == message.from_user.id:
                all_info["musicbot"][i]["in_online"] = False
                break
        with open("reg.json", "w") as reg:
            json.dump(all_info, reg)
        return agent_ghost.send_message(message.chat.id, "Вы успешно вышли с аккаунта!", reply_markup=keyboard_start)
    else:
        return agent_ghost.register_next_step_handler(
            agent_ghost.send_message(message.chat.id, "Нужно ответить либо \"Да\", либо \"Нет\"!"), logout_account)


# функция регистрации
def registration_login(message):
    if message.text.lower() == "отмена":
        return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_start)
    else:
        with open("reg.json", "r") as reg:
            all_info = json.load(reg)
        for i in all_info.get('musicbot'):
            if i.get('user_id') == message.from_user.id:
                return agent_ghost.send_message(message.chat.id,
                                                "Уже есть зарегистрированный пользователь на этом телеграм-аккаунте!",
                                                reply_markup=keyboard_start)
        for i in all_info.get('musicbot'):
            if i.get('login') == message.text.lower():
                return agent_ghost.register_next_step_handler(
                    agent_ghost.send_message(message.chat.id, "Такой логин уже зарегистрирован! Попробуйте другой",
                                             reply_markup=keyboard_cancel), registration_login)
        all_info.get('musicbot').append(
            {"login": message.text.lower(), "password": None, "name": None, "lvl_right": 1, "in_online": False,
             "user_id": message.from_user.id, "time_in": None})
        with open("reg.json", "w") as reg:
            json.dump(all_info, reg)
        return agent_ghost.register_next_step_handler(
            agent_ghost.send_message(message.chat.id, "Введите пароль", reply_markup=keyboard_cancel),
            registration_password)


# продолжение регистрации если все True, ввод пароля
def registration_password(message):
    if message.text.lower() == "отмена":
        return agent_ghost.send_message(message.chat.id,
                                        "Операция отмена. Если Вы захотите продолжить регистрацию по этому телеграм-аккаунту, то Вам нужно нажать \"Забыли пароль?\" в начальном меню",
                                        reply_markup=keyboard_start)
    else:
        with open("reg.json", "r") as reg:
            all_info = json.load(reg)
        for i in range(len(all_info.get('musicbot'))):
            if all_info['musicbot'][i]['user_id'] == message.from_user.id:
                all_info['musicbot'][i]['password'] = message.text
                break
        with open("reg.json", "w") as reg:
            json.dump(all_info, reg)
        return agent_ghost.register_next_step_handler(
            agent_ghost.send_message(message.chat.id, "Введите свое имя", reply_markup=keyboard_cancel),
            registration_name)


# продолжение регистрации, ввод имени
def registration_name(message):
    if message.text.lower() == "отмена":
        return agent_ghost.send_message(message.chat.id, "Операция отмена. Если Вы захотите продолжить регистрацию по этому телеграм-аккаунту, то Вам нужно нажать \"Забыли пароль?\" в начальном меню", reply_markup=keyboard_start)
    else:
        with open("reg.json", "r") as reg:
            all_info = json.load(reg)
        for i in range(len(all_info.get('musicbot'))):
            if all_info['musicbot'][i]['user_id'] == message.from_user.id:
                all_info['musicbot'][i]['name'] = message.text.title()
                all_info['musicbot'][i]['in_online'] = True
                all_info['musicbot'][i]['time_in'] = time.time()
                break
        with open("reg.json", "w") as reg:
            json.dump(all_info, reg)
    return agent_ghost.send_message(message.chat.id, "Регистрация пройдена успешно", reply_markup=keyboard_lvl_1)


# функция авторизации с проверкой на логин пользователя телеграм-аккаунта
def authorization_login(message):
    if message.text.lower() == "отмена":
        return agent_ghost.send_message(message.chat.id, "Операция отмена", reply_markup=keyboard_start)
    else:
        with open("reg.json", "r") as reg:
            all_info = json.load(reg)
        for i in all_info.get('musicbot'):
            if i.get('user_id') == message.from_user.id and i.get('login') == message.text.lower():
                return agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите пароль", reply_markup=keyboard_cancel), authorization_password)
        else:
            return agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Логин введен не верно либо логин не принадлежит этому телеграм-аккаунту.\n\nПопробуйте снова", reply_markup=keyboard_cancel), authorization_login)


# продолжение авторизации, чек пароля
def authorization_password(message):
    if message.text.lower() == "отмена":
        return agent_ghost.send_message(message.chat.id, "Операция отмена", reply_markup=keyboard_start)
    else:
        lvl_right = 0
        with open("reg.json", "r") as reg:
            all_info = json.load(reg)
        for i in range(len(all_info.get('musicbot'))):
            if all_info['musicbot'][i]['user_id'] == message.from_user.id and all_info['musicbot'][i]['password'] == message.text:
                all_info['musicbot'][i]['in_online'] = True
                all_info['musicbot'][i]['time_in'] = time.time()
                with open("reg.json", 'w') as reg:
                    json.dump(all_info, reg)
                lvl_right = all_info['musicbot'][i]['lvl_right']
                if lvl_right == 1:
                    return agent_ghost.send_message(message.chat.id,
                                                    f"Добро пожаловать, {all_info['musicbot'][i]['name']}!",
                                                    reply_markup=keyboard_lvl_1)
                elif lvl_right == 2:
                    return agent_ghost.send_message(message.chat.id,
                                                    f"Добро пожаловать, {all_info['musicbot'][i]['name']}!",
                                                    reply_markup=keyboard_lvl_2)
                elif lvl_right == 10:
                    return agent_ghost.send_message(message.chat.id,
                                                    f"Добро пожаловать, {all_info['musicbot'][i]['name']}!",
                                                    reply_markup=keyboard_all)
        else:
            return agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пароль введен не верно\n\nПопробуйте снова", reply_markup=keyboard_cancel), authorization_password)


# запрос конкретного действия с текстом
def statistic_check_message(message):
    if message.text.lower() == "отмена":
        with open("reg.json", "r") as reg:
            all_info = json.load(reg)
        for i in all_info.get('musicbot'):
            if i.get('user_id') == message.from_user.id:
                if i.get('lvl_right') == 1:
                    return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_1)
                elif i.get('lvl_right') == 2:
                    return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_2)
                elif i.get('lvl_right') == 10:
                    return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_all)
    else:
        global message_user
        message_user = message.text.lower()
        return agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите текст"),
                                                      statistic_text)


# подсчет информации о тексте
def statistic_text(message):
    lvl_right = 0
    with open("reg.json", "r") as reg:
        all_info = json.load(reg)
    for i in all_info.get("musicbot"):
        if i.get('user_id') == message.from_user.id:
            lvl_right = i.get('lvl_right')
            break
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
    if lvl_right == 1:
        if message_user.lower() == "количество слов":
            return agent_ghost.send_message(message.chat.id, f"Количество слов: {stat[5]}", reply_markup=keyboard_lvl_1)
        elif message_user.lower() == "количество символов":
            return agent_ghost.send_message(message.chat.id, f"Количество символов: {stat[0]}",
                                            reply_markup=keyboard_lvl_1)
        elif message_user.lower() == "количество гласных букв":
            return agent_ghost.send_message(message.chat.id, f"Количество гласных букв: {stat[1]}",
                                            reply_markup=keyboard_lvl_1)
        elif message_user.lower() == "количество согласных букв":
            return agent_ghost.send_message(message.chat.id, f"Количество согласных букв: {stat[2]}",
                                            reply_markup=keyboard_lvl_1)
        elif message_user.lower() == "количество гласных и согласных букв":
            return agent_ghost.send_message(message.chat.id,
                                            f"Количество гласных букв: {stat[1]}\nКоличество согласных букв: {stat[2]}",
                                            reply_markup=keyboard_lvl_1)
        elif message_user.lower() == "количество цифр":
            return agent_ghost.send_message(message.chat.id, f"Количество цифр: {stat[3]}", reply_markup=keyboard_lvl_1)
        elif message_user.lower() == "количество спец. символов":
            return agent_ghost.send_message(message.chat.id, f"Количество спец. символов: {stat[4]}",
                                            reply_markup=keyboard_lvl_1)
        elif message_user.lower() == "всю информацию":
            with open("stat.txt", "w") as file:
                file.write(f"""Количество символов: {stat[0]}\nКоличество слов: {stat[5]}\nКоличество цифр: {stat[3]}\n
                Количество знаков пунктуации: {stat[4]}\nКоличество гласных букв: {stat[1]}\nКоличество согласных букв: {stat[2]}""")
            return agent_ghost.send_document(message.chat.id, open("stat.txt", "r"), reply_markup=keyboard_lvl_1)
    elif lvl_right == 2:
        if message_user.lower() == "количество слов":
            return agent_ghost.send_message(message.chat.id, f"Количество слов: {stat[5]}", reply_markup=keyboard_lvl_2)
        elif message_user.lower() == "количество символов":
            return agent_ghost.send_message(message.chat.id, f"Количество символов: {stat[0]}",
                                            reply_markup=keyboard_lvl_2)
        elif message_user.lower() == "количество гласных букв":
            return agent_ghost.send_message(message.chat.id, f"Количество гласных букв: {stat[1]}",
                                            reply_markup=keyboard_lvl_2)
        elif message_user.lower() == "количество согласных букв":
            return agent_ghost.send_message(message.chat.id, f"Количество согласных букв: {stat[2]}",
                                            reply_markup=keyboard_lvl_2)
        elif message_user.lower() == "количество гласных и согласных букв":
            return agent_ghost.send_message(message.chat.id,
                                            f"Количество гласных букв: {stat[1]}\nКоличество согласных букв: {stat[2]}",
                                            reply_markup=keyboard_lvl_2)
        elif message_user.lower() == "количество цифр":
            return agent_ghost.send_message(message.chat.id, f"Количество цифр: {stat[3]}", reply_markup=keyboard_lvl_2)
        elif message_user.lower() == "количество спец. символов":
            return agent_ghost.send_message(message.chat.id, f"Количество спец. символов: {stat[4]}",
                                            reply_markup=keyboard_lvl_2)
        elif message_user.lower() == "всю информацию":
            with open("stat.txt", "w") as file:
                file.write(f"""Количество символов: {stat[0]}\nКоличество слов: {stat[5]}\nКоличество цифр: {stat[3]}\n
                Количество знаков пунктуации: {stat[4]}\nКоличество гласных букв: {stat[1]}\nКоличество согласных букв: {stat[2]}""")
            return agent_ghost.send_document(message.chat.id, open("stat.txt", "r"), reply_markup=keyboard_lvl_2)
    elif lvl_right == 10:
        if message_user.lower() == "количество слов":
            return agent_ghost.send_message(message.chat.id, f"Количество слов: {stat[5]}", reply_markup=keyboard_all)
        elif message_user.lower() == "количество символов":
            return agent_ghost.send_message(message.chat.id, f"Количество символов: {stat[0]}",
                                            reply_markup=keyboard_all)
        elif message_user.lower() == "количество гласных букв":
            return agent_ghost.send_message(message.chat.id, f"Количество гласных букв: {stat[1]}",
                                            reply_markup=keyboard_all)
        elif message_user.lower() == "количество согласных букв":
            return agent_ghost.send_message(message.chat.id, f"Количество согласных букв: {stat[2]}",
                                            reply_markup=keyboard_all)
        elif message_user.lower() == "количество гласных и согласных букв":
            return agent_ghost.send_message(message.chat.id,
                                            f"Количество гласных букв: {stat[1]}\nКоличество согласных букв: {stat[2]}",
                                            reply_markup=keyboard_all)
        elif message_user.lower() == "количество цифр":
            return agent_ghost.send_message(message.chat.id, f"Количество цифр: {stat[3]}", reply_markup=keyboard_all)
        elif message_user.lower() == "количество спец. символов":
            return agent_ghost.send_message(message.chat.id, f"Количество спец. символов: {stat[4]}",
                                            reply_markup=keyboard_all)
        elif message_user.lower() == "всю информацию":
            with open("stat.txt", "w") as file:
                file.write(f"""Количество символов: {stat[0]}\nКоличество слов: {stat[5]}\nКоличество цифр: {stat[3]}\n
                Количество знаков пунктуации: {stat[4]}\nКоличество гласных букв: {stat[1]}\nКоличество согласных букв: {stat[2]}""")
            return agent_ghost.send_document(message.chat.id, open("stat.txt", "r"), reply_markup=keyboard_all)


# проверка на "счастливое" число
def lucky_number(message):
    lvl_right = 0
    with open("reg.json", "r") as reg:
        all_info = json.load(reg)
    for i in all_info.get('musicbot'):
        if i.get('user_id') == message.from_user.id:
            lvl_right = i.get('lvl_right')
            break
    if message.text.lower() == "отмена":
        if lvl_right == 1:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_1)
        elif lvl_right == 2:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_2)
        elif lvl_right == 10:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_all)
    else:
        if message.text.isdigit():
            number_list = list(message.text)
            number = []
            for i in number_list:
                number.append(int(i))
            if sum(number[:int(len(number) / 2)]) == sum(number[int(len(number) / 2):]):
                if lvl_right == 1:
                    return agent_ghost.send_message(message.chat.id, "Счастливое", reply_markup=keyboard_lvl_1)
                elif lvl_right == 2:
                    return agent_ghost.send_message(message.chat.id, "Счастливое", reply_markup=keyboard_lvl_1)
                elif lvl_right == 10:
                    return agent_ghost.send_message(message.chat.id, "Счастливое", reply_markup=keyboard_lvl_1)
            else:
                if lvl_right == 1:
                    return agent_ghost.send_message(message.chat.id, "Облом, не счастливое",
                                                    reply_markup=keyboard_lvl_2)
                elif lvl_right == 2:
                    return agent_ghost.send_message(message.chat.id, "Облом, не счастливое",
                                                    reply_markup=keyboard_lvl_2)
                elif lvl_right == 10:
                    return agent_ghost.send_message(message.chat.id, "Облом, не счастливое",
                                                    reply_markup=keyboard_lvl_2)
        else:
            return agent_ghost.register_next_step_handler(
                agent_ghost.send_message(message.chat.id, "Воспринимаю только цифры\n\nВведите еще раз",
                                         reply_markup=keyboard_cancel), lucky_number)


# функция калькулятор
def calculator(message):
    lvl_right = 0
    with open("reg.json", "r") as reg:
        all_info = json.load(reg)
    for i in all_info.get('musicbot'):
        if i.get('user_id') == message.from_user.id:
            lvl_right = i.get('lvl_right')
            break
    if message.text.lower() == "отмена":
        if lvl_right == 1:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_1)
        elif lvl_right == 2:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_2)
        elif lvl_right == 10:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_all)
    else:
        # основная функция калькулятора
        def calc(message_list, lvl_right_var):
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
            if lvl_right_var == 1:
                return agent_ghost.send_message(message.chat.id, message_list[0], reply_markup=keyboard_lvl_1)
            elif lvl_right_var == 2:
                return agent_ghost.send_message(message.chat.id, message_list[0], reply_markup=keyboard_lvl_2)
            elif lvl_right_var == 10:
                return agent_ghost.send_message(message.chat.id, message_list[0], reply_markup=keyboard_all)

        # функция сплита по пробелам
        def space(solve, lvl_right_var1):
            solve_list = solve.split(" ")
            return calc(solve_list, lvl_right_var1)

        # функция сплита, если пользователь вводит пример слитно
        def no_space(solve, lvl_right_var1):
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
            return calc(solve_list, lvl_right_var1)

        # проверка примера на слитность написания
        primer = message.text
        c = 0
        for element in primer:
            if element == " ":
                space(primer, lvl_right)
                c += 1
                break
        if c == 0:
            no_space(primer, lvl_right)


# функция проверки на четность числа
def par(message):
    lvl_right = 0
    with open("reg.json", "r") as reg:
        all_info = json.load(reg)
    for i in all_info.get('musicbot'):
        if i.get('user_id') == message.from_user.id:
            lvl_right = i.get('lvl_right')
            break
    if message.text.lower() == "отмена":
        if lvl_right == 1:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_1)
        elif lvl_right == 2:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_2)
        elif lvl_right == 10:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_all)
    else:
        if message.text.isdigit():
            if int(message.text) % 2 == 0:
                if lvl_right == 1:
                    return agent_ghost.send_message(message.chat.id, "Число четное", reply_markup=keyboard_lvl_1)
                elif lvl_right == 2:
                    return agent_ghost.send_message(message.chat.id, "Число четное", reply_markup=keyboard_lvl_2)
                elif lvl_right == 10:
                    return agent_ghost.send_message(message.chat.id, "Число четное", reply_markup=keyboard_all)
            else:
                if lvl_right == 1:
                    return agent_ghost.send_message(message.chat.id, "Число не четное!!", reply_markup=keyboard_lvl_1)
                elif lvl_right == 2:
                    return agent_ghost.send_message(message.chat.id, "Число не четное!!", reply_markup=keyboard_lvl_2)
                elif lvl_right == 10:
                    return agent_ghost.send_message(message.chat.id, "Число не четное!!", reply_markup=keyboard_all)
        else:
            return agent_ghost.register_next_step_handler(
                agent_ghost.send_message(message.chat.id, "Воспринимаю только цифры", reply_markup=keyboard_cancel),
                par)


# функция проверки на палиндром
def palindrome(message):
    lvl_right = 0
    with open("reg.json", "r") as reg:
        all_info = json.load(reg)
    for i in all_info.get('musicbot'):
        if i.get('user_id') == message.from_user.id:
            lvl_right = i.get('lvl_right')
            break
    if message.text.lower() == "отмена":
        if lvl_right == 1:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_1)
        elif lvl_right == 2:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_2)
        elif lvl_right == 10:
            return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_all)
    else:
        if re.findall(r"\d+", message.text):
            return agent_ghost.register_next_step_handler(
                agent_ghost.send_message(message.chat.id, "Без цифр пожалуйста", reply_markup=keyboard_cancel),
                palindrome)
        else:
            if message.text.lower() == message.text.lower()[::-1]:
                if lvl_right == 1:
                    return agent_ghost.send_message(message.chat.id, "Это слово - палиндром",
                                                    reply_markup=keyboard_lvl_1)
                elif lvl_right == 2:
                    return agent_ghost.send_message(message.chat.id, "Это слово - палиндром",
                                                    reply_markup=keyboard_lvl_2)
                elif lvl_right == 10:
                    return agent_ghost.send_message(message.chat.id, "Это слово - палиндром", reply_markup=keyboard_all)
            else:
                if lvl_right == 1:
                    return agent_ghost.send_message(message.chat.id, "Не является палиндромом",
                                                    reply_markup=keyboard_lvl_1)
                elif lvl_right == 2:
                    return agent_ghost.send_message(message.chat.id, "Не является палиндромом",
                                                    reply_markup=keyboard_lvl_2)
                elif lvl_right == 10:
                    return agent_ghost.send_message(message.chat.id, "Не является палиндромом",
                                                    reply_markup=keyboard_all)


# функция кодировки фото
def photo_code(message):
    lvl_right = 0
    with open("reg.json", "r") as reg:
        all_info = json.load(reg)
    for i in all_info.get('musicbot'):
        if i.get('user_id') == message.from_user.id:
            lvl_right = i.get('lvl_right')
            break
    if message.content_type == "text":
        if message.text.lower() == "отмена":
            if lvl_right == 1:
                return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_1)
            elif lvl_right == 2:
                return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_2)
            elif lvl_right == 10:
                return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_all)
        else:
            return agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Я принимаю только фото!\nP.S. или слово \"отмена\".", reply_markup=keyboard_cancel), photo_code)
    elif message.content_type == "photo":
        file_info = agent_ghost.get_file(message.photo[-1].file_id)
        downloaded_file = agent_ghost.download_file(file_info.file_path)
        with open('photo.png', 'wb') as photo:
            photo.write(downloaded_file)
        with open('photo.png', 'rb') as photo:
            photo_coding = base64.b64encode(photo.read()).decode('utf-8')
        with open('photo.txt', "w") as file:
            file.write(photo_coding)
        if lvl_right == 1:
            return agent_ghost.send_document(message.chat.id, open("photo.txt", "r"), reply_markup=keyboard_lvl_1)
        elif lvl_right == 2:
            return agent_ghost.send_document(message.chat.id, open("photo.txt", "r"), reply_markup=keyboard_lvl_2)
        elif lvl_right == 10:
            return agent_ghost.send_document(message.chat.id, open("photo.txt", "r"), reply_markup=keyboard_all)
    elif message.content_type == "document":
        return agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Отправьте сжатое фото\nP.S. поставьте галочку при отправке фотографии", reply_markup=keyboard_cancel), photo_code)


# def photo_send(message):
#     lvl_right = 0
#     with open("reg.json", "r") as reg:
#         all_info = json.load(reg)
#     for i in all_info.get('musicbot'):
#         if i.get('user_id') == message.from_user.id:
#             lvl_right = i.get('lvl_right')
#             break
#     if message.content_type == "text":
#         if message.text.lower() == "отмена":
#             if lvl_right == 1:
#                 return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_1)
#             elif lvl_right == 2:
#                 return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_lvl_2)
#             elif lvl_right == 10:
#                 return agent_ghost.send_message(message.chat.id, "Операция отменена", reply_markup=keyboard_all)
#         else:
#             return agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Я принимаю только фото!\nP.S. или слово \"отмена\".", reply_markup=keyboard_cancel), photo_code)
#     elif message.content_type == "photo":
#         file_info = agent_ghost.get_file(message.photo[-1].file_id)
#         downloaded_file = agent_ghost.download_file(file_info.file_path)
#         with open('photo.png', 'wb') as photo:
#             photo.write(downloaded_file)
#         with open('photo.png', 'rb') as photo:
#             photo_coding = base64.b64encode(photo.read()).decode('utf-8')
#         with open('photo.txt', "w") as file:
#             file.write(photo_coding)
#         if lvl_right == 1:
#             return agent_ghost.send_document(message.chat.id, open("photo.txt", "r"), reply_markup=keyboard_lvl_1)
#         elif lvl_right == 2:
#             return agent_ghost.send_document(message.chat.id, open("photo.txt", "r"), reply_markup=keyboard_lvl_2)
#         elif lvl_right == 10:
#             return agent_ghost.send_document(message.chat.id, open("photo.txt", "r"), reply_markup=keyboard_all)
#     elif message.content_type == "document":
#         return agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Отправьте сжатое фото\nP.S. поставьте галочку при отправке фотографии", reply_markup=keyboard_cancel), photo_code)



# agent_ghost.polling(none_stop=True, interval=0)
agent_ghost.infinity_polling(timeout=10, long_polling_timeout=5)
