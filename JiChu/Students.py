# 输入学生信息
def input_students():
    L=[]
    while True:
        name = input("请输入学生姓名：")
        if not name:
            break
        age = input("请输入学生年龄：")
        score = input("请输入学生成绩：")
        S={}
        S["name"] = name
        S["age"] = age
        S["score"] = score
        L.append(S)
    return L
#打印学生信息
def output_students(L):
    print("+------------+------+-------+")
    print("|    name    |  age | score |")
    print("+------------+------+-------+")
    for S in L:
        t=(S["name"].center(12),
           str(S["age"]).center(6),
           str(S["score"]).center(7))
        line="|%s|%s|%s|" % t
        print(line)
    print("+------------+------+-------+")

# 修改信息
def modify_students(docs):
    name = input("请输入需要修改学生的姓名")
    for d in docs:
        if d["name"] == name:
            score = int(input("请输入新成绩："))
            d["score"] = score
            print("学生",name,"的成绩已被修改为：",score)
        else:
            return ("没找到姓名为",name,"的学生信息")

# 删除信息
def delete_students(docs):
    name = input("请输入需要删除的学生姓名")
    # docs是列表 该列表里由很多学生信息即字典组成
    for i in range(len(docs)):
        if docs[i]["name"] == name:
            del docs[i]
            print("已成功删除学生",name,"信息")
            return
    else:
        print("未找到",name,"该学生信息")
# 打印菜单
def show_menu():
    print("+-------------------------------+")
    print("|  1) 添加学生信息               |")
    print("|  2) 查看所有学生信息           |")
    print("|  3) 修改学生信息               |")
    print("|  4) 删除学生信息               |")
    print("|  q) 退出                      |")
    print("+-------------------------------+")

# 主函数
def main():
    docs=[]
    while True:
        show_menu() #创建一个列表  用来接收学生信息
        s=input("请选择：")
        if s == "1":
            docs +=input_students()
        elif s == "2":
            output_students(docs)
        elif s == "3":
            modify_students(docs)
        elif s == "4":
            delete_students(docs)
        elif s == "q":
            return

main()

# L = input_students()
# output_students(L)
# print("--------------年龄从大到小排序-------------------------")
# def get_age(S):
#     return S["age"]
# L2 =sorted(L,key=get_age,reverse=True)
# output_students(L2)
# print("--------------成绩从高到低排序-------------------------")
# L3 =sorted(L,key=lambda S:S["score"],reverse=True)
# output_students(L3)
# print("添加信息")
# L += input_students()
# print("添加后信息为：")
# output_students(L)
