ed = ''
number = 0
repeat = True
sm = 0
m = 0
km = 0
mile = 0
inch = 0
yard = 0
while repeat:
    print("Введите единицу измерения")
    print("(см) (метр) (км) (миль) (дюйм) (ярд)")
    ed = input()
    if ed == "см" or ed == "метр" or ed == "км" or ed == "миль" or ed == "дюйм" or ed == "ярд":
        print("Введите количетсво", ed)
        number = float(input())
        if ed == "см":
            m = number * 0.01
            km = number * 0.00001
            mile = number * 0.000006213727366498068
            inch = number * 0.393701
            yard = number * 0.0109361
            print(ed, "будет:", m, "метров")
            print(ed, "будет:", km, "километров")
            print(ed, "будет:", mile, "миль")
            print(ed, "будет:", inch, "дюймов")
            print(ed, "будет:", yard, "ярд")
            print("Повторить? да/нет")
            rep = input()
            if rep == "нет":
                print("Пока")
                repeat = False
        elif ed == "метр":
            sm = number * 100
            km = number * 0.001
            mile = number * 0.000621371
            inch = number * 39.3701
            yard = number * 1.09361
            print(ed, "будет:", sm, "сантиметров")
            print(ed, "будет:", km, "километров")
            print(ed, "будет:", mile, "миль")
            print(ed, "будет:", inch, "дюймов")
            print(ed, "будет:", yard, "ярд")
            print("Повторить? да/нет")
            rep = input()
            if rep == "нет":
                print("Пока")
                repeat = False
        elif ed == "км":
            sm = number * 100000
            m = number * 1000
            mile = number * 0.621371
            inch = number * 39370.1
            yard = number * 1093.61
            print(ed, "будет:", sm, "сантиметров")
            print(ed, "будет:", m, "метров")
            print(ed, "будет:", mile, "миль")
            print(ed, "будет:", inch, "дюймов")
            print(ed, "будет:", yard, "ярд")
            print("Повторить? да/нет")
            rep = input()
            if rep == "нет":
                print("Пока")
                repeat = False
        elif ed == "миль":
            sm = number * 0.000006213727366498068
            m = number * 1609.34
            km = number * 0.621371
            inch = number * 63360
            yard = number * 1760
            print(ed, "будет:", sm, "сантиметров")
            print(ed, "будет:", m, "метров")
            print(ed, "будет:", km, "километров")
            print(ed, "будет:", inch, "дюймов")
            print(ed, "будет:", yard, "ярд")
            print("Повторить? да/нет")
            rep = input()
            if rep == "нет":
                print("Пока")
                repeat = False
        elif ed == "дюйм":
            sm = number * 2.54
            m = number * 0.0254
            km = number * 0.00002539998628400741
            mile = number * 0.00001578282828282828
            yard = number * 0.0277778
            print(ed, "будет:", sm, "сантиметров")
            print(ed, "будет:", m, "метров")
            print(ed, "будет:", km, "километров")
            print(ed, "будет:", mile, "миль")
            print(ed, "будет:", yard, "ярд")
            print("Повторить? да/нет")
            rep = input()
            if rep == "нет":
                print("Пока")
                repeat = False
        elif ed == "ярд":
            sm = number * 91.44
            m = number * 0.9144
            km = number * 0.0009144
            mile = number * 0.000568182
            inch = number * 36
            print(ed, "будет:", sm, "сантиметров")
            print(ed, "будет:", m, "метров")
            print(ed, "будет:", km, "километров")
            print(ed, "будет:", mile, "миль")
            print(ed, "будет:", inch, "дюймов")
            print("Повторить? да/нет")
            rep = input()
            if rep == "нет":
                print("Пока")
                repeat = False
    else:
        print("Вы ввели не верную единицу измерения")
        print("Повторить попытку снова? да/нет")
        rep = input()
        if rep == "нет":
            print("Пока")
            repeat = False