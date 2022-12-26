import datetime
import telebot
from tel_app.models import *
from django.utils import timezone

config = {
    "name": "",
    "token": "5956132893:AAFF-d6ntEWNb9iNS2i6gx4CzdEcydQ4w7c"
}

agent_ghost = telebot.TeleBot(config["token"])

all_categories = Categorie.objects.all()
keyboard_categories = telebot.types.ReplyKeyboardMarkup()
for key in all_categories:
    keyboard_categories.add(telebot.types.KeyboardButton(key.nameCategories))
keyboard_categories.add(telebot.types.KeyboardButton('Корзина'))

keyboard_cancel = telebot.types.ReplyKeyboardMarkup()
keyboard_cancel.add(telebot.types.KeyboardButton('Назад'))

keyboard_cart_or_next = telebot.types.ReplyKeyboardMarkup()
keyboard_cart_or_next.add(telebot.types.KeyboardButton('Продолжить'),
                          telebot.types.KeyboardButton('Корзина'))

keyboard_pay = telebot.types.ReplyKeyboardMarkup()
keyboard_pay.add(telebot.types.KeyboardButton("Удалить товар из корзины"),
                 telebot.types.KeyboardButton("Очистить корзину"),
                 telebot.types.KeyboardButton('Оплатить'),
                 telebot.types.KeyboardButton('Меню'))


@agent_ghost.message_handler(commands=["start", "buttons"])
def start(message):
    if message.text == "/start":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)


@agent_ghost.message_handler(content_types=["text"])
def get_text(message):
    if message.text == "Корзина":
        all_cart_user = Order.objects.filter(idUser=message.chat.id)
        all_cart = []
        for i in range(len(all_cart_user)):
            all_cart.append(f"{i+1}. {all_cart_user[i].nameProd} -> {all_cart_user[i].value} шт. = {all_cart_user[i].price}$\n")
        if all_cart:
            all_cart.insert(0, "Ваша корзина:\n\n")
            agent_ghost.send_message(message.chat.id, "".join(all_cart), reply_markup=keyboard_pay)
        else:
            all_cart.append("Ваша корзина:\n\nПусто")
            agent_ghost.send_message(message.chat.id, "".join(all_cart), reply_markup=keyboard_pay)
    elif message.text == "Меню":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
    elif message.text == "Продолжить":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
    elif message.text == "Очистить корзину":
        all_products = Order.objects.filter(idUser=message.chat.id)
        if all_products:
            for i in all_products:
                Product.objects.filter(nameProd=i.nameProd).update(value=Product.objects.get(nameProd=i.nameProd).value+i.value)
            all_products.delete()
            agent_ghost.send_message(message.chat.id, "Корзина очищена!")
            agent_ghost.send_message(message.chat.id, "Ваша корзина:\n\nПусто", reply_markup=keyboard_pay)
        else:
            agent_ghost.send_message(message.chat.id, "Ваша корзина:\n\nПусто", reply_markup=keyboard_pay)
    elif message.text == "Удалить товар из корзины":
        all_products = Order.objects.filter(idUser=message.chat.id)
        if all_products:
            keyboard_products_user = telebot.types.InlineKeyboardMarkup()
            for i in all_products:
                ss = telebot.types.InlineKeyboardButton(text=i.nameProd.nameProd, callback_data="delete" + i.nameProd.nameProd)
                keyboard_products_user.add(ss)
            agent_ghost.send_message(message.chat.id, "Какой товар хотите удалить?", reply_markup=keyboard_products_user)
        else:
            agent_ghost.send_message(message.chat.id, "Ваша корзина:\n\nПусто", reply_markup=keyboard_pay)

    else:
        all_products_of_categ = Product.objects.filter(nameCategorie__nameCategories=message.text)
        if all_products_of_categ:
            keyboard_all_products_of_categ = telebot.types.InlineKeyboardMarkup()
            for j in all_products_of_categ:
                if j.value >= 1:
                    keyboard_all_products_of_categ.add(telebot.types.InlineKeyboardButton(text=f"{j.nameProd} - {j.price}$", callback_data=j.nameProd))
            agent_ghost.send_message(message.chat.id, f"Товары категории \"{message.text}\"", reply_markup=keyboard_all_products_of_categ)
        else:
            agent_ghost.send_message(message.chat.id, "Некорректный ввод")


