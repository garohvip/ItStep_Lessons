a = (7, 14, 21, 28)
b = (7, 15, 22, 28)
c = (6, 15, 2, 28)
view = []

print("Задача 1. Вывод элементов которые есть во всех кортежах:")
for i in range(len(a)):
    if a[i] == b[i] == c[i]:
        view.append(a[i])
print("Во всех кортежах есть число(а): ", view)
print(" ")

print(" ")
view = []
print("Задача 2. Вывод элементов которые есть во всех кортежах:")
for i in range(len(a)):
    if a[i] != b[i] and a[i] != c[i] and a[i] not in view:
        view.append(a[i])
for i in range(len(b)):
    if b[i] != a[i] and b[i] != c[i] and b[i] not in view:
        view.append(b[i])
for i in range(len(c)):
    if c[i] != a[i] and c[i] != b[i] and c[i] not in view:
        view.append(c[i])
print("В a and b and c уникальные числа это: ", view)
print(" ")

print(" ")
print("Задача 3. Вывод элементов которые есть во всех кортежах по рядам:")
print("Элементы a in b:")
for i in range(len(a)):
    if a[i] == b[i]:
        print(a[i])
print("Элементы b in c:")
for i in range(len(b)):
    if b[i] == c[i]:
        print(b[i])
print("Элементы c in a:")
for i in range(len(c)):
    if c[i] == a[i]:
        print(c[i])
print("Элементы на одной линии сразу в трех кортежах:")
for i in range(len(a)):
    if a[i] == b[i] == c[i]:
        print(a[i])