import datetime
import telebot
from tel_app.models import *

config = {
    "name": "",
    "token": "5956132893:AAFF-d6ntEWNb9iNS2i6gx4CzdEcydQ4w7c"
}

agent_ghost = telebot.TeleBot(config["token"])

all_categories = Categorie.objects.all()
keyboard_categories = telebot.types.ReplyKeyboardMarkup()
for key in all_categories:
    keyboard_categories.add(telebot.types.KeyboardButton(key.nameCategories))

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
    if message.text == "Корзина":
        all_cart_user = Order.objects.filter(idUser=1)
        all_cart = [f"Ваша корзина:\n\n"]
        for i in range(len(all_cart_user)):
            all_cart.append(f"{i+1}. {all_cart_user[i].nameProd} -> {all_cart_user[i].value} шт. = {all_cart_user[i].price}$\n")
        agent_ghost.send_message(message.chat.id, "".join(all_cart), reply_markup=keyboard_pay)
    elif message.text == "Меню":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
    else:
        keyboard_all_products_of_categ = telebot.types.InlineKeyboardMarkup()
        all_products_of_categ = Product.objects.filter(nameCategorie__nameCategories=message.text)
        for j in all_products_of_categ:
            if j.value >= 1:
                keyboard_all_products_of_categ.add(telebot.types.InlineKeyboardButton(text=f"{j.nameProd} - {j.price}$", callback_data=j.nameProd))
        agent_ghost.send_message(message.chat.id, f"Товары категории \"{message.text}\"", reply_markup=keyboard_all_products_of_categ)


def add_product_cart(message):
    if message.text == "Назад":
        Order.objects.filter(idUser=message.chat.id, nameProd=name_product, value=0, price=0).delete()
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
    else:
        if message.text.isdigit():
            if int(message.text) >= 1:
                price_prod = Product.objects.filter(nameProd=name_product)
                for i in price_prod:
                    price_prod_var = i.price
                date_var = str(datetime.datetime.now())[0:10].split("-")
                time_var = str(datetime.datetime.now())[11:19].split(":")
                Order.objects.get_or_create(
                    nameProd=Product.objects.filter(nameProd=name_product)[0].id,
                    idUser=message.chat.id,
                    dtOrder=datetime.datetime(year=int(date_var[0]), month=int(date_var[1]), day=int(date_var[2]), hour=int(time_var[0]), minute=int(time_var[1]), second=int(time_var[2])),
                    value=int(message.text),
                    price=float(int(message.text) * float(price_prod_var))
                )
                agent_ghost.send_message(message.chat.id, f"Добавлено в корзину в количество {message.text} шт.")
            else:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введи положительное число!"), add_product_cart)
        else:
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введи только число!"), add_product_cart)


@agent_ghost.callback_query_handler(func=lambda call: True)
def callback_data(call):
    global name_product
    name_product = call.data
    if call.message:
        agent_ghost.register_next_step_handler(agent_ghost.send_message(call.message.chat.id, f"Введите количество товара:", reply_markup=keyboard_cancel), add_product_cart)


# agent_ghost.polling(none_stop=True, interval=0)
agent_ghost.infinity_polling(timeout=10, long_polling_timeout=5)
