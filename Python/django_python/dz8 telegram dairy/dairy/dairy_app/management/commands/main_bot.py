import datetime
import time
from dairy_app.management.commands.config_bot import TOKEN
from telebot import types
import telebot
import dairy_app.management.commands.notes_bot as notes_bot
# import dairy_app.management.commands.plan_bot as plan_bot
from dairy_app.models import *

agent_ghost = telebot.TeleBot(TOKEN)

keyboard_notes = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_notes.add(types.KeyboardButton("Добавить запись"),
                   types.KeyboardButton("Изменить запись"),
                   types.KeyboardButton("Удалить запись"),
                   types.KeyboardButton("Посмотреть записи"),
                   types.KeyboardButton("Меню"))

# keyboard_plan = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# keyboard_plan.add(types.KeyboardButton("Добавить план"),
#                   types.KeyboardButton("Изменить план"),
#                   types.KeyboardButton("Удалить план"),
#                   types.KeyboardButton("Посмотреть план"),
#                   types.KeyboardButton("Меню"))

keyboard_stop_edit = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_stop_edit.add(types.KeyboardButton("Отменить операцию ввода текста"))

keyboard_all = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_all.add(types.KeyboardButton("Записи"))
                 # types.KeyboardButton("Планы"))

keyboard_reg_auth = types.InlineKeyboardMarkup()
keyboard_reg_auth.add(types.InlineKeyboardButton(text="Авторизация", callback_data="auth"),
                      types.InlineKeyboardButton(text="Регистрация", callback_data="reg"))

keyboard_stop = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_stop.add(types.KeyboardButton("Хватит"))

keyboard_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_menu.add(types.KeyboardButton("Меню"))


@agent_ghost.message_handler(commands=["start"])
def start(message):
    if message.text == "/start":
        agent_ghost.send_message(message.chat.id, "Привет, незнакомец. Я бот-ежедневник. Вот мой функционал:\n\n1. Записи\n\nНо для начала работы нужно зарегистрироваться либо авторизоваться", reply_markup=keyboard_reg_auth)


@agent_ghost.message_handler(content_types=["text"])
def get_text(message):
    if check_time_auth(message):
        if message.text == "Записи":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Здесь Вы можете написать все, что угодно в своих записях! Функционал предоставлен на кнопках.", reply_markup=keyboard_notes), next_move_one)
        # elif message.text == "Планы":
        #     agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Здесь Вы можете написать план на определенную дату! Функционал предоставлен на кнопках.", reply_markup=keyboard_plan), next_move_one)
        elif message.text == "Меню":
            agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
        else:
            agent_ghost.send_message(message.chat.id, "Некорректный ввод")
            agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    else:
        agent_ghost.send_message(message.chat.id, f"Уважаемый, {message.chat.first_name}, время авторизации вышло.\nАвторизуйтесь по новой", reply_markup=keyboard_reg_auth)


