# 输入三行文字， 让其在方框中居中显示

a=input("请输入第一个字符串:")
b=input("请输入第二个字符串:")
c=input("请输入第三个字符串:")

m=len(a)
if len(b)>m:
    m=len(b)
if len(c)>m:
    m=len(c)

line1="+"+"-"*(m+2)+"+"
print(line1)
# 打印第1行
left=(m-len(a))//2
right=m-left-len(a)
line="| "+" "*left+a+" "*right+" |"
print(line)
# 打印第2行
left=(m-len(b))//2
right=m-left-len(b)
line="| "+" "*left+b+" "*right+" |"
print(line)
# 打印第3行
left=(m-len(c))//2
right=m-left-len(c)
line="| "+" "*left+c+" "*right+" |"
print(line)
print(line1)