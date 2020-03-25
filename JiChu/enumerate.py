print('-------------------------')
def myzip(iter1,iter2):
    it1=iter(iter1)
    it2=iter(iter2)
    while True:
        a = next(it1)
        b = next(it2)
        yield (a,b)

def get_lines():
    L=[]
    while True:
        s = input('请输入：')
        if not s:
            break
        L.append(s)
    return L

def print_line(L):
    for numbers,text in enumerate(L,start=1):
        print('第',numbers,'行',text)


num=[00000,11111,22222,33333,44444,55555]
name=['零零零零零','一一一一一','二二二二二','三三三三三','四四四四四']
for n,a in zip(name,num):
    print(n,'阿拉伯数字是：',a)

print('-------------------------')
# enumerate(iterable[,start]) 枚举函数  start 从多少开始
for x in enumerate(name,start=100):
    index,element=x
    print("索引是：",index,"对应元素是：",element)

print('-------------------------')
d=dict( zip(name,num))
print(d)

print('-------------------------')
if __name__=='__main__':
    print_line(get_lines())