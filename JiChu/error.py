def get_score():
    try:
        score = int(input("请输入成绩:"))
    except:
        return 0
    if 0 <= score <= 100:
        return score
    return 0

score = get_score()
print("成绩为：",score)

def get_age():
    age = int(input("请输入年龄："))
    assert 0 <= age <= 140,"年龄不合法"
    return age
try:
    age = get_age()
except ValueError as VE:
    print("错误:",VE)
    age = 0
except AssertionError as AE:
    print('错误:',AE)
    age = 0
print('年龄:',age)
