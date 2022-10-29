file1 = open(path1, "r")
file2 = open(path2, "w")
eng_word = enterbox("Input your word: ", "Transliteration in English")
eng_file = file1.readlines()
englist = list(eng_word)
transword = []
for eng in englist:
    for line in eng_file:
        if line.startswith(eng):
            print(line)
            x = line.split(" ")
            y = x[1].rstrip()
            transword.append(y)

new_word = "".join(transword)
file2.write(new_word)
#with open('text2.txt', 'w') as f:
    #f.write(new_word)

#with open('text2.txt', 'w') as f:
    #f.write(str_ru.encode('utf-8').decode('utf-8'))

#with open('str_ru_bytes.txt', 'wb') as f:
    #f.write(str_ru.encode('utf-8'))




file1.close()
file2.close()