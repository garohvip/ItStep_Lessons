from easygui import *

# Просмотр ассортимента товаров магазина
def outputProduct(connection):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT nameProduct, price FROM `products`""")
        all_products = cursor.fetchall()
    new_var = "\n".join([i.get('nameProduct') + " --- " + str(i.get('price')) + "$" for i in all_products]) # рассортировка для красоты
    return f"""Ассортимент товаров магазина АТБ\n\n{new_var}"""


# Добавление продуктов в корзину
def insertCart(connection, login):
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM `products`""")  # Считываем все продукты для возможности выбора пользователем из списка
        all_products = cursor.fetchall()
    info_prod = "\n".join([f"{i.get('nameProduct')} = {i.get('price')}$" for i in all_products])  # Рассортировка для всех продуктов
    choice_products = multchoicebox(info_prod, "Choose", [f"{i.get('nameProduct')}" for i in all_products]) # Выбор пользователем продуктов из списка
    enter_count_products = multenterbox("Enter", "Enter", [i for i in choice_products])  # Ввод количества выбранных продуктов пользователем
    enter_products_count = "\n".join([f"{choice_products[i]} - {enter_count_products[i]} шт." for i in range(
        len(choice_products))])  # Рассортировка всех выбранных продуктов и их количества пользователем
    if buttonbox(f"Все верно?:\n\n{enter_products_count}", "Enter", ["YES", "NO"]) == "YES":  # Проверка действий пользователя (те ли продукты выбрали и ввел ли правильное количество их)
        check_products_in_cart = []  # Переменная для проверки наличия выбранных пользователем продуктов в корзине, дабы изменить количество выбранных продуктов если они уже имеются в корзине
        prices = []  # Переменная для добавления списка price из таблицы products в таблицу cart (Для дальнейшего подсчета суммы оплаты всех продуктов, которые есть в корзине)
        with connection.cursor() as cursor:
            for i in choice_products:  # Прохожу по списку всех продуктов, которые выбрал пользователь
                cursor.execute(
                    f"""SELECT nameProduct FROM `cart` WHERE loginUser = '{login}' AND nameProduct = '{i}'""")  # получаю все продукты, которые уже есть в корзине, из тех продуктов, которые выбрал пользователь
                check_products_in_cart.append(cursor.fetchone())
        check_products_in_cart = list(filter(None,
                                             check_products_in_cart))  # если продукта нет в корзине, то в списке появляется None. Здесь я убираю все None из списка
        new_var = []  # переменная для отправки запроса и получения инфы с БД, а так же для изменения уже имеющихся продуктов в корзине
        new_choice_products = {}  # словарь для добавления уже имеющихся продуктов и их количество для покупки в корзине# if check_products_in_cart:  # Если список не пуст, то срабатывает код на изменение количества продуктов, которые уже есть в корзине и добавление тех продуктов, которых еще не в корзине
        for i in check_products_in_cart:  # Прохожу по списку продуктов, которые уже есть в корзине
            for j in range(
                    len(choice_products)):  # Прохожу по списку всех продуктов, которые выбрал пользователь для покупки
                if i.get('nameProduct') == choice_products[
                    j]:  # если продукт, который есть в корзине совпадает с продуктом который выбрал пользователь, то удаляю есть из списка всех продуктов, которые выбрал пользователь для покупки
                    new_choice_products = dict(nameProduct=choice_products[j], count=enter_count_products[
                        j])  # добавляю в словарь продукты и его количество для покупки, которые выбрал пользователь
                    choice_products.pop(
                        j)  # удаляю уже имеющийся продукт в корзине из списка всех продуктов, которые выбрал пользователь для покупки
                    enter_count_products.pop(
                        j)  # удаляю количество определенного продукта из списка всех продуктов, которые выбрал пользователь для покупки
                    break  # останавливаю цикл так как только 1 раз может попастся определенный продукт
            new_var.append(
                new_choice_products)  # добавляю словарь с продуктом и его количеством для покупки в список для дальнейшей работы с этой переменной
        with connection.cursor() as cursor:
            for i in new_var:  # прохожу по списку словарей с продуктами и их количество для покупки, чтобы получить количество продуктов, которые уже есть в корзине, чтобы их прибавить в БД
                cursor.execute(
                    f"""SELECT count FROM `cart` WHERE loginUser = '{login}' AND nameProduct = '{i.get('nameProduct')}'""")
                prices.append(
                    cursor.fetchone())  # добавляю в пустой список дабы не создавать новую переменную (в дальнейшем аннулирую этот список)
            for i in range(len(new_var)):  # изменяю количество уже имеющихся продуктов в БД
                cursor.execute(
                    f"""UPDATE `cart` SET count = {int(new_var[i].get('count')) + int(prices[i].get('count'))} WHERE loginUser = '{login}' AND nameProduct = '{new_var[i].get('nameProduct')}'""")
                connection.commit()
            prices = []  # аннулировал список
            for i in choice_products:  # прошелся по списку всех продуктов которые выбрал пользователь для покупки
                cursor.execute(f"""SELECT price FROM `products` WHERE nameProduct = '{i}'""")
                prices.append(cursor.fetchone())  # получил цену этих продуктов, чтобы добавить в дальнейшем их в БД
            for i in range(
                    len(choice_products)):  # прошелся по количеству элементов в списке, чтобы добавить все новые продукты в БД
                cursor.execute(
                    f"""INSERT INTO `cart` (loginUser, nameProduct, count, price) VALUES ('{login}', '{choice_products[i]}', '{enter_count_products[i]}', '{prices[i].get('price')}')""")
                connection.commit()
        return "Успешно добавлено в корзину!"
    else:
        return "Операция отменена"


