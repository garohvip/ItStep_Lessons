import os.path

path1 = os.path.join("txtfile1.txt")
path2 = os.path.join("txtfile2.txt")

file1 = open(path1, "r")
file2 = open(path2, "w")
file1_read = file1.readlines()
print(file1_read)

file1_read.pop()
for i in file1_read:
    file2.write(i)

# for i in range(len(file1_read)-1):
#     file2.write(file1_read[i])

# for i in file1_read[:-1]:
#     file2.write(i)

file1.close()
file2.close()