class Student:
    def set_info(self,name,age=0):
        print("set_info方法被调用")
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name,"今年",self.age,"岁")

s1 = Student()
s1.id = 11111111
print("学号是：",s1.id)
s2 = Student()
s1.set_info("david",20)
s2.set_info("lihui",24)
# del s1.id   # 删除属性
print("学号是：",s1.id)
s1.show_info()
s2.show_info()