# 方法一
def fib(max):
    L =[]
    n,a,b =0,0,1
    while n < max:
        L.append(b)
        a,b = b,a+b
        n = n+1
    return  L
for x in fib(5):
    print(x)
print('-------------------------')
# 方法二

def fib2(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
for x in fib2(5):
    print(x)

