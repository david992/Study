try:
    f = open(r"C:\Users\Admin\Desktop\Mysql.txt")

    while True:
        s = f.readline()
        if not s :
            break
        if s[-1]== '\n':
            print('读取成功，内容是---->',s,end='')
        else:
            print('读取成功，内容是---->', s)
    print('打开成功')
    f = open("C:/Users/Admin/Desktop/cat7")
except OSError as OSErr:
    print('打开失败',OSErr)
f.close()

