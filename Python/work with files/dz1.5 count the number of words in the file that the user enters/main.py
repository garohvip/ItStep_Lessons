import os

path = os.path.join("txtfile1.txt")

file = open(path, 'r')
file_read = file.read().split()
count = 0
find = input("Input word which would you like find and count: ")
for i in file_read:
    if find.lower() in i.lower():
        count += 1
print(f"Words in text of file equals: {count} things")
file.close()

#Recomended words: aliqua, lorem, elit