def add_product_cart(message):
    if message.text == "Назад":
        agent_ghost.send_message(message.chat.id, "Какая категория товара Вас интересует?", reply_markup=keyboard_categories)
    else:
        if message.text.isdigit():
            if int(message.text) >= 1:
                price_prod_var = 0.0
                price_prod = Product.objects.filter(nameProd=name_product)
                cart = Order.objects.filter(idUser=message.chat.id, nameProd__nameProd__contains=name_product)
                users_value = 0
                users_price = 0
                value_one_prod = 0
                for i in price_prod:
                    if int(message.text) <= int(i.value):
                        price_prod_var = i.price
                        value_one_prod = int(i.value) - int(message.text)
                    else:
                        return agent_ghost.send_message(message.chat.id, "Такого количества товара нет на складе. Извините за неудобства!\n\nКакая категория товара Вас интересует?", reply_markup=keyboard_categories)
                if cart:
                    for i in cart:
                        users_value = int(i.value) + int(message.text)
                        users_price = float(i.price) + int(message.text) * float(price_prod_var)
                        break
                else:
                    users_value = int(message.text)
                    users_price = float(price_prod_var) * int(message.text)
                cart.delete()
                Order.objects.get_or_create(
                    nameProd=Product.objects.get(nameProd=name_product),
                    idUser=message.chat.id,
                    dtOrder=timezone.now(),
                    value=users_value,
                    price=users_price
                )
                price_prod.update(value=value_one_prod)
                agent_ghost.send_message(message.chat.id, f"Добавлено в корзину в количество {message.text} шт.", reply_markup=keyboard_cart_or_next)
            else:
                agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введи положительное число!"), add_product_cart)
        else:
            agent_ghost.register_next_step_handler(agent_ghost.send_message(message.chat.id, "Введи только число!"), add_product_cart)


@agent_ghost.callback_query_handler(func=lambda call: True)
def callback_data(call):
    global name_product
    name_product = call.data
    if call.message:
        if call.data[:6] == "delete":
            one_prod = Order.objects.filter(idUser=call.message.chat.id, nameProd__nameProd=call.data[6:])
            for i in one_prod:
                Product.objects.filter(nameProd=i.nameProd).update(value=Product.objects.get(nameProd=i.nameProd).value+i.value)
            one_prod.delete()
            all_products = Order.objects.filter(idUser=call.message.chat.id)
            agent_ghost.send_message(call.message.chat.id, f"Товар \"{call.data[6:]}\" успешно удален из вашей корзины!")
            all_cart = []
            for i in range(len(all_products)):
                all_cart.append(f"{i+1}. {all_products[i].nameProd} -> {all_products[i].value} шт. = {all_products[i].price}$\n")
            if all_cart:
                all_cart.insert(0, "Ваша корзина:\n\n")
                agent_ghost.send_message(call.message.chat.id, "".join(all_cart), reply_markup=keyboard_pay)
            else:
                all_cart.append("Ваша корзина:\n\nПусто")
                agent_ghost.send_message(call.message.chat.id, "".join(all_cart), reply_markup=keyboard_pay)
        else:
            agent_ghost.register_next_step_handler(agent_ghost.send_message(call.message.chat.id, f"Введите количество товара:", reply_markup=keyboard_cancel), add_product_cart)


# agent_ghost.polling(none_stop=True, interval=0)
agent_ghost.infinity_polling(timeout=10, long_polling_timeout=5)
