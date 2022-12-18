import json
import time
import base64
import telebot
import re
import pymysql

config = {
    "name": "",
    "token": "5956132893:AAFF-d6ntEWNb9iNS2i6gx4CzdEcydQ4w7c"
}

agent_ghost = telebot.TeleBot(config["token"])

connection = pymysql.connect(
    host="localhost",
    port=3306,
    user='root',
    password='DataBase0321',
    database='shop_cart_telegram',
    cursorclass=pymysql.cursors.DictCursor
)
with connection.cursor() as cursor:
    cursor.execute(f"""SELECT nameCategories FROM `categories`""")
    all_categories = cursor.fetchall()
keyboard_categories = telebot.types.InlineKeyboardMarkup()
for key in all_categories:
    keyboard_categories.add(telebot.types.InlineKeyboardButton(text=key.get('nameCategories'), callback_data=key.get('nameCategories')))

keyboard_cancel = telebot.types.ReplyKeyboardMarkup()
keyboard_cancel.add(telebot.types.KeyboardButton('Назад'))

keyboard_cart_or_next = telebot.types.ReplyKeyboardMarkup()
keyboard_cart_or_next.add(telebot.types.KeyboardButton('Продолжить'),
                          telebot.types.KeyboardButton('Корзина'))

keyboard_pay = telebot.types.ReplyKeyboardMarkup()
keyboard_pay.add(telebot.types.KeyboardButton('Оплатить'),
                 telebot.types.KeyboardButton('Меню'))


@agent_ghost.message_handler(commands=["start", "buttons"])
def start(message):
    if message.text == "/start":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)


@agent_ghost.message_handler(content_types=["text"])
def get_text(message):
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user='root',
        password='DataBase0321',
        database='shop_cart_telegram',
        cursorclass=pymysql.cursors.DictCursor
    )
    if message.text == "Назад":
        with connection.cursor() as cursor:
            cursor.execute(f"""DELETE FROM `cartUser` WHERE idTelegramUser = {message.from_user.id} AND value IS NULL""")
            connection.commit()
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
    elif message.text == "Продолжить":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
    elif message.text == "Меню":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
    elif message.text == "Корзина":
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM `cartUser` WHERE idTelegramUser = {message.from_user.id}""")
            all_cart_user = cursor.fetchall()
        all_cart = [f"Ваша корзина:\n\n"]
        for i in range(len(all_cart_user)):
            all_cart.append(f"{i+1}. {all_cart_user[i].get('nameCategories')} -> {all_cart_user[i].get('nameProd')} - {all_cart_user[i].get('value')} шт. = {all_cart_user[i].get('price')}$\n")
        agent_ghost.send_message(message.chat.id, "".join(all_cart), reply_markup=keyboard_pay)
    else:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT nameProd FROM `products`""")
            all_products = cursor.fetchall()
        for i in all_products:
            if i.get('nameProd') == message.text:
                with connection.cursor() as cursor:
                    cursor.execute(f"""UPDATE `cartUser` SET nameProd = '{i.get('nameProd')}' WHERE idTelegramUser = {message.from_user.id} AND nameProd IS NULL""")
                    connection.commit()
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Сколько хотите приобрести товара?", reply_markup=keyboard_cancel), add_product_cart)


def add_product_cart(message):
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user='root',
        password='DataBase0321',
        database='shop_cart_telegram',
        cursorclass=pymysql.cursors.DictCursor
    )
    if message.text == "Назад":
        with connection.cursor() as cursor:
            cursor.execute(f"""DELETE FROM `cartUser` WHERE idTelegramUser = {message.from_user.id} AND value IS NULL""")
            connection.commit()
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
    else:
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT nameProd FROM `cartUser` WHERE idTelegramUser = {message.from_user.id} AND value IS NULL""")
            nameProduct = cursor.fetchone()
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT value, price FROM `products` WHERE nameProd = '{nameProduct.get('nameProd')}'""")
            all_products = cursor.fetchone()
        if all_products.get('value') >= int(message.text):
            with connection.cursor() as cursor:
                cursor.execute(f"""UPDATE `cartUser` SET value = {int(message.text)}, price = {float(all_products.get('price')) * int(message.text)} WHERE idTelegramUser = {message.from_user.id} AND nameProd = '{nameProduct.get('nameProd')}' AND value IS NULL""")
                connection.commit()
            agent_ghost.send_message(message.chat.id, f"Товар '{nameProduct.get('nameProd')}' в количество {message.text} шт. успешно добавлено в корзину", reply_markup=keyboard_cart_or_next)
        else:
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Количество товара, которое Вы ввели превышает количество товара на складе.\n\nНапишите новое количество:", reply_markup=keyboard_cancel), add_product_cart)


@agent_ghost.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            password='DataBase0321',
            database='shop_cart_telegram',
            cursorclass=pymysql.cursors.DictCursor
        )
        with connection.cursor() as cursor:
            cursor.execute("""SELECT nameCategories FROM `categories`""")
            all_categories = cursor.fetchall()
        for i in all_categories:
            if i.get('nameCategories') == call.data:
                with connection.cursor() as cursor:
                    cursor.execute(f"""INSERT INTO `cartUser` (idTelegramUser, nameCategories) VALUES ({call.from_user.id}, '{i.get('nameCategories')}')""")
                    connection.commit()
                with connection.cursor() as cursor:
                    cursor.execute(f"""SELECT * FROM `products` WHERE nameCategories = '{call.data}'""")
                    all_products = cursor.fetchall()
                keyboard_all_products = telebot.types.ReplyKeyboardMarkup()
                phrases = [f"Товары категории {i.get('nameCategories')}:\n\n"]
                for prod in range(len(all_products)):
                    keyboard_all_products.add(telebot.types.KeyboardButton(all_products[prod].get('nameProd')))
                    if all_products[prod].get('value') > 0:
                        phrases.append(f"{prod+1}. {all_products[prod].get('nameProd')} - {all_products[prod].get('price')}$\n")
                    elif all_products[prod].get('value') == 0:
                        phrases.append(f"{prod+1}. {all_products[prod].get('nameProd')} - {all_products[prod].get('price')}$ (нет в наличии)\n")
                keyboard_all_products.add(telebot.types.KeyboardButton('Назад'))
                agent_ghost.send_message(call.message.chat.id, "".join(phrases), reply_markup=keyboard_all_products)


# agent_ghost.polling(none_stop=True, interval=0)
agent_ghost.infinity_polling(timeout=10, long_polling_timeout=5)




