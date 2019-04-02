# coding=utf-8
# Version:python3.7.3
# Tools:Pycharm
__date__ = '2019/4/1 14:18'
__author__ = 'Lee7'

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200
    def __test(self):
        print("私有方法 %d %d" % (self.num1,
                              self.__num2))
class B(A):
    def demo(self):
        # print("访问父类的私有属性 %d"%self._A__num2)
        # self.__test()
        pass

a = A()
b = B()
print(b)
# 在外界不能直接访问对象的私有属性/方法
print(b.num1)
# print(b.__num2)
# b.__test
# a._A__test
b.demo()
a._A__test
