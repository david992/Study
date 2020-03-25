#Mymod1.py

#  自定义模块
'''模块说明文档
'''
def input_stu():
    L =[]
    while True:
        S={}
        name = input("请输入姓名：")
        if not name:
            break

        age = input("请输入年龄：")
        score = input("请输入成绩：")
        S["name"] = name
        S["age"] = age
        S["score"] = score
        L.append(S)
        return L

def output_stu(lst):
    print("+------------+------+-------+")
    print("|    name    |  age | score |")
    print("+------------+------+-------+")
    for s in lst:
        d = (s['name'].center(12),
             str(s['age']).center(6),
             str(s['score']).center(7))
        line = '|%s|%s|%s|' % d
        print(line)
    print("+------------+------+-------+")
print(__file__)
print(__doc__)
print(__name__)
print(__package__)