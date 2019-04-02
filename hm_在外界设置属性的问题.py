# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/3/30 17:21'
__author__ = 'Lee7'

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