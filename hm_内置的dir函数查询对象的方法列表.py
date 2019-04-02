# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/3/29 17:09'
__author__ = 'Lee7'

# class Cat:
#     """这是一个猫类"""
#     def eat(self):
#         print("%s 在吃东西" % self.name)
#     def drink(self):
#         print("喝")
#     # def kill(self,name):
#     #     print("杀死了%s"%name)
# tom = Cat()
# tom.eat()
# tom.drink()
# tom.name("TOM")
# addr = id(tom)
# lize = Cat()
# lize.name = "LIZE"
# lize.eat()
# lize.kill("TOM")
# addr1 = id(lize)
# print(tom)
# print("%d"%addr)
# print("%x"%addr)
# print(lize)
# print("%d"%addr1)
# print("%x"%addr1)

class Cat:
    def eat(self):
        print(" %s 要吃鱼"%self.name)
    def drink(self):
        print(" %s 要喝水"%self.name)

tom = Cat()
tom.name = "小花猫"
tom.eat()
tom.drink()

lzee = Cat()
lzee.name = "安琪拉"
lzee.eat()
lzee.drink()