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
    cursor.execute(f"""SELECT categories FROM `products`""")
    all_categories = cursor.fetchall()
keyboard_categories = telebot.types.InlineKeyboardMarkup()
for key in all_categories.get('categories'):
    keyboard_categories.add(telebot.types.InlineKeyboardButton(text=key, callback_data=key))


@agent_ghost.message_handler(commands=["start", "buttons"])
def start(message):
    if message.text == "/start":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)


@agent_ghost.message_handler(content_types=["text"])
def get_text(message):
    pass


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
        for i in all_categories.get('categories'):
            if call.data == i:
                with connection.cursor() as cursor:
                    cursor.execute(f"""SELECT categories FROM `products`""")
                    all_categories = cursor.fetchall()
                with connection.cursor() as cursor:
                    cursor.execute(f"""SELECT * FROM `products` WHERE categoriez = '}'""")
                    all_prod = cursor.fetchall()
                agent_ghost.send_message(call.message.chat.id, call.message.from_user.id)
                keyboard_all_product = telebot.types.InlineKeyboardMarkup()
                for i in list_hoz:
                    keyboard_all_product.add(telebot.types.InlineKeyboardButton(text=i, callback_data=i))
                keyboard_all_product.add(telebot.types.InlineKeyboardButton(text="Back", callback_data="back"))
                agent_ghost.send_message(call.message.chat.id, "Товары категории \"Хоз. товары\"", reply_markup=keyboard_all_product)
        # elif call.data == "electro":
        #     keyboard_all_product = telebot.types.InlineKeyboardMarkup()
        #     for i in list_elect:
        #         keyboard_all_product.add(telebot.types.InlineKeyboardButton(text=i, callback_data=i))
        #     keyboard_all_product.add(telebot.types.InlineKeyboardButton(text="Back", callback_data="back"))
        #     agent_ghost.send_message(call.message.chat.id, "Товары категории \"Электроника\"", reply_markup=keyboard_all_product)
        # elif call.data == "back":
        #     agent_ghost.send_message(call.message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
        # for i in list_hoz:
        #     if i == call.data:
        #         connection = pymysql.connect(
        #             host="localhost",
        #             port=3306,
        #             user='root',
        #             password='DataBase0321',
        #             database='shop_cart_telegram',
        #             cursorclass=pymysql.cursors.DictCursor
        #         )
        #         with connection.cursor() as cursor:
        #             cursor.execute(f"""INSERT INTO `cart` (idUser, nameUser, idProd, amountProd, priceAll) VALUES ({call.message.from_user.id}, '{call.message.from_user.first_name}', 1, 22, 66.22)""")
        #         agent_ghost.send_message(call.message.chat.id, f"Товар \"{i}\" успешно добавлен в корзину")
        #         break
        # for i in list_elect:
        #     if i == call.data:
        #         agent_ghost.send_message(call.message.chat.id, f"Товар \"{i}\" успешно добавлен в корзину")
        #         break


# agent_ghost.polling(none_stop=True, interval=0)
agent_ghost.infinity_polling(timeout=10, long_polling_timeout=5)




