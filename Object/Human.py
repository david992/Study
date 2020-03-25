class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.money = 0
    def teach(self,other,skill):
        print(self.name,"教",other.name,skill)
    def human(self):
        print("human被调用")
    def works(self,money):
        self.money += money
        print(self.name,"工作赚了",money,"元")
    def borrow(self,other,money):
        if other.money > money:
            print(other.name,"借给",self.name,money,"元")
            other.money -= money
            self.money += money
        else:
            print(other.name,"无法给",self.name,"借钱")
class student(Human):
        def __init__(self, name, age):
            '''子类中也有init方法时候，基类的init方法不会被自动调用
            需要用显式调用'''
            super().__init__(name,age)
        def  study(self,sub):
            print(self.name,"学习",sub)
        def teach(self, other, skill):
            print(self.name, "教", other.name, "学习", skill)
        def human(self):
            print("student被调用")
        def super_human(self):
            '''调用父类human方法'''
            #super(__class__,self).human()
            super().human()
zhang3 = Human("david",24)
li4 = Human("李卉",20)
li4.teach(zhang3,"web")
zhang3.teach(li4,"Python")
li4.works(4000)
zhang3.borrow(li4,2000)

stu1 = student("cgl",22)
stu1.study("English")
stu1.teach(zhang3,"math")
stu1.__class__.__base__.teach(stu1,zhang3,"math")

print("-------------")

stu1.human()

print("-------------")
stu1.__class__.__base__.human(stu1)
stu2 = student("zhouyijie",22)

stu2.super_human()