#装饰器函数
def message(fn):
    def fx(name,x):
        print(name,"来办理业务...")
        fn(name,x)
        print(name,"已办理",x,"元相关业务...")
    return fx

def check(fn):
    def fx(name,x):
        print("checking...")
        if True:
            print("success")
            fn(name,x)
    return fx

def savemoney(name,x):
    print(name,"存款",x,"元人命币")

@check
@message
def withdrow(name,x):
    print(name,"取款",x,"元人命币")

savemoney("david",200)
print("***************")
withdrow("david",100)