class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def human(self):
        print("姓名:",self.name)
        print("年龄:",self.age)
class student(Human):
        def __init__(self, name, age,id=0):
            '''子类中也有init方法时候，
            基类的init方法不会被自动调用
            需要用显式调用'''
            super().__init__(name,age)
            self.id = id
        def human(self):
            super().human()
            print("学号：",self.id)

s1 = student("david",24,100)
s1.human()