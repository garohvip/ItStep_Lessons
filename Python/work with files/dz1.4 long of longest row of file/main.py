import os

path1 = os.path.join("filetxt1.txt")

file = open(path1, "r", encoding='utf-8')
file_read = file.readlines()
line = ""
count = 0
for i in file_read:
    if len(i) > len(line):
        line = i
for i in line:
    count += 1
print(f"Long of longest row of file \"{path1}\" equals: {count} symbols.\nThis is a row with text: {line[:-1]}.")
file.close()