def next_move_one(message):
    if message.text in ["Добавить запись", "Изменить запись", "Удалить запись", "Посмотреть записи"]:
        if message.text == "Добавить запись":
            if notes_bot.check_notes(message):
                keyboard_rewrite_edit = types.InlineKeyboardMarkup()
                keyboard_rewrite_edit.add(types.InlineKeyboardButton(text="Да", callback_data="rewrite"),
                                          types.InlineKeyboardButton(text="Нет", callback_data="menu"))
                agent_ghost.send_message(message.chat.id, "У Вас уже есть запись за сегодня. Перезаписать?", reply_markup=keyboard_rewrite_edit)
            else:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введите запись"), notes_bot.add_notes)
        elif message.text == "Изменить запись":
            keyboard_notes_edit_next = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            keyboard_notes_edit_next.add(types.KeyboardButton("Изменить записанное"),
                                         types.KeyboardButton("Добавить к записанному"),
                                         types.KeyboardButton("Меню"))
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Изменить или добавить к существующей записи?", reply_markup=keyboard_notes_edit_next), next_move_two)
        elif message.text == "Удалить запись":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Введите дату в формате ГГГГ-ММ-ДД\nПример: {str(datetime.datetime.now())[:10]}"), notes_bot.del_notes)
        elif message.text == "Посмотреть записи":
            keyboard_notes_view_next = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            keyboard_notes_view_next.add(types.KeyboardButton("Все даты с записями"),
                                         types.KeyboardButton("Запись по дате"),
                                         types.KeyboardButton("Меню"))
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Выберите ниже действие", reply_markup=keyboard_notes_view_next), next_move_two)
    # elif message.text in ["Добавить план", "Изменить план", "Удалить план", "Посмотреть план"]:
    #     if message.text == "Добавить план":
    #         agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Введите дату на которую хотите записать план в формате ГГГГ-ММ-ДД \nПример: {str(datetime.datetime.now())[:10]}", reply_markup=keyboard_menu), plan_add_check)
    #     elif message.text == "Изменить план":
    #         pass
    #         # agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Введите дату на которую хотите записать план в формате ГГГГ-ММ-ДД \nПример: {str(datetime.datetime.now())[:10]}"), check_edit_plan)
    #     elif message.text == "Удалить план":
    #         agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Введите дату на которую хотите записать план в формате ГГГГ-ММ-ДД \nПример: {str(datetime.datetime.now())[:10]}"), plan_bot.del_notes)
    #     elif message.text == "Посмотреть план":
    #         keyboard_plan_view_next = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    #         keyboard_plan_view_next.add(types.KeyboardButton("Все даты с планами"),
    #                                     types.KeyboardButton("План по дате"),
    #                                     types.KeyboardButton("Меню"))
    #         agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Выберите ниже действие", reply_markup=keyboard_plan_view_next), next_move_two)
    elif message.text == "Меню":
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    else:
        agent_ghost.send_message(message.chat.id, "Некорректный ввод. Попробуйте снова")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)


def next_move_two(message):
    if message.text in ["Все даты с записями", "Запись по дате"]:
        if message.text == "Все даты с записями":
            data = Note.objects.filter(datalogin__login=message.chat.id)
            if data:
                all_date = []
                for i in data:
                    all_date.append(i.datenotes)
                agent_ghost.send_message(message.chat.id, "Все даты с записями:\n\n" + "".join([i + "\n" for i in all_date]))
                agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
            else:
                agent_ghost.send_message(message.chat.id, "У Вас еще нет записей")
                agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
        elif message.text == "Запись по дате":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Введите дату в формате ГГГГ-ММ-ДД\nПример: {str(datetime.datetime.now())[:10]}"), notes_bot.view_notes_for_date)
    elif message.text in ["Изменить записанное", "Добавить к записанному"]:
        if message.text == "Изменить записанное":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Введите дату в формате ГГГГ-ММ-ДД\nПример: {str(datetime.datetime.now())[:10]}"), edit_notes_rewrite)
        elif message.text == "Добавить к записанному":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Введите дату в формате ГГГГ-ММ-ДД\nПример: {str(datetime.datetime.now())[:10]}"), edit_notes_add)
        elif message.text == "Меню":
            agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    # elif message.text in ["Все даты с планами", "План по дате"]:
    #     if message.text == "Все даты с планами":
    #         data = Plan.objects.filter(datalogin__login=message.chat.id)
    #         if data:
    #             all_date = []
    #             for i in data:
    #                 all_date.append(i.dateplan)
    #             agent_ghost.send_message(message.chat.id, "Все даты с планами:\n\n" + "".join([i + "\n" for i in all_date]))
    #             agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    #         else:
    #             agent_ghost.send_message(message.chat.id, "У Вас еще нет планов")
    #             agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    #     elif message.text == "План по дате":
    #         agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Введите дату в формате ГГГГ-ММ-ДД\nПример: {str(datetime.datetime.now())[:10]}"), plan_bot.view_plan_for_date)
    elif message.text == "Меню":
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    else:
        agent_ghost.send_message(message.chat.id, "Некорректный ввод. Попробуйте снова")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)


# def check_edit_plan(message):
#     data = Plan.objects.filter(datalogin__login=message.chat.id, dateplan=message.text)
#     if data:
#         all_data_of_date = data[0].text
#         data[i]['plan']["r" + message.text] = data[i]['plan'].pop(message.text)
#         c = []
#         for j in range(len(all_data_of_date)):
#             c.append(f"{j+1}) {all_data_of_date.get(str(j+1))}\n")
#         with open("bd.json", "w") as f:
#             json.dump(data, f)
#         agent_ghost.send_message(message.chat.id, f"План за {message.text}:\n\n{''.join([el for el in c])}")
#         agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Какой пункт плана хотите изменить?", reply_markup=keyboard_menu), edit_plan_item)
#     else:
#         agent_ghost.send_message(message.chat.id, f"Плана за {message.text} не найдено!")
#         agent_ghost.send_message(message.chat.id, f"Вы в меню", reply_markup=keyboard_all)


