
def main():
    list=[]
    str = input("请输入字符串：")
    N = int(input("请输入位移量："))
    for i in str:
        n = ord(i)
        new_str= chr(n+N)
        list.append(new_str)
    S = "".join(list)
    print(S)
if __name__ =="__main__":
    main()