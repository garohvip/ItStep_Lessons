import os

path = os.path.join("txtfile1.txt")

file1 = open(path, "r")
file2 = open(path, "r")
file_read_symbol = file2.read()
file_read_line = file1.readline()
print(file_read_line)
print(file_read_symbol)
count_symbol = 0
count_lines = 0
for i in file_read_symbol:
    count_symbol += 1
for j in file_read_line:
    count_lines += 1
print(f"Символов в файле {count_symbol}")
print(f"Строк в файле {count_lines}")
file1.close()
file2.close()