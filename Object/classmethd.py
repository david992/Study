class Car:
    count = 0
    @classmethod
    def getTotalCount(cls):
        '''此方法为类方法，
        第一个参数cls，代表调用此方法的类'''
        return cls.count
    @classmethod
    def updateCount(cls,number):
        cls.count += number
print(Car.getTotalCount())
Car.updateCount(1) #Car类调用类方法
print(Car.getTotalCount())
c1 =Car()
c1.updateCount(100)     #Car类的实例也能调用类方法  将 C1.__class__传入cls
print(Car.getTotalCount())