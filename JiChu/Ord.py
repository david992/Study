s=input("您输入的字符是：")
b=int(input("您输入的字符编码是：") )
d=int(input("您输入的整数是："))
print("整数转换为16进制后为：",hex(d))          #整数转换为16进制
print("整数转换为8进制后为：",oct(d))           #整数转换为8进制后
print("整数转换为2进制后为：",bin(d))           #整数转换为2进制后
print("字符编码是：",ord(s))                   #字符转字符编码
print("字符编码对应的值",chr(b))               #字符编码转字符
print(ord("a")-ord("A"))

 