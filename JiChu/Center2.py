# 输入三行文字， 让其在方框中居中显示

a=input("请输入第一个字符串:")
b=input("请输入第二个字符串:")
c=input("请输入第三个字符串:")

m=max(len(a),len(b),len(c))
line1="+"+"-"*(m+2)+"+"
print(line1)
print( "| "+a.center(m)+" |")
print( "| "+b.center(m)+" |")
print( "| "+c.center(m)+" |")
print(line1)