# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/3/30 17:44'
__author__ = 'Lee7'

class Cat:
    def __init__(self,new_name,new_age):

        print("这是一个初始化方法")

        #self.属性名 = 属性的初始值
        #self.name = "TOM"
        self.name = new_name
        self.age = new_age
        # self.gender = True
    def eat(self):
        print("%s爱吃鱼" % self.name)

    def suishu(self):
        print("%s现在有%d岁啦" % (self.name,self.age))
        return
tom = Cat("SillyB",5)

print(tom.name)
tom.eat()
tom.suishu()