# def edit_plan_item(message):
#     if message.text == "Меню":
#         with open("bd.json", "r") as f:
#             data = json.load(f)
#         for i in range(len(data)):
#             if data[i].get('login') == message.chat.id:
#                 for j in data[i]['plan']:
#                     if "r" in j:
#                         data[i]['plan'][j[1:]] = data[i]['plan'].pop(j)
#                         with open("bd.json", "w") as f:
#                             json.dump(data, f)
#                         return agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
#     else:
#         with open("bd.json", "r") as f:
#             data = json.load(f)
#         for i in range(len(data)):
#             if data[i].get('login') == message.chat.id:
#                 for j in data[i]['plan']:
#                     if "r" in j:
#                         for k in data[i]['plan'][j]:
#                             if int(message.text) == int(k):
#                                 agent_ghost.send_message(message.chat.id, f"Пункт плана №{message.text} от {j[1:]}:\n\n{data[i]['plan'][j][k]}")
#                                 data[i]['plan'][j]["r" + k] = data[i]['plan'][j].pop(k)
#                                 with open("bd.json", "w") as f:
#                                     json.dump(data, f)
#                                 return agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Введите новый текст пункта плана"), plan_bot.edit_plan_dump)
#         else:
#             for i in range(len(data)):
#                 if data[i].get('login') == message.chat.id:
#                     for j in data[i]['plan']:
#                         if "r" in j:
#                             data[i]['plan'][j[1:]] = data[i]['plan'].pop(j)
#                             with open("bd.json", "w") as f:
#                                 json.dump(data, f)
#                                 return agent_ghost.send_message(message.chat.id, f"Пункта плана №{message.text} не найдено!\n\nВы в меню", reply_markup=keyboard_all)


def edit_notes_add(message):
    data = Note.objects.filter(datalogin__login=message.chat.id, datenotes=message.text)
    if data:
        all_data_of_date = data[0].text
        data.update(edit=True)
        c = int(len(all_data_of_date) / 4096)
        s = 0
        agent_ghost.send_message(message.chat.id, f"Текст записи за {message.text}:")
        for j in range(c+1):
            agent_ghost.send_message(message.chat.id, all_data_of_date[s:s+4096])
            s += 4096
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Для того, чтобы добавить текст к записи Вам нужно просто вставить в строку ниже свой текст, "
                                                                                         f"после чего отправить его мне\n\nМаксимум Вы можете отправить 4096 символов в одном "
                                                                                         f"телеграм-сообщении!", reply_markup=keyboard_stop_edit), notes_bot.edit_notes_add_dump)
    else:
        agent_ghost.send_message(message.chat.id, f"Записи за {message.text} не найдено!")
        agent_ghost.send_message(message.chat.id, f"Вы в меню", reply_markup=keyboard_all)


def edit_notes_rewrite(message):
    data = Note.objects.filter(datalogin__login=message.chat.id, datenotes=message.text)
    if data:
        all_data_of_date = data[0].text
        data.update(edit=True)
        c = int(len(all_data_of_date) / 4096)
        s = 0
        agent_ghost.send_message(message.chat.id, f"Текст записи за {message.text}:")
        for j in range(c+1):
            agent_ghost.send_message(message.chat.id, all_data_of_date[s:s+4096])
            s += 4096
        agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Для того, чтобы изменить запись Вам нужно скопировать текст, вставить в строку ниже и изменить "
                                                                                         f"где нужно, после чего отправить его мне\n\nМаксимум Вы можете отправить 4096 символов в одном "
                                                                                         f"телеграм-сообщении! Если у Вас больше символов то можете добавить к записям при помощи "
                                                                                         f"специальной кнопки \"Добавить к записям\"", reply_markup=keyboard_stop_edit), notes_bot.edit_notes_rewrite_dump)
    else:
        agent_ghost.send_message(message.chat.id, f"Записи за {message.text} не найдено!")
        agent_ghost.send_message(message.chat.id, f"Вы в меню", reply_markup=keyboard_all)


