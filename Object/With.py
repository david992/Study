class A:
    def __enter__(self):
        print("已进入with语句")
        return  self
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''
        此方法在退出with时候自动调用
        :param exc_type:  没有异常时为none，出现异常时为异常类型
        :param exc_val: 没有异常时为none，出现异常时绑定错误对象
        :param exc_tb: 没有异常时为none，在出现异常时绑定treaceback对象
        :return:
        '''
        if exc_type is None:
            print("已经离开with语句，离开时正常")
        else:
            print("已经离开with语句，离开时异常")
            print("异常类型：",exc_type)
            print("错误对象：",exc_val)
            print("treaceback：",exc_tb)
        print("已退出with语句")
def read(filename="file.txt"):
    try:
        with open(filename) as f:
            print("正在读取文件")
            n = int (f.read())
            print("n=",n)
            print("文件关闭")
    except:
        print("打开失败")
read()
with A() as a:
    print("这是with语句内的一条语句")
    int(input("——>"))