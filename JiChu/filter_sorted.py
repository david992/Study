# filter(func,iterable)
# 筛选可迭代对象中数据，返回一个新可迭代对象
# 函数func对元素求值，返回false则丢弃数据，返回true则保留该数据。
def isodd(x):
    return x%2==1
for x in filter(isodd,range(1,10)):
    print(x)
enev=[x for x in filter(lambda x:x%2==1,range(1,10))]
print(enev)
def isprime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
        return True
L=list(filter(isprime,range(100)))
print(L)


# sorted()
# 将可迭代对象的数据排序，生成排序后的列表。
print("排序后：",sorted(L,key=abs,reverse=True))