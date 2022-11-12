def main(number):
    for i in range(number):
        yield i


a = main(10)
for j in a:
    print(j)