# Просмотр корзины
def checkCart(connection, login):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT nameProduct, count FROM `cart` WHERE loginUser = '{login}'""")  # считал имя и количество продуктов
        all_products_cart = cursor.fetchall()
        cursor.execute(f"""SELECT price FROM `cart` WHERE loginUser = '{login}'""")  # считал цену товаров (для удобства разделил)
        all_products_cart_price = cursor.fetchall()
    if all_products_cart:  # проверка на наличие товаров в корзине
        for i in range(len(all_products_cart)):
            all_products_cart[i]['price'] = f"{all_products_cart_price[i].get('price') * all_products_cart[i].get('count')}"  # изменяю цену товара в переменной для дальнейшего вывода общей цены всех покупок и каждого товара отдельно
        new_var = "\n".join([i.get('nameProduct') + " - " + str(i.get('count')) + " шт. --- " + i.get('price') + "$" for i in all_products_cart])  # красота для вывода
        all_summa = 0  # для подсчета общей суммы всех товаров
        for i in range(len(all_products_cart)):
            all_summa += int(all_products_cart[i].get('price'))  # подсчет общей суммы всех товаров
        return f"""Корзина {login}:\n\n{new_var}\n\nОбщая сумма: {all_summa}$"""
    else:
        return """Корзина пуста"""


# Удаление товара из корзины
def deleteCart(connection, login):
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT nameProduct, count FROM `cart` WHERE loginUser = '{login}'""")  # считал имя и количество продуктов
        all_products_cart = cursor.fetchall()
        cursor.execute(f"""SELECT price FROM `cart` WHERE loginUser = '{login}'""")  # считал цену товаров (для удобства разделил)
        all_products_cart_price = cursor.fetchall()
    if all_products_cart:  # проверка на наличие товаров в корзине
        for i in range(len(all_products_cart)):
            all_products_cart[i]['price'] = f"{all_products_cart_price[i].get('price') * all_products_cart[i].get('count')}"  # для вывода общей суммы конкретного товара
        new_var = "\n".join([i.get('nameProduct') + " - " + str(i.get('count')) + " шт. --- " + i.get('price') + "$" for i in all_products_cart])  # для красоты вывода
        enter_count_products = multenterbox(f"""Корзина {login}:\n\n{new_var}""", "Enter", [i.get('nameProduct') for i in all_products_cart])  # пользователь вписывает количество каждого товара для удаления
        next_stage = 0  # для проверки на дурака
        for i in range(len(enter_count_products)):  # цикл для замены пустых скобок в списке на нули (для корректной работы кода)
            if enter_count_products[i] == '':
                enter_count_products[i] = 0
        for i in range(len(all_products_cart)):  # собственно сама проверка на дурака (если пользователь вводить количество определенного продукта больше чем он положил его в корзину)
            if all_products_cart[i].get('count') >= int(enter_count_products[i]):
                next_stage += 1
            else:
                break
        if next_stage == len(enter_count_products):  # если проверка на дурака пройдена, то продолжается процесс
            for i in range(len(all_products_cart)):
                if all_products_cart[i].get('count') > int(enter_count_products[i]):  # если количество товара которое хочет удалить пользователь меньше чем есть в корзине
                    with connection.cursor() as cursor:  # Тогда вычитаем количество товара из того количества, которое есть в корзине и изменяем его в БД
                        cursor.execute(f"""UPDATE `cart` SET count = {all_products_cart[i].get('count') - int(enter_count_products[i])} WHERE loginUser = '{login}' AND nameProduct = '{all_products_cart[i].get('nameProduct')}'""")
                        connection.commit()
                elif all_products_cart[i].get('count') == int(enter_count_products[i]):  # если количество товара которое хочет удалить пользователь равно количеству товара в корзине
                    with connection.cursor() as cursor:  # тогда удаляем товар из БД
                        cursor.execute(f"""DELETE FROM `cart` WHERE loginUser = '{login}' AND nameProduct = '{all_products_cart[i].get('nameProduct')}'""")
                        connection.commit()
            return """Продукты успешно удалены"""
        else:
            return """Вы хотите удалить больше продуктов чем есть в корзине!"""
    else:
        return """Корзина пуста"""


# Очистить корзину
def cleanTrash(connection, login):
    if buttonbox("Вы точно хотите очистить корзину?", "Enter", ["Очистить", "Отмена"]) == "Очистить":  # подтверждение очистки корзины
        with connection.cursor() as cursor:
            cursor.execute(f"""DELETE FROM `cart` WHERE loginUser = '{login}'""")
            connection.commit()
        return "Корзина очищена!"
