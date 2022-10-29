import os

path1 = os.path.join("txtfile1.txt")
path2 = os.path.join("txtfile2.txt")

file1 = open(path1, "r")
file2 = open(path2, "w")
file1_read = file1.read()
for i in file1_read:
    if i == "*":
        i = "&"
    elif i == "&":
        i = "*"
    file2.write(i)

file1.close()
file2.close()