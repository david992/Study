def make_power(y):
    def fx(arg):
        return arg ** y
    return fx
pow2 = make_power(2)
print("3的平方",pow2(3))
pow3 = make_power(3)
print("3的立方",pow3(3))
print(sum(map(lambda x:x**2,range(1,10))))
print(sum(map(make_power(2),range(1,10))))
print("---------------------------------------")
def make_func(a,b,c):
    def fx(x):
        return a*x**2+b*x+c
    return fx
fx1=make_func(4,6,9) #创建函数Y=4x²+6x+9
print(fx1(5))#给x赋值 x=5  并求值