# def plan_add(message):
#     with open("bd.json", "r") as f:
#         data = json.load(f)
#     if message.text.lower() == "хватит":
#         for i in range(len(data)):
#             if data[i].get("login") == message.chat.id:
#                 for j in data[i]['plan']:
#                     if "r" in j:
#                         data[i]['plan'][j[1:]] = data[i]['plan'].pop(j)
#                         with open("bd.json", "w") as f:
#                             json.dump(data, f)
#                             return agent_ghost.send_message(message.chat.id, f"План за {j[1:]} успешно добавлен!\n\nВы в меню", reply_markup=keyboard_all)
#     else:
#         for i in range(len(data)):
#             if data[i].get('login') == message.chat.id:
#                 for j in data[i]['plan']:
#                     if "r" in j:
#                         count = len(data[i]['plan'][j])
#                         if count == 0:
#                             data[i]['plan'][j]["1"] = message.text
#                             with open("bd.json", "w") as f:
#                                 json.dump(data, f)
#                             agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Пункт плана {str(count+2)}", reply_markup=keyboard_stop), plan_add)
#                         else:
#                             data[i]["plan"][j][str(count+1)] = message.text
#                             with open("bd.json", "w") as f:
#                                 json.dump(data, f)
#                             agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, f"Пункт плана {str(count+2)}", reply_markup=keyboard_stop), plan_add)


# def plan_add_check(message):
#     if message.text == "Меню":
#         agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
#     else:
#         data = Plan.objects.filter(datalogin__login=message.chat.id, dateplan=message.text)
#         if data:
#             agent_ghost.send_message(message.chat.id, f"На {message.text} уже есть план. Для начала удалите его или измените содержимое")
#             agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
#         else:
#             Plan.objects.get_or_create(
#                 datalogin=User.objects.filter(login=message.chat.id),
#                 dateplan=message.text,
#
#             )
#             agent_ghost.send_message(message.chat.id, "С каждой отправкой сообщения будет добавлять +1 пункт плана пока не введете ключевое слово \"Хватит\"")
#             agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Пункт плана 1", reply_markup=keyboard_stop), plan_add)


def check_time_auth(message):
    data = User.objects.filter(login=message.chat.id)
    if time.time() - int(data[0].time) <= 86400:
        return True
    else:
        return False


def auth(message):
    var = User.objects.filter(login=message.chat.id)
    if var[0].password == message.text:
        var.update(time=int(time.time()))
        agent_ghost.send_message(message.chat.id, f"Добро пожаловать, {message.chat.first_name}!")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    else:
        agent_ghost.send_message(message.chat.id, "Пароль не верный. Повторите операцию снова", reply_markup=keyboard_reg_auth)


def auth_reg_check(message):
    data = User.objects.filter(login=message.chat.id)
    if data:
        return True
    else:
        return False


def reg(message):
    User.objects.get_or_create(
        login=message.chat.id,
        password=message.text,
        time=int(time.time())
    )
    agent_ghost.send_message(message.chat.id, f"Регистрация прошла успешно. Добро пожаловать, {message.chat.first_name}!")
    agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)


@agent_ghost.callback_query_handler(func=lambda call: call.data in ["auth", "reg", "rewrite", "menu"])
def auth_reg(call):
    if call.message:
        if call.data == "auth":
            if auth_reg_check(call.message):
                agent_ghost.register_next_step_handler(agent_ghost.send_message(call.message.chat.id, "Введи пароль"), auth)
            else:
                agent_ghost.send_message(call.message.chat.id, "У Вас еще нет аккаунта. Зарегистрируйтесь")
        elif call.data == "reg":
            if auth_reg_check(call.message):
                agent_ghost.send_message(call.message.chat.id, "У Вас уже есть аккаунт. Авторизуйтесь")
            else:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(call.message.chat.id, "Введите пароль"), reg)
        elif call.data == "rewrite":
            agent_ghost.register_next_step_handler(agent_ghost.send_message(call.message.chat.id, "Введите запись"), notes_bot.add_notes)
        elif call.data == "menu":
            agent_ghost.send_message(call.message.chat.id, "Вы в меню", reply_markup=keyboard_all)


agent_ghost.polling(none_stop=True, interval=0)
