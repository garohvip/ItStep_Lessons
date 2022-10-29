import os.path

path = os.path.join("data_base", "test1.txt")
math = os.path.join("data_base", "test2.txt")

# file = open(path, "r")
# str_var = file.readlines(3)
# print(str_var)
# file.close()

# file1 = open(path, "r")
# file2 = open(math, "w")
# # if file2.readline().split(" ")
# spliting_var = file1.read().split()
# print(spliting_var)
# for i in spliting_var:
#     if len(i) >= 7:
#         file2.write(i + "\n")
# file1.close()
# file2.close()

# file1 = open(path, "r")
# file2 = open(math, "w")
# # if file2.readline().split(" ")
# spliting_var = file1.read().split("\n")
# print(spliting_var)
# spliting_var.reverse()
# for i in spliting_var:
#     file2.write(i + "\n")
# file1.close()
# file2.close()

file1 = open(path, "r")
file2 = open(math, "w")
# if file2.readline().split(" ")
spliting_var = file1.read().split("\n")
print(spliting_var)
for i in spliting_var[::-1]:
    file2.write(i + "\n")
file1.close()
file2.close()