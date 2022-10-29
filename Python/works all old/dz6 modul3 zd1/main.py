args = ["Володя", "Саня сварщик", 34, 75, "Питон", 11]
args2 = args[-1]
args1 = args[0]
args.pop(0)
args.pop()
args.append(args1)
args.insert(0, args2)
print(args)