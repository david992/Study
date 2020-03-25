def myield(n):
    i = 0
    while i < n:
        yield i
        i += 1

for x in myield(3):
    print(x)