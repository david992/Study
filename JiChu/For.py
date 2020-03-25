print("-----for循环-----")
L=[1,3,5,7,9]
for i in L:
    print(i)


print("-----while实现for-----")
it = iter(L)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print('终止迭代')
        break