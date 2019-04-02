#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/1 19:45'
__author__ = 'Lee7'

"""
需求
1.在Dog类中封装方法game
    ·普通狗只是简单的玩耍
2.定义XiaoTianDog继承Dog，并重写game
    ·哮天犬在天上玩
3.定义Person类，并且封装一个和狗玩的方法
    ·在方法内部，直接让狗对象调用game方法
"""
class Dog:
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s 愉快的玩耍"%self.name)

class XTDog(Dog):
    def  game(self):
        print("%s 飞到了天上玩耍"%self.name)

class Person:
    def __init__(self,name):
        self.name = name
    def game_with_dog(self,dog):
        print("%s 和 %s 快乐的玩耍。。。"%(self.name,dog.name))

        #让狗玩耍
        dog.game()

a = Dog("叮当")
b = XTDog("提莫")
c = Person("小明")

c.game_with_dog(a)
c.game_with_dog(b)