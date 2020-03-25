class MyNumber:
    def __init__(self,v):
        self.data = v
    def __repr__(self):
        return "MyNumber(%d)"  % self.data
    def myadd(self,other):
        var = self.data + other.data
        return MyNumber(var)
    def __add__(self, other):
        '''运算符重载'''
        print("__add__被调用")
        var = self.data + other.data
        return var
    def __rsub__(self, lhs):
        '''反向运算符重载'''
        print("__rsub__被调用")
        var = self.data - lhs
        return var
    def __iadd__(self, other):
        '''赋值运算符重载'''
        print("__iadd__被调用")
        var =  self.data + other.data
        return var

n1 = MyNumber(100)
n2 = MyNumber(200)
n3 =n1.myadd(n2)
print("n3=",n3)
print("-------------")
n4 = n1 + n3
print("n4=",n4)
print("-------------")
n5 = 2 - n1
print("n5=",n5)
print("-------------")
n2 += n1
print("n2=",n2)