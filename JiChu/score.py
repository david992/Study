# 输入成绩 输出最高分 最低分  平均分

x=int(input("成绩1："))
y=int(input("成绩2："))
z=int(input("成绩3："))
print ("成绩分别是",x,y,z)
# 方法1
# if x>y:
#     max=x
#     if max>z:
#         print("最高分",max)
#     else:
#         print("最高分",z)
# else:
#     max=y
#     if max>z:
#         print("最高分",max)
#     else:
#         print("最高分",z)
# if x<y:
#     min=x
#     if min<z:
#         print("最底分",min)
#     else:
#         print("最底分",z)
# else:
#     min=y
#     if min<z:
#         print("最底分",min)
#     else:
#         print("最底分",z)

# 方法2
max=x
if y>max:
    max=y
if z>max:
    max=z
print("最高分", max)
min=x
if y<min:
    min=y
if z<min:
    min=z
print("最底分", min)
print("平均分：", (x + y + z) / 3)
