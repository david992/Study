import  time
#计算密集型
def count(x,y):
    c = 0
    while c < 1000000:
        c += 1
        x += 1
        y += 1

#IO密集型
def write():
    f = open("test.txt","w")
    for i in range(1000000):
        f.write(str(i)+"\n")
    f.close()

def read():
    f = open("test.txt")
    lines = f.readlines()
    f.close()
t= time.time()
# 执行计算密集型
#for i in range(10):
#   count(1,1)
#执行IO密集型
# for i in range(10):
#     write()
#     read()
# print("CPU",time.time()-t)