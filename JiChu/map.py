# map(func,iterables)
# 用函数对可迭代对象中的每个元素作为参数计算出新的可迭代对象，
# 当最短的可迭代对象不在提供数据时，结束。
import math
def pow2(x):
    return x**2
s=0
L=[]
for x in map(pow2,range(1,10)):
    s +=x
    L.append(x)
print(L)
print(s)

def pow3(x):
    return (x**2)
print(sum(map(pow3,range(1,10))))

print(sum(map(lambda x:x**2,range(1,10))))

def jiecheng(n):
    # sum=1
    # for i in range(1,n+1):
    #     sum *= i
    # return sum
    if n == 1:
        return  1
    else:
        return n*jiecheng(n-1)

def mysum(n):
    #方法一 循环
    # sum=0
    # for x in range(1,n+1):
    #     sum += x
    # return sum

    #方法二 函数式编程
    # return sum(range(1,n+1))

    #方法三 递归
    if n==1:
        return 1
    return n + mysum(n-1)
print(mysum(100))

print(jiecheng(5))
print(math.factorial(5))