def prodNum(a, b):
    if b == 0:
        return 1
    else:
        return a * prodNum(a, b-1)

print(prodNum(5, 3))