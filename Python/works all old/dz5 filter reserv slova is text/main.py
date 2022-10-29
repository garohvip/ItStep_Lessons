#Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua
text = input("Введите текст: ")
number = int(input("Введите число, сколько хотите ввести зарезервированных слов: "))
s = []
h = 0
repeat = True
spliting = text.split()

while repeat:
    if number >= 1 and number <= 3:
        while h != number:
            s.append(input("Введите зарезервированное слово: "))
            h += 1
        repeat = False
    else:
        print("Введите количество от 1 до 3 слов включительно")
        repeat = False

for i in range(len(s)):
    for j in range(len(spliting)):
        if s[i] in spliting[j]:
            spliting[j] = spliting[j].upper()

split1 = ' '.join(spliting)
print(split1)