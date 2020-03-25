w=int(input("请输入三角形宽度："))

print("--------第一个三角形--------")
i = 1
while i <= w:
    # Spece = w - i
    # print(" " * Spece + "*" * i)
    # i += 1
    fmt ="%%%ds" % w
    print(fmt % ("*" *i))
    i += 1

print("--------第二个三角形--------")
i = w
while i > 0:
    Spece =w - i
    print(" "* Spece + "*" * i)
    i -=1

print("--------第三个三角形--------")
i = w
while i > 0:
    print("*" * i)
    i -=1