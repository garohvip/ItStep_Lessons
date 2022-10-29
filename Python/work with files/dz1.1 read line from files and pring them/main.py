import os.path

path1 = os.path.join("data_base", "txtfile1.txt")
path2 = os.path.join("data_base", "txtfile2.txt")

file1 = open(path1, "r")
file2 = open(path2, "r")
read_string = file1.read().split("\n")
reading_string = file2.read().split("\n")
for i in range(len(read_string)):
    if read_string[i] != reading_string[i]:
        print(f"В файле \"{path1}\" строчка под номером {i+1} не совпадает со строчкой \"{path2}\" под таким же номером")
        print(f"В файле \"{path1}\" эта строчка \"{read_string[i]}\"")
        print(f"В файле \"{path2}\" эта строчка \"{reading_string[i]}\"")

file1.close()
file2.close()