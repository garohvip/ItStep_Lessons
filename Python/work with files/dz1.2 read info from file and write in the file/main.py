import os.path


path1 = os.path.join("data_base", "filetxt1.txt")
path2 = os.path.join("data_base", "filetxt2.txt")

file1 = open(path1, "r", encoding='utf-8')
file2 = open(path2, "w", encoding='utf-8')
read_file1 = file1.read()
amo_sym = 0
amo_lin = 1
vowels = 0
consonants = 0
numbers = 0
space = 0
for i in read_file1:
    if i != " " and i != "\n":
        amo_sym += 1
        if i.lower() in 'aeiouy' or i.lower() in 'ауоыэяюёие':
            vowels += 1
        elif i.lower() in 'bcdfghjklmnpqrstvwxz' or i.lower() in 'бвгджзйклмнпрстфхцчшщ':
            consonants += 1
    if i == "\n":
        amo_lin += 1
    if i in "1234567890":
        numbers += 1
    if i == " ":
        space += 1
file2.write(f"В файле \"{path1}\" находится:\n    •Символов не включая пробелы: {amo_sym}\n    •Символов включая пробелы: {amo_sym + space}\n    •Строк: {amo_lin}\n    •Гласных букв: {vowels}\n    •Согласных букв: {consonants}\n    •Цифр: {numbers}")
file1.close()
file2.close()