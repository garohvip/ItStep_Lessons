import datetime
from dairy_app.management.commands.config_bot import TOKEN
from telebot import types
import telebot
from dairy_app.models import *

agent_ghost = telebot.TeleBot(TOKEN)

keyboard_all = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_all.add(types.KeyboardButton("Записи"))
                 # types.KeyboardButton("Планы"))


def check_notes(message):
    date = str(datetime.datetime.now())[:10]
    data = Note.objects.filter(datalogin__login=message.chat.id, datenotes=date)
    if data:
        return True
    else:
        return False


def add_notes(message):
    date = str(datetime.datetime.now())[:10]
    data = Note.objects.filter(datalogin__login=message.chat.id, datenotes=date)
    if data:
        data.update(text=message.text)
        agent_ghost.send_message(message.chat.id, f"Запись за {date} успешно перезаписана!")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    else:
        Note.objects.get_or_create(
            datalogin=User.objects.get(login=message.chat.id),
            datenotes=date,
            text=message.text
        )
        agent_ghost.send_message(message.chat.id, f"Запись успешно добавлена за {date}!")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)


def del_notes(message):
    data = Note.objects.filter(datalogin__login=message.chat.id, datenotes=message.text)
    if data:
        data.delete()
        agent_ghost.send_message(message.chat.id, f"Запись за {message.text} успешно удалена!")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    else:
        agent_ghost.send_message(message.chat.id, f"Записи за {message.text} не найдено!")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)


def view_notes_for_date(message):
    data = Note.objects.filter(datalogin__login=message.chat.id, datenotes=message.text)
    if data:
        all_data_of_date = data[0].text
        c = int(len(all_data_of_date) / 4096)
        s = 0
        agent_ghost.send_message(message.chat.id, f"Запись за {message.text}:")
        for j in range(c+1):
            agent_ghost.send_message(message.chat.id, all_data_of_date[s:s+4096])
            s += 4096
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    else:
        agent_ghost.send_message(message.chat.id, f"Записи за {message.text} не найдено!")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)


def edit_notes_rewrite_dump(message):
    data = Note.objects.filter(datalogin__login=message.chat.id, edit=True)
    if message.text == "Отменить операцию ввода текста":
        data.update(edit=False)
        agent_ghost.send_message(message.chat.id, "Операция отменена")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    else:
        data.update(text=message.text, edit=False)
        agent_ghost.send_message(message.chat.id, "Успешно перезаписано")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)


def edit_notes_add_dump(message):
    data = Note.objects.filter(datalogin__login=message.chat.id, edit=True)
    if message.text == "Отменить операцию ввода текста":
        data.update(edit=False)
        agent_ghost.send_message(message.chat.id, "Операция отменена")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
    else:
        all_data_of_date = data[0].text
        data.update(text=all_data_of_date + " " + message.text, edit=False)
        agent_ghost.send_message(message.chat.id, "Текст к записи успешно добавлен")
        agent_ghost.send_message(message.chat.id, "Вы в меню", reply_markup=keyboard_all)
