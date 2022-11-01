# PYTHON DEVELOPER HOMEWORK
____
## Условие задачи:

### Создать базу данных под названием `Sales` с тремя таблицами:
- Таблица со списком информации о сотрудниках/продавцов, под названием `Salesmen`
- Таблица со списком информации о покупателях, под названием `Customers`
- Таблица со списком сделок (информация про продажи), под названием `Sales`

###### :loudspeaker: *Да, название БД совпадает с названием таблицы*

### Создать приложение для работы с таблицами:

1. Вывод информации с определенными параметрами
   * Добавить возможность сохранения выведенной информации в файл
2. Добавление информации
3. Редактирование информации
4. Удаление информации

____

## Инструкция:

### 1. Создать БД
Я использовал для работы с БД приложение **MySQL Workbench 8.0 CE**

Для создания БД нужно ввести команду:
```
CREATE SCHEMA `name`;
```
![Code](file:///C:/Users/solando/Desktop/ItStep_Lessons/Screenshot_1.png "Code")

Где `name` - название вашей БД

После чего нажать на :zap: (молния)

![ZAP](file:///C:/Users/solando/Desktop/ItStep_Lessons/Screenshot_2.png "ZAP")

И должна появится внизу такая надпись c :white_check_mark: (зеленым кружочком и белой галочкой)

![Green mark](file:///C:/Users/solando/Desktop/ItStep_Lessons/Screenshot_3.png "Green mark")

Далее слева есть список ваших БД. Для отображения созданной БД нужно ее обновить нажав: :arrows_counterclockwise: (обновить)

![Reload](file:///C:/Users/solando/Desktop/ItStep_Lessons/Screenshot_4.png "Reload")

Вот и наша БД

![Result](file:///C:/Users/solando/Desktop/ItStep_Lessons/Screenshot_5.png "Result")

### 2. Ввод данных для работы с БД

Данные БД должны совпадать с данными в вашей БД.\
А это: `port` `user` `host` `password` `database`

Эту информацию Вы видите каждый раз, когда выбираете свой `connect`

![Connect](file:///C:/Users/solando/Desktop/ItStep_Lessons/Screenshot_6.png "Connect")

Эти данные нужно внести в текстовый файл `pass.txt` в таком порядке:

Где `host` = `localhost`\
Где `port` = `3306`\
Где `user` = `root`\
**Далее**\
Где `password` = `ваш пароль` (Пароль Вы создавали при установке MySQL)\
Где `database` = `название БД` (Название БД Вы вводили, когда создавали ее через код выше)

**Пример:**

![Example](file:///C:/Users/solando/Desktop/ItStep_Lessons/Screenshot_7.png "Example")

### 3. Запуск

- Для начала работы нужно запустить файл `start.py` для создания всех необходимых таблиц
- Дождаться окончания загрузки данных
- Запустить основной файл `main.py`
- **PERFECT**

____