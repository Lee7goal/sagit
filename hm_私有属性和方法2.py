#coding=utf-8
#Version:python3.7.3
#Tools:Pycharm
__date__ = '2019/4/1 15:54'
__author__ = 'Lee7'

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 300
    def __test(self):
        print("测试输出%d %d"%(self.num1,self.__num2))
    def test(self):
        print("测试输出 %d "%(self.__num2))

class B(A):
    def demo(self):
        self.test()

b = B()
b.demo()
b._A__test()