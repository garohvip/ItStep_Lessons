#-------------- ВАРИАНТ 1 ----------------

# args = ["Ивано", "+", "Франковск"]
# args1 = "+"
# for i in range(len(args)):
#     if args1 in args[i]:
#         args.pop(i)
#         args.insert(i, '-')
#         break
# print(args)

#------------- ВАРИАНТ 2 (ПО ЗАДАНИЮ) ----------------

args = ["Ивано", "+", "Франковск"]
args1 = args.index("+")
args.pop(args1)
args.insert(args1, "-")
print(args)