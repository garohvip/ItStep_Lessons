import os.path

path1 = os.path.join("txtfile1.txt")
path2 = os.path.join("txtfile2.txt")
symbol = [".", ",", "!"]

file1 = open(path1, 'r')
file2 = open(path2, 'w')
file1_read = file1.read().split("\n")
print(file1_read)
for i in file1_read:
    p = i.split()
    for j in p:
        for sym in symbol:
            if sym in j:
                file2.write(f"{j} (В слове {len(j)-1} букв) ")
                break
        else:
            file2.write(f"{j} (В слове {len(j)} букв) ")
    file2.write("\n")

file1.close()
file2.close()