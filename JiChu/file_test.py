def input_phone():
    '''读取用户输入，形成元组列表并返回'''
    L = []
    while True:
        name = input('name:')
        if not name:
            break
        number = input('number:')
        L.append((name,number))
    return L

def write_file(lst,filename="phone.txt"):
    '''将lst内元素存到文件filename中'''
    try:
        f = open(filename,'w')
        for name, number in lst:
            f.write(name)
            f.write(",")
            f.write(number)
            f.write('\n')
        f.close()
    except OSError:
        print('写入失败')


if __name__ == '__main__':
    L = input_phone()
    print(L)
    write_file(L)

