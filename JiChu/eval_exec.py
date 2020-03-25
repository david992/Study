# eval(字符串，globals，locals)
# 把一个字符串当做一个表达式运行，返回表达式执行后的结果

# exec(字符串，globals，locals)
# 把一个字符串当做程序执行

x=20
y=90
S=eval("x+y")
T="print(x,y,x+y)"
exec(T)
exec(T,{"x":200,"y":900})
exec(T,{"x":2},{"y":900})               #  优先访问局部变量 再访问全局变量
exec(T,{"x":2,"y":9},{"x":200})
print(S)