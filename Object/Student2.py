class Student:
    def __init__(self,name,address):  #初始化方法
        print("__init__方法被调用")
        self.name = name
        self.address = address
    def set_add(self,add):
        self.address = add

    def show_info(self,age):
        print("家住",self.address,"的学生",self.name,"今年",age,"岁")
        # self——————> 谁调用这个方法，这个self指的就是这个对象
A = Student("david","武汉")
# A.__init__("david","Wuhan")  显式调用
A.show_info(24)
A.set_add("宜昌")
A.show_info(24)

