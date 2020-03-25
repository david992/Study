def read_info(filename='phone.txt'):
    '''读取信息'''
    L=[]
    try:
        f = open(filename)
        while True:
            s = f.readline()
            if not s:
                break
            s = s.strip() #去掉右边换行符'\n'
            name,number = s.split(',')
            L.append((name,number))
        f.close()
    except OSError:
        print('打开失败')
    return L

def print_info(lst):
    for s in lst:
        m = len(s[0])
        if m < len(s[1]):
            m = len(s[1])
    n = m+2
    print("+","-"*n,"+","-"*n,"+")
    print("|",str('name').center(n),"+", str('number').center(n),"|")
    print("+","-"*n,"+","-"*n,"+")
    for s in lst:
        # t = (str(s[0]).center(n),str(s[1]).center(n))
        # line = "|%s|%s|" % t
        # print( line)     # %s 占位符直接跟   而使用 ， 连接会有间隔
        print("|",str(s[0]).center(n),"+", str(s[1]).center(n),"|")
    print("+","-"*(n),"+","-"*(n),"+")

if __name__ == '__main__':
    L = read_info()
    # print(L)
    print_info(L)

    t = ("蒋代伟")
    print("答案：", "    蒋代伟     ".rstrip())      #使用 ， 连接会有间隔
    line = "答案：%s" % t         # %s 占位符直接跟所需要的内容
    print(line)