import os

path = os.path.join("txtfile1.txt")

file = open(path, "r+")
file_read = file.readlines()
print(file_read)
file.seek(0)
file.truncate()
for i in file_read:
    if i[-2] == ",":
        file.write(f"{i}********\n")
    else:
        file.write(f"{i}")
file.close()