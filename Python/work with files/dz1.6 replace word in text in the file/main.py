import os

path = os.path.join("filetxt1.txt")

# file = open(path, "r")
# file_read = file.read().split()
# print(file.read())
# find_word = input("Enter the word you want to find in the file: ")
# howmany_replacements = int(input("How mant replacements you want make: "))
# count = 0
# for i in range(len(file_read)):
#     if find_word.lower() in file_read[i].lower():
#         file_read[i] = input("What word do you want to replace the word with: ")
#         count += 1
#         if howmany_replacements == count:
#             break
# print(file_read)
# file.close()

file = open(path, "r")
file_read = file.read()
print(file_read)
find_word = input("enter find word: ")
replace_word = input("enter replace word: ")
new_file_read = file_read.replace(find_word, replace_word, int(input("How many words do you want to replace: ")))
print(new_file_read)
file.close()