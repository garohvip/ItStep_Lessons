import json
import time
import base64
import telebot
import re

config = {
    "name": "",
    "token": "5956132893:AAFF-d6ntEWNb9iNS2i6gx4CzdEcydQ4w7c"
}


list_elect = ["Xiaomi - 1999$", "Iphone - 19999$", "Samsung - 4000$"]
list_hoz = ["Тряпка - 50$", "Мочалка - 150$", "Сушилка - 1050$", "Пакет - 1$"]

agent_ghost = telebot.TeleBot(config["token"])


# keyboard_product = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
# keyboard_product.add(telebot.types.KeyboardButton("Xiaomi Redmi Note 99T"),
#                      telebot.types.KeyboardButton("Iphone 9"))


# keyboard_product = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
# keyboard_product.add(telebot.types.KeyboardButton("Тряпка"),
#                      telebot.types.KeyboardButton("Мочалка"))


keyboard_categories = telebot.types.InlineKeyboardMarkup()
keyboard_categories.add(telebot.types.InlineKeyboardButton(text="Хоз. товары", callback_data="hoz"),
                        telebot.types.InlineKeyboardButton(text="Электроника", callback_data="electro"))


@agent_ghost.message_handler(commands=["start", "buttons"])
def start(message):
    if message.text == "/start":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)


@agent_ghost.message_handler(content_types=["text"])
def get_text(message):
    pass
    # if message.text == "Xiaomi Redmi Note 99T":
    #     agent_ghost.send_message(message.chat.id, "Товар \"Xiaomi Redmi Note 99T\" успешно добавлен в корзину!\n\nКакая категория товара Вас интересует?", reply_markup=keyboard_categories)
    # elif message.text == "Iphone 9":
    #     agent_ghost.send_message(message.chat.id, "Товар \"Iphone 9\" успешно добавлен в корзину!\n\nКакая категория товара Вас интересует?", reply_markup=keyboard_categories)


# def all_pr_hoz(message):
#     if message.text == "Тряпка":
#         agent_ghost.send_message(message.chat.id, "Товар \"Тряпка\" успешно добавлен в корзину!\n\nКакая категория товара Вас интересует?", reply_markup=keyboard_categories)
#     elif message.text == "Мочалка":
#         agent_ghost.send_message(message.chat.id, "Товар \"Мочалка\" успешно добавлен в корзину!\n\nКакая категория товара Вас интересует?", reply_markup=keyboard_categories)


# def all_pr_electro(message):
#     if message.text == "Xiaomi Redmi Note 99T":
#         agent_ghost.send_message(message.chat.id, "Товар \"Xiaomi Redmi Note 99T\" успешно добавлен в корзину!\n\nКакая категория товара Вас интересует?", reply_markup=keyboard_categories)
#     elif message.text == "Iphone 9":
#         agent_ghost.send_message(message.chat.id, "Товар \"Iphone 9\" успешно добавлен в корзину!\n\nКакая категория товара Вас интересует?", reply_markup=keyboard_categories)


# def all_product(message):

@agent_ghost.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        if call.data == "hoz":
            keyboard_all_product = telebot.types.InlineKeyboardMarkup()
            for i in list_hoz:
                keyboard_all_product.add(telebot.types.InlineKeyboardButton(text=i, callback_data=i))
            keyboard_all_product.add(telebot.types.InlineKeyboardButton(text="Back", callback_data="back"))
            agent_ghost.send_message(call.message.chat.id, "Товары категории \"Хоз. товары\"", reply_markup=keyboard_all_product)
        elif call.data == "electro":
            keyboard_all_product = telebot.types.InlineKeyboardMarkup()
            for i in list_elect:
                keyboard_all_product.add(telebot.types.InlineKeyboardButton(text=i, callback_data=i))
            keyboard_all_product.add(telebot.types.InlineKeyboardButton(text="Back", callback_data="back"))
            agent_ghost.send_message(call.message.chat.id, "Товары категории \"Электроника\"", reply_markup=keyboard_all_product)
        elif call.data == "back":
            agent_ghost.send_message(call.message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
        for i in list_hoz:
            if i == call.data:
                agent_ghost.send_message(call.message.chat.id, f"Товар \"{i}\" успешно добавлен в корзину")
                break
        for i in list_elect:
            if i == call.data:
                agent_ghost.send_message(call.message.chat.id, f"Товар \"{i}\" успешно добавлен в корзину")
                break


# agent_ghost.polling(none_stop=True, interval=0)
agent_ghost.infinity_polling(timeout=10, long_polling_timeout=5)
