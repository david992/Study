
def my_add(x,y):
    return x+y
def my_mul(x,y):
    return x*y
def my_sub(x,y):
    return x-y
def my_div(x,y):
    return x/y

def get_op(s):
    if s == "+" or s == "加":
        return my_add
    elif s == "*" or s == "乘":
        return my_mul
    elif s == "-" or s == "减":
        return my_sub
    elif s == "/" or s == "除":
        return my_div

def main():
    while True:
        S=input("请输入计算式：")
        L=S.split()
        a,s1,b = L
        a=int(a)
        b=int(b)
        fn=get_op(s1)
        print("结果：",fn(a,b))
main()