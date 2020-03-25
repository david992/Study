import random

def write_file(filename="file1.txt"):
    try:
        with open(filename,'w') as f:
            i=1
            while i < 50 :
                f.write(str(i))
                f.write(",")
                f.write("David"+str(i))
                f.write(",")
                f.write(str(random.randint(60,100)))
                f.write(",")
                f.write(str(15071237400+i))
                f.write('\n')
                i +=1
    except OSError:
        print('写入失败')
